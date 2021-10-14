import command_system
import keyb

def stipsoc():
    message = '🌟Материальная помощь:\n• Единовременная выплата — 4000 р.\n\n🌟Социальные стипендии:\n• Государственная социальная стипендия — 2592 р.\n• Повышенная социальная стипендия до конца 2 курса или 20 лет — 9925 р.\nКритерии отбора: https://www.sut.ru/university/structure/vrso/uvsr/otdel-po-socialnoy-rabote/stipendii/gosudarstvennaya-socialnaya-stipendiya-studentam'
    attachment = ''
    keyboard = {
            "one_time": False,
            "inline": True,
            "buttons": [
                [keyb.get_button(label = 'Меню', color = 'negative')]
            ]
            }


    return message, attachment, keyboard

stipsoc_command = command_system.Command()

stipsoc_command.keys = ['[club87513693|@vuts.bonch] социальная помощь', 'социальная помощь', 'илья, социальная помощь', 'илья социальная помощь']
stipsoc_command.process = stipsoc
