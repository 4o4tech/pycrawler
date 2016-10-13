import requests
import json

def getJson():
    url = 'https://www.shanbay.com/read/news/'
    cookie = 'csrftoken=ofiNMhN6e7rvVgf04HhkBcbecSsfZUm6; __utma=183787513.389002341.1468132282.1471585695.1471589324.5; __utmc=183787513; __utmz=183787513.1468132282.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); sessionid=ukekrzs0627fh61mlogeoco7qyufftqp; userid=22911613; SERVER_ID=48d4283e-da342983'
    header={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch, br',
    'Accept-Language':'zh - CN,zh;q = 0.8, en - US;q = 0.6, en;q = 0.4',
    'Cookie': cookie,
    'Host':'www.shanbay.com',
    'Referer':'https:shanbay.com/read/news',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36',
    }
    text = requests.get(url, headers=header).text

    return json.loads(text)

def jsonTodir(text):
    print(text)

def main():
    jsonText = getJson()

    jsonTodir(jsonText)

if __name__ == '__main__':
    main()