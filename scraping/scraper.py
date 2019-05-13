from selenium import webdriver

import time

driver=webdriver.Chrome()

driver.get('https://www.youtube.com/watch?v=skFOyjFJ4pc')
time.sleep(15)

count = 1

driver.execute_script('window.scrollTo(0, 250);')

SCROLL_PAUSE_TIME = 5


# Get scroll height
last_height = driver.execute_script("return document.documentElement.scrollHeight")
print(last_height)

while count < 10000:
    #now wait let load the comments
    time.sleep(SCROLL_PAUSE_TIME)
    i = str(1000 * count)
    driver.execute_script('window.scrollTo(0, document.documentElement.scrollHeight);')
    print(count)
    count+=1
    new_height = driver.execute_script("return document.documentElement.scrollHeight")
    print(new_height)
    if last_height == new_height:
        break
    last_height = new_height    

count = 0
fd = open("dump.txt", "w+")
comment_div=driver.find_element_by_xpath('//*[@id="contents"]')
comments=comment_div.find_elements_by_xpath('//*[@id="content-text"]')
for comment in comments:
    fd.write(comment.text + "\n")
    count += 1
fd.close()
driver.quit()