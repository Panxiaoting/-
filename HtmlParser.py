import re
from urllib.parse import urljoin

from bs4 import BeautifulSoup


class HtmlParser(object):

    def parser(self,page_url,html_cont):
        '''
        用于解析网页内容，抽取URl和数据
        :param page_url: 下载页面的URl
        :param html_cont: 下载页面的内容
        :return: 返回 URL 和数据
        '''
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont,'html.parser')
        new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_new_data(page_url,soup)
        return new_urls,new_data

    def _get_new_urls(self,page_url,soup):

        new_urls = set()

        links = soup.find_all('a',href = re.compile("/item/(%.{2})+$")) #利用正则找出网页符合格式的链接
        for link in links:
            #提起 href 属性
            new_url = link['href']
            #拼接成完整网址
            new_full_url = urljoin(page_url,new_url)
            new_urls.add(new_full_url)
        print(new_urls)
        return new_urls

    def _get_new_data(self,page_url,soup):

        data = {}
        data['url'] = page_url
        title = soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1')
        data['title'] = title.get_text()
        summary = soup.find('div',class_= 'lemma-summary')
        # 获取 tag 中包含的所有文本内容，包括子孙tag中的内容，并将结果作为Unicode 字符串返回
        data['summary'] =summary.get_text()
        return data
