import smtplib
from itsdangerous import TimedJSONWebSignatureSerializer as serializer
link = 'www.google.com'
# with smtplib.SMTP('smtp.gmail.com',587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.ehlo()
#     smtp.login('ayanshaikh7187@gmail.com','ocxlsqyxxajskdbo')
#     subject = 'Greeting From Ayan'
#     body = f'Hi GOOD MORNING! {link}'
#     msg = f'Subject: {subject}\n\n{body}'
#     smtp.sendmail('ayanshaikh7187@gmail.com','ayanshaikh1522@gmail.com',msg)


SECRET_KEY = 'mo9(&5*%g2(o2@o70s1$=l8bgw!wt%j0jd964hikkqu=l*o4_@'


def give_token(usernames):
    s = serializer(SECRET_KEY,60)
    token = s.dumps({'username1':usernames}).decode('utf-8')
    return token


def sendemail(usernames, email):
    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        links = 'http://localhost:8000/email_confirm/'
        link = give_token(usernames)
        smtp.login('ayanshaikh7187@gmail.com','ocxlsqyxxajskdbo')
        subject = 'Click on the below link for further processs'
        body = f'{links + link}'
        msg = f'Subject: {subject}\n\nClink on the Give Link , which will take you to your last stage of registration\n\n{body}\n\n\nif you did not made this reuest than simply ignore it'
        smtp.sendmail('ayanshaikh7187@gmail.com',email,msg)


sendemail('ayan8125','ayanshaikh1522@gmail.com')