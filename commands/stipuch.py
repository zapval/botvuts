import command_system
import keyb

def stipuch():
    message = '🌟Государственные стипендии:\n• Государственная академическая стипендия — 1727 р.\n\n🌟Стипендии ВУЦ для кадровых военнослужащих:\n🎖1 курс\n• Успевающим во всех случаях — 2591 р.\n🎖2 - 5 курс\n• Успевающим на "хорошо" или "отлично" — 6909 р.\n• Успевающим в других случаях — 5182 р.'
    attachment = ''
    keyboard = {
            "one_time": False,
            "inline": True,
            "buttons": [
                [keyb.get_button(label = 'Меню', color = 'negative')]
            ]
            }


    return message, attachment, keyboard

stipuch_command = command_system.Command()

stipuch_command.keys = ['[club87513693|@vuts.bonch] за учебу', 'за учебу', 'илья, за учебу', 'илья за учебу']
stipuch_command.process = stipuch
