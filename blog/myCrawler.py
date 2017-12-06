import requests
from urllib import parse
from bs4 import BeautifulSoup

def spider(item_name):
    url_item_name = parse.quote(item_name.encode('euc-kr'))

    url = 'http://search.11st.co.kr/SearchPrdAction.tmall?method=getTotalSearchSeller&isGnb=Y&prdType=&category=&cmd=&pageSize=&lCtgrNo=&mCtgrNo=&sCtgrNo=&dCtgrNo=&fromACK=recent&semanticFromGNB=&gnbTag=TO&schFrom=&schFrom=&ID=&ctgrNo=&srCtgrNo=&keyword=&adUrl=&adKwdTrcNo=&adPrdNo=&targetTab=T&kwd=' + url_item_name
    resp = requests.get(url)
    resp.raise_for_status()

    resp.encoding='euc-kr'
    plain_text = resp.text

    soup = BeautifulSoup(plain_text, 'lxml')
    mytag = soup.find_all(True, {"class": ["sale_price", "list_info"]})

    mytag2 = soup.find_all(True, {"class": ["photo_wrap"]}, "a")


    #for link in soup.select('div.list_info p.info_tit a') :
    data = {}
    count = -1;
    for link in mytag:
        if(link.find('a')):
            count+=1
            href = link.find('a').get('href')        # to get product href
            product_name = link.find('a').string        # to get prouct name
            data[count] = str(href) + ", " + str(product_name)  # add into dictionary
        else:
            product_price = link.string                             # to get product price

            if(product_price):
                data[count] = data[count] +", " + str(product_price).replace(",",".")

    #for value in data.values():
    #    print(value)


    count=0
    for link2 in mytag2:
        if(link2.img):
            data[count] = data[count] + ", " + str(link2.img.get('data-original'))
            count+=1

    resp.close()
    return data

