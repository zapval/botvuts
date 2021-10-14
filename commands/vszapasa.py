import command_system
import keyb

def vszapasa():
    message = 'Какие команды есть в этом разделе:'
    attachment = ''
    keyboard = {
            "one_time": False,
            "inline": True,
            "buttons": [
                [keyb.get_button(label = 'Поступление на в/с запаса', color = 'secondary')],
                [keyb.get_button(label = 'Обучение на в/с запаса', color = 'secondary')],
                [keyb.get_button(label = 'Меню', color = 'negative')]
            ]
            }


    return message, attachment, keyboard

vszapasa_command = command_system.Command()

vszapasa_command.keys = ['[club87513693|@vuts.bonch] в/с запаса', 'в/с запаса', 'илья, в/с запаса', 'илья в/с запаса']
vszapasa_command.process = vszapasa
