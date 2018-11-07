import requests
from bs4 import BeautifulSoup



proxies = {
	"http":'http://127.0.0.1:8080'
}

# def getHTMLText(url,proxies):
# 	r = requests.get(url,proxies=proxies)
# 	r.raise_for_status()
# 	r.encoding = r.apparent_encoding
# 	return r.text

if __name__ == '__main__':
	i = 1
	url = 'http://www.xicidaili.com/wn/' + str(i)
	r = requests.

	# getHTMLText(url,proxies)
