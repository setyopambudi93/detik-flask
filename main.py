import requests
from bs4 import BeautifulSoup


peramban = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
              'Chrome/95.0.4638.69 Safari/537.36'}

param = {
    'tag_from': 'wp_cb_mostPopular_more'
}
def scraper():
    url = 'https://www.detik.com/terpopuler?'
    req = requests.get(url, params=param, headers=peramban)
    soup = BeautifulSoup(req.text, 'html.parser')
    detik_pop = soup.find('div', 'grid-row list-content')
    ambil_item = detik_pop.find_all('div', 'media media--left media--image-radius block-link')
    data_list =[]
    for item in ambil_item:
        judul = item.find(attrs={'class': 'media__title'}).text
        gambar = item.find('img')['src']
        data_dict ={
            'Judul': judul,
            'Gambar': gambar.replace('?w=220&q=90', '')
        }
        data_list.append(data_dict)

    return data_list