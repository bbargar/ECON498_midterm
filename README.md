# ECON498_midterm

# Introduction

This code is meant for web scrapping two different websites. The websites are [coingecko](coingecko.com) and [coinmarketcap](coinmarketcap.com). Through these codes, you can gather live data for a period of time, and parse the data into datasets.

# Installation

# Usage and Steps

Simply put, the code is run in three steps.
`STEP 1`: Run the request codes for both websites at the same time.
`STEP 2`: Run the parse code for one website.
`STEP 3`: Run the parse code for the second website.

In order to run this code, open two terminals. Run `coingecko_request.py` in one terminal and `coinmarketcap_request.py` in the other. 
- It is important to note that these need to run at the same time in order to gather data from the websites close to the same time period. Without doing this, the data loses accuracy in true comparison. 

After requesting the data, run `coinmarketcap_midterm_parse.py` and then run `coingecko_midterm_parse.py`. 
- Following this step, you can run a deeplink code on the request files. See example `coinmarketcap_deeplink.py`. These new files will save under folder name `deep_link_html`. While this is not a necessary step, it could prove useful in gathering more information from each file. In my case, I wrote a deeplink code but found that all the information I was looking for was in my original parsed files, which made deeplink unnecessary. 

# Code Logic

It is necessary to understand what is happening when each code runs. This is explained as follows:

`coinmarketcap_request.py`: will request each of the first 5 pages from [coinmarketcap](coinmarketcap.com) every 15 minutes, for a 48 hour long window. 
- All of the files this code gathers will save under folder name `html_files_cmc`. 

`coinmarketcap_midterm_parse.py`: Because my computer is slow, and the request code brought so much data, I transfered the first 200 files in `html_files_cmc` to a new folder named `new_html_files_cmc`. This is only neccessary if you receive a memory error from your terminal. Following this, this code will parse information from each file in `new_html_files_cmc` and save this parsed information as a dataset named `coinmarketcap_midterm2_dataset.csv` under the folder name `parsed_files_cmc`.

`coingecko_request.py`: will request the first 5 pages from [coingecko](coingecko.com) for the same length of time as coinmarketcap and save to folder name `html_files_cgecko`. Unlike coinmarketcap, this request code uses the API of coingecko due to a request error from coingecko's website. This request code looks slightly different, but runs under the same logic as `coinmarketcap_request.py`. Because this code is requested as API, each file saves as a json array of objects.

`coingecko_midterm_parse.py`: With the same problem of computer memory, I transfered the first 200 files from `html_files_cgecko` into a folder named `new_html_files_cgecko`. This code then parsed information from each file in `new_html_files_cgecko` and saved this information as a dataset named `coingecko_midterm3_dataset.csv` in the folder named `parsed_files_cgecko`. 




