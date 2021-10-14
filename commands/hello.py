import command_system
import keyb

def hello():
    message = 'Привет, студент!\nЯ Илья, бот-справочник ВУЦ, который поможет тебе ответить на многие вопросы.\n\nДля того, чтобы я реагировал на твои команды, тебе потребуется обратиться ко мне как "Илья".\n\nУвидел ошибку, есть предложение, хочешь задать вопрос касательно содержимого?\nНапиши действующему Председателю Студенческого совета ВУЦ — @zapeka_infinity (Валентину Запеке)'
    attachment = ''
    keyboard = {
            "one_time": False,
            "inline": True,
            "buttons": [
                [keyb.get_button(label = 'Частозадаваемые', color = 'secondary'),
                keyb.get_button(label = 'Стипендии', color = 'secondary')],
                [keyb.get_button(label = 'Общежития', color = 'secondary'),
                keyb.get_button(label = 'Студсовет ВУЦ', color = 'secondary')],
                [keyb.get_button(label = 'Администрация ВУЦ', color = 'secondary')],
                [keyb.get_button(label = 'Где', color = 'secondary'),
                keyb.get_button(label = 'В/с запаса', color = 'secondary')],
                [keyb.get_button(label = 'Важное 1 курс', color = 'secondary')]
            ]
            }


    return message, attachment, keyboard

hello_command = command_system.Command()

hello_command.keys = ['[club87513693|@vuts.bonch] меню', 'меню', 'Начать', 'илья, помощь', 'илья помощь']
hello_command.process = hello
