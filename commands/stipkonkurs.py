import command_system
import keyb

def stipkonkurs():
    message = 'Если Вы являетесь студентом ИКТВ-XX, то можете подать заявление на дополнительные стипендии за достижения и учебу.\n\n✅Сбор заявлений на Повышенную ГА стипендию, Именные стипендии происходит 2 раза в год в СЕНТЯБРЕ и в ФЕВРАЛЕ.\n\n✅Сбор заявлений на Стипендию Президента/Правительства РФ по приоритетным направлениям происходит в ФЕВРАЛЕ.\nДля данной стипендии выбираются те студенты, кто ранее подавал заявление на Повышенную ГА стипендию или Именные стипендии.\n\n✅Сбор заявлений на Стипендию Президента/Правительства РФ происходит в ИЮНЕ.\nДля данной стипендии выбираются те студенты, кто ранее подавал заявление на Повышенную ГА стипендию или Именные стипендии.'
    attachment = ''
    keyboard = {
            "one_time": False,
            "inline": True,
            "buttons": [
                [keyb.get_button(label = 'Повышенная ГА стипендия', color = 'secondary')],
                [keyb.get_button(label = 'Именная стипендия', color = 'secondary')],
                [keyb.get_button(label = 'Меню', color = 'negative')]
            ]
            }


    return message, attachment, keyboard

stipkonkurs_command = command_system.Command()

stipkonkurs_command.keys = ['[club87513693|@vuts.bonch] подать заявление', 'подать заявление', 'илья, подать заявление', 'илья подать заявление']
stipkonkurs_command.process = stipkonkurs
