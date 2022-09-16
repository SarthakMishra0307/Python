import requests

payload = {'page':2,'count' : 25}

payload2 = {'username': 'corey', 'password' : 'testing'} 
# res = requests.get("https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
# TIMEOUT: timeout= 3
res = requests.get("https://httpbin.org/get", params=payload)

res2 = requests.post("https://httpbin.org/post", params=payload2)

r_dict = res2.json()
# print(dir(res))

# dir(res)
# help(res)
# res.content
# IMP
# res.headers

print(res.url)
print(r_dict['args'])



