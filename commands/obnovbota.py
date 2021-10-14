import command_system
import keyb

def obnovbota():
    message = 'Бот обновлен'
    attachment = ''
    keyboard = {"buttons":[],"one_time":True}


    return message, attachment, keyboard

obnovbota_command = command_system.Command()

obnovbota_command.keys = ['[club87513693|@vuts.bonch] обновление бота', 'обновление бота', 'илья, обновление бота', 'обновление бота']
obnovbota_command.process = obnovbota
