import scrapy
from scrapy.crawler import CrawlerProcess
import csv

'''
This code defines a Scrapy spider called CompanySpider which starts at the URL https://firststop.sos.nd.gov/search/business. The parse method fills out and submits the search form to search for companies whose names start with "X". The parse_results method extracts the company data from the search results table and saves it to a CSV file called companies.csv.
'''

class CompanySpider(scrapy.Spider):
    name = 'companies'
    start_urls = ['https://firststop.sos.nd.gov/search/business']
    
    def parse(self, response):
        # find the form
        form = response.xpath('//form[@id="entitysearchform"]')
        
        # fill out the form
        formdata = {
            'ctl00$MainContent$frmSearch$txtSearchCriteria': 'X',
            'ctl00$MainContent$frmSearch$btnSearch': 'Search',
            '__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            '__LASTFOCUS': '',
            '__VIEWSTATE': response.xpath('//input[@id="__VIEWSTATE"]/@value')
                                .extract_first(),
            '__VIEWSTATEGENERATOR': response.xpath('//input[@id="__VIEWSTATEGENERATOR"]/@value')
                                        .extract_first(),
            '__EVENTVALIDATION': response.xpath('//input[@id="__EVENTVALIDATION"]/@value')
                                    .extract_first()
        }
        
        # submit the form and call the parse_results method
        yield scrapy.FormRequest.from_response(form, formdata=formdata, callback=self.parse_results)
    
    def parse_results(self, response):
        # get the table rows containing the companies
        rows = response.xpath('//table[@id="MainContent_dgrdSearchResults"]/tr')
        
        # create a CSV file to store the results
        with open('companies.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Company', 'Registered Agent', 'Owners'])
            
            # iterate over the rows and extract the company data
            for row in rows[1:]:
                company_name = row.xpath('td[1]/a/text()').extract_first().strip()
                registered_agent = row.xpath('td[2]/text()').extract_first().strip()
                owners = row.xpath('td[3]/text()').extract_first().strip()
                
                # write the data to the CSV file
                writer.writerow([company_name, registered_agent, owners])


if __name__=="__main__":
    # Create an instance or CrawlerProcess and name it process
    process = CrawlerProcess()
    process.crawl(CompanySpider)
    process.start()
    