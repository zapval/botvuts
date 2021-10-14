import command_system
import keyb

def gderts():
    message = 'Деканат РТС:\n👱Декан Кирик Дмитрий Игоревич\n📍Находится в 1 корпусе на 4 этаже – 446/1\n☎Телефон: +7 (812) 305-12-48\n✉E-mail: rs@spbgut.ru\n⏳Часы работы: Пн-Пт 10:00 - 16:00\n🍴Обеденный перерыв: 13:00 - 14:00\n📋Информация подробнее: https://www.sut.ru/education/fakulteti-i-instituti/rts\n👣ГУТ.Навигатор: nav.sut.ru/?cab=k1-446'
    attachment = ''
    keyboard = {
            "one_time": False,
            "inline": True,
            "buttons": [
                [keyb.get_button(label = 'Меню', color = 'negative')]
            ]
            }


    return message, attachment, keyboard

gderts_command = command_system.Command()

gderts_command.keys = ['[club87513693|@vuts.bonch] где деканат ртс', 'где деканат ртс', 'илья, где деканат ртс', 'илья где деканат ртс']
gderts_command.process = gderts
