import command_system
import keyb

def chastfakult():
    message = '📚В начале каждого семестра в личном кабинете студента идет запись на факультативы Учеба — Факультативы.\n\n• Вам следует отметить факультативы, которые хочется посещать;\n• Распечатать заявление;\n• Подписать заявление у руководителя факультатива;\n• Следить за расписанием факультатива и появлением письма на вашей электронной почте или в личном кабинете студента.'
    attachment = ''
    keyboard = {
            "one_time": False,
            "inline": True,
            "buttons": [
                [keyb.get_button(label = 'Меню', color = 'negative')]
            ]
            }


    return message, attachment, keyboard

chastfakult_command = command_system.Command()

chastfakult_command.keys = ['[club87513693|@vuts.bonch] факультативы', 'факультативы', 'илья, факультативы', 'илья факультативы']
chastfakult_command.process = chastfakult
