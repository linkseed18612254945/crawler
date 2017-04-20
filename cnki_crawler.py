import requests
from bs4 import BeautifulSoup
import time

BASIC_URL = 'http://kns.cnki.net/kcms/detail/detail.aspx?dbcode=CJFD&filename=XDTQ{0}{1}{2}&dbname=CJFDLAST2015'
BASIC_URL_2 = 'http://kns.cnki.net/kcms/detail/detail.aspx?dbcode=CJFD&filename=XDTQ{0}{1}{2}&dbname=CJFDLAST2015'


def get_url(url):
    r = requests.get(url)
    bf = BeautifulSoup(r.content.decode('utf-8'), 'html.parser')
    r.close()
    return bf

def to_str(n, type):
    if n == 'Z1':
        return n
    if type == 1:
        return str(year)
    elif type == 2:
        if n > 10:
            return str(month)
        else:
            return '0' + str(n)
    else:
        if n < 10:
            return '00' + str(n)
        else:
            return '0' + str(n)


def write_title_abstract(iden, title, abstract):
    address = r'cnki/' + iden + '.txt'
    with open(address, 'a', encoding='utf-8') as f:
        f.write(title + '\n')
        f.write(abstract + '\n')
        f.write('\n')


if __name__ == '__main__':
    year = 2014
    number = 8
    title = ''
    abstract = ''
    for i in range(9, 10):
        month = 'Z1'
        print('开始下载第{0}月'.format(month))
        iden = to_str(year, 1) + to_str(month, 2)
        number = 1
        while True:
            url = BASIC_URL.format(to_str(year, 1), to_str(month, 2), to_str(number, 3))
            bf = get_url(url)
            print(url)
            title = bf.title.string.strip()
            print(title)
            if title == '知网节':
                break
            abstract = bf.find(id='ChDivSummary').string.strip()
            number += 1
            time.sleep(5)
            if abstract[:3] != '<正>':
                write_title_abstract(iden, title[:-7], abstract)