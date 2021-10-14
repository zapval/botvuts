import command_system
import keyb

def chastsprav():
    message = '📄Справку по месту учебы можно заказать:\n• В 1 корпусе на 3 этаже — 305/1;\n• Личный кабинет студента — Личное — Заказ справок.\n• Срок изготовления 3 рабочих дня.\n• Забирать готовые справки в 305/1.\n• Срок хранения для тех, кто заказал через личный кабинет, 2 недели.\n\n📄Справки о сумме выдачи стипендии можно заказать:\n• В 1 корпусе на 6 этаже — 623/1 или 625/1.'
    attachment = ''
    keyboard = {
            "one_time": False,
            "inline": True,
            "buttons": [
                [keyb.get_button(label = 'Меню', color = 'negative')]
            ]
            }


    return message, attachment, keyboard

chastsprav_command = command_system.Command()

chastsprav_command.keys = ['[club87513693|@vuts.bonch] справки', 'справки', 'илья, справки', 'илья справки']
chastsprav_command.process = chastsprav
