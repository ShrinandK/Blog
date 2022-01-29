# import libraries
from selenium import webdriver
import pandas as pd

# function to extract text from table data
def getData(allData):
    tempData = []
    for data in allData:
        tempData.append(data.text)
    return tempData
     
# setting driver path
DRIVER_PATH = 'C:\Selenium\ChromeDriver/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

columnNames = []
dataToInsert = []

# iterating through pages 1 and 2
for page in range(1,3):
    # giving the url page wise
    basePath = 'https://www.scrapethissite.com/pages/forms/?page_num='+str(page)
    driver.get(basePath)
    
    # extracting the headings once
    if page == 1:
        headingData = driver.find_elements_by_xpath("//th")
        for heading in headingData:
            columnNames.append(heading.text)
        
    # extracting required data
    nameData = getData(driver.find_elements_by_xpath("//td[@class ='name']"))
    yearData = getData(driver.find_elements_by_xpath("//td[@class ='year']"))
    winData = getData(driver.find_elements_by_xpath("//td[@class ='wins']"))
    lossData = getData(driver.find_elements_by_xpath("//td[@class ='losses']"))
    
    # appending the data for final dataframe creation
    dataToInsert.extend(list(zip(nameData,yearData,winData,lossData)))

# closing the opened chrome browser
driver.quit()

# creating dataframe 
df = pd.DataFrame(data = dataToInsert, columns = columnNames[:4])