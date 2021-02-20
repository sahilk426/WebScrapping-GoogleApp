from google_play_scraper import reviews
result,continuation_token=reviews("com.google.android.googlequicksearchbox")
a=[]
for x in result:
	a.append(x)
	
