import requests

class TiebaSpider():
    def __init__(self,kw,max_pn):#kw,关键词/max_pn，一屏幕多少条
        self.max_pn = max_pn
        self.kw = kw
        self.base_url = "https://tieba.baidu.com/f?kw={}&ie=utf-8&pn={}"
        self.headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
        }
        pass#pass 占位用

    #获取Url列表
    def get_url_list(self):
        #获取列表
        url_list = []
        for pn in range(0,self.max_pn,50):
            url = self.base_url.format(self.kw.pn)
            url_list.append(url)

        return url_list

    def get_content(self,url):
        response = requests.get(
            url = url,
            headers = self.headers
            )
        return response.content

    def run(self):
        #获取url列表
        url_list = self.get_url_list()
        #发送响应请求
        content = self.get_content(url)
        #从响应中提取数据
        items = self.get_items(content,url_list.index(url) + 1)
        # 4. 保存数据
        self.save_items(items)

        pass

    def get_items(self,content,idx):
        '''
        从响应内容中提取数据
        :param content: 
        :return: 
        '''
        with open('08-{}.html'.format(idx),'wb') as f:
            f.write(content)
        return None

    def save_items(self,items):
        '''
        保存数据
        :param items: 
        :return: 
        '''
        pass

if __name__ == '__main__':
    spider = TiebaSpider("英雄联盟", 150)
    spider.run()





