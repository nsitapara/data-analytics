import pandas as pd
import requests
from bs4 import BeautifulSoup
from splinter import Browser
import pymongo

def scrape():
        
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    date_list = []
    title_list = []
    url_list = []
    article_data = []
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    # data = soup.find_all('ul', class_='item_list ')
    #     slides = data.find_all('div', class_=)
    slides = soup.find_all('li', class_='slide')

    for item in slides:
        date = item.find('div', class_="list_date")
        url = item.find('a')['href']
        title = item.find('h3')
        paragraph = item.find('div', class_='article_teaser_body')
        link = 'https://mars.nasa.gov/' + url
        # print(date.text)
        # print(link)
        # print(title.text)
        date_list.append(date.text)
        url_list.append(link)
        title_list.append(title.text)
        article_data.append((paragraph.text))


    # for item in url_list:
    #     url = item
    #     browser.visit(url)
    #     html = browser.html
    #     soup = BeautifulSoup(html, 'html.parser')
    #     slides = soup.find_all('div', class_='clearfix')
    #     text_of_article = []
    #     for items in slides:
    #         to_append = items.find_all('p')
    #         for words in to_append:
    #             to_text = words.text
    #             text_of_article.append(to_text)
    #     string_of_list = ''
    #     for txt in text_of_article:
    #         var1 = string_of_list
    #         var2 = txt
    #         string_of_list = var1 + var2
    #     article_data.append(string_of_list)
    #     break


    # print(article_data)

    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)
    client.drop_database('nasa_data')
    db = client.nasa_data
    collection = db.items
    for x in range(len(url_list)):
        post = {
            'title': title_list[x],
            'date': date_list[x],
            'url': url_list[x],
            'paragraph' : article_data[x]
            }
        collection.insert_one(post)
        break
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    slides = soup.find_all('article', class_='carousel_item')[0]
    url = slides['style']
    url = url.split("'")[1]
    base_url = 'https://www.jpl.nasa.gov'
    featured_image_url = base_url + url
    print(featured_image_url)

    db = client.nasa_data
    collection = db.wallpaper
    db = client.nasa_data
    collection = db.featured_image_url
    post = {
        'featured_image_url':featured_image_url
    }
    collection.insert_one(post)

## Mars weather scrape from twitter
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    tweets = soup.find_all('p', class_='TweetTextSize')
    mars_weather = tweets[0].text
    print(mars_weather)
    collection = db.mars_weather
    post = {
        'mars_weather':mars_weather
    }
    collection.insert_one(post)

##Mars facts scrape
    url = 'http://space-facts.com/mars/'
    dataframe = pd.read_html(url)
    dataframe = dataframe[0]
    dataframe = dataframe.rename(columns={0:"Description",\
                                        1:"Information"})
    print(dataframe)

    description = dataframe["Description"].tolist()
    information = dataframe["Information"].tolist()
    zipped = zip(description,information)
    zipped = dict(zipped)
    collection = db.mars_facts
    post = {
        'mars_facts':zipped
    }
    collection.insert_one(post)
    return "scraping done"