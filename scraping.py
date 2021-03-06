# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import datetime as dt

# Function to initialize the browser, create a data dictionary and end WebDriver and return the scraped data
def scrape_all():
    # Initiate headless driver for deployment
    browser = Browser("chrome", executable_path="chromedriver", headless=False)

    # Set the executable path and initialize the chrome browser in splinter
    executable_path = {'executable_path': 'chromedriver'}
    browser = Browser('chrome', **executable_path)



    # Define function
    def mars_news(browser):

        # Visit the mars nasa news site
        url = 'https://mars.nasa.gov/news/'
        browser.visit(url)
        # Optional delay for loading the page
        browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)


        # Set up the HTML parser
        html = browser.html
        news_soup = BeautifulSoup(html, 'html.parser')
        slide_elem = news_soup.select_one('ul.item_list li.slide')

        # Add try/except for error handling
        try:
            # Begin our scraping, scraping title
            slide_elem.find("div", class_='content_title')


            # Use the parent element to find the first `a` tag and save it as `news_title`
            news_title = slide_elem.find("div", class_='content_title').get_text()
            news_title


            # Scraping summary text
            slide_elem.find("div", class_='article_teaser_body').get_text()


            # Use the parent element to find the paragraph text
            news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
            news_p
        except AttributeError:
            return None, None

        return news_title, news_p
    # Set our news title and paragraph variables, we'll be using the mars_news function to pull this data
    news_title, news_p = mars_news(browser)


    # ### Future Images
    # Space Images

    def featured_image(browser):
        # Visit URL
        url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
        browser.visit(url)


        # Find and click the full image button
        full_image_elem = browser.find_by_id('full_image')
        full_image_elem.click()


        # Find the more info button and click that
        browser.is_element_present_by_text('more info', wait_time=1)
        more_info_elem = browser.find_link_by_partial_text('more info')
        more_info_elem.click()


        # Parse the resulting html with soup
        html = browser.html
        img_soup = BeautifulSoup(html, 'html.parser')

        try:
            # Find the relative image url
            img_url_rel = img_soup.select_one('figure.lede a img').get("src")
            img_url_rel
        except AttributeError:
            return None

        # Use the base URL to create an absolute URL
        img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
        
        return img_url


    # Scrape Mars Data: Mars Facts
    def mars_facts():
        try:
            # Scrape the entire table with Pandas
            df = pd.read_html('http://space-facts.com/mars/')[0]
        except BaseException:
            return None

        # Assign columns and set index of dataframe    
        df.columns=['Description', 'Mars']
        df.set_index('Description', inplace=True)
        df


        # Convert our DataFrame back into HTML-ready code using the .to_html() function
        return df.to_html()

    # Scrape the full resolution images    
    def Mars_hemispheres_HDImages(browser):
        # Visit URL
        url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
        browser.visit(url)     
        
        mars_hemispheres = []
        for x in range(4):
            full_image_hem = browser.find_by_css('a.product-item h3')[x]
            full_image_hem.click()

            # Parse the resulting html with soup
            html = browser.html
            img_soup = BeautifulSoup(html, 'html.parser')

            #try:
            # Find the relative image url
            img_url_HD = img_soup.find('a',text='Sample').get('href')
            img_title = img_soup.find('h2', class_='title').text
            #except AttributeError:
            #    return None

            mars_hemispheres.append({'title':img_title,'img_url':img_url_HD}) 

            print("NEW PAGE\n" + browser.html)
            browser.back()
        
        return mars_hemispheres

    # Run all scraping functions and store results in dictionary
    data = {
        "news_title": news_title,
        "news_paragraph": news_p,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "Hemispheres": Mars_hemispheres_HDImages(browser),
        "last_modified": dt.datetime.now()
    }

    # Shut down automated browser
    browser.quit()
    return data

if __name__ == "__main__":
    # If running as script, print scraped data
    print(scrape_all())
