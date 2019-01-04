from bs4 import BeautifulSoup
import urllib.request
import re
import csv

url = "https://play.eslgaming.com/team/13114925"
id = url[len(url) - 8:len(url)]
# user = str(input("Please paste the team link. ( Format : https://play.eslgaming.com/team/UNIQUE TEAM ID HERE"))
link = urllib.request.urlopen(url).read()
wins = 0
loss = 0
ties = 0
game = 0
soup = BeautifulSoup(link, 'html.parser')
if "matches" in url:
    text = (soup.find_all("td"))
else:
    text = (soup.find_all("b"))
text = str(text)
# clean = re.sub(r'\<[^>]*\>', '', text)
clean = text
clean = "".join(clean.split())
clean_len = len(clean)

for counter in range(clean_len):
    if clean[counter:counter + 4] == "wins":
        wins = wins + 1
        game = game + 1
        print(clean[counter:counter + 4])
    elif clean[counter:counter + 4] == "loss":
        loss = loss + 1
        game = game + 1
        print(clean[counter:counter + 4])
    elif clean[counter:counter + 5] == "draws":
        ties = ties + 1
        game = game + 1

    elif clean[counter:counter + 17] == "bgcolor=" + '"#7BA37F"':
        wins = wins + 1
        game = game + 1
    elif clean[counter:counter + 17] == "bgcolor=" + '"#EEE295"':
        ties = ties + 1
        game = game + 1

    elif clean[counter:counter + 17] == "bgcolor=" + '"#AC6060"':
        loss = loss + 1
        game = game + 1

print("The team has won", wins, "times, lost", loss, "times and tied", ties, "times.")
print("Has a", float(wins / game * 100), "% Win percentage.")
