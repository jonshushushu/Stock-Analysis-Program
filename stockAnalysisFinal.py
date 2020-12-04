"""
Jonny Xue
This program asks a user for an input of the abbreviation of a stock's name. It then pulls data from yahoo finance
to display the price per share, daily and percent change, and the P:E for a specific time

Used stack overflow,online textbook and motley fool for references
"""
import urllib.request
import urllib.parse
from datetime import datetime
import re

#gets time
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

#pulls out also html info from yahoo finance and converts into a string
stockName=input("Please enter abbreviation of stock you want to analyze (Eg.Apple would be AAPL):")
url=('https://finance.yahoo.com/quote/'+stockName+'?p='+stockName+'&.tsrc=fin-srch')
headers={}
headers['User-Agent']="Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"#for espionage purposes
req=urllib.request.Request(url, headers=headers)
resp=urllib.request.urlopen(req)
respData = resp.read().decode('utf-8')

PriceRegex=re.compile(r'data-reactid="33">(\d+,*\d*\.\d+)')
PRmo=PriceRegex.search(respData)
price=PRmo.group(1)

EPSRegex=re.compile(r'data-reactid="71">(\d+,*\d*\.\d+)')
EPSmo=EPSRegex.search(respData)
EPS=EPSmo.group(1)

ChangeRegex=re.compile(r'data-reactid="34">(\+?-?\d+\.\d+\s\(\+?-?\d+\.\d+%\))')
Changemo=ChangeRegex.search(respData)
change=Changemo.group(1)

#Formalizes the pulled info
stockPrice=float(price.replace(',',''))#.replace so it can be turned to float
EPSnum=float(EPS)
PEratio=round(stockPrice/EPSnum,2) #calculates the PE ratio

#displays retrieved info for user
print('Here is the stock analysis for '+stockName+' as of '+current_time)
print('Price per share: ', stockPrice)
print('Earning per share: ', EPS)
print('Daily change and (percent change): ', change)
print('P/E ratio: ',PEratio,'\n^This indicates how much investors are willing to pay for every dollar of earnings,\na high P/E ratio generally indicates that investors expect higher earnings or over-confidence.')

