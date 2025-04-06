from imports import ReplyKeyboardMarkup, KeyboardButton, requests, datetime, moon_phase_dict, schedule, time
from import_api import bot, key_api


def keyboard():
    """
    Создаёт клавиатуру с помощью ReplyKeyboardMarkup()

    :return: kb
    """
    kb = ReplyKeyboardMarkup()
    btn_15_min = KeyboardButton('Раз в 5 секунд')
    btn_1_hour = KeyboardButton('Раз в час')
    btn_6_hour = KeyboardButton('Раз в 6 часов')
    btn_disable = KeyboardButton('Выключить')
    kb.add(btn_15_min, btn_1_hour, btn_6_hour, btn_disable)
    return kb


def info_from_api_today():
    """
    Возвращает f-строку с данном от http://api.weatherapi.com/ в нужном формате и виде.

    :return: f'''
День | {datetime.now().strftime("%d.%m.%Y")}
Время | {datetime.now().strftime("%H:%M:%S")}
Погода сейчас | {response.json()["current"]["condition"]["text"]}
Погода на день | {response.json()["forecast"]["forecastday"][0]["day"]["condition"]["text"]}
Температура | {response.json()["current"]["temp_c"]} C
Температура по ощущениям | {response.json()["current"]["feelslike_c"]}
Максимальная температура | {response.json()["forecast"]["forecastday"][0]["day"]["maxtemp_c"]} C
Минимальная температура | {response.json()["forecast"]["forecastday"][0]["day"]["mintemp_c"]} C
Средняя температура | {response.json()["forecast"]["forecastday"][0]["day"]["avgtemp_c"]} C
Время восхода | {datetime.strptime(response.json()["forecast"]["forecastday"][0]["astro"]["sunrise"],
                                   "%I:%M %p").strftime("%H:%M")}
Время заката | {datetime.strptime(response.json()["forecast"]["forecastday"][0]["astro"]["sunset"],
                                  "%I:%M %p").strftime("%H:%M")}
Фаза луны | {moon_phase_dict[moon_phase]}
'''
    """
    response = requests.get(f'http://api.weatherapi.com/v1/forecast.json?key={key_api}&q=Moscow&days=1&aqi=no&\
                              alerts=yes&lang=ru')

    moon_phase = response.json()["forecast"]["forecastday"][0]["astro"]["moon_phase"]

    return f'''
День | {datetime.now().strftime("%d.%m.%Y")}
Время | {datetime.now().strftime("%H:%M:%S")}
Погода сейчас | {response.json()["current"]["condition"]["text"]}
Погода на день | {response.json()["forecast"]["forecastday"][0]["day"]["condition"]["text"]}
Температура | {response.json()["current"]["temp_c"]} C
Температура по ощущениям | {response.json()["current"]["feelslike_c"]}
Максимальная температура | {response.json()["forecast"]["forecastday"][0]["day"]["maxtemp_c"]} C
Минимальная температура | {response.json()["forecast"]["forecastday"][0]["day"]["mintemp_c"]} C
Средняя температура | {response.json()["forecast"]["forecastday"][0]["day"]["avgtemp_c"]} C
Время восхода | {datetime.strptime(response.json()["forecast"]["forecastday"][0]["astro"]["sunrise"],
                                   "%I:%M %p").strftime("%H:%M")}
Время заката | {datetime.strptime(response.json()["forecast"]["forecastday"][0]["astro"]["sunset"], 
                                  "%I:%M %p").strftime("%H:%M")}
Фаза луны | {moon_phase_dict[moon_phase]}
'''


def sender_message(chat_id):
    """
    Отправляет сообщение в чат с информацией от функции info_from_api_today(). Сделано отдельной функцией так как
    schedule просит первый параметр 'job' в виде callable.

    :param chat_id:
    :return:
    """
    bot.send_message(chat_id, info_from_api_today())


def run_schedule():
    """
    Проверка нужности выполнения работы по заданному расписанию.

    :return:
    """
    while True:
        schedule.run_pending()
        time.sleep(1)
