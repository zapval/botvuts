import command_system
import keyb

def gdebyroprop():
    message = 'Бюро пропусков:\n📍Находится во 2 корпусе на 1 этаже – 117/2\n☎Телефон: +7 (812) 326-31-55, доб. 1113\n⏳Часы работы: Пн-Пт 10:00 - 17:30\n🍴Обеденный перерыв: 13:00 - 14:00\n👣ГУТ.Навигатор: nav.sut.ru/?cab=k2-117'
    attachment = ''
    keyboard = {
            "one_time": False,
            "inline": True,
            "buttons": [
                [keyb.get_button(label = 'Меню', color = 'negative')]
            ]
            }


    return message, attachment, keyboard

gdebyroprop_command = command_system.Command()

gdebyroprop_command.keys = ['[club87513693|@vuts.bonch] бюро пропусков', 'бюро пропусков', 'илья, бюро пропусков', 'илья бюро пропусков']
gdebyroprop_command.process = gdebyroprop
