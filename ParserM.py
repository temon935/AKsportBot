import csv
import os
import time
import requests
from bs4 import BeautifulSoup

URL1 = 'https://www.marathonbet.ru/su/betting/6?periodGroupAllEvents=12'
URL2 = 'https://www.marathonbet.ru/su/liveresults.htm?form_name=form&sportMenuMinimized=true&1897129037=on&submit=%D0' \
       '%9F%D0%BE%D0%BA%D0%B0%D0%B7%D0%B0%D1%82%D1%8C '
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                         ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
           'accept': '*/*'}
HOST = 'https://www.marathonbet.ru'
FILE = 'games.csv'


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_live_data(html):
    soup = BeautifulSoup(html.text, 'html.parser')
    results = []
    try:
        lig_events = soup.find_all('a', class_='event-info-label')
        for i in range(len(lig_events)):
            lig_event = soup.find_all('a', class_='event-info-label')[i].get_text(strip=True)
            if lig_event:
                team1 = lig_event.split(' - ')[0]
                team2 = lig_event.split(' - ')[1]
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
                pass
    except AttributeError:
        print('scaning...')
        time.sleep(1)
    return results


def live_data_analysis(results):
    interesting_results = []
    for i in results:
        if i['Текущая разница'] >= 5 and i['Текущая четверть'] >= 3 and i['Текущая разница'] <= 120:
            interesting_results.append(i)
    return interesting_results


def get_data_for_csv(html):
    soup = BeautifulSoup(html.text, 'html.parser')
    events_containers = soup.find_all('div', class_='bg coupon-row')
    events_list = []
    for event in events_containers:
        kfs = event.find_all('span', class_='selection-link active-selection')
        if float(kfs[0].text) < 1.22 or float(kfs[1].text) < 1.22:
            events_list.append({
                'Команда 1': event.find_all('a', class_='member-link')[0].find_next('span').get_text(),
                'Команда 2': event.find_all('a', class_='member-link')[1].find_next('span').get_text(),
                'Кэф 1': f"к{kfs[0].text}",
                'Кэф 2': f"к{kfs[1].text}",
                'Время': event.find_all('td', class_='date')[0].get_text(strip=True)
            })
        else:
            pass
    return events_list


def save_file(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Команда 1', 'Команда 2', 'Кэф 1', 'Кэф 2', 'Время'])
        for item in items:
            writer.writerow([item['Команда 1'], item['Команда 2'], item['Кэф 1'],
                             item['Кэф 2'], item['Время']])


def file_work(interesting_results):
    with open('games.csv') as f:
        reader = csv.DictReader(f, delimiter=';')
        stroki = ''
        for row in reader:
            kf1 = float(str(row['Кэф 1'])[1:])
            kf2 = float(str(row['Кэф 2'])[1:])
            if kf1 < kf2:
                leader = str(row['Команда 1'])
                looser = str(row['Команда 2'])
            elif kf1 > kf2:
                leader = str(row['Команда 2'])
                looser = str(row['Команда 1'])

            for i in interesting_results:
                if i['Лидер'] == looser:
                    stroki += (f"Матч: {i['Команда 1']} - {i['Команда 2']}\nФаворит: {leader}\n"
                          f"Счет: '{i['Результат']}'\nкэфы перед матчем: {kf1} - {kf2}\n\n")

                else:
                    pass

        if stroki != '':
            return stroki
        else:
            pass




def start():
    try:
        a = get_live_data(get_html(URL2))
        b = live_data_analysis(a)
        stroka = file_work(b)
        if stroka != None:
            return stroka
        else:
            pass

    except FileNotFoundError:
        print('Формирую расписание...')
        a1 = get_data_for_csv(get_html(URL1))
        save_file(a1, FILE)



