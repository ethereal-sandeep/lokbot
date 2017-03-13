# lokbot

Problem Statement
https://github.com/Loktra/software-engineer/blob/master/Web%20Crawler.md

Requirement: pip, scrapy

install scrapy: pip install scrapy

usage: scrapy crawl shopping -a keyword="iphone 7" -a page=2 -o output.json

-a is to supply argument
### The first query is getting the total number of results for a given keyword.
  `example: $ scrapy crawl shopping -a keyword="iphone 7" -o output_query_one.json`
 
### The second query is to find all results for a given keywords on a specified page.
    `$ scrapy crawl shopping -a keyword="iphone 7" -a page=2 -o output_query_two.json`
