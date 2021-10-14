import command_system
import keyb

def chastzanat():
    message = '⏳Расписание занятий в СПбГУТ:\n09:00 - 10:35 — 1 пара\n10:45 - 12:20 — 2 пара\n12:20 - 13:00 — обед\n13:00 - 14:35 — 3 пара\n14:45 - 16:20 — 4 пара\n16:30 - 18:05 — 5 пара\n18:15 - 19:50 — 6 пара\n20:00 - 21:35 — 7 пара\n\n⏳Расписание занятий ВУЦ:\n08:30 — построение\n08:35 - 08:55 — проверка наличия личного состава\n09:00 - 09:45 — 1 час\n09:50 - 10:35 — 2 час\n10:45 - 11:30 — 3 час\n11:35 - 12:20 — 4 час\n12:20 - 13:30 — обед\n13:30 - 14:15 — 5 час\n14:20 - 15:05 — 6 час\n15:10 - 15:55 — 7 час\n16:00 - 16:45 — 8 час\n16:59 - 17:30 — 9 час\n\n⏳Расписание занятий можно смотреть:\n• Bonch Bot VK https://vk.com/bonchschedule\n• Bonch Bot TG t.me/BonchGUTBot\n• Сайт https://bonch.glitch.me/\n• Приложение Бонч.Расписание ъыъ.рф/Бонч.Расписание\n• Сайт СПбГУТ https://www.sut.ru/studentu/raspisanie \n• Личный кабинет студента'
    attachment = ''
    keyboard = {
            "one_time": False,
            "inline": True,
            "buttons": [
                [keyb.get_button(label = 'Меню', color = 'negative')]
            ]
            }


    return message, attachment, keyboard

chastzanat_command = command_system.Command()

chastzanat_command.keys = ['[club87513693|@vuts.bonch] расписание занятий', 'расписание занятий', 'илья, расписание занятий', 'илья расписание занятий']
chastzanat_command.process = chastzanat
