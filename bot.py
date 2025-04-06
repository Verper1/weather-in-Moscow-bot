from imports import schedule, threading
from functions import keyboard, sender_message, run_schedule
from import_api import bot


def main():
    """
    Главная функция для работы бота. В ней присутствуют декораторы,
    проверка на выполнения job от schedule с помощью threading.Thread(target=run_schedule, daemon=True).start() и
    проверка ботом новых сообщений с помощью bot.infinity_polling().

    :return:
    """

    @bot.message_handler(commands=['start'])
    def start_command(message):
        """
        Отправляет приветственное сообщение на команду /start.

        :param message:
        :return:
        """

        bot.send_message(message.chat.id, 'Это бот для отправления данных о погоде в Москве. Выбери режим работы:',
                         reply_markup=keyboard())


    @bot.message_handler(func=lambda message: message.text in ['Раз в 5 секунд', 'Раз в час', 'Раз в 6 часов',
                                                               'Выключить'])
    def sender_mode(message):
        """
        Отправляет сообщение в заданном режиме с помощью schedule.every(...).seconds/hours.do(job)

        :param message:
        :return:
        """

        schedule.clear()

        if message.text == 'Раз в 5 секунд':
            schedule.every(5).seconds.do(lambda: sender_message(message.chat.id))
        elif message.text == 'Раз в час':
            schedule.every(1).hour.do(lambda: sender_message(message.chat.id))
        elif message.text == 'Раз в 6 часов':
            schedule.every(6).hours.do(lambda: sender_message(message.chat.id))
        else:
            schedule.clear()


    # Запускаем планировщик в отдельном потоке.
    threading.Thread(target=run_schedule, daemon=True).start()

    # Запускаем бота в работу.
    bot.infinity_polling()
