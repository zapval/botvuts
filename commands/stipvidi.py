import command_system
import keyb

def stipvidi():
    message = 'Какие команды есть в этом разделе:'
    attachment = ''
    keyboard = {
            "one_time": False,
            "inline": True,
            "buttons": [
                [keyb.get_button(label = 'За учебу', color = 'secondary')],
                [keyb.get_button(label = 'За достижения и учебу', color = 'secondary')],
                [keyb.get_button(label = 'Социальная помощь', color = 'secondary')],
                [keyb.get_button(label = 'Меню', color = 'negative')]
            ]
            }


    return message, attachment, keyboard

stipvidi_command = command_system.Command()

stipvidi_command.keys = ['[club87513693|@vuts.bonch] виды стипендий', 'виды стипендий', 'илья, виды стипендий', 'илья виды стипендий']
stipvidi_command.process = stipvidi
