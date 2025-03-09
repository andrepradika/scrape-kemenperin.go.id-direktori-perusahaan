import scrapy
import pandas as pd
from scrapy.http import Request
from scrapy.crawler import CrawlerProcess
import os

class KemenperinSpider(scrapy.Spider):
    name = "kemenperin"
    start_urls = [
        "https://kemenperin.go.id/direktori-perusahaan?what=&prov=pRBFSgZUsxfx5FxXQaXXma-gMpg0M8mJdzBxwDmg8cM,&hal=_HBcwUtv9eQaoDTpF-qSLaBbxhxyUgTlsTbT5--yBPc,"
    ]

    custom_settings = {
        "DOWNLOAD_DELAY": 3,
        "RANDOMIZE_DOWNLOAD_DELAY": True,
        "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "RETRY_ENABLED": True,
        "RETRY_TIMES": 5,
    }

    def parse(self, response):
        # Check for 403 errors and retry
        if response.status == 403:
            self.logger.warning("403 Forbidden! Retrying...")
            yield Request(response.url, dont_filter=True)

        data = []
        for row in response.css("#newspaper-a tbody tr"):
            nomor = row.css("td:nth-child(1)::text").get()
            perusahaan = row.css("td:nth-child(2) b::text").get()
            alamat = row.css("td:nth-child(2)::text").getall()
            kbli = row.css("td:nth-child(3)::text").get()

            # Clean up the address
            alamat = " ".join([a.strip() for a in alamat if a.strip()])

            data.append({
                "No": nomor,
                "Perusahaan": perusahaan,
                "Alamat": alamat,
                "KBLI": kbli
            })

        # Save data to CSV & Excel
        self.save_data(data)

        # Follow pagination links
        next_pages = response.css(".pagination li a::attr(href)").getall()
        for next_page in next_pages:
            yield response.follow(next_page, callback=self.parse)

    def save_data(self, data):
        df = pd.DataFrame(data)

        # Save CSV (append mode)
        df.to_csv("output/kemenperin.csv", mode="a", header=not os.path.exists("output/kemenperin.csv"), index=False)


if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(KemenperinSpider)
    process.start()
