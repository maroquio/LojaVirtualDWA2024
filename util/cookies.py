NOME_COOKIE_AUTH = "jwt-token"
NOME_HEADER_AUTH = "Authorization"
TEMPO_COOKIE_AUTH = 24*3600


def adicionar_mensagem_sucesso(response, mensagem):
    response.set_cookie(
        key="message_success",
        value=mensagem,
        max_age=1,
        httponly=True,
        samesite="lax",
    )
    return response


def adicionar_mensagem_info(response, mensagem):
    response.set_cookie(
        key="message_info",
        value=mensagem,
        max_age=1,
        httponly=True,
        samesite="lax",
    )
    return response


def adicionar_mensagem_alerta(response, mensagem):
    response.set_cookie(
        key="message_warning",
        value=mensagem,
        max_age=1,
        httponly=True,
        samesite="lax",
    )
    return response


def adicionar_mensagem_erro(response, mensagem):
    response.set_cookie(
        key="message_danger",
        value=mensagem,
        max_age=1,
        httponly=True,
        samesite="lax",
    )
    return response


def adicionar_cookie_auth(response, token, max_age=TEMPO_COOKIE_AUTH):
    response.set_cookie(
        key=NOME_COOKIE_AUTH,
        value=token,
        max_age=max_age,
        httponly=True,
        samesite="lax",
    )
    return response


def excluir_cookie_auth(response):
    response.set_cookie(
        key=NOME_COOKIE_AUTH,
        value=" ",
        httponly=True,
        expires=0,
        samesite="lax",
    )
    return response
