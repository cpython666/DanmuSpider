# https://api.bilibili.com/x/web-interface/wbi/search/type?search_type=video&keyword=315%E6%99%9A%E4%BC%9A
import requests
import re
import os
class DanmuSpider:
    def __init__(self):
        self.keyword ='315晚会'
        self.page_size=50
        self.cookie = self.get_cookie()
        self.url="https://api.bilibili.com/x/web-interface/wbi/search/type"
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            "cookie": self.cookie,
        }
        self.params = {
            "keyword": self.keyword,
            'search_type':'video',
            'page_size':self.page_size,
            'highlight':0
        }
        self.video_list=[]
        self.file=open(f'{self.keyword}.txt','a',encoding='utf-8')
    def get_cookie(self):
        files=os.listdir()
        if 'mycookie.txt' in files:
            with open('mycookie.txt') as f:
                return f.read()
        elif 'cookie.txt' in files:
            with open('cookie.txt') as f:
                return f.read()
        else:
            raise Exception('请创建一个cookie.txt文件或者mycookie.txt文件，并在其中粘贴你的cookie')
    def get_info(self):
        res = requests.get(self.url, headers=self.headers, params=self.params)
        if res.ok:
            data=res.json()['data']
            print(data)

            self.total=data['numResults']
            self.page_nums=data['numPages']
            print(f"根据你的关键字{self.keyword}，检索到了{data['numResults']}条视频。每页{self.page_size}条的话一共有{self.page_nums}页")
        else:
            raise Exception(f'请求错误，{res.text}')
    def get_danmu(self,top=10):
        counter=0
        for i in range(1,self.page_nums):
            self.params['page']=i
            video_list = requests.get(self.url, headers=self.headers, params=self.params).json()['data']['result']
            for video in video_list:
                print(f'正在解析视频：{video["title"]},视频链接：{video["arcurl"]},弹幕数量：{video["danmaku"]}')
                self.get_danmu_by_aid(video['aid'])
                counter+=1
                if counter==top:
                    return
    def get_danmu_by_aid(self,aid):
        url=f'https://api.bilibili.com/x/web-interface/view?aid={aid}'
        cid=requests.get(url=url,headers=self.headers).json()['data']['cid']
        html=requests.get(f'https://api.bilibili.com/x/v1/dm/list.so?oid={cid}',headers=self.headers).content.decode('utf-8')
        danmu_list=re.findall('<d p=".*?">(.*?)</d>',html)
        print(danmu_list)
        self.file.write('\n'.join(danmu_list))
    # def test(self):
    #     import chardet
    #     headers={
    #         'User-Agent':'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24'}
    #
    #     # self.headers['Accept']='text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'
    #     r=requests.get(f'https://api.bilibili.com/x/v1/dm/list.so?oid=1471465268',headers=headers)
    #     print(r)
    #     print(r.encoding)
    #     encoding = chardet.detect(r.content)['encoding']
    #     print(encoding)
    #     html = r.content.decode(encoding)
    #     print(html)
    def run(self):
        self.get_info()
        self.get_danmu()
d=DanmuSpider()
d.run()

# d.test()
