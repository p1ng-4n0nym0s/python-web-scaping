import requests
from bs4 import BeautifulSoup
import smtplib

URL = "https://www.amazon.in/realme-Sparkling-Blue-64GB-Storage/dp/B07Y6CBZJK/ref=sr_1_7?dchild=1&keywords=realme+6&qid=1589004679&s=electronics&sr=1-7"

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0'}
def check_price():

    page = requests.get(URL,headers=headers)

    soup = BeautifulSoup(page.content,'html.parser')

    title = soup.find(id='productTitle').get_text()
    price = soup.find(id='priceblock_ourprice').get_text()
    converted_price =price[2:8]
    new_converted_price = converted_price.replace(',','',1)
    final_price = float(new_converted_price)

    print(title.strip())
    print(final_price)

    if(final_price > 12500):
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('your-email-here','your-password-here')

    subject = "Price dropped"
    body = "check the link https://www.amazon.in/realme-Sparkling-Blue-64GB-Storage/dp/B07Y6CBZJK/ref=sr_1_7?dchild=1&keywords=realme+6&qid=1589004679&s=electronics&sr=1-7"

    msg = f"Subject: {subject}\n\n\n{body}"

    server.sendmail(
        'your-email-here' ,
        'recipient-email-here', 
        msg
    )
    print('E-mail has been sent!!!')
    server.quit()
while(True):
    check_price()
    time.sleep()