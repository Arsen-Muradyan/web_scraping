from bs4 import BeautifulSoup
import requests
from csv import writer
response = requests.get("https://webscraper.io/test-sites/e-commerce/allinone/computers")

soup = BeautifulSoup(
  response.text,
  "html.parser"
)

products = soup.select("div.row>div.col-sm-4.col-lg-4.col-md-4")
with open("products.csv", "w") as csv_file:
  csv_writer = writer(csv_file)
  headers = ["Title", "Price", "Description"]
  csv_writer.writerow(headers)
  for product in products:
    title = product.find(class_="title").get_text()
    price = product.find(class_="price").get_text().replace("$", "")
    desc = product.find(class_="description").get_text()
    csv_writer.writerow([title, price, desc])
# print(rows)