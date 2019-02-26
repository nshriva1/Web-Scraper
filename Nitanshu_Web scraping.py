# import libraries
import requests
from bs4 import BeautifulSoup

for i in range(50):
    page = requests.get("https://theyfightcrime.org/")
    soup = BeautifulSoup(page.text, 'html.parser')
    parag = soup.find_all('p')
    str1 = str(parag[1])
    str1 = str1.replace('<p>','').replace("</p>",'')
    str1 = str1.split(".")
    male_file = open('male_file.txt',"a")
    female_file = open("female_file.txt","a")
    male_file.write(str1[0]+"\n")
    female_file.write(str1[1]+"\n")
    male_file.close()
    female_file.close()





