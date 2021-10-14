import command_system
import keyb

def gdedekanat():
    message = 'Какие команды есть в этом разделе:'
    attachment = ''
    keyboard = {
            "one_time": False,
            "inline": True,
            "buttons": [
                [keyb.get_button(label = 'Где деканат ИКСС', color = 'secondary')],
                [keyb.get_button(label = 'Где деканат РТС', color = 'secondary')],
                [keyb.get_button(label = 'Меню', color = 'negative')]
            ]
            }


    return message, attachment, keyboard

gdedekanat_command = command_system.Command()

gdedekanat_command.keys = ['[club87513693|@vuts.bonch] деканаты', 'деканаты', 'илья, деканаты', 'илья деканаты']
gdedekanat_command.process = gdedekanat
