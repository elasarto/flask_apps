import time
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

#get Mars content
def scrape():
    browser = init_browser()
    content = {}

#get Mars news story
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    time.sleep(1)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    content["date"] = soup.find("div", class_="list_date").get_text()
    content["headline"] = soup.find("div", class_="content_title").get_text()
    content["text"] = soup.find("div", class_="article_teaser_body").get_text()

#get Mars featured image
    url_2 = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url_2)
    time.sleep(1)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    content["image"] = soup.article.a['data-fancybox-href']

#get Mars weather tweet
    url_3 = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url_3)
    time.sleep(1)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    
    content["weather"] = soup.find("div", class_="js-tweet-text-container").get_text()

 #get Mars facts  
    url_4 = "https://space-facts.com/mars/"
    browser.visit(url_4)
    time.sleep(1)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    
    facts = soup.find_all('tr')
    for fact in facts:
        text = fact.text    
        content["facts"] = text
    

#get Mars hemispheres  
    url_5 = "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"
    browser.visit(url_5)
    time.sleep(1)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    
    items = soup.find_all("div", class_="wide-image-wrapper")
    for item in items:
        link = item.find('a')
        href = link['href']
        text = item.find('h3')
    
        title = text.text
    
        content['hemisphere1'] = href

#get Mars hemispheres  
    url_6 = "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced"
    browser.visit(url_6)
    time.sleep(1)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    
    items = soup.find_all("div", class_="wide-image-wrapper")
    for item in items:
        link = item.find('a')
        href = link['href']
        text = item.find('h3')
    
        title = text.text
    
        content['hemisphere2'] = href

#get Mars hemispheres  
    url_7 = "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced"
    browser.visit(url_7)
    time.sleep(1)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    
    items = soup.find_all("div", class_="wide-image-wrapper")
    for item in items:
        link = item.find('a')
        href = link['href']
        text = item.find('h3')
    
        title = text.text
    
        content['hemisphere3'] = href

#get Mars hemispheres  
    url_8 = "https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"
    browser.visit(url_8)
    time.sleep(1)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    
    items = soup.find_all("div", class_="wide-image-wrapper")
    for item in items:
        link = item.find('a')
        href = link['href']
        text = item.find('h3')
    
        title = text.text
    
        content['hemisphere4'] = href





















    return(content)
  


