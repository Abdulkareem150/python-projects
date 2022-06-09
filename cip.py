import requests
from bs4 import BeautifulSoup
login_url= 'https://www.cip.com.ng/login'
data = {
    'username': '08107762646',
    'password': 'Abdulkareem150'
}
with requests.Session() as s:
    response = requests.po


