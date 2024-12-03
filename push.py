import time
import hmac
import hashlib
import base64
import urllib.parse
import requests
import json

from email.mime.text import MIMEText
from email.utils import formataddr
import smtplib
import random
def dingtalk_msg(access_token, secret, text_message):
    # 生成签名
    timestamp = str(round(time.time() * 1000))
    secret_enc = secret.encode('utf-8')
    string_to_sign = f'{timestamp}\n{secret}'
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))

    # 构造请求URL
    webhook_url = f"https://oapi.dingtalk.com/robot/send?access_token={access_token}&timestamp={timestamp}&sign={sign}"

    # 消息内容
    message = {
        "msgtype": "text",
        "text": {
            "content": text_message
        }
    }

    # 发送消息
    headers = {
        "Content-Type": "application/json",
        "timestamp": timestamp,
        "sign":sign
    }

    response = requests.post(webhook_url, data=json.dumps(message), headers=headers)

    # 检查响应
    if response.status_code == 200:
        print("Message sent successfully!")
        print("Response:", response.json())
    else:
        print("Failed to send message.")
        print("Status code:", response.status_code)
        print("Response:", response.text)



def sendmail(smtp_sever, smtp_port, login_addr, from_addr, password, to_addr, text_title = '', text_message = ''):
    sever = smtplib.SMTP(smtp_sever,int(smtp_port))
    sever.starttls()
    sever.login(login_addr,password)
    
    msg = MIMEText(text_message, 'plain', 'utf-8')
    msg['From'] = formataddr((from_addr.split('@')[0], from_addr)) 
    msg['To'] = formataddr((to_addr.split('@')[0], to_addr)) 
    msg['Subject'] = text_title


    sever.sendmail(from_addr,to_addr,msg.as_string())

    sever.quit()


def index_html():
    return '''
    <html>
    <head>
        <title>Universal Message Push System</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                background-color: #f9f9f9;
                color: #333;
                padding: 50px;
            }
            h1 {
                font-size: 3em;
                color: #cc0000;
            }
            p {
                font-size: 1.2em;
                color: #555;
            }
            footer {
                margin-top: 30px;
                font-size: 0.9em;
                color: #666;
            }
        </style>
    </head>
    <body>
        <h1>Welcome to UMPF</h1>
        <p>Message Push System</p>
        <footer>UMPF Gateway v1.0.0</footer>
    </body>
    </html>
    '''