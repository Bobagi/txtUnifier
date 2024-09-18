# TXT File Unifier

This Python script combines multiple numbered TXT files into a single file named `unified.txt`. It reads files from a source directory, merges their content in numerical order of the filenames, and saves the result in a specified destination directory.

## Features

- **Automated Sorting**: Automatically sorts and processes files based on the numeric ordering in their filenames.
- **Directory Management**: Creates the destination directory if it does not already exist.
- **Simple and Efficient**: Merges files in a straightforward and efficient manner.

## Prerequisites

Ensure you have Python installed on your machine. The script is compatible with Python 3.x. You can download and install Python from [here](https://www.python.org/downloads/).

## Installation

No installation is needed. Just ensure you have the Python interpreter installed.

## Usage

1. **Prepare Your Files**:
   - Place all your `.txt` files that you want to unify in the `files` directory. Ensure each file's name contains a number that represents its order.

2. **Run the Script**:
   - Navigate to the directory containing the script.
   - Run the script using Python:
     ```bash
     python unify_txt_files.py
     ```

3. **Check the Output**:
   - Once the script has completed execution, check the `result` directory for the `unified.txt` file.

## How It Works

The script performs the following steps:
- Reads all filenames in the `files` directory.
- Filters and sorts files based on the numeric value in their filenames.
- Sequentially reads each file's content and writes it to `unified.txt` in the `result` directory.

## Customization

If you need to change the source or destination directories or the output file's name:
- Open `unify_txt_files.py` with a text editor.
- Modify the values of `source_directory`, `destination_directory`, or `output_filename` at the bottom of the script.

## Troubleshooting

- **Missing Files**: Ensure all files are correctly numbered and placed in the `files` directory.
- **Permission Issues**: Make sure you have the necessary permissions to read from the source directory and write to the destination directory.

## Contributing

Feel free to fork this project and submit pull requests. You can also open an issue if you find bugs or have feature requests.

## License

This script is released under the MIT License. See the LICENSE file in the repository for more details.
