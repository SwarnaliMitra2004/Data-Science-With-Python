import requests
import re

url = "https://raw.githubusercontent.com/selva86/datasets/master/sample.html"

r = requests.get(url)
html = r.text

text = re.findall(r'<[^>]+>(.*?)</[^>]+>', html, re.DOTALL)

print(text)