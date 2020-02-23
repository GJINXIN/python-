import wx
import requests
import json
import jsonpath

def openfile(event):     # 定义打开文件事件
    url='https://m.look.360.cn/events/feiyan'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 QIHU 360EE'}
    parse_page(url)
    

def parse_page(url):
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36 QIHU 360EE'}

    response=requests.get(url,headers=headers)
    texts=response.content.decode('utf-8')
    state = json.loads(response.content)
    provincelen = len(state['data'])
    i = 0
    j = 0
    m=""
    d=""
    for i in range(provincelen):
        citylen = len(state['data'][i]['cities'])
        for j in range(citylen):
            cityName = state['data'][i]['cities'][j]['cityName']
            diagnosed = state['data'][i]['cities'][j]['diagnosed']
            cured = state['data'][i]['cities'][j]['cured']
            died = state['data'][i]['cities'][j]['died']
            
            s =str(cityName)+"  确诊病例"+str(diagnosed)+"  已治愈"+str(cured)+"  死亡人数  "+str(died)
            m = m + s +'\n'
        d =d+m
        content_text.SetValue(d)
          
        
 
app = wx.App()
frame = wx.Frame(None,title = "肺炎疫情实时数据获取",pos = (1000,200),size = (500,400))
 
panel = wx.Panel(frame)
 

open_button = wx.Button(panel,label = "获取疫情信息")
open_button.Bind(wx.EVT_BUTTON,openfile)    # 绑定打开文件事件到open_button按钮上
 
 
content_text= wx.TextCtrl(panel,style = wx.TE_MULTILINE)
#  wx.TE_MULTILINE可以实现以滚动条方式多行显示文本,若不加此功能文本文档显示为一行
 
box = wx.BoxSizer() # 不带参数表示默认实例化一个水平尺寸器

box.Add(open_button,proportion = 2,flag = wx.EXPAND|wx.ALL,border = 3) # 添加组件

 
v_box = wx.BoxSizer(wx.VERTICAL) # wx.VERTICAL参数表示实例化一个垂直尺寸器
v_box.Add(box,proportion = 1,flag = wx.EXPAND|wx.ALL,border = 3) # 添加组件
v_box.Add(content_text,proportion = 5,flag = wx.EXPAND|wx.ALL,border = 3) # 添加组件
 
panel.SetSizer(v_box) # 设置主尺寸器
 
frame.Show()
app.MainLoop()