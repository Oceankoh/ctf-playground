import requests
import string
#!"#$%&\'()*+, -./:;<=>?@[\]^_
charset = '`{|}~\n\t\r' 

for char in charset:
    r = requests.post(
        "https://0ac4007c04989b4cc0a88cc1003c00b2.web-security-academy.net/post/comment",
        data={
            "csrf": "PNICJUBOLMTp5k69IUKeCRtoWUOi6Ubx",
            "postId": "9",
            "comment": "comment",
            "name": 'name',
            "website": f"http://website.com{char}",
            "email": "email@email.com"
        },
        cookies={
            'session': '3WwHcsPjmFi6NBE6aETH0jKpgMWvs9Vm'
        }
    )
    print(char)
