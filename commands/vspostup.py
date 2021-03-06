import command_system
import keyb

def vspostup():
    message = '🎖Военнослужащие запаса готовятся по программам подготовки солдат/офицеров запаса, возможность обучения по которым предоставляется студентам 2 и 3 курса ЛЮБОГО факультета СПбГУТ.\n\n🎖Отбор начинается ориентировочно В НАЧАЛЕ ОКТЯБРЯ:\n• Из числа студентов 2 курса сроком обучения 2,5 года по программе офицеров запаса;\n• Из числа студентов 3 курса сроком обучения 1,5 года по программе солдат запаса;\n• Набор девушек НЕ ОСУЩЕСТВЛЯЕТСЯ.\n\n📍Адрес: Английский проспект, д.3\n\nПри подаче заявления при себе иметь:\n• Паспорт гражданина РФ и копию (стр. 2, 3 или копию справки о регистрации по месту временного пребывания);\n• Приписное свидетельство и ксерокопию (стр. 1, 2, 3, 4);\n• Четыре фотографии размером 3х4 см без головного убора, черно-белые, матовые.\n\n🎖Памятка студентам СПбГУТ представлена документом ниже.\n\n🎖Документ с таблицами перевода физической подготовки и среднего балла за обучения представлена документом ниже.\n\n🎖По всем возникающим вопросам обращаться к @id174326837 (Евгению Бабурину).'
    attachment = 'doc436020620_570798450', 'doc-194336319_607468877'
    keyboard = {
            "one_time": False,
            "inline": True,
            "buttons": [
                [keyb.get_button(label = 'Статистика прошлого года', color = 'secondary')],
                [keyb.get_button(label = 'Меню', color = 'negative')]
            ]
            }


    return message, attachment, keyboard

vspostup_command = command_system.Command()

vspostup_command.keys = ['[club87513693|@vuts.bonch] поступление на в/с запаса', 'поступление на в/с запаса', 'илья, поступление на в/с запаса', 'илья поступление на в/с запаса']
vspostup_command.process = vspostup
