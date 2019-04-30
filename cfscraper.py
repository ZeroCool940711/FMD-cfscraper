import cfscrape, sys

url = sys.argv[1]

scraper = cfscrape.create_scraper()  # returns a CloudflareScraper instance

if "http" or "https" not in scraper:
    url = "http://"+ url
    
tokens, user_agent = cfscrape.get_tokens(url)

# print the cloudflare tokens and user_agent used
print tokens, user_agent