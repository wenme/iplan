# -*- coding: utf-8 -*-

import urllib, urllib2
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import json
import time

EMAIL_HOST = 'smtp.126.com'
EMAIL_USER = 'k332465723'
EMAIL_PASS = '332465723ck'
EMAIL_POSTFIX = '126.com'

def sending_mail(to_email_list):
    smtpserver = 'smtp.'
    subject = u'系统可能无法使用'
    content = u'偷偷告诉你一下：\n\n      刚刚发现系统可能已崩溃了，正常服务无法使用，请尽快登录服务器并排查原因。\n\nBest Wishes,\nCK'
    from_email = EMAIL_USER + '<' + EMAIL_USER + '@' + EMAIL_POSTFIX + '>'
    msg = MIMEText(content.encode('utf-8'))
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = ';'.join(to_email_list)
    try:
        s = smtplib.SMTP()
        s.connect(EMAIL_HOST)
        s.login(EMAIL_USER, EMAIL_PASS)
        s.sendmail(from_email, to_email_list, msg.as_string())
        s.close()
        return True
    except Exception, e:
        print 'email error:', str(e), time.strftime('%Y-%m-%d %H:%M:%S')
        return False

def main():
    data = {
        'account': 'ck',
        'passwd': '332465723'
    }

    url = 'http://api.i-plan.com.cn/common/error_detect/'
    post_data = urllib.urlencode(data)
    try:
        request = urllib2.urlopen(url, post_data)
        ret = request.read()
        ret_json = json.loads(ret)
        if ret_json['response'] == 1:
            print 'it\'s OK!', time.strftime('%Y-%m-%d %H:%M:%S')
        else:
            print 'invalid request!', time.strftime('%Y-%m-%d %H:%M:%S')
    except Exception, e:
        to_email_list = []
        to_email_list.append('332465723@qq.com')
        to_email_list.append('18399251@qq.com')
        to_email_list.append('383985933@qq.com')
        sending_mail(to_email_list)
        print str(e)
        pass

if __name__ == '__main__':
    main()
