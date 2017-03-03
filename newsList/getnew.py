#/usr/bin 
#-*- coding:utf-8 -*-

from selenium import webdriver

def running():
	driver = webdriver.PhantomJS('/Users/jimzezhang/workspace/phantomjs/bin/phantomjs') # or add to your PATH
	driver.set_window_size(1024, 768) # optional
	driver.get('https://google.com/')
	driver.save_screenshot('screen.png') # save a screenshot to disk
	sbtn = driver.find_element_by_css_selector('button.gbqfba')
	sbtn.click()

	 

def main():
	print '*'*10 + ' Beginning '+ '*'*10
	running()
	print '*'*10 + 'Finished' + '*'*10

if __name__ == '__main__':
	main()