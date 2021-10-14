import command_system
import keyb

def gdesocotdel():
    message = 'Социальный отдел:\n📍Находится во 2 корпусе на 1 этаже – 139/2\n☎Телефон: +7 (812) 326-31-63, доб. 2152\n✉e-mail: osr@spbgut.ru\n⏳Часы работы:\nПонедельник 14:00 - 17:00\nВторник ПРИЕМА НЕТ\nCреда 10:00 - 17:00\nЧетверг ПРИЕМА НЕТ\nПятница 10:00 - 13:00\n🍴Обеденный перерыв: 13:00 - 14:00\n👣ГУТ.Навигатор: nav.sut.ru/?cab=k2-139'
    attachment = ''
    keyboard = {
            "one_time": False,
            "inline": True,
            "buttons": [
                [keyb.get_button(label = 'Меню', color = 'negative')]
            ]
            }


    return message, attachment, keyboard

gdesocotdel_command = command_system.Command()

gdesocotdel_command.keys = ['[club87513693|@vuts.bonch] социальный отдел', 'социальный отдел', 'илья, социальный отдел', 'илья социальный отдел']
gdesocotdel_command.process = gdesocotdel
