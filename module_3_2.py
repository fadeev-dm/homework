def send_email(message, recipient, *, sender = 'university.help@gmail.com'):
    ending = '.com', '.ru', '.net'
    i = '@'
    if not (i in recipient and sender):
        #print('ТЕСТ')
        for j in ending:
            if not (j in recipient and sender):
                return f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}'
    elif not (recipient.endswith(ending) and sender.endswith(ending)):
        return f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}'
    elif recipient == sender:
        return 'Нельзя отправить письмо самому себе!'
    elif sender == 'university.help@gmail.com':
        return f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}'
    else:
        return f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.'

print(send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com'))
print(send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com'))
print(send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.ua'))
print(send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru'))