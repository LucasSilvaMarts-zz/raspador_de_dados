import requests
from parsel import Selector


response = requests.get("https://books.toscrape.com/")
elements_selector = Selector(text=response.text)

thumbnail_url = "div.image_container a::attr(href)"

for url in elements_selector.css(thumbnail_url).getall():
    thumbnail_request = requests.get("https://books.toscrape.com/" + url)
    thumbnail_selector = Selector(text=thumbnail_request.text)
    book_title = thumbnail_selector.css("div.product_main h1")
    print(book_title.get())


print(elements_selector.css("img").getall()[0])
