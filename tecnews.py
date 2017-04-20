import requests
from bs4 import BeautifulSoup
import simpletool
import os

year = 2014
month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
#month = ['07', '08', '09', '10', '11', '12']
date = 31
page_base = 'http://digitalpaper.stdaily.com/http_www.kjrb.com/kjrb/html/'
count = 0


def tec_craw():
    def wr_content(b_node, file_name):
        global count
        for x in b_node('area'):
            content_id = x['href']
            if content_id[-2:] == str(-1):
                count += 1
                content_page = day_page + content_id
                r_content = requests.get(content_page)
                b_content = BeautifulSoup(r_content.content.decode('utf8'), 'html.parser')
                with open(file_name, 'a', encoding='utf-8') as f:
                    title = b_content.find("div", class_="biaoti")
                    if type(b_content.title.string) is not None:
                        if title.string is not None:
                            f.write('Title--' + title.string + '\n')
                        else:
                            f.write('Title--' + '\n')
                        for p in b_content.find_all('p'):
                            if p.string is not None:
                                sents = p.string.lstrip()
                                f.write(sents + '\n')
                        f.write('\n')


    dir_name = r'C:\Users\Administrator\PycharmProjects\crawler' + '\\' + str(year)
    if str(year) not in os.listdir(r'C:\Users\Administrator\PycharmProjects\crawler'):
        os.mkdir(dir_name)
    for m in month:
        for d in range(1, date+1):
            print('processed: ' + str(year) + '.' + m + '.' + str(d) + ' articles')
            try:
                if len(str(d)) < 2:
                    str_d = '0' + str(d)
                else:
                    str_d = str(d)
                node = 'node_2.htm'
                day_page = page_base + str(year) + '-' + m + '/' + str_d + '/'
                node_page = day_page + node
                r_node = requests.get(node_page)
                b_node = BeautifulSoup(r_node.content.decode('utf8'), 'html.parser')
                if b_node('title')[0].string == '科技网404错误跳转页面!':
                    continue
                nodes = b_node('a', id='pageLink')
                file_name = dir_name + '/' + str(year) + m + str_d
                wr_content(b_node, file_name)
                for i in nodes[1:]:
                    node = i['href']
                    node_page = day_page + node
                    r_node = requests.get(node_page)
                    b_node = BeautifulSoup(r_node.content.decode('utf8'), 'html.parser')
                    wr_content(b_node, file_name)
            except:
                print('-----------------'+m+d+'----------------------')
                continue
if __name__ == '__main__':
    tec_craw()
