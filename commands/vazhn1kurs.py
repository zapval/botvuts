import command_system
import keyb

def vazhn1kurs():
    message = 'Какие команды есть в этом разделе:'
    attachment = ''
    keyboard = {
            "one_time": False,
            "inline": True,
            "buttons": [
                [keyb.get_button(label = 'БСК', color = 'secondary')],
                [keyb.get_button(label = 'Воинский учет', color = 'secondary')],
                [keyb.get_button(label = 'Медосмотр', color = 'secondary')],
                [keyb.get_button(label = 'Меню', color = 'negative')]
            ]
            }


    return message, attachment, keyboard

vazhn1kurs_command = command_system.Command()

vazhn1kurs_command.keys = ['[club87513693|@vuts.bonch] важное 1 курс', 'важное 1 курс', 'илья, важное 1 курс', 'илья важное 1 курс']
vazhn1kurs_command.process = vazhn1kurs
