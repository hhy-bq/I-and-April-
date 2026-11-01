import re
s = open("page.txt",encoding='utf-8').read()
title = re.search(r"<title>(.*?)</title>", s).group(1)
print(title)

links = []

for part in s.split('href="')[1:]:
    url = part.split('"')[0]
    if "http" in url:
        print(url)
        links.append(url)

print("链接个数", len(links), "个")
