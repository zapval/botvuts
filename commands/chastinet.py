import command_system
import keyb

def chastinet():
    message = '📌Инструкция:\n\n1. Подключитесь к сети Wi-Fi: Bonch, ключ сети: FtYpp86z;\n2. Откройте любую страницу в браузере;\n3. Когда Вас перекинет на точку авторизации, введите свои данные. Логин и пароль для входа можно взять в личном кабинете студента во вкладке "Доступы к сервисам"'
    attachment = ''
    keyboard = {
            "one_time": False,
            "inline": True,
            "buttons": [
                [keyb.get_button(label = 'Меню', color = 'negative')]
            ]
            }


    return message, attachment, keyboard

chastinet_command = command_system.Command()

chastinet_command.keys = ['[club87513693|@vuts.bonch] интернет в здании университета', 'интернет в здании университета', 'илья, интернет в здании университета', 'илья интернет в здании университета']
chastinet_command.process = chastinet
