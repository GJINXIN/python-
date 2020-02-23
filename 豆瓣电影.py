import requests
import json
import re
from lxml import etree
def parse_page(url):
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}

    response=requests.get(url,headers=headers)
    texts=response.content.decode('utf-8')
    html = etree.HTML(texts)
    
    filmname = html.xpath('//div[@class="indent"]/div/table/tr/td/div/a/span/text()')
    i=0
    for each in filmname:
        i+=1
    for j in range(i):
        filmname = html.xpath('//div[@class="indent"]/div/table/tr/td/div/a/span/text()')[j]
        fileitem = html.xpath('//div[@class="indent"]/div/table/tr/td/div/p/text()')[j]
        print(filmname)
        print(fileitem)
        print("  ")
        
    
    


    with open("doubandianying", "wb") as f:
        f.write(response.content)


def main():
    url='https://movie.douban.com/chart'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
    parse_page(url)



if __name__=='__main__':
    main()