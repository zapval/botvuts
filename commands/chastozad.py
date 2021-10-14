import command_system
import keyb

def chastozad():
    message = 'Какие команды есть в этом разделе:'
    attachment = ''
    keyboard = {
            "one_time": False,
            "inline": True,
            "buttons": [
                [keyb.get_button(label = 'Интернет в здании университета', color = 'secondary')],
                [keyb.get_button(label = 'Курение', color = 'secondary'),
                keyb.get_button(label = 'Факультативы', color = 'secondary')],
                [keyb.get_button(label = 'Расписание занятий', color = 'secondary')],
                [keyb.get_button(label = 'Справки', color = 'secondary')],
                [keyb.get_button(label = 'Меню', color = 'negative')]
            ]
            }


    return message, attachment, keyboard

chastozad_command = command_system.Command()

chastozad_command.keys = ['[club87513693|@vuts.bonch] частозадаваемые', 'частозадаваемые', 'илья, частозадаваемые', 'илья частозадаваемые']
chastozad_command.process = chastozad
