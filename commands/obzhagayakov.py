import command_system
import keyb

def obzhagayakov():
    message = '👩Заведующая Даниленко Наталья Леонидовна\n⏳Часы работы:\nПонедельник 8:45 - 17:45\nВторник 11:00 - 20:00\nСреда 8:45 - 17:45\nЧетверг 8:45 - 17:45\nПятница 8:45 - 16:30\n👩Паспортистка Костенко Александра Людвиговна\n⏳Часы работы: Вт 11:00 - 16:00\n👥Тип общежития: Коридорный\n📍Адрес: Яковлевский переулок, дом 8 (м. Электросила)\n👬Кол-во проживающих в комнате: 2-4 человека\n💰Цена руб/мес: 3540'
    attachment = 'photo-87513693_457242699', 'photo-87513693_457242698', 'photo-87513693_457242697', 'photo-87513693_457242696'
    keyboard = {
            "one_time": False,
            "inline": True,
            "buttons": [
                [keyb.get_button(label = 'Меню', color = 'negative')]
            ]
            }


    return message, attachment, keyboard

obzhagayakov_command = command_system.Command()

obzhagayakov_command.keys = ['[club87513693|@vuts.bonch] общежитие "яковлевское"', 'общежитие "яковлевское"', 'илья, общежитие "яковлевское"', 'илья общежитие "яковлевское"', 'илья, общежитие яковлевское', 'илья общежитие яковлевское', 'илья, общага яковлевское', 'илья общага яковлевское']
obzhagayakov_command.process = obzhagayakov
