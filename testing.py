import urllib.request
import re
query = input()
query1 = query.replace(" ", "%20")
print(query1)
html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + query1)
ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
print("https://www.youtube.com/watch?v=" + ids[0])
