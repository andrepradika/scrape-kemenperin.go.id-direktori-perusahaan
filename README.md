# Kemenperin Scraper

This is a Scrapy-based web scraper designed to extract company directory information from the Indonesian Ministry of Industry (Kementerian Perindustrian) website. The scraper retrieves company names, addresses, and KBLI (Indonesian Standard Industrial Classification) codes and stores them in a CSV file.

## Features
- Extracts company details from the Kemenperin directory.
- Handles pagination automatically.
- Implements retry logic for handling 403 errors.
- Saves extracted data into CSV format.
- Uses a random download delay to mimic human behavior and avoid blocking.

## Requirements
Make sure you have the following dependencies installed:

- Python 3.x
- Scrapy
- Pandas

You can install the required dependencies using:

```bash
pip install scrapy pandas
```

## Project Structure
```
.
├── kemenperin_spider.py   # Main Scrapy spider
├── output/                # Folder where the scraped data is stored
│   ├── kemenperin.csv     # Output file (appended during each run)
└── README.md              # Documentation
```

## Usage
### Running the Spider
To start scraping, run the following command:

```bash
python kemenperin_spider.py
```

The scraped data will be saved in `output/kemenperin.csv`.

### Handling Errors
If the scraper encounters a `403 Forbidden` error, it will automatically retry up to 5 times.

## Output Format
The extracted data will be saved in CSV format with the following columns:

| No | Perusahaan | Alamat | KBLI |
|----|-----------|--------|------|
| 1  | Company A | Address A | KBLI Code A |
| 2  | Company B | Address B | KBLI Code B |

## Notes
- Ensure that the `output/` directory exists before running the script, or modify the script to create it dynamically.
- The scraper follows pagination to retrieve all available data.

## License
This project is licensed under the MIT License.

## Disclaimer
This scraper is intended for educational and research purposes only. Ensure compliance with the website's terms of service before running the scraper.

## Author
andrepradika