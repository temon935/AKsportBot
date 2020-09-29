import csv
import os
import time
import requests
from bs4 import BeautifulSoup

URL = 'https://www.fonbet.ru/live/basketball/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                         ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
           'accept': '*/*'}
HOST = 'https://www.marathonbet.ru'
FILE = 'bets.csv'


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_live_data(html):
    soup = BeautifulSoup(html.text, 'html.parser')
    print(soup)
    results = []
    try:
        lig_events = soup.find_all('div', class_='table__match-title-text')
        print(lig_events)
        '''for i in range(len(lig_events)):
            lig_event = soup.find_all('a', class_='event-info-label')[i].get_text(strip=True)
            if lig_event:
                try:
                    team1 = lig_event.split(' - ')[0]
                    team2 = lig_event.split(' - ')[1]
                except:
                    team1 = lig_event.split(' @ ')[0]
                    team2 = lig_event.split(' @ ')[1]
                match_live_result = soup.find_all('div', class_='event-info link')[i].find_next('div', class_='result red').get_text(strip=True)
                scores = match_live_result.split('(')[0]
                score_team1 = int(scores.split(':')[0])
                score_team2 = int(scores.split(':')[1])
                difference = abs(score_team1 - score_team2)
                counter = 0
                for symbol in match_live_result:
                    if symbol == ':':
                        counter += 1
                    else:
                        pass
                if score_team1 > score_team2:
                    favorite = team1
                elif score_team1 < score_team2:
                    favorite = team2
                else:
                    favorite = 'Ничья'
                results.append({
                        'Команда 1': team1,
                        'Команда 2': team2,
                        'Результат': match_live_result,
                        'Текущая разница': difference,
                        'Текущая четверть': (counter-1),
                        'Лидер': favorite
                    })
            else:
                pass'''
    except AttributeError:
        print('scaning...')
        time.sleep(1)
    # return results


def start():
    try:
        a = get_live_data(get_html(URL))
        pass

    except FileNotFoundError:
        pass

    except ValueError:
        pass
start()