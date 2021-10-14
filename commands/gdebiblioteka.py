import command_system
import keyb

def gdebiblioteka():
    message = 'Библиотека:\n📍Находится во 2 корпусе на 1 этаже – 103/2\n⏳Часы работы: Пн-Пт 11:00 - 16:00\n👣ГУТ.Навигатор: nav.sut.ru/?cab=k2-103'
    attachment = ''
    keyboard = {
            "one_time": False,
            "inline": True,
            "buttons": [
                [keyb.get_button(label = 'Меню', color = 'negative')]
            ]
            }


    return message, attachment, keyboard

gdebiblioteka_command = command_system.Command()

gdebiblioteka_command.keys = ['[club87513693|@vuts.bonch] библиотека', 'библиотека', 'илья, библиотека', 'илья библиотека']
gdebiblioteka_command.process = gdebiblioteka
