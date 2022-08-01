from bs4 import BeautifulSoup
import requests
import smtplib
import os

PRODUCT = "https://www.amazon.com/dp/B075VJXQWR?binding=kindle_edition" \
          "&ref_=dbs_s_ks_series_rwt_tkin&qid=1659343264&sr=1-8"

GMAIL_SMTP = "smtp.gmail.com"
FROM_EMAIL = 'testingpythoncode0@gmail.com'
PASSWORD = os.environ['email_password']
TO_EMAIL = 'justkeepitanonymous@gmail.com'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Cookie": "PHPSESSID=cjsq36omd7kbdssahm8c2skf61; _ga=GA1.2.5782469.1659343182; _gid=GA1.2.1392753985.1659343182",
}

response = requests.get(PRODUCT, headers=headers)
product_html = response.text

soup = BeautifulSoup(product_html, parser="lxml", features="lxml")
price = soup.find(class_="a-size-large").getText().split()
price_as_float = float(price[0].split('$')[1])

if price_as_float < 20:
    with smtplib.SMTP(GMAIL_SMTP, port=587) as connection:
        connection.starttls()
        connection.login(FROM_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=FROM_EMAIL,
            to_addrs=TO_EMAIL,
            msg=f"Subject:Low Price for The Godfather\n\nThe price of the book you are monitoring has fallen below $10.\n"
                f"You can buy it here:\n"
                f"{PRODUCT}"
        )

