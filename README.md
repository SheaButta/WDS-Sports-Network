# WDS-Sports-Network

## Overview of Project

### Purpose
The purpose of this project was to analyze sports websites to determine the best site reporting information on the NCAA National Football Championship.  Once I determined the site with the most valuable information, I began to inspect the site code and narrow down parent takes and determine if there was a pattern that I could use to consistently capture the necessary data to report on the NCAA National Football Championship.  


__Requirements for Project__
- Load data into MongoDB
- Visualize using Flask

## Resources
- Pandas
- HTML/JavaScript/BootStrap 
- Flask
- Splinter
- Beautiful Soup
- Visual Studio
- MongoDB

  
## Results
My analysis determined the best resource to scrape and report on the required information for the NCAA National Football Championship.  After scraping the information from the resource, I loaded the data into a MongoDB database.  The data was loaded into a collection that will maintain a list of dictionaries going forward.

The below illustrates a scraping of data that was loaded into MongoDB for test purposes.  Each scrape spent the least amount of time in a site and closed the browser accordingly.

![WDS Sport Report](https://github.com/SheaButta/Mission-to-Mars/blob/main/images/Mars_factsheet_table.PNG)

The below illustrates a "PreGame" scraping of data that was loaded into MongoDB in preparation for the NCAA Football Championship game.  Each scrape spent the least amount of time in a site and closed the browser accordingly.

![Mars Hemispheres](https://github.com/SheaButta/Mission-to-Mars/blob/main/images/Mars_hemisphere_Images.PNG)

Once the scraping and load completed, the data was visualized via a Flask application utilizing JavaScript and BootStrap.  An interested user will just click the "Game Update" button to get the most up-to-date information related to this championship game.


## Summary
After I started working, it became evident that Flask is extremely powerfull and actually actually has a data file structure where specific files must be placed.  Mostly notibly are the "index.html" which should be located in the /templates directory and any website images should be located in the /static directory.  

![](https://github.com/SheaButta/Mission-to-Mars/blob/main/images/Mission-to-Mars_title.PNG)

 





