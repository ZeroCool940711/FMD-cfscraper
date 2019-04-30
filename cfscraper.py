import cloudscraper, sys, requests

url = sys.argv[1]

scraper = cloudscraper.create_scraper()  # returns a CloudScraper instance
 
tokens, user_agent = scraper.get_tokens(url)

# print the cloudflare tokens and user_agent used
print tokens, user_agent
