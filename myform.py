from bottle import post, request
import re
mailregex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

@post('/home', method='post')
def my_form():
    error = None
    quest = request.forms.get('QUEST')#Вопрос
    mail = request.forms.get('ADRESS')#Адрес
    if quest is None or quest == '' and mail is None or mail == '':#Проверка введенности обоих полей
        error = "Both fields are empty"
    if quest is None or quest == '':#Проверка введенности вопроса
        error = "Empty question field"
    else:
        if mail is None or mail == '':#Проверка введенности почты
            error = "Empty mail field"
        elif mailregex.match(mail) is None:#Проверка валидности почты
            error = "Invalid mail address"
    if error is None:
        return "Thanks! The answer will be sent to the mail %s" % mail
    else:
        return "Oops an error has occurred: %s" % error
