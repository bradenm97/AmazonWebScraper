### AmazonWebScraper

## Project Overview

I created a web scraper using Pythons Beautiful soup. The script takes in an input from the user. This input is what gets searched in Amazon. The code will loop until every item on the first twenty pages of results have been scrapped.  The scraper is looking into the HTML code grabbing the text associated with different tags. The findings are then ran through a number of error proofing to help us receive clean data. The results are then stored and published into an CSV. A tableau [dashboard](https://public.tableau.com/app/profile/braden.millard/viz/AmazonWebScrapingResultsDashboard1/AmazonWebScrapingDashboard) was created to display the findings.


Lessons Learned

The big take away from this project is how error proofing your code can save you a lot of headaches. Originally, I was going to scrape the raw data, clean in Excel and then build a dashboard in Excel. However, after a few attempts I decided to error proof the Python code and then use visualization tool better suited to this type of data.
