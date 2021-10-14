import command_system
import keyb

def gdevoenuchstol():
    message = 'Военно-учетный стол:\n📍Находится в 1 корпусе на 2 этаже – 227/1\n☎Телефон: +7 (812) 305-12-34, доб. 1216\n✉e-mail: otdel-2@spbgut.ru\n⏳Часы работы:\nПонедельник 10:00 - 16:00\nВторник 10:00 - 16:00\nСреда ПРИЕМА НЕТ\nЧетверг 10:00 - 16-00\nПятница 10:00 - 15:00\n🍴Обеденный перерыв: 13:00 - 14:00\n👣ГУТ.Навигатор: nav.sut.ru/?cab=k1-227'
    attachment = ''
    keyboard = {
            "one_time": False,
            "inline": True,
            "buttons": [
                [keyb.get_button(label = 'Меню', color = 'negative')]
            ]
            }


    return message, attachment, keyboard

gdevoenuchstol_command = command_system.Command()

gdevoenuchstol_command.keys = ['[club87513693|@vuts.bonch] военно-учетный стол', 'военно-учетный стол', 'илья, военно-учетный стол', 'илья военно-учетный стол']
gdevoenuchstol_command.process = gdevoenuchstol
