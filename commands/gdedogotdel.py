import command_system
import keyb

def gdedogotdel():
    message = 'Договорной отдел:\n📍Находится во 2 корпусе на 2 этаже – 214/2\n☎Телефон: +7 (812) 305-12-07, доб. 1347\n✉e-mail: dogovor258@mail.ru\n⏳Часы работы:\nПонедельник 10:00 - 16:00\nВторник 10:00 - 16:00\nСреда 10:00 - 16:00\nЧетверг ПРИЕМА НЕТ\nПятница 10:00 - 16:00\n🍴Обеденный перерыв: 13:00 - 14:00\n👣ГУТ.Навигатор: nav.sut.ru/?cab=k2-214'
    attachment = ''
    keyboard = {
            "one_time": False,
            "inline": True,
            "buttons": [
                [keyb.get_button(label = 'Меню', color = 'negative')]
            ]
            }


    return message, attachment, keyboard

gdedogotdel_command = command_system.Command()

gdedogotdel_command.keys = ['[club87513693|@vuts.bonch] договорной отдел', 'договорной отдел', 'илья, договорной отдел', 'илья договорной отдел']
gdedogotdel_command.process = gdedogotdel
