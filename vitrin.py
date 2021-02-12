
from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup
from time import gmtime, strftime


filename = strftime("%d_%m__%H-%M", gmtime())
ua = UserAgent(cache=False)
ua = ua['google chrome']
headers_dict = {'User-Agent': ua}


#url = "https://www.sahibinden.com/kategori-vitrin?viewType=Classic&category=3530&sorting=date_desc"
def add_sahibindencom(urls):
    newilan_links = []
    for i in urls:
        newilan_links.append("https://www.sahibinden.com"+i)
    return newilan_links

def main(url):
    ilan_links = []
    ilan_titles = []
    ilan_linksw_titles = []
    a = "ARANAN LİNK -> "+ url
    ilan_linksw_titles.append(a)
    req = requests.get(url, headers=headers_dict)
    context = req.content
    soup = BeautifulSoup(context, "html.parser")
   

    for link in soup.find_all("td", {"class": "searchResultsLargeThumbnail"}):
        ilan_links.append(link.find("a")["href"])
        ilan_titles.append(link.find("img")["alt"])

    ilan_links = add_sahibindencom(ilan_links)
   
    
    for i in range(len(ilan_links)):
        #print(ilan_links[i])
        links = (ilan_titles[i]+ " -> "+ilan_links[i])
        ilan_linksw_titles.append(str(links))

    return ilan_linksw_titles

#print(main(url))