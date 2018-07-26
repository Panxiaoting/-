import requests



class HtmlDownloader(object):

    def download(self,url):
        if url is None:
            return None

        user_agent = 'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11'
        header = {'User-Agent':user_agent}
        r = requests.get(url,headers= header)
        if r.status_code == 200:
            r.encoding = 'utf-8'
            return r.text
        return None





























