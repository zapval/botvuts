import command_system
import keyb

def vazhn1medosm():
    message = '⚕Что нужно взять:\n• Сертификат о прививках (+ его копия);\n• Справка 086у;\n• Свежая флюорография (максимум 1 год).'
    attachment = ''
    keyboard = {
            "one_time": False,
            "inline": True,
            "buttons": [
                [keyb.get_button(label = 'Меню', color = 'negative')]
            ]
            }


    return message, attachment, keyboard

vazhn1medosm_command = command_system.Command()

vazhn1medosm_command.keys = ['[club87513693|@vuts.bonch] медосмотр', 'медосмотр', 'илья, медосмотр', 'илья медосмотр']
vazhn1medosm_command.process = vazhn1medosm
