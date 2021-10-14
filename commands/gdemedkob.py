import command_system
import keyb

def gdemedkob():
    message = 'Медицинский кабинет:\n📍Находится в 1 корпусе на 1 этаже – 102/1\n☎Телефон: +7 (812) 305-12-17\n⏳Часы работы: Пн-Пт 10:00 - 15:00\n👣ГУТ.Навигатор: nav.sut.ru/?cab=k1-102'
    attachment = ''
    keyboard = {
            "one_time": False,
            "inline": True,
            "buttons": [
                [keyb.get_button(label = 'Меню', color = 'negative')]
            ]
            }


    return message, attachment, keyboard

gdemedkob_command = command_system.Command()

gdemedkob_command.keys = ['[club87513693|@vuts.bonch] медицинский кабинет', 'медицинский кабинет', 'илья, медицинский кабинет', 'илья медицинский кабинет']
gdemedkob_command.process = gdemedkob
