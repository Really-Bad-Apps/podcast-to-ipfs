import sys
import tempfile
import tempfile
import os
import logging

sys.path.append('src')

from pg_podcast_toolkit import podcast_tools
from pg_podcast_toolkit import podcast_ipfs_tools

# Configure logging to write to stdout
logging.basicConfig(
    level=logging.INFO,
    handlers=[
        logging.StreamHandler(sys.stdout)  # Add StreamHandler for stdout
    ],
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Example format
)


IPFS_GATEWAY = os.environ.get('IPFS_GATEWAY', '/ip4/127.0.0.1/tcp/5001')

# load the podcast file into podcast_etree
podcast_etree = podcast_tools.load_podcast_file_into_etree('bballrss.xml')

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
    print(media_resource)

# now try and write the modified document
updated_podcast_etree = podcast_ipfs_tools.add_ipfs_alt_enclosures_to_podcast(podcast_etree, lst_media_resource)

# If you need to save the modified tree back to a file
updated_podcast_etree.write('output.xml', pretty_print=True, xml_declaration=True, encoding='UTF-8')

