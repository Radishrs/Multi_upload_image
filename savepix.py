import urllib
import urllib2

url = 'http://savepic.ru/index.php'
data = {}
data['file'] = '' #open('c:/Cookie].png', 'rb')
data['font1'] = 'decor'
data['font2'] = '14'
data['note'] = ''
data['orient'] = 'h'
data['size1'] = '1'
data['rotate'] = '00'
data['flip'] = '0'
data['mini'] = '300x225'
data['opt1[]'] = 'gallery'

url_value = urllib.urlencode(data)
req = urllib2.Request(url, url_value)
response = urllib2.urlopen(req)
print(response)
the_page = response.read()

def save(html, name):
    open('c:/' + name, 'wb').write(html)
    print('done')

save(the_page, 'pix.html')
