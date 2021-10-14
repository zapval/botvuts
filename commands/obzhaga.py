import command_system
import keyb

def obzhaga():
    message = 'Какие команды есть в этом разделе:'
    attachment = ''
    keyboard = {
            "one_time": False,
            "inline": True,
            "buttons": [
                [keyb.get_button(label = 'Общежитие "Яковлевское"', color = 'secondary')],
                [keyb.get_button(label = 'Общежитие "Стойкости"', color = 'secondary')],
                [keyb.get_button(label = 'Общежитие "Дальневосточное"', color = 'secondary')],
                [keyb.get_button(label = 'Меню', color = 'negative')]
            ]
            }


    return message, attachment, keyboard

obzhaga_command = command_system.Command()

obzhaga_command.keys = ['[club87513693|@vuts.bonch] общежития', 'общежития', 'илья, общежития', 'илья общежития', 'илья, общага', 'илья общага']
obzhaga_command.process = obzhaga
