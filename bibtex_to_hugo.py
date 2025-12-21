#!/usr/bin/env python3
"""
Convert BibTeX entries to Hugo webpage structure.

Takes a BibTeX file and creates a folder structure where each entry gets:
- A subfolder named "pub_<bibtex_key>"
- A cite.bib file with the BibTeX entry
- An index.md file with Hugo-compatible frontmatter
"""

import os
import sys
import argparse
import re
from typing import Dict, List, Tuple
from pathlib import Path
from pylatexenc.latex2text import LatexNodes2Text
import logging
import requests

# Set up a logging to print out
logging.basicConfig(
    level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s"
)


class bibtexParser:
    def __init__(self, file_path):
        """Initialise bibtexParser with a file path to a .bib file."""
        self.file_path = file_path

        # Precompile the regular expression to split bibtex string into chunks
        self.pattern_chunk_split = re.compile(r"(@[A-Za-z]+{)")

        self.bibtex_string = None
        self.metadata_entries = []
        self.parsed_entries = []
        self.raw_entries = []

    def read_bibtex_file(self):
        """Read the .bib file and store the contents as a string."""
        logging.info(f"Reading {self.file_path}")
        if not self.file_path.endswith(".bib"):
            logging.error(
                f"Invalid file type: {self.file_path}, must be a .bib file"
            )
            return  # Abort the operation after logging the error

        if not os.path.exists(self.file_path):
            logging.error(f"File not found: {self.file_path}")
            return  # Abort the operation after logging the error

        try:
            with open(self.file_path, "r") as f:
                self.bibtex_string = f.read()

            if self.bibtex_string:
                logging.info(f"Successfully read {self.file_path}")
            else:
                logging.warning(f"The file {self.file_path} is empty")
        except Exception as e:
            logging.error(f"Error reading {self.file_path}: {str(e)}")

    def extract_metadata(self):
        """
        Splits the BibTeX string into chunks and extracts metadata for each
        entry.

        Chunks are split using '@entry' as a delimiter. The method then filters
        out blank  entries and delimiters, retaining only chunks with metadata.
        The metadata is stored as a string in a list.
        """
        logging.info("Extracting metadata")
        try:
            chunks = re.split(
                self.pattern_chunk_split, self.bibtex_string.strip()
            )

            for chunk in chunks:
                logging.debug(f"Processing chunk: {chunk[:80]}...")                

                chunk_type_match = re.match(r"@(?P<type>[A-Za-z]+){", chunk)
                if chunk_type_match:
                    entry_type = chunk_type_match.group("type").lower()
                    tmp_raw_entry = chunk.strip()
                    logging.debug(f"Detected entry type: {entry_type}")

                metadata = self._extract_entry_metadata(chunk)
                if metadata:
                    logging.info(f"Extracted metadata chunk: {metadata[:30]}...")
                    assert entry_type is not None, f"Entry type could not be determined for chunk: {chunk[:30]}..."
                    assert tmp_raw_entry is not None, f"Raw entry could not be determined for chunk: {chunk[:30]}..."
                    metadata = metadata + f"\ntype = {entry_type}"


                    tmp_raw_entry = tmp_raw_entry + chunk
                    logging.debug(f"Appending raw entry {tmp_raw_entry}")
                    self.raw_entries.append(tmp_raw_entry.strip())

                    self.metadata_entries.append(metadata)
                else:
                    logging.debug(f"Skipping invalid metadata: {chunk[:30]}")

            logging.info(
                f"{len(self.metadata_entries)} entry metadata extracted"
            )

        except re.error as e:
            # If the pattern to split the string into chunks is invalid
            logging.error(f"Invalid regular expression pattern: {str(e)}")

    def parse_metadata(self, pattern=None):
        """
        Parse each metadata string into a dictionary of key-value pairs, where
        each dictionary represents a single bibtex entry.
        """
        logging.info("Parsing the bibtex entries")
        if not pattern:
            pattern = r'(\w+)\s*=\s*(?:"([^"]*)"|\{([^\}]*)\}|(\w+))'

        # Iterate over each metadata entry and parse it, keep track of the index to obtain raw entry
        idx = 0

        for metadata in self.metadata_entries:
            logging.debug(f"Parsing metadata: {metadata[:30]}...")
            parsed_data = self._parse_metadata(metadata, pattern)

            bibtex_key = metadata.split(',', 1)[0]  # Extract the bibtex key
            parsed_data['key'] = bibtex_key.strip()

            parsed_data['raw'] = self.raw_entries[idx]
            idx += 1

            self.parsed_entries.append(parsed_data)

            if not parsed_data:
                logging.debug(f"Failed to parse: {metadata[:30]}")

        logging.info(f"{len(self.parsed_entries)} valid entries parsed")

    def add_urls_from_doi(self):
        """
        If the 'doi' key is present, construct the URL with the DOI. Update the
        entry with the redirected URL.
        """
        logging.info("Adding redirected URLs from DOI")
        for idx, entry in enumerate(self.parsed_entries):
            if "doi" in entry:
                url = self._get_url_from_doi(entry["doi"], idx=idx)
                self.parsed_entries[idx]["doi_url"] = url
                self.parsed_entries[idx]["url"] = url
            else:
                logging.info(f"No DOI found in entry {idx}")
        logging.info("Adding redirected URLs completed")

    def extract_parsed_entries(self):
        """Return the parsed entries as a list of dictionaries."""
        logging.info(
            f"{len(self.parsed_entries)} entries extracted from {self.file_path}"  # noqa
        )
        return json.dumps(self.parsed_entries, indent=4)

    def parse_bibtex(self, json=False):
        """
        Main entry point to parse the bibtex file. Read the bibtex string,
        chunk the bibtex string, parse the entries, add URLs from DOI, and
        return the parsed entries as a JSON or a list of dictionaries.
        """
        try:
            self.read_bibtex_file()
            self.extract_metadata()
            self.parse_metadata()
            #self.add_urls_from_doi()

            if json:
                self.extract_parsed_entries()
            else:
                return self.parsed_entries

        except Exception as e:
            logging.error(f"An unexpected error occurred: {str(e)}")

    def save_parsed_entries(self, output_path):
        """Save the parsed entries to a json."""
        with open(output_path, "w") as f:
            json_data = self.extract_parsed_entries()
            f.write(json_data)
        logging.info(f"Saved parsed entries to {output_path}")

    def _extract_entry_metadata(self, chunk):
        """
        Extracts the metadata from a chunk if it is valid. An invalid chunk is
        one that is empty or contains the delimiter '@'.

        Parameters:
        - chunk (str): A chunk of the BibTeX string.

        Returns:
        - str: The metadata if valid, None otherwise.
        """
        chunk = chunk.strip()
        if chunk and chunk[0] != "@":
            return chunk

    def _parse_metadata(self, metadata, pattern):
        """
        Parses the metadata string for a single entry into a dictionary of
        key-value pairs.

        This method uses regular expressions to extract bibtex entry fields
        and their values from the metadata.

        It handles exceptions related to regular expression errors.

        Parameters:
        - metadata (str): The metadata string to parse.
        - pattern (str): The regular expression pattern used to identify
          key-value pairs within the metadata.

        Returns:
        - dict: A dictionary containing parsed key-value pairs from the bibtex
          entry, or None if an error occurs.
        """
        try:
            matches = re.findall(pattern, metadata)
            matches = [
                tuple(x for x in match if x not in (None, ""))
                for match in matches
            ]
            parsed_data = {key.lower(): value for key, value in matches}
            return parsed_data

        except re.error as e:
            logging.error(f"Invalid regular expression pattern: {str(e)}")
            return None

    def _get_url_from_doi(self, doi, idx=None):
        """
        Constructs a URL from a DOI and retrieves the final redirected URL.

        This method attempts to construct a URL using the extracted. It then
        uses an HTTP HEAD request to follow redirects and retrieve the final
        redirected URL.

        It handles various HTTP and request-related exceptions.

        Parameters:
        - doi (str): The Digital Object Identifier (DOI) from which to
          construct the URL.
        - idx (int, optional): The index of the entry, used for logging.

        Returns:
        - str: The final redirected URL obtained from the DOI, or None if an
        error occurs.
        """
        try:
            url = "http://dx.doi.org/" + doi
            response = requests.head(url, allow_redirects=True)
            return response.url

        except requests.exceptions.RequestException as e:
            logging.error(
                f"An error occurred while getting URL for entry {idx}, DOI {doi}: {str(e)}"  # noqa
            )
        except Exception as e:
            logging.error(
                f"An unexpected error occurred while getting URL for entry {idx}, DOI {doi}: {str(e)}"  # noqa
            )
        return None


