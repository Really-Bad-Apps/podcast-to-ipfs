# Podcast to IPFS Toolkit

The Podcast to IPFS Toolkit is designed to enhance Podcasting 2.0 feeds by integrating InterPlanetary File System (IPFS) support. This script automates the process of downloading media from an existing podcast RSS feed, uploading it to an IPFS node, and generating a new RSS feed that includes `ipfs://` URIs for the media content.

## Features

- Downloads media files from a given Podcasting 2.0 RSS feed.
- Uploads media files to an IPFS node.
- Generates a new RSS feed with `ipfs://` URIs for media enclosures.
- Supports custom IPFS gateway configurations.
- Adjustable logging levels for monitoring the process.

## Prerequisites

- Python 3.8 or newer.
- Access to an IPFS node with a configured gateway.
- The `pg_podcast_toolkit` library and its dependencies installed.

### Tip 

If you are using the Brave browser it has a built-in IPFS node you can enable that defaults to http://127.0.0.1:45005 See: [IPFS Support In Brave](https://brave.com/blog/ipfs-support/)

## Installation

Before running the script, ensure that you have Python installed on your system and that the required libraries are installed using pip:

```bash
pip install pg_podcast_toolkit
```

## Usage

```bash
python podcast_to_ipfs.py --gateway <IPFS_GATEWAY> --input_url <PODCAST_RSS_FEED_URL> --output_file <OUTPUT_RSS_FILE_PATH> [--log_level <LOG_LEVEL>]
```

### Arguments

- `--gateway`: The IPFS gateway address (default: `/ip4/127.0.0.1/tcp/5001` or value from `IPFS_GATEWAY` environment variable).
- `--input_url`: URL of the input podcast RSS feed.
- `--output_file`: File path for the output RSS feed with IPFS URIs.
- `--log_level`: (Optional) Set the logging level (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL). Default: INFO.


## Example

To process the RSS feed found at https://example.com/podcast/rss.xml, download its media files, upload them to IPFS, and generate an updated RSS feed named updated_feed.xml in the current directory, use:

```bash
python podcast_to_ipfs.py --input_url "https://example.com/podcast/rss.xml" --output_file "./updated_feed.xml"
```

## Contributing

Contributions are welcome! Whether you're fixing bugs, improving the documentation, or adding new features, your help is appreciated. To contribute:

1. Fork the repository.
2. Create a new branch for your changes.
3. Implement your changes.
4. Submit a pull request with a clear description of your improvements.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
