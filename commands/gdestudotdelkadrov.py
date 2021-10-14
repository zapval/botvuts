import command_system
import keyb

def gdestudotdelkadrov():
    message = 'Студенческий отдел кадров:\n📍Находится в 1 корпусе на 3 этаже – 305/1\n☎Телефон: +7 (812) 305-12-91, доб. 1407\n⏳Часы работы:\nПонедельник 11:00 - 13:00, 15:00 - 17:00\nВторник 11:00 - 13:00, 15:00 - 17:00\nСреда 11:00 - 13:00, 15:00 - 17:00\nЧетверг ПРИЕМА НЕТ\nПятница 11:00 - 13:00\n🍴Обеденный перерыв: 13:00 - 15:00\n👣ГУТ.Навигатор: nav.sut.ru/?cab=k1-305'
    attachment = ''
    keyboard = {
            "one_time": False,
            "inline": True,
            "buttons": [
                [keyb.get_button(label = 'Меню', color = 'negative')]
            ]
            }


    return message, attachment, keyboard

gdestudotdelkadrov_command = command_system.Command()

gdestudotdelkadrov_command.keys = ['[club87513693|@vuts.bonch] студенческий отдел кадров', 'студенческий отдел кадров', 'илья, студенческий отдел кадров', 'илья студенческий отдел кадров']
gdestudotdelkadrov_command.process = gdestudotdelkadrov
