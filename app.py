import configparser

from flask import Flask, render_template, request, jsonify
from push import *



config = configparser.ConfigParser()
config.read('config.info')

app = Flask("MsgPush")

Dingtalk_enable = 'MsgDingtalk' in config
EMail_enable = 'MsgEMail' in config


@app.route('/')
def home():
    return index_html()

@app.route('/Dingtalk', methods = ['POST'])
def dtk_api():
    if request.method =='POST' and Dingtalk_enable:
        print(1)
        dingtalk_msg(access_token = config['MsgDingtalk']['access_token'], 
                     secret = config['MsgDingtalk']['secret'], 
                     text_message = f"{request.form['title']}\n{request.form['msg']}")
        return jsonify({'success':'ok'})
    else:
        return jsonify({'success':'no'})

@app.route('/EMail', methods = ['POST'])
def email_api():
    if request.method =='POST' and EMail_enable:
        print(2)

        sendmail(smtp_sever = config['MsgEMail']['smtp_sever'], 
                 smtp_port = config['MsgEMail']['smtp_port'], 
                 login_addr = config['MsgEMail']['login_addr'], 
                 from_addr = config['MsgEMail']['from_addr'], 
                 password = config['MsgEMail']['password'], 
                 to_addr = config['MsgEMail']['to_addr'], 
                 text_title = request.form['title'], 
                 text_message = request.form['msg'])
        return jsonify({'success':'ok'})
    else:
        return jsonify({'success':'no'})

if __name__ == '__main__':
    app.run(host = config['MsgAPP']['host'],
            port = config['MsgAPP']['port'],
            debug=config.getboolean('MsgAPP', 'debug'))
