import command_system
import keyb

def chastkuren():
    message = '🚬Курение разрешено только за забором университета. За нарушение правил студент вызывается на комиссию, это карается вплоть до отчисления.'
    attachment = ''
    keyboard = {
            "one_time": False,
            "inline": True,
            "buttons": [
                [keyb.get_button(label = 'Меню', color = 'negative')]
            ]
            }


    return message, attachment, keyboard

chastkuren_command = command_system.Command()

chastkuren_command.keys = ['[club87513693|@vuts.bonch] курение', 'курение', 'илья, курение', 'илья курение']
chastkuren_command.process = chastkuren
