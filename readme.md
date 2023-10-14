# Duplicate File Finder

This tool scans directories and identifies duplicate files based on their size and SHA-256 hash. The tool is optimized to handle a large number of files efficiently using parallel processing.

## Details

This tool is written in Python and uses the following built-in libraries:
- `os`
- `hashlib`
- `concurrent.futures`

There's no need to install any external modules.

## Features

- **Fast Scanning**: Uses `os.walk()` to efficiently scan directories and subdirectories.
- **Size Filtering**: Filters potential duplicates based on their file size before hashing.
- **Parallel Processing**: Utilizes multiple processes to compute file hashes in parallel.
- **SHA-256 Hashing**: Uses SHA-256 hashing to ensure accurate duplicate detection.

## Getting Started

1. Ensure you have Python installed on your machine.
2. Clone the repository or download the script.
3. Navigate to the directory containing the script using your terminal or command prompt.

## How to Use

- Execute the script using the following command: python Duplicate_Files_Remover.py
- The tool will scan the current directory and its subdirectories for duplicate files.
- Once completed, it will display any duplicates found.

## Contributions

Contributions are welcome! If you find any issues or have suggestions, please open an issue. Pull requests are also encouraged.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgements

- Thanks to the Python community for maintaining such a powerful and easy-to-use language.
- Special thanks to anyone who contributes or uses this tool.