import requests
import re

def send(filename):
    url = 'http://savepic.ru/index.php'
    data = {}
    file = {'file': open(filename, 'rb')}
    data['font1'] = 'decor'
    data['font2'] = '14'
    data['note'] = ''
    data['orient'] = 'h'
    data['size1'] = '1'
    data['size2'] = '100x75'
    data['rotate'] = '00'
    data['flip'] = '0'
    data['mini'] = '300x225'
    data['opt1[]'] = 'gallery'

    req = requests.post(url, data=data, files=file)
    return req.content.decode('cp1251')


def save(html, name):
    open('c:/' + name, 'wb').write(html)
    print('done')


def parse(html):
    """
    return image  like:
    http://savepic.ru/4778518.jpg
    """
    maxi = re.findall('id="http" type="text" value="(.+)" size=', html) 
    return maxi[0]


def get_image_url(html):
    big = parse(html)
    mini = big[:len(big)-4] + 'm' + big[-4:]
    return big,mini

def getUrlsByFile(filename):
    return get_image_url(send(filename))

if __name__ == '__main__':
    html = send('d:/tumblr_mh58209cC51qmc07eo1_500.jpg')
    print(html)
    f = parse(html)
    print(get_image_url(f))
