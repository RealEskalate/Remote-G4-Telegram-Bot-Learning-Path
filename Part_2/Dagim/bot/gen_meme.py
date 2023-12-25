import requests
from bs4 import BeautifulSoup
import random 


class Genmeme: 
    def __init__(self ):
        pass 

    def generate(self):
        url = f"https://programmerhumor.io/memes/api/page/{str(random.randint(1,20))}/"
        print(url)
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")
        img = soup.findAll("div", class_="g1-frame-inner")
        img_list = []
        for i in img:
            
            a = i.findAll("img")
            # print(a)
            for j in a:
                img_list.append(j['data-src'])
        return random.choice(img_list)
    


