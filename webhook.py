import requests
import json

webhook_url = 'http://127.0.0.1:5000/webhook'
# BANK side like SBI,HDFC bank OR razorpay (it act like server side, which will return response to webhook.py)
data = { 'name': 'ssddds Journey', 
         'Channel URL': 'https://www.youtube.com/channel/UC4Snw5yrSDMXys31I18U3gg' }

r = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})

