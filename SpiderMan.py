from DataOpuput import DataOutput
from HtmlDownloader import HtmlDownloader
from HtmlParser import HtmlParser
from URLManager import UrlManager


class SpiderMan(object):
    def __init__(self):
        self.manager = UrlManager()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.output = DataOutput()
    def crawl(self,root_url):
        # 添加入口 URl
        self.manager.add_new_url(root_url)

        n = 0
        # 判断 URL 管理器中是否有新的url，同时判断抓取量多少个 URl
        while (self.manager.has_new_url() and self.manager.old_url_size() < 100):
            try:

                # 从 URl 管理器获取新的 url
                new_url = self.manager.get_new_url()

                # 从 Html 下载器下载网页
                html = self.downloader.download(new_url)

                # HTML 解析器抽取网页数据
                new_urls,data = self.parser.parser(new_url,html)
                if n == 0:
                    # 将抽取的 urls 添加到URL 管理器中
                    self.manager.add_new_urls(new_urls)

                # 数据存储器 存储文件
                self.output.store_data(data)
                n +=1


                print('已经抓取%s个连接'% self.manager.old_url_size())

            except Exception as e:
                print(e)
        # 数据存储器将文件输出成指定格式
        self.output.output_html(self.output.filepath)
        self.output.output_end(self.output.filepath)

if __name__ == '__main__':
    spider_man = SpiderMan()
    print('spider_man 完成')
    spider_man.crawl('https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB')
















