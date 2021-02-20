import requests
from bs4 import BeautifulSoup
import reviews
url="https://play.google.com/store/apps/details?id=com.google.android.googlequicksearchbox"
r=requests.get(url)
htmlContent=r.content
#print(htmlContent)
soup=BeautifulSoup(htmlContent,"html.parser")
dev=soup.find("a",class_="hrTbp R8zArc")
desc=soup.find("meta",property="og:description")
description=desc["content"]
rate=soup.find("div",class_="BHMmbe")
dwnl=soup.find("div",class_="IxB2fe")
d=[]


#Developer Name
print("******************Developer Name******************")
print()
print("Developed by "+dev.get_text()+".")
print()
#Description
print("******************Description******************")
print()
print(description)
print()
#Rating
print("******************Rating******************")
print()
print("Rated:"+rate.get_text()+" out of 5 stars.")
print()
#Downloads
print("******************Number of Downloads******************")
print()
for e in dwnl.stripped_strings:
	d.append(e)
	
#print(d)

print("Downloaded by more than "+d[5]+" peoples.")
print()
#Reviews
print("******************Reviews******************")
print()
for y in reviews.a:
	print()
	print(y)



