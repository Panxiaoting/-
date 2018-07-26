import hashlib
import pickle
from pickle import load


class UrlManager(object):
    def __init__(self):
        self.new_urls = self.load_progress('new_urls.txt') # 未爬取 URL 集合
        self.old_urls = self.load_progress('old_urls.txt')# 已爬取 URl 合集

    def has_new_url(self):
        '''
        判断是否有未爬取的URL
        :return:
        '''
        return self.new_url_size() != 0

    def get_new_url(self):

        '''
        获取一个未爬起的URl
        :return:
        '''
        new_url = self.new_urls.pop()
        m = hashlib.md5()
        m.update(new_url.encode())
        self.old_urls.add(m.hexdigest()[8:-8])
        return new_url
    def add_new_url(self,url):
        '''
        将新的URL 添加到未爬取的 URL 集合中
        :param url: 单个url
        :return:
        '''
        if url is None:
            return
        m = hashlib.md5()
        m.update(url.encode())
        url_md5 = m.hexdigest()[8:-8]
        if url not in self.new_urls and url_md5 not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self,urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def new_url_size(self):
        return len(self.new_urls)


    def old_url_size(self):  #已调用
        return len(self.old_urls)

    def load_progress(self,path):
        print('从文件加载进度：%s'% path)
        try:
            with open(path,'rb') as f:
                tmp = load(f)
                return tmp
        except:
            print('无进度文件，创建：%s'% path)
        return set()



































