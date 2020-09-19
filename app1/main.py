import requests
from bs4 import BeautifulSoup
import openpyxl

headers = {
     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36' }
url = 'https://www.wildberries.ru/catalog/'


print('Сколько будет категорий')
i=int(input())
print('тепер напишите их нажимая enter после каждой категории')
categorys=[]
for x in range(0,i):
    categorys.append(input())

wb = openpyxl.Workbook()
wb.remove(wb['Sheet'])



for category in categorys:
    wb.create_sheet ( title = '1 лист' , index = 0 )
    new_url=url+category
    fullPage = requests.get ( new_url , headers = headers )
    soup = BeautifulSoup ( fullPage.content , 'html.parser' )
    hrefs = soup.findAll ( "a", {"class":"ref_goods_n_p j-open-full-product-card"} )
    hrefs=[x["href"] for x in hrefs]
    sheet=wb['1 лист']
    i=1
    c=1
    #igrushki/antistress
    h1 = soup.findAll ( "strong" , { "class": "brand-name c-text-sm" } )
    h2 = soup.findAll ( "span" , { "class": "goods-name c-text-sm" } )
    h3 = soup.findAll ( "span" , { "class": "dtList-comments-count c-text-sm" } )
    h4 = soup.findAll ( "span" , { "class": "price" } )
    h5 = soup.findAll ( "del" ,)


    for x in h1:
        cell = sheet.cell ( row = c , column = 1 )
        cell.value = x.text[:-2]
        c+=1
    c=1
    for x in h2:
        cell = sheet.cell ( row = c , column = 2 )
        cell.value = x.text
        c+=1
    c=1
    for x in h3:
        cell = sheet.cell ( row = c , column = 4 )
        cell.value = x.text
        c+=1
    c = 1
    for x in h4:
        cell = sheet.cell ( row = c , column = 7 )
        if x.ins:
            cell.value = x.ins.text
        else:
            cell.value=x.next.text
        c += 1

    for href in hrefs:
        fullPage1 = requests.get ( href , headers = headers )
        soup1 = BeautifulSoup ( fullPage1.content , 'html.parser' )

        buf = soup1.find ( "del" , { "class": "c-text-base" } )
        cell = sheet.cell ( row = i , column = 8 )
        if buf:
            cell.value = buf.text

        buf = soup1.find ( "span" , { "class": "j-article" } )
        cell = sheet.cell ( row = i , column = 3 )
        cell.value = buf.text
        cell = sheet.cell ( row = i , column = 10 )
        cell.value = href

        i+=1



#print(*[x["href"] for x in hrefs])

wb.save('main.xlsx')
