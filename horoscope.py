from vk_api import VkApi
from vk_api.utils import get_random_id
from datetime import date
from datetime import datetime
data = open('api.txt','r')
ACCESS_TOKEN = str(data.readline())
ACCESS_TOKEN = ACCESS_TOKEN[:len(ACCESS_TOKEN)-1]
PEER_ID = str(data.readline())
ZODIAC_SIGNS = {'овен':'♈️Овен:',
                'телец':'♉️Телец:',
                'близнецы':'♊️Близнецы:',
                'рак':'♋️Рак:',
                'лев':'♌️Лев:',
                'дева':'♍️Дева:',
                'весы':'♎️Весы:',
                'скорпион':'♏️Скорпион:',
                'стрелец':'♐️Стрелец:',
                'козерог':'♑️Козерог:',
                'водолей':'♒️Водолей:',
                'рыбы':'♓️Рыбы:'}


def horoscopes_for_period(date_from,date_to,zodiac_sign):
    vk_session = VkApi(token=ACCESS_TOKEN)
    vk = vk_session.get_api()
    posts = vk.wall.get(
    domain='neural_horo',
    )['items']
    result=[]
    zodiac_sign=zodiac_sign.lower()
    date_to=date_to.timestamp()
    date_from=date_from.timestamp()
    for i in range(1, len(posts)):
        post_i = posts[i]['text']
        post_i_text=post_i.split()
        formatted_sign=ZODIAC_SIGNS[zodiac_sign]
        poz_1=post_i_text.index(formatted_sign)
        if zodiac_sign!='рыбы':
            poz_of_sign_in_signs_list=list(ZODIAC_SIGNS.keys()).index(zodiac_sign)
            next_sign=list(ZODIAC_SIGNS.keys())[poz_of_sign_in_signs_list+1]
            formatted_next_sign=ZODIAC_SIGNS[next_sign]
            poz_2=post_i_text.index(formatted_next_sign)
            horoscope_for_one_sign = post_i_text[poz_1:poz_2]
        else:
            horoscope_for_one_sign = post_i_text[poz_1::]
        if posts[i]['date']>=date_from and posts[i]['date']<=date_to:
            post_time = posts[i]['date']
            result.append({
                datetime.fromtimestamp(post_time).strftime('%Y-%m-%d %H:%M:%S'):
                          ' '.join(horoscope_for_one_sign)
                          })
    return result


if __name__ == '__main__':
    date_to = datetime(2022,5,12)
    date_from = datetime(2022,5,2)
    zodiac_sign = 'рыбы'
    print(horoscopes_for_period(date_from, date_to, zodiac_sign))
