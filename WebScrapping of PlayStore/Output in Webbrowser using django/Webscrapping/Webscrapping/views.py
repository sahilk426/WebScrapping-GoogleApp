from django.shortcuts import render


def button(request):
	return render(request,"WebScrap.html")



def output(request):
	import requests
	from bs4 import BeautifulSoup
	from google_play_scraper import reviews
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
	print("Developed by "+dev.get_text()+".")
	
	a="Developed by "+dev.get_text()+"."
	
	



	#Description

	print(description)
	

	#Rating

	print("Rated:"+rate.get_text()+" out of 5 stars.")
	b="Rated:"+rate.get_text()+" out of 5 stars."

	#Downloads

	for e in dwnl.stripped_strings:
		d.append(e)
		


	print("Downloaded by more than "+d[5]+" peoples.")
	c="Downloaded by more than "+d[5]+" peoples."
	
	#Reviews

	result, continuation_token =reviews("com.google.android.googlequicksearchbox")
	
	print(result)
	y=result
	
	return render(request,"WebScrap.html",{"data1":a,"data2":description,"data3":b,"data4":c,"data6":y})



