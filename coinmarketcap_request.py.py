import urllib.request
import os
import datetime
import time


if not os.path.exists('html_files_cmc'):
	os.mkdir('html_files_cmc')



cmc_one = 'http://coinmarketcap.com/'
cmc_two = 'http://coinmarketcap.com/2/'
cmc_three = 'http://coinmarketcap.com/3/'
cmc_four = 'http://coinmarketcap.com/4/'
cmc_five = 'http://coinmarketcap.com/5/'



for i in range(192):
	# Start of coinmarketcap page 1
	current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")
	print(current_time_stamp)
	f = open("html_files_cmc/coinmarketcap.html" + current_time_stamp + ".html" + "page1", "wb")
	response = urllib.request.urlopen(cmc_one)
	html = response.read()
	f.write(html)
	f.close()
	time.sleep(15)
	# Start of coinmarketcap page 2
	current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")
	print(current_time_stamp)
	f = open("html_files_cmc/coinmarketcap.html" + current_time_stamp + ".html" + "page2", "wb")
	response = urllib.request.urlopen(cmc_two)
	html = response.read()
	f.write(html)
	f.close()
	time.sleep(15)
	# Start of coinmarketcap page 3
	current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")
	print(current_time_stamp)
	f = open("html_files_cmc/coinmarketcap.html" + current_time_stamp + ".html" + "page3", "wb")
	response = urllib.request.urlopen(cmc_three)
	html = response.read()
	f.write(html)
	f.close()
	time.sleep(15)
	# Start of coinmarketcap page 4
	current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")
	print(current_time_stamp)
	f = open("html_files_cmc/coinmarketcap.html" + current_time_stamp + ".html" + "page4", "wb")
	response = urllib.request.urlopen(cmc_four)
	html = response.read()
	f.write(html)
	f.close()
	time.sleep(15)
	# Start of coinmarketcap page 5
	current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")
	print(current_time_stamp)
	f = open("html_files_cmc/coinmarketcap.html" + current_time_stamp + ".html" + "page5", "wb")
	response = urllib.request.urlopen(cmc_five)
	html = response.read()
	f.write(html)
	f.close()
time.sleep(840)

