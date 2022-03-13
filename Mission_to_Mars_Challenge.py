#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager


# In[14]:


# Import pandas
import pandas as pd


# In[2]:


# Set up Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[4]:


# set up the HTML parser
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[5]:


slide_elem.find('div', class_='content_title')


# In[6]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[7]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# In[9]:


### Featured Images


# # Visit URL
# url = 'https://spaceimages-mars.com'
# browser.visit(url)

# # Find and click the full image button
# full_image_elem = browser.find_by_tag('button')[1]
# full_image_elem.click()

# # Find and click the full image button
# full_image_elem = browser.find_by_tag('button')[1]
# full_image_elem.click()

# In[10]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# # Find the relative image url
# img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
# img_url_rel

# In[15]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[16]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[17]:


df.to_html()


# In[18]:


browser.quit()


# # Start of Mission_to_Mars_Challenge_starter_code

# In[4]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[5]:


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[6]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[7]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[8]:


slide_elem.find('div', class_='content_title')


# In[9]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[10]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# In[11]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[12]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[13]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[14]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[15]:


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[16]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[17]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[18]:


df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# In[20]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# In[55]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
product_soup = soup(browser.html, 'html.parser')
product_list = product_soup     .find('div', class_='collapsible results')     .find_all('div', 'item')

# for each product visit the page, scrape data
for product in product_list:
    # get link for product and visit page    
    link = product.find('a').get('href')
    browser.visit(f"{url}{link}")
    
    # get the html
    hemi_soup = soup(browser.html, 'html.parser')
    
    # get the image title (only 1 h2 on page)  
    hemi_title = hemi_soup.find('h2').text
    
    # get the image link (seek an anchor link labeled Sample)
    hemi_url = hemi_soup.find('a', string="Sample").get('href')
    hemisphere_image_urls.append({
        'img_url': f"{url}{hemi_url}",
        'title': hemi_title })
    browser.back()


# In[56]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[57]:


# 5. Quit the browser
browser.quit()


# In[ ]:




