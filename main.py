import requests
import sys
import time
import random



# stuff for the request
def codemain():

    profile_url = input('Enter your namemc URL: e.g: https://namemc.com/profile/Unpacks.5 ') # defining the url

    with open('/Users/AlecG/Documents/Coding/Web Automation/NameMC Profile Viewbot/proxies.txt', 'r') as f:
        proxies1 = f.read().splitlines()
        proxy2 = random.choice(proxies1)
        
    proxies = {
    'http': f'{proxy2}'
    }


    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'
    headers = {'user-agent': f'{user_agent}'}

    if profile_url == profile_url:
        r = requests.get(f'{profile_url}', proxies=proxies, headers=headers)
        time.sleep(10)
        print(f'Pinged {profile_url} with proxy {proxy2} and status code {r.status_code}')

codemain()

#cls to clr powershell
