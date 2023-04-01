import os
try:
    import requests
except:
    os.system('pip install requests ')
   
try:
    import time
except:
    os.system('pip install time')



g = "\033[1;32m"
r = "\033[1;31m"
id=input(g+' inter your  tele id')
token=input(r+"inter your Tokn bot")
link = input(g+"[~] ادخل رابط المنشور : ")

m=0
try:
	ree = requests.get(link).text
	if "media_id" in ree:
		
		uu = ree.split('media_id":"')[1].split('"')[0]
		print(f"{g}[ {uu} ] DONE GET ID POST")
		time.sleep(2)
		requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text=ايدي منشور{uu}")
		
		url = "https://www.instagram.com/api/v1/media/"+id+"/likers/"
		headers = {
    "Host": "www.instagram.com",
    "user-agent": "Mozilla/5.0 (Linux; Android 7.0; Lenovo K53a48 Build/NRD90N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36",
    "viewport-width": "360",
    "accept": "*/*",
    "x-asbd-id": "198387",
    "x-csrftoken": "Ye7NqApGmQVybvKqBQVwKlceDO0Zht6J",
    "x-ig-app-id": "1217981644879628",
    "referer": link,
    "accept-encoding": "gzip, deflate, sdch, br",
    "accept-language": "ar-EG,ar;q\u003d0.8,en-US;q\u003d0.6,en;q\u003d0.4",
    "cookie": 'mid=Y83WYwABAAG1muBigpOEBOy0R5tI;ig_did=260D38C2-3E35-4FDD-8C11-EDEBB7346E9A;ig_nrcb=1;datr=5z_YY76uvkVOr138hT9g0rQ7;shbid="16500\05457055641229\0541706798795:01f7e936f330355399eb2de81575aabf9e323d8b4f530fe5d93bbd31fe45a07bc3e4add9";shbts="1675262795\05457055641229\0541706798795:01f7f8064121b83986b00931d067bac19271f20e265a56bd3639684e274e472caa833c9d";ig_direct_region_hint="ODN\05457055641229\0541706798805:01f7a1df3ab2af99b37d446bf9322acebddadfcd81c2b5fde83ddb9e2169e1f6403a0797";sessionid='+sessionid+';csrftoken=Ye7NqApGmQVybvKqBQVwKlceDO0Zht6J;rur="LDC\05457055641229\0541706798858:01f7ef09ec77691b2f477880e9ef68bb8e456c392546e0bfb5142248bec0d2e56de7d201";ds_user_id='+ds
		}
		re = requests.get(url,headers=headers)
		for i in re.json()["users"]:
			requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text=ايدي منشور{uh}") 
			pk = (i["pk"])
			m+=1
			
		
	else:
		print(r+" روح ارشق ")
except:print(r+"روح ارشق ")
