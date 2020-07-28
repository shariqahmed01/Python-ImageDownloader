import pandas as pd
import urllib.request


opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
urllib.request.install_opener(opener)


def url_to_jpg(i, url, file_path):
    filename = 'image-{}.jpg'.format(i)
    full_path = '{}{}'.format(file_path, filename)
    urllib.request.urlretrieve(url, full_path)
    print('{} saved.'.format(filename))
    return None
FILENAME = 'images.csv'
FILE_PATH = 'images/'

urls = pd.read_csv(FILENAME)


for i, url in enumerate(urls.values):
    url_to_jpg(i, url[0], FILE_PATH)