def parse_bibtex_file(bibtex_path: str) -> List[Dict[str, str]]:
    """
    Parse a BibTeX file and extract entries.
    
    Returns a list of dictionaries, each containing:
    - 'key': the BibTeX key
    - 'type': the entry type (article, inproceedings, etc.)
    - 'raw': the raw BibTeX entry
    - 'fields': dictionary of fields and values
    """
    with open(bibtex_path, 'r', encoding='utf-8') as f:
        content = f.read()

    parser = bibtexParser(bibtex_path)

    library = parser.parse_bibtex()    

    print(library)
    
    return library



def format_authors(authors_str: str) -> str:
    """
    Format author string for Hugo frontmatter.
    
    Converts "Author One and Author Two and Author Three" to a YAML list.
    """
    if not authors_str:
        return "[]"
    
    # Split by " and "
    authors = [a.strip() for a in authors_str.split(' and ')]

    # Detect order: name, family or family, name
    formatted_authors = []
    for author in authors:
        if ',' in author:
            parts = [part.strip() for part in author.split(',', 1)]
            formatted_authors.append(f"{parts[1]} {parts[0]}")  # Given Family
        else:
            formatted_authors.append(author)  # Assume Given Family
    
    authors = formatted_authors

    # remove trailing commas from author names
    authors = [author.rstrip(',') for author in authors]

    # replace Stefan Schupp with "admin"
    authors = [author if author.lower() != "stefan schupp" else "admin" for author in authors]

    # Format as markdown list
    return '\n' + ',\n'.join(f'  - {author}' for author in authors) + '\n'


def create_index_md(entry: Dict[str, str], pub_key: str) -> str:
    """
    Create the index.md content for a Hugo publication.
    
    Generates frontmatter with common fields extracted from the BibTeX entry.
    """
    
    # Extract common fields
    title = entry.get('title', 'Untitled')
    authors = entry.get('author', '')
    year = entry.get('year', '')
    abstract = entry.get('abstract', '')
    
    # Map publication type to Hugo type
    pub_type_map = {
        'article': 'journal',
        'inproceedings': 'conference',
        'incollection': 'book-chapter',
        'book': 'book',
        'mastersthesis': 'thesis',
        'phdthesis': 'thesis',
        'techreport': 'report',
        'inbook': 'book-chapter',
    }
    publication_type = pub_type_map.get(entry['type'], 'misc')
    
    # Extract journal/venue information
    journal = entry.get('journal', '')
    booktitle = entry.get('booktitle', '')
    venue = journal or booktitle or ''
    
    # Extract volume, pages, etc.
    volume = entry.get('volume', '')
    number = entry.get('number', '')
    pages = entry.get('pages', '')
    doi = entry.get('doi', '')
    url = entry.get('url', '')
    date = entry.get('date', '')
    
    # Build the markdown file
    md_content = f"""---
title: '{title}'
authors:
  {format_authors(authors).strip()}
publication_types: ["{publication_type}"]
publication: "{venue}"
summary: ""
abstract: "{abstract}"
"""
    
    if year:
        md_content += f'publishDate: "{year}-01-01T00:00:00Z"\n'
        md_content += f'year: "{year}"\n'
    if date:
        md_content += f'date: "{date}"\n'

    # Add optional fields
    if volume:
        md_content += f'volume: "{volume}"\n'
    if number:
        md_content += f'issue: "{number}"\n'
    if pages:
        md_content += f'pages: "{pages}"\n'
    if doi:
        md_content += f'hugoblox:\n\
    ids:\n\
        doi: "{doi}"\n'
    if url:
        md_content += f'links:\n  - name: URL\n    url: "{url}"\n'
    
    md_content += """---
"""
    
    return md_content


