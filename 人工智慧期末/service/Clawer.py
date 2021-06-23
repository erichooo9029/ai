import os
import urllib.request as ur
from bs4 import BeautifulSoup
from urllib import request
import requests
import random
import psycopg2
import json
import time
def getCk101Url(url):
    print("getCk101Url url:" + url)
    # 瀏覽器請求頭（大部分網站沒有這個請求頭可能會報錯）
    index = []
    mheaders = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
    req = request.Request(url,headers=mheaders) #新增headers避免伺服器拒絕非瀏覽器訪問
    page = request.urlopen(req)
    html = page.read()
    soup = BeautifulSoup(html.decode('utf-8'), 'html.parser')
    main = soup.find('div','bt-main-cont')
    search_li = main.find_all('li')
    for li in search_li:
        element = li.find('a').get('href')
        if not element is None:
            index.append(element)

    getOne = index[random.randint(0, len(index)-1)]
    print("getCk101Url back url :" + getOne)
    return getOne

def getCk101Photo(url):
    print("photo url:"+url)
    index = []
    mheaders = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
    req = request.Request(url, headers=mheaders)  # 新增headers避免伺服器拒絕非瀏覽器訪問
    page = request.urlopen(req)
    html = page.read()
    soup = BeautifulSoup(html.decode('utf-8'), 'html.parser')
    main_table = soup.find(id = 'lightboxwrap')
    img_all = main_table.find_all('img')

    for img in img_all:
        element = img.get('file')
        if not element is None:
            index.append(element)

    getOne = index[random.randint(0, len(index)-1)]
    print("photo back url :" + getOne)
    return getOne

def getnhentai():
    index = []
    nowpath = os.path.abspath('./本' )
    mheaders = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
    req = request.Request('https://nhentai.net/g/363218/', headers=mheaders)  # 新增headers避免伺服器拒絕非瀏覽器訪問
    page = request.urlopen(req)
    html = page.read()
    soup = BeautifulSoup(html.decode('utf-8'), 'html.parser')
    main_table = soup.find(class_ = 'lazyload')
    img_all = main_table.find_all('img')

    for img in img_all:
        element = img.get('file')
        ur.urlretrieve(element, os.path.join(nowpath, str(img) + '.jpg'), reporthook=None, data=None)
        #print("已增加第" + str(img) + "頁。")
        time.sleep(1)

def nhentai():
    inFo = ""
    resp = requests.get('https://nhentai.net/g/363218/')
    soup = BeautifulSoup(resp.text, 'html.parser')
    main_titles = soup.find_all('div','gallery')

    for title in main_titles:

        if "Chinese" in caption.text:
            inFo += caption.text.strip() + "\n"
            inFo += "https://nhentai.net/" + cover.find("a")['href'] + "\n"

    return inFo

def ticketInfo1():
    my_headers = {'cookie': 'over18=1;'}
    inFo = ""
    resp = requests.get('https://www.ptt.cc/bbs/Beauty/index.html', headers = my_headers)
    soup = BeautifulSoup(resp.text, 'html.parser')
    main_titles = soup.find_all('div', 'title')

    for title in main_titles:

        if "正妹" in title.text:
            inFo += title.text.strip() + "\n"
            inFo += "https://www.ptt.cc" + title.find("a")['href'] + "\n"

    return inFo
def ticketInfo2():
    my_headers = {'cookie': 'over18=1;'}
    inFo = ""
    resp = requests.get('https://www.ptt.cc/bbs/Gossiping/index.html', headers = my_headers)
    soup = BeautifulSoup(resp.text, 'html.parser')
    main_titles = soup.find_all('div', 'title')

    for title in main_titles:
    
        if "問卦" in title.text:
            inFo += title.text.strip() + "\n"
            inFo += "https://www.ptt.cc" + title.find("a")['href'] + "\n"
        time.sleep(1);
    return inFo

def googlesearchnews():
    inFo = ""
        # Google 搜尋 URL
    google_url = 'https://www.google.com.tw/search'

    # 查詢參數
    my_params = {'q': '疫情新聞'}

    # 下載 Google 搜尋結果
    r = requests.get(google_url, params = my_params)

    # 確認是否下載成功
    if r.status_code == requests.codes.ok:
      # 以 BeautifulSoup 解析 HTML 原始碼
      soup = BeautifulSoup(r.text, 'html.parser')

      # 觀察 HTML 原始碼
      # print(soup.prettify())

      # 以 CSS 的選擇器來抓取 Google 的搜尋結果
      items = soup.select('div.g > h3.r > a[href^="/url"]')
      for i in items:
        # 標題
        inFo += i.text + "\n"
        inFo += i.get('href') + "\n"

        print("標題：" + i.text)
        # 網址
        print("網址：" + i.get('href'))
    return inFo
        
