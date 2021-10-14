import command_system
import keyb

def gdestudgor():
    message = 'Студенческий городок:\n📍Находится во 2 корпусе на 1 этаже – 148/2\n☎Телефон: +7 (812) 305-19-12\n✉e-mail: campus@spbgut.ru\n⏳Часы работы:\nПонедельник 10:00 - 13:00\nВторник 10:00 - 16:30\nСреда 10:00 - 16:30\nЧетверг 10:00 - 16:30\nПятница нет приема\n🍴Обеденный перерыв: 13:00 - 14:00\n👣ГУТ.Навигатор: nav.sut.ru/?cab=k2-148'
    attachment = ''
    keyboard = {
            "one_time": False,
            "inline": True,
            "buttons": [
                [keyb.get_button(label = 'Меню', color = 'negative')]
            ]
            }


    return message, attachment, keyboard

gdestudgor_command = command_system.Command()

gdestudgor_command.keys = ['[club87513693|@vuts.bonch] студенческий городок', 'студенческий городок', 'илья, студенческий городок', 'илья студенческий городок']
gdestudgor_command.process = gdestudgor
