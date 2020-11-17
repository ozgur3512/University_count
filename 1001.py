import requests
from bs4 import BeautifulSoup

url=requests.get("https://toptalent.co/turkiyedeki-universiteler-listesi")

content=url.content
soup=BeautifulSoup(content,"html.parser")
a=soup.find_all("tr")
while True:
    x=0
    sehir_ismi=input("Sehir ismi gir:")
    for i in a:
        c=i.text
        c=c.replace("\n"," ")

        c=c.split(" ")

        for i in c:
            if(sehir_ismi in i):
                x+=1


    print(x)