def ticketInfo():
    inFo = ""
    resp = requests.get('https://www.ptt.cc/bbs/Japan_Travel/index.html')
    soup = BeautifulSoup(resp.text, 'html.parser')
    main_titles = soup.find_all('div', 'title')

    for title in main_titles:

        if "遊記" in title.text:
            inFo += title.text.strip() + "\n"
            inFo += "https://www.ptt.cc" + title.find("a")['href'] + "\n"

    return inFo

def imageInfo(url):
    print('IG url:' + url)
    imageUrl = ""
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    image = soup.find("meta", property="og:image")

    imageUrl = image["content"]
    print('image url:' + imageUrl)

    return imageUrl

def exchangeRate(country):
    rateString = ""
    resp = requests.get('http://www.findrate.tw/'+country+'/')
    resp.encoding = "utf-8"
    soup = BeautifulSoup(resp.text, 'html.parser')
    first_table = soup.find('table')
    index = 0
    main_tr = first_table.find_all('tr')
    for title in main_tr:
        index = index + 1
        if index == 2:
            temp = ""
            tdNum = 0
            main_td = title.find_all("td")
            for td in main_td:
                tdNum = tdNum + 1
                if tdNum != 4:
                    temp = temp + td.text + "|"

            temp = temp + "\n"
            rateString += temp

        if index == 3:
            temp = ""
            tdNum = 0
            main_td = title.find_all("td")
            for td in main_td:
                tdNum = tdNum + 1
                if tdNum != 4:
                    temp = temp + td.text + "|"

            temp = temp + "\n"
            rateString += temp

    rateString += "\n連結:http://www.findrate.tw/"+country+"/"
    return rateString

def fruitPrice(fruit):
    fruitString = ""
    resp = requests.get("https://www.twfood.cc/fruit/"+fruit+")")
    resp.encoding = "utf-8"
    soup = BeautifulSoup(resp.text, 'html.parser')
    table = soup.find_all('table', 'table-hover')
    main_tr = table[0].find_all('tr')

    index = 0
    temp = ""
    for tr in main_tr:
        if index%3 == 0:
            main_td = tr.find_all("th")
            if temp != "":
                temp +="\n"

            temp +=  main_td[0].text.strip()

        if index%3 == 1:
            main_str = tr.find_all("span")
            price = tr.find_all("th","vege_chart_th_unit")
            temp +="\n " + str(main_str[0].text).strip() +" "+ str(price[0].text).strip()

        if index%3 == 2:
            main_str = tr.find_all("span")
            price = tr.find_all("th","vege_chart_th_unit")
            temp +="\n " + str(main_str[0].text).strip() +" "+ str(price[0].text).strip()

        index = index + 1

    return temp

def getYahooNews(keyword):

    url = 'https://tw.finance.yahoo.com/news_search.html?ei=Big5&q=' + quote(keyword.encode('big5'))

    #請求網站

    list_req = requests.get(url)

    #將整個網站的程式碼爬下來

    soup = BeautifulSoup(list_req.content, "html.parser")

    

    getNew= soup.find('table',{'id':'newListTable'}) #抓到新聞的table

    getAllNews=getNew.find_all('table');

    

    for i in range(0,len(getAllNews)):

        onebody=getAllNews[i];

        NewTitle=onebody.find_all('a',{'class':'mbody'});

        NewsDt=onebody.find('span',{'class':'t1'});

        if (len(NewTitle) >= 1):

            print("文章標題:"+NewTitle[1].text+NewsDt.text)

        Context=onebody.find_all('span',{'class':'mbody'});

        if(len(Context)>=1):

            print("內文:"+Context[0].text)

        print('');



def getSebUrl(url):
    # 瀏覽器請求頭（大部分網站沒有這個請求頭可能會報錯）
    print(url)
    mheaders = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
    req = request.Request(url,headers=mheaders) #新增headers避免伺服器拒絕非瀏覽器訪問
    page = request.urlopen(req)
    html = page.read()
    soup = BeautifulSoup(html.decode('utf-8'), 'html.parser')
    body = soup.find(id="pins")
    link = body.find_all("li")
    next_link = []
    for li_element in link:
        # print(li_element.find('a').get('href'))
        next_link.append(li_element.find('a').get('href'))

    num = random.randint(1, len(next_link)-1)

    return next_link[num]  # python3 python2版本直接返回html

def getHtmlImgUrl(url):
    print(url)
    index = []
    mheaders = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
    req = request.Request(url, headers=mheaders)  # 新增headers避免伺服器拒絕非瀏覽器訪問
    page = request.urlopen(req)
    html = page.read()
    soup = BeautifulSoup(html.decode('utf-8'), 'html.parser')
    body = soup.find(class_="pagenavi")
    page = body.find_all("a")

    for page_element in page:
        # print(page_element.get('href').split('/'))
        element = page_element.get('href').split('/')
        if element[len(element)-1] != "":
            index.append(int(element[len(element)-1]))

    return url+"/"+str(random.randint(1, index[4]))

