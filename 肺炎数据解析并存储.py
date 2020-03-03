import requests
import json
import jsonpath
def parse_page(url):
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 QIHU 360EE'}

    response=requests.get(url,headers=headers)
    texts=response.content.decode('utf-8')
    print(texts)
    state = json.loads(response.content)

    with open("feiyan.json", "w",encoding='utf-8') as f:
        f.write(json.dumps(state,indent=2,ensure_ascii=False))
        print("保存成功")
        
    provincelen = len(state['data'])
    i = 0
    j = 0
    for i in range(provincelen):
        if state['data'][i]['cities'] is None:
            continue    
        citylen = len(state['data'][i]['cities'])
        provincename = state['data'][i]['data']['provinceName']
        confirmedCount = state['data'][i]['data']['confirmedCount']
        curedCount = state['data'][i]['data']['curedCount'] 
        deadCount = state['data'][i]['data']['deadCount'] 
        provincecontent = str(provincename) + "确诊病例:" +str(confirmedCount) + "已治愈" + str(curedCount) + "死亡人数" + str(deadCount)
        with open("feiyan.txt","a") as f:
            f.write(str(provincecontent)+'\n')
        print("  ")
        print(provincename," 确诊病例:",confirmedCount," 已治愈:",curedCount," 死亡人数:",deadCount)
        print("  ")
        for j in range(citylen):
            cityName = state['data'][i]['cities'][j]['cityName']
            diagnosed = state['data'][i]['cities'][j]['diagnosed']
            cured = state['data'][i]['cities'][j]['cured']
            died = state['data'][i]['cities'][j]['died']
            print(cityName," 确诊病例:",diagnosed," 已治愈:",cured," 死亡人数:",died)
            citycontent = str(cityName) + " 确诊病例:"+str(diagnosed) + "已治愈" + str(cured) + "死亡人数" + str(died)
            with open("feiyan.txt","a") as f:
                f.write(str(citycontent)+'\n')
    
    countrylen = len(state['country'])
    c = 0
    for c in range(countrylen):
        countryname = state['country'][c]['provinceName']
        diagnosed = state['country'][c]['diagnosed']
        cured = state['country'][c]['cured']
        died = state['country'][c]['died']
        print(countryname," 确诊病例:",diagnosed," 已治愈:",cured," 死亡人数:",died)


    


def main():
    url='https://m.look.360.cn/events/feiyan'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 QIHU 360EE'}
    parse_page(url)



if __name__=='__main__':
    main()

