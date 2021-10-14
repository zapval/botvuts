import command_system
import keyb

def stipimen():
    message = 'Именная стипендия.\n\n✅Данная стипендия назначается на 1 семестр.\n\n✅Для участия в конкурсе необходимо соответствовать следующим критериям:\n1. Иметь средний балл по итогам двух последних сессий только 5.0;\n2. Не иметь действующих дисциплинарных взысканий;\n3. В течение последнего года принимать участие в учебной, физкультурной, спортивной, общественной, научной, научно-технической, творческой, экспериментальной и инновационной деятельности, в мероприятиях военно-патриотической направленности.\n\n✅Порядок заполнения характеристики и заявления:\n1. Заполните характеристику-рекомендацию претендента (характеристика прикреплена ниже к сообщению);\n2. Характеристика должна быть в doc или docx файле;\n3. Переименуйте получившийся документ в формат: Характеристика_ФамилияИО.doc или Характеристика_ФамилияИО.docx;\n4. Заполните заявление претендента (заявление прикреплено ниже к сообщению);\n5. Заявление должно быть в doc или docx файле;\n6. Вставьте в этот же документ фото/сканы/скрины из зачетной книжки или личного кабинета студента:\nФИО студента\nЭкзамены за 2 последние сессии\nЗачеты за 2 последние сессии\nКурсовые работы за 2 последние сессии\nНаучно-исследовательские работы за 2 последние сессии (если таковые имеются)\nПрактики за 2 последние сессии (если таковые имеются)\n7. Вставьте фото/сканы/скрины всех документов, подтверждающих достижения за последний год;\n8. Переименуйте получившийся документ в формат: ФамилияИО.doc или ФамилияИО.docx;\n9. Вышлите данные документы в личные сообщения группы vk.me/vuts.bonch ;\n10. Администратор проверит правильность заполнения заявления и характеристики и ответит вам, что принял документы.'
    attachment = 'doc-194336319_586166045', 'doc-194336319_586166065'
    keyboard = {
            "one_time": False,
            "inline": True,
            "buttons": [
                [keyb.get_button(label = 'Меню', color = 'negative')]
            ]
            }


    return message, attachment, keyboard

stipimen_command = command_system.Command()

stipimen_command.keys = ['[club87513693|@vuts.bonch] именная стипендия', 'именная стипендия', 'илья, именная стипендия', 'илья именная стипендия']
stipimen_command.process = stipimen
