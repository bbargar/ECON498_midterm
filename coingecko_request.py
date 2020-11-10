import urllib.request
import os
import datetime
import time


if not os.path.exists('html_files_cgecko'):
	os.mkdir('html_files_cgecko')


# After receiving an Error 403 code from Coingecko's website, it was best to use an API instead
cgecko_one = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=false&price_change_percentage=24h%2C%207d' 
cgecko_two = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=2&sparkline=false&price_change_percentage=24h%2C%207d'
cgecko_three = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=3&sparkline=false&price_change_percentage=24h%2C%207d'
cgecko_four = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=4&sparkline=false&price_change_percentage=24h%2C%207d'
cgecko_five = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=5&sparkline=false&price_change_percentage=24h%2C%207d'


for i in range(192):
	# Start of Coingecko page 1
	current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")
	print(current_time_stamp)
	f = open("html_files_cgecko/coingecko.html" + current_time_stamp + ".html" + "page1", "wb")
	response = urllib.request.urlopen(cgecko_one)
	html = response.read()
	f.write(html)
	f.close()
	time.sleep(15)
	# Start of Coingecko page 2
	current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")
	print(current_time_stamp)
	f = open("html_files_cgecko/coingecko.html" + current_time_stamp + ".html" + "page2", "wb")
	response = urllib.request.urlopen(cgecko_two)
	html = response.read()
	f.write(html)
	f.close()
	time.sleep(15)
	# Start of Coingecko page 3
	current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")
	print(current_time_stamp)
	f = open("html_files_cgecko/coingecko.html" + current_time_stamp + ".html" + "page3", "wb")
	response = urllib.request.urlopen(cgecko_three)
	html = response.read()
	f.write(html)
	f.close()
	time.sleep(15)
	# Start of Coingecko page 4
	current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")
	print(current_time_stamp)
	f = open("html_files_cgecko/coingecko.html" + current_time_stamp + ".html" + "page4", "wb")
	response = urllib.request.urlopen(cgecko_four)
	html = response.read()
	f.write(html)
	f.close()
	time.sleep(15)
	# Start of Coingecko page 5
	current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")
	print(current_time_stamp)
	f = open("html_files_cgecko/coingecko.html" + current_time_stamp + ".html" + "page5", "wb")
	response = urllib.request.urlopen(cgecko_five)
	html = response.read()
	f.write(html)
	f.close()
time.sleep(840)