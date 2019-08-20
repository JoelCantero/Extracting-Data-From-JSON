import json,urllib.request, urllib.parse, urllib.error

url = input('Enter location: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
try:
  js = json.loads(data)
except:
  js = None

print('Retrieved', len(data), 'characters')
sum = 0
for comment in js["comments"]:
  sum = sum + int(comment["count"])


print('Count:', len(js["comments"]))
print('Sum:', sum)
