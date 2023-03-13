# sayari_scraper
## main.py

This code defines a Scrapy spider called CompanySpider which starts at the URL https://firststop.sos.nd.gov/search/business. The parse method fills out and submits the search form to search for companies whose names start with "X". The parse_results method extracts the company data from the search results table and saves it to a CSV file called companies.csv.

## plot.py

This code maps the nodes and its connecting endes to generate a graph for entity resolution
