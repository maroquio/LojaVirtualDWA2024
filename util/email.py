import os
from mailersend import emails
from dotenv import load_dotenv

def enviar_email(nome_destinatario: str, email_destinatario: str, mensagem: str):
    load_dotenv()
    mailer = emails.NewEmail(os.getenv('MAILER_SEND_TOKEN'))
    # define an empty dict to populate with mail values
    mail_body = {}
    mail_from = {
        "name": "Loja Virtual",
        "email": "contato@cachoeiro.es",
    }
    recipients = [
        {
            "name": nome_destinatario,
            "email": email_destinatario,
        }
    ]
    reply_to = {
        "name": "Loja Virtual",
        "email": "contato@cachoeiro.es",
    }
    mailer.set_mail_from(mail_from, mail_body)
    mailer.set_mail_to(recipients, mail_body)
    mailer.set_subject("Bem-vindo!", mail_body)
    #mailer.set_html_content("This is the HTML content", mail_body)
    mailer.set_plaintext_content(mensagem, mail_body)
    mailer.set_reply_to(reply_to, mail_body)
    mailer.send(mail_body)