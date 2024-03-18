import sys
import tempfile
import os
import logging
import argparse

from pg_podcast_toolkit import podcast_tools
from pg_podcast_toolkit import podcast_ipfs_tools

import argparse
import os
import sys
import logging
from pg_podcast_toolkit import podcast_tools, podcast_ipfs_tools
import tempfile

# Set up argument parsing
parser = argparse.ArgumentParser(description='Modify an existing Podcast 2.0 feed to add IPFS support.')
parser.add_argument('--gateway', type=str, default=os.environ.get('IPFS_GATEWAY', '/ip4/127.0.0.1/tcp/5001'),
                    help='The IPFS gateway address. Default: /ip4/127.0.0.1/tcp/5001 or value from IPFS_GATEWAY environment variable.')
parser.add_argument('--input_url', type=str, required=True,
                    help='URL of the input podcast RSS feed.')
parser.add_argument('--output_file', type=str, required=True,
                    help='File path for the output RSS feed.')
parser.add_argument('--log_level', type=str, default='INFO',
                    help='Set the logging level (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL). Default: INFO.')

args = parser.parse_args()

IPFS_GATEWAY = args.gateway
INPUT_URL = args.input_url
OUTPUT_FILE = args.output_file

# Set logging level
logging_level = getattr(logging, args.log_level.upper(), None)
if not isinstance(logging_level, int):
    raise ValueError(f'Invalid log level: {args.log_level}')

logging.basicConfig(
    level=logging_level,
    handlers=[logging.StreamHandler(sys.stdout)],
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)

# load the podcast file into podcast_etree
podcast_etree = podcast_tools.load_podcast_from_url_into_etree(INPUT_URL)

# extract the media resources, this is a map of guid -> mediaresource
map_media_resources = podcast_tools.extract_enclosures(podcast_etree)

# now download the media files and add them to IPFS
with tempfile.TemporaryDirectory() as temp_dir:
    # now download the media files
    lst_media_resource = podcast_tools.download_media(map_media_resources, destination_dir = temp_dir)
    # now add the files to IPFS
    lst_media_resource = podcast_ipfs_tools.add_files_to_ipfs(lst_media_resource, IPFS_GATEWAY)

# now see what we get back
for media_resource in lst_media_resource:
    logging.info(media_resource)

# now try and write the modified document
updated_podcast_etree = podcast_ipfs_tools.add_ipfs_alt_enclosures_to_podcast(podcast_etree, lst_media_resource)

# If you need to save the modified tree back to a file
updated_podcast_etree.write(OUTPUT_FILE, pretty_print=True, xml_declaration=True, encoding='UTF-8')

