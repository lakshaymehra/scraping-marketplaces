# To run this file, Use:
# scrapy runspider amazon_review.py -o customer_reviews.csv

import scrapy
urls = []

class AmazonReviewSpider(scrapy.Spider):
    name = 'amazon_review'

    def start_requests(self):
        # Look into the Amazon Bestsellers list for ~100 BestSelling Mobile Phones
        base_url = 'https://www.amazon.in/gp/bestsellers/electronics/1389432031/ref=zg_bs_pg_{}?ie=UTF8&pg='
        for i in range(1,3):
            urls.append(base_url.format(str(i)) + str(i))
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # For each mobile, go to the reviews page
        data = response.css('.zg-item')
        data = [x.attrib['href'] for x in data.css('.a-link-normal') if x.attrib['href'].find('/product-reviews/') != -1]
        data = list(set(data))
        data = ['https://amazon.in'+x for x in data]
        for url in data:
            yield scrapy.Request(url=url, callback=self.parse_each_page)

    def parse_each_page(self,response):

        # From the review page, fetch the product title and all the reviews along with star ratings
        data = response

        # Collecting product star ratings
        star_rating = data.css('.a-link-normal').css('.review-rating')

        # Collecting product name
        product_title = data.css('.product-title').css('.a-link-normal')

        # Collecting user reviews/comments
        comment_titles = data.css('.review-title-content')
        comments = data.css('.review-text-content')

        count = 0

        # Combining the results
        for review in star_rating:

            comment = ''.join(comments[count].xpath(".//text()").extract())
            comment = comment.replace('\n','').strip()
            comment_title = ''.join(comment_titles[count].xpath(".//text()").extract()).replace('\n','').strip()
            full_comment = comment_title + ' : ' + comment
            complete_review =  {'Product Name': ''.join(product_title.xpath('.//text()').extract()).strip(),
                   'Star Rating': ''.join(review.xpath('.//text()').extract()).strip(),
                   'Customer Review': full_comment
                   }
            yield complete_review
            count = count + 1
