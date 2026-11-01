s = open("page.txt",encoding='utf-8').read()
a = s.find("<title>")
b = s.find("</title>")
print(a,b)
print(s[a+len("<title>"):b])
print(s.count("DeepSeek"))




links = []

for part in s.split('href="')[1:]:
    url = part.split('"')[0]
    if "http" in url:
        print(url)
        links.append(url)

print("链接个数", len(links), "个")
