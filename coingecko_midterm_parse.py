import os
import glob
import pandas as pd 
import json
import sys
import numpy as np


if not os.path.exists("parsed_files_cgecko"):
	os.mkdir("parsed_files_cgecko")

df = pd.DataFrame()
# print(df)


for html_files_name in glob.glob('new_html_files_cgecko/*.html*'):
	scrape_time = os.path.basename(html_files_name).replace('coingecko','').replace('.html','')
	f = open(html_files_name, 'r')
	print(f)
	json_data = json.load(f)
	# print(json_data)
	
	# print(len(json_data))

	for coin in json_data:
		indexing = json_data.index(coin)
		df = df.append({
			'id': json_data[indexing]['id'],
			'time': scrape_time,
			'symbol': json_data[indexing]['symbol'],
			'image': json_data[indexing]['image'],
			'name': json_data[indexing]['name'],
			'market_cap': json_data[indexing]['market_cap'],
			'market_cap_change_percentage_24h': json_data[indexing]['market_cap_change_percentage_24h'],
			'total_supply': json_data[indexing]['total_supply'],
			'max_supply': json_data[indexing]['max_supply'],
			'current_price': json_data[indexing]['current_price'],
			'price_change_percentage_24h_in_currency': json_data[indexing]['price_change_percentage_24h_in_currency'],
			'price_change_24h': json_data[indexing]['price_change_24h'],
			'ath': json_data[indexing]['ath'],
			'ath_change_percentage':json_data[indexing]['ath_change_percentage'],
			'atl': json_data[indexing]['atl'],
			'atl_change_percentage': json_data[indexing]['atl_change_percentage']
		}, ignore_index=True)

print(df)
df.to_csv("parsed_files_cgecko/coingecko_midterm3_dataset.csv")