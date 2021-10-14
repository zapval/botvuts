import command_system
import keyb

def stipendia():
    message = 'Какие команды есть в этом разделе:'
    attachment = ''
    keyboard = {
            "one_time": False,
            "inline": True,
            "buttons": [
                [keyb.get_button(label = 'Рассчет стипендий для ВУЦ', color = 'secondary')],
                [keyb.get_button(label = 'Виды стипендий', color = 'secondary')],
                [keyb.get_button(label = 'Подать заявление', color = 'secondary')],
                [keyb.get_button(label = 'Меню', color = 'negative')]
            ]
            }


    return message, attachment, keyboard

stipendia_command = command_system.Command()

stipendia_command.keys = ['[club87513693|@vuts.bonch] стипендии', 'стипендии', 'илья, стипендии', 'илья стипендии']
stipendia_command.process = stipendia
