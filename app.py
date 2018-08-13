import requests
from bs4 import BeautifulSoup
import json



def get_num(city):
    city_json = json.load(open('city.json', 'r', encoding='utf-8'))
    for k, v in city_json.items():
        if k == city:
            return v


def get_soup(city):
    city_num = get_num(city)
    # print(city_num)
    url = 'http://www.weather.com.cn/weather/' + city_num + '.shtml'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        'Cookie': 'HMACCOUNT=44AE9D6C8B4817BD; BAIDUID=C0C5471E571B1E851B4B81612FE9B3B7:FG=1; BIDUPSID=C0C5471E571B1E851B4B81612FE9B3B7; PSTM=1515734692; MCITY=-167%3A; pgv_pvi=9404981248; cflag=15%3A3; FP_UID=149da3d244b0f94aac5144dd80a432ba; BDUSS=WpOMm5wQ0RCSDhPa2F0eHhLS203U3cxSVZPdXVaR1pRN2EyYzBWaUlQOUpCQ1piQVFBQUFBJCQAAAAAAAAAAAEAAAD1exDIenhfNDc2AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEl3~lpJd~5ad; locale=zh'
    }
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    ul_res = soup.find_all('ul', class_='t clearfix')
    for ul in ul_res:
        date = ul.find_all('h1')
        wea = ul.find_all('p', class_="wea")
        tem = ul.find_all('p', class_="tem")
        win = ul.find_all('p', class_="win")

    date_res = [data.string for data in date]
    wea_res = [w['title'] for w in wea]
    tem_res = [t.span.string + '/' + t.i.string for t in tem]
    win_res = [w.em.span['title'] + ' ' + w.i.string for w in win]

    final = {}
    for i in range(len(date_res)):
        final[i] = date_res[i] + ' ' + wea_res[i] + ' ' + tem_res[i] + ' ' + win_res[i]
    print(final)
    return final


if __name__ == '__main__':
    get_soup('乐亭')
