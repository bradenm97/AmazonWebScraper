#Scraping 20 pages of results


from bs4 import BeautifulSoup
import csv
from selenium import webdriver

#getting to next page
def geturl(searchterm):
    template = 'https://www.amazon.com/s?k={}&ref=nb_sb_noss'
    searchterm = searchterm.replace(' ', '+')
    
    #adding next page url data
    url = template.format(searchterm)
    url += '&page={}'
    
    return url

def extract_record(item): 
    atag = item.h2.a
    description = atag.text.strip()
    url = 'https://www.amazon.com' + atag.get('href')
        
    try:
        price_parent = item.find('span', 'a-price')
        price = price_parent.find('span','a-offscreen').text
    except(AttributeError):
        return
    try:
        fullrating = item.i.text
        rating = fullrating[:3]  
    except(AttributeError):
        return
    
    try:
        review_count = item.find('span', {'class': 'a-size-base s-underline-text'}).text
    except(AttributeError):
        return
   
    
    
    result = (description, price, rating, review_count, url)
    
    return result


def main(searchterm):
    driver = webdriver.Chrome()
    
    records = []
    url = geturl(searchterm)
    
    for page in range(1,21):
        driver.get(url.format(page))
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        results = soup.find_all('div', {'data-component-type': 's-search-result'})
        
        for item in results:
            record = extract_record(item)
            if record:
                records.append(record)
                
    driver.close()
    
    with open('amazonresults.csv', 'w', newline ='', encoding ='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Description','Price','Rating','NumberOfReviews','url', searchterm])
        writer.writerows(records)
      
amazonlookup = input("what do you want to look up on Amazon?")

main(amazonlookup)

print("CSV was created for ",amazonlookup)