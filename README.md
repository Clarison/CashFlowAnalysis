# Financial Statement Data Extraction and Analysis

## Introduction

This repository provides a comprehensive solution for extracting financial statement data from companies' 10-K PDF filings and converting it into a clean, tabular format that is easily accessible for analysis. This project aims to facilitate financial analysis by automating the process of data extraction, cleaning, and storage.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- **PDF Parsing**: Automatically extracts financial data from 10-K PDF filings.
- **Data Cleaning**: Cleans and formats the extracted data for consistency and accuracy.
- **Tabular Storage**: Stores the cleaned financial data in a tabular format for easy access.
- **Scalable**: Can be used for multiple companies and 10-K filings.
- **Customizable**: Easily adaptable to different financial statement structures.

## Requirements

To use this tool, you need the following:

- Python (>= 3.6)
- Libraries: pandas, PyPDF2, pdfplumber, tabula-py
- Git (for cloning the repository)

## Installation

1. Clone this repository to your local machine:

   ```shell
   git clone https://github.com/yourusername/financial-statement-extraction.git
   ```

2. Install the required Python libraries:

   ```shell
   pip install pandas PyPDF2 pdfplumber tabula-py
   ```

## Usage

1. **Data Extraction**: 

   - Place the 10-K PDF filings of the companies you want to analyze in a directory.
   - Modify the extraction script to specify the directory path and customize extraction logic if needed.
   - Run the extraction script to extract financial data from the PDFs.

2. **Data Cleaning**:

   - Modify the cleaning script to handle specific data formatting or inconsistencies.
   - Run the cleaning script to clean and format the extracted financial data.

3. **Tabular Storage**:

   - Organize the cleaned data into tables or data frames as needed.
   - Store the tables in a format like CSV, Excel, or a database for easy access.

4. **Analysis**:

   - Use the cleaned and stored financial data for analysis, reporting, or visualization.

## Contributing

Contributions to improve this project are welcome. Please fork the repository, create a new branch for your changes, and submit a pull request with your enhancements.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to reach out if you have any questions or need further assistance. Happy analyzing!
