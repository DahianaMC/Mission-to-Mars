# Mission-to-Mars
## Challenge
- Objectives
  - Use BeautifulSoup and Splinter to automate a web browser and scrape high-resolution images for Mars Hemespheres.
  - Use a MongoDB database to store data from the web scrape.
  - Use a web application and Flask to display the data from the web scrape.
  - Use Bootstrap to style the web app.
  
- Summary
  - Obtain high-resolution images for each of Mars's hemispheres using Beautiful and Splinter to scrape the images, click each hemisphere’s link to access the full-resolution image’s URL.
  - Both the image URL string (for the full-resolution image) and the hemisphere title (with the name) were saved using a Python dictionary to store the data using the keys `img_url` and `title`.
  - Append the dictionary with the image URL string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.
  - Using Flask, store the data scraped in a MongoDB.  Finally Bootstrap was used to style the web page.

- Files for challenge:
  - scraping.py (python file to scrape Mars data)
  - app.py (Flask app)
  - templates folder (index.html is inside this folder)
  
## Screenshot of Mission of Mars
![Mission_to_Mars.png](https://github.com/DahianaMC/Mission-to-Mars/blob/master/Mission_to_Mars.png)
  
  