def getImage(url):
    print(url)
    mheaders = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
    req = request.Request(url, headers=mheaders)  # 新增headers避免伺服器拒絕非瀏覽器訪問
    page = request.urlopen(req)
    html = page.read()
    soup = BeautifulSoup(html.decode('utf-8'), 'html.parser')
    body = soup.find(class_='main-image')
    img = body.find('img').get('src')

    return  img

def getCk101Url(url):
    print("getCk101Url url:" + url)
    # 瀏覽器請求頭（大部分網站沒有這個請求頭可能會報錯）
    index = []
    mheaders = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
    req = request.Request(url,headers=mheaders) #新增headers避免伺服器拒絕非瀏覽器訪問
    page = request.urlopen(req)
    html = page.read()
    soup = BeautifulSoup(html.decode('utf-8'), 'html.parser')
    main = soup.find('div','bt-main-cont')
    search_li = main.find_all('li')
    for li in search_li:
        element = li.find('a').get('href')
        if not element is None:
            index.append(element)

    getOne = index[random.randint(0, len(index)-1)]
    print("getCk101Url back url :" + getOne)
    return getOne

def getCk101Photo(url):
    print("photo url:"+url)
    index = []
    mheaders = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
    req = request.Request(url, headers=mheaders)  # 新增headers避免伺服器拒絕非瀏覽器訪問
    page = request.urlopen(req)
    html = page.read()
    soup = BeautifulSoup(html.decode('utf-8'), 'html.parser')
    main_table = soup.find(id = 'lightboxwrap')
    img_all = main_table.find_all('img')

    for img in img_all:
        element = img.get('file')
        if not element is None:
            index.append(element)

    getOne = index[random.randint(0, len(index)-1)]
    print("photo back url :" + getOne)
    return getOne

def SqlFindDataUrl():
    #connect info
    host = os.environ['DATABASE_HOST']
    port = os.environ['DATABASE_PORT']
    database = os.environ['DATABASE']
    user = os.environ['DATABASE_USER']
    passwd = os.environ['DATABASE_PASSWORD']

    #construct connect string
    conn = psycopg2.connect(database=database,host=host,user=user,password=passwd,port=port)
    cur = conn.cursor()

    #查共有幾個
    sql = "SELECT count(*) FROM image"
    cur.execute(sql)
    rows=cur.fetchall()

    #random其中一個
    ranId = random.randint(1,int(rows[0][0]))
    takeUrl = "SELECT title,url FROM image WHERE id ={0}".format(ranId)
    cur.execute(takeUrl)
    titleRow = cur.fetchall()

    conn.commit() # 查询时无需，此方法提交当前事务。如果不调用这个方法，无论做了什么修改，自从上次调用#commit()是不可见的
    cur.close()
    conn.close()

    return titleRow[0][1]

def randomIgImage():
    url = SqlFindDataUrl()
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    main_table = soup.find('article')
    img_all = main_table.find_all('img')


def takeDigCurrency(coin):
    resp=""
    url = 'https://max-api.maicoin.com/api/v2/tickers/' + coin
    req = requests.get(url)
    print('resp json:' + req.text)
    output = json.loads(req.text)
    resp += '24小時前價格：' + output['open'] + '\n'
    resp += '24小時內最低價：' + output['low'] + '\n'
    resp += '24小時內最高價：' + output['high'] + '\n'
    resp += '最後交易價:' + output['last']
    return resp

def takeUsdtPremium(price):
    print("price --->" + price)
    target = price.split("@")
    result = ""
    temp = ""

    resp = requests.get('http://www.findrate.tw/USD/')
    resp.encoding = "utf-8"
    soup = BeautifulSoup(resp.text, 'html.parser')
    first_table = soup.find('table')
    index = 0
    main_tr = first_table.find_all('tr')
    for title in main_tr:
        index = index + 1
        if index == 3:
            tdNum = 0
            main_td = title.find_all("td")
            for td in main_td:
                tdNum = tdNum + 1
                if tdNum == 3:
                    temp = td.text
    rate1 = "{:.4f}".format(float(target[1])/float(temp)*100)
    rate2 = "{:.4f}".format(float(target[2])/float("3.67")*100)
    result += "USDT兌NTD溢價率：" + rate1 +'% \n'
    result += "USDT兌AED溢價率：" + rate2 + '% \n'
    result += "USD兌NTD 1:" + temp
    return result

if __name__ == '__main__':
    # Test Function
    # IgUrl = "https://www.instagram.com/p/BymVt2NH5OE/?igshid=7jpeb1f596h6"
    # IString = exchangeRate("JPY")
    # IArray = getCk101Photo('https://ck101.com/thread-5017396-1-1.html')
    # IArray = getImage('https://www.mzitu.com/187752/16')
    # SData = randomIgImage()
    # IArray = takeDigCurrency('usdttwd')
    IArray = takeUsdtPremium("!U溢價@28.34@3.74")
    #k=ticketInfo1()
    #y=ticketInfo()
    z=ticketInfo2()
  
    print(z)
    print(IArray)
