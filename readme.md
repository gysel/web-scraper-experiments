# Web scraper

Scrape a website using [scrapy](https://scrapy.org/), identify all PDF files, and download them all.
For example to avoid ad-infested websites with useful content to keep kids busy.

First you run the spider: `scrapy runspider main.py -o pdfs.json`.   
Then you download all found PDFs: `python3 process.py`.
