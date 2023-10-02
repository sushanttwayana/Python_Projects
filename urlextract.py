# package that collects url and allows us to extract and use different urls

from urllib.request import urlopen

page = urlopen("https://facebook.com/")
# print(page.headers)

sourcecode = page.read()
print(sourcecode)