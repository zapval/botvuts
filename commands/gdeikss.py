import command_system
import keyb

def gdeikss():
    message = 'Деканат ИКСС:\n👩Декан Окунева Дарина Владимировна\n📍Находится в 1 корпусе на 5 этаже – 507/1, 509/1, 511/1, 515/1\n☎Телефон: +7 (812) 305-12-49, +7 (812) 305-12-50, +7 (812) 305-12-51\n✉E-mail: okuneva.dv@spbgut.ru\n⏳Часы работы: Пн-Пт 10:00 - 16:00\n🍴Обеденный перерыв: 13:00 - 14:00\n📋Информация подробнее: https://www.sut.ru/education/fakulteti-i-instituti/ikss\n👣ГУТ.Навигатор: nav.sut.ru/?cab=k1-511'
    attachment = ''
    keyboard = {
            "one_time": False,
            "inline": True,
            "buttons": [
                [keyb.get_button(label = 'Меню', color = 'negative')]
            ]
            }


    return message, attachment, keyboard

gdeikss_command = command_system.Command()

gdeikss_command.keys = ['[club87513693|@vuts.bonch] где деканат иксс', 'где деканат иксс', 'илья, где деканат иксс', 'илья где деканат иксс']
gdeikss_command.process = gdeikss
