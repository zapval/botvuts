import command_system
import keyb

def gde():
    message = 'Какие команды есть в этом разделе:'
    attachment = ''
    keyboard = {
            "one_time": False,
            "inline": True,
            "buttons": [
                [keyb.get_button(label = 'Деканаты', color = 'secondary'),
                keyb.get_button(label = 'Библиотека', color = 'secondary'),
                keyb.get_button(label = 'Медицинский кабинет', color = 'secondary')],
                [keyb.get_button(label = 'Бюро пропусков', color = 'secondary'),
                keyb.get_button(label = 'Социальный отдел', color = 'secondary')],
                [keyb.get_button(label = 'Договорной отдел', color = 'secondary'),
                keyb.get_button(label = 'Военно-учетный стол', color = 'secondary')],
                [keyb.get_button(label = 'Студенческий городок', color = 'secondary')],
                [keyb.get_button(label = 'Студенческий отдел кадров', color = 'secondary')],
                [keyb.get_button(label = 'Меню', color = 'negative')]
            ]
            }


    return message, attachment, keyboard

gde_command = command_system.Command()

gde_command.keys = ['[club87513693|@vuts.bonch] где', 'где', 'илья, где', 'илья где']
gde_command.process = gde
