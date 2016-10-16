# Crawl taobao modles information

Evironment:python 2.7.11

The website is 'https://mm.taobao.com/json/request_top_list.htm?page='+ **num**
the page number can change.

##Steps
1. Filter the a target class names 'lady-name'
2. Get the names and url id number
3. Analyze the information page is
    *'https://mm.taobao.com/self/info/model_info_show.htm?user_id=' + id
get the information and picture
4.store the name, height,weight,size,bar,shose, img_url in to the mysql


##Feture 

The data will be visialization, show as webpage