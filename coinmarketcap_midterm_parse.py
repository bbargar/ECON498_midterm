from bs4 import BeautifulSoup
import os
import glob
import pandas as pd 

if not os.path.exists("parsed_files_cmc"):
	os.mkdir("parsed_files_cmc")

df = pd.DataFrame()

for one_file_name_cmc in glob.glob("new_html_files_cmc/*.html*"):
	# one_file_name_cmc = 'html_files_cmc/coinmarketcap20201030205747.html'
	print(one_file_name_cmc)
	scrape_time = os.path.basename(one_file_name_cmc).replace("coinmarketcap","").replace(".html","")
	f = open(one_file_name_cmc, "rb")
	html = f.read()
	soup = BeautifulSoup(html, "html.parser")
	f.close()

	try:

		currency_table = soup.find("tbody")
		currency_rows = currency_table.find_all("tr")

		for r in currency_rows:
			currency_columns = r.find_all("td")
			# print(len(currency_columns))
			if len(currency_columns)>10:
				currency_price = currency_columns[3].find("a", {"class": "cmc-link"}).text.replace("$","").replace(",","")
				currency_logo = currency_columns[2].find("img", {"class": "coin-logo"})
				currency_name = currency_columns[2].find("p").text
				currency_symbol = currency_columns[2].find("p", {"class": "coin-item-symbol"}).text
				currency_marketcap = currency_columns[6].find("p").text.replace("$","").replace(",","")
				currency_link = currency_columns[2].find("a")["href"]
				currency_24hr = currency_columns[4].find("span").text
				currency_7d = currency_columns[5].find("span").text
				df = df.append({
						'time': scrape_time,
						'price': currency_price,
						'logo': currency_logo,
						'name': currency_name,
						'symbol': currency_symbol,
						'marketcap': currency_marketcap,
						'link': currency_link,
						'24hr': currency_24hr,
						'7d': currency_7d
					}, ignore_index=True)
	except:
		pass

df.to_csv("parsed_files_cmc/coinmarketcap_midterm2_dataset.csv")