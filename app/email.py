import requests
from datetime import datetime
from flask import current_app

def send_simple_message(to, subject, newUser):
    print('Enviando mensagem (POST)...', flush=True)
    app = current_app

    print('URL:', app.config['API_URL'], flush=True)
    print('API:', app.config['API_KEY'], flush=True)
    print('FROM:', app.config['API_FROM'], flush=True)
    print('TO:', to, flush=True)
    print('ASSUNTO:', app.config['FLASKY_MAIL_SUBJECT_PREFIX'], flush=True)

    resposta = requests.post(
        app.config['API_URL'],
        auth=("api", app.config['API_KEY']),
        data={
            "from": app.config['API_FROM'],
            "to": to,
            "subject": app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + ' ' + subject,
            "text": "Novo usuário cadastrado: " + newUser
        }
    )

    print('Resposta:', resposta, '-', datetime.now().strftime("%d/%m/%Y %H:%M:%S"), flush=True)
    return resposta