def create_cite_bib(entry: Dict[str, str]) -> str:
    """
    Create the cite.bib file content (just the raw BibTeX entry).
    """
    return entry['raw'] + '\n'


def process_bibtex(bibtex_file: str, output_folder: str, dry_run: bool = False) -> None:
    """
    Process a BibTeX file and create the Hugo folder structure.
    
    Args:
        bibtex_file: Path to the BibTeX file
        output_folder: Path to the folder where subfolders will be created
        dry_run: If True, only print what would be done without creating files
    """
    # Validate inputs
    if not os.path.isfile(bibtex_file):
        raise FileNotFoundError(f"BibTeX file not found: {bibtex_file}")
    
    if not os.path.isdir(output_folder):
        if dry_run:
            print(f"[DRY RUN] Would create output folder: {output_folder}")
        else:
            os.makedirs(output_folder, exist_ok=True)
            print(f"Created output folder: {output_folder}")
    
    # Parse the BibTeX file
    print(f"Parsing BibTeX file: {bibtex_file}")
    entries = parse_bibtex_file(bibtex_file)
    print(f"Found {len(entries)} entries")
    
    # Process each entry
    for i, entry in enumerate(entries, 1):
        pub_key = entry['key']
        pub_folder = os.path.join(output_folder, f"{pub_key}")
        
        # Create the subfolder
        if dry_run:
            print(f"[DRY RUN] ({i}/{len(entries)}) Would create folder: {pub_folder}")
        else:
            os.makedirs(pub_folder, exist_ok=True)
            print(f"({i}/{len(entries)}) Created folder: pub_{pub_key}")
        
        # Create cite.bib
        cite_path = os.path.join(pub_folder, "cite.bib")
        cite_content = create_cite_bib(entry)
        
        if dry_run:
            print(f"[DRY RUN] Would create: {cite_path}")
        else:
            with open(cite_path, 'w', encoding='utf-8') as f:
                f.write(cite_content)
            print(f"  Created: cite.bib")
        
        # Create index.md
        index_path = os.path.join(pub_folder, "index.md")
        index_content = create_index_md(entry, pub_key)
        
        if dry_run:
            print(f"[DRY RUN] Would create: {index_path}")
            print(f"[DRY RUN] Content preview:")
            print(index_content[:200] + "...")
        else:
            with open(index_path, 'w', encoding='utf-8') as f:
                f.write(index_content)
            print(f"  Created: index.md")
    
    if not dry_run:
        print(f"\nSuccessfully processed {len(entries)} entries!")


def main():
    parser = argparse.ArgumentParser(
        description='Convert BibTeX entries to Hugo webpage structure',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s publications.bib ./publications/
  %(prog)s data.bib ./output/ --dry-run
        """
    )
    
    parser.add_argument(
        'bibtex_file',
        help='Path to the BibTeX file'
    )
    parser.add_argument(
        'output_folder',
        help='Folder where publication subfolders will be created'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be done without creating files'
    )
    
    args = parser.parse_args()
    
    try:
        process_bibtex(args.bibtex_file, args.output_folder, args.dry_run)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
