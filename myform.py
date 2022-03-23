from bottle import post, request

@post('/home', method='post')
def my_form():
    mail = request.forms.get('ADRESS')
    if (mail == None)
        return ("Adress is null")
    return ("Thanks! The answer will be sent to the mail %s" % mail)
    