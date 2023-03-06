from bs4 import BeautifulSoup
import requests
import lxml

URL = "https://www.amazon.ca/Apple-MacBook-14-inch-8%E2%80%91core-" \
      "14%E2%80%91core/dp/B09JQL8KP9/?_encoding=UTF8&pd_rd_w=1j1IP&content-" \
      "id=amzn1.sym.b09e9731-f0de-43db-b62a-8954bcec282c&pf_rd_p=b09e9731-f0de-" \
      "43db-b62a-8954bcec282c&pf_rd_r=X9CN4S5JB3SEM6SPYSH5&pd_rd_wg=7s9BV&pd_rd_r=" \
      "92acc695-305f-4c7b-b080-ae2a86078d12&ref_=pd_gw_ci_mcx_mr_hp_atf_m"

header = {
      "Accept-Language": "en-US,en-TR;q=0.9,en;q=0.8,tr-TR;q=0.7,tr;q=0.6",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
}
response = requests.get(URL, headers=header)
web_page = response.text

soup = BeautifulSoup(web_page, "lxml")

price = soup.find(name="span", class_="a-offscreen").getText()

product_price = float(price.replace("$", "").replace(",", ""))
print(product_price)