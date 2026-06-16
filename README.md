# OSINT Google Dorks Automation Tool

This project has been developed as part of a Final Degree Project (TFG) in Computer Engineering.

## Description

The objective of this project is to automate the generation of Google Dorks queries and facilitate the collection of publicly available information through OSINT (Open Source Intelligence) techniques.

The tool allows users to generate advanced search queries based on parameters provided by the user, execute searches, process the obtained information, and present the results in a structured manner.

## Features

- Automatic generation of Google Dorks queries
- User-defined search parameters
- Search execution through web requests
- Extraction of result links
- Basic result processing
- Error handling and input validation
- Simulated results generation when search engines block automated requests

## Technologies

- Python 3
- Requests
- BeautifulSoup

## Installation

Clone the repository:

```bash
git clone https://github.com/Eranfg/osint-google-dorks-tool.git
```

Access the project directory:

```bash
cd osint-google-dorks-tool
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the application:

```bash
python main.py
```

The program will request the following parameters:

- Domain name
- File type

Example:

```text
Domain: nasa.gov
File type: pdf
```

Generated query:

```text
site:nasa.gov filetype:pdf
```

## Project Structure

```text
osint-google-dorks-tool/
│
├── main.py
├── dorks.py
├── scraper.py
├── requirements.txt
└── README.md
```

## Limitations

Modern search engines implement protection mechanisms against automated traffic. As a result, obtaining real search results through automated HTTP requests may not always be possible.

To allow validation of the complete workflow, the tool includes a simulated results mechanism that demonstrates the functionality of the application when real results cannot be retrieved.

## Future Improvements

Possible future developments include:

- Integration with Selenium-based browsers
- Support for specialized APIs
- Advanced filtering and classification of results
- Graphical User Interface (GUI)
- Automatic report generation

## Academic Context

This project has been developed within the framework of a Final Degree Project (TFG) focused on the application of OSINT techniques and Google Dorks automation for cybersecurity purposes.

## Author

Erán Franquiz

## License

This project is intended for academic and educational purposes.