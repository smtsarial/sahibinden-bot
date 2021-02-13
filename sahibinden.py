
from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup
from time import gmtime, strftime


filename = strftime("%d_%m__%H-%M", gmtime())
ua = UserAgent(cache=False)
ua = ua['google chrome']
headers_dict = {'User-Agent': ua}

#url = "https://www.sahibinden.com/ticari-araclar-kamyon-kamyonet-hino-fb-fb-110?sorting=date_desc"

def page_offset_calcultor():
    offsets = []
    urls = []
    url = "https://www.sahibinden.com/ticari-araclar-kamyon-kamyonet-hino-fb-fb-110?sorting=date_desc"
    for i in range(1, 2):
        a = (i*10*2)-20
        urls.append(url+str(a))
    return urls

def filtre_en_yeni(urls):
    url = []
    for i in urls:
        url.append(i+"&sorting=date_desc")
    return url

def add_sahibindencom(urls):
    newilan_links = []
    for i in urls:
        newilan_links.append("https://www.sahibinden.com"+i)
    return newilan_links

def main(url):
    #urls = page_offset_calcultor()
    #urls = filtre_en_yeni(urls)
    ilan_linksw_titles = []
    ilan_links = []
    ilan_titles = []

    a = "ARANAN LİNK -> "+url
    ilan_linksw_titles.append(a)
    req = requests.get(url, headers=headers_dict)
    context = req.content
    soup = BeautifulSoup(context, "html.parser")

    for link in soup.find_all("td", {"class": "searchResultsLargeThumbnail"}):
        ilan_links.append(link.find("a")["href"])
        ilan_titles.append(link.find("img")["alt"])

    ilan_links = add_sahibindencom(ilan_links)
    
    
    for i in range(len(ilan_links)):
        links = (ilan_titles[i]+ " -> "+ilan_links[i])
        ilan_linksw_titles.append(str(links))

    return ilan_linksw_titles

#TESTER
#print(main(url))