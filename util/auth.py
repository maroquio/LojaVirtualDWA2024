import secrets
from typing import Optional
import bcrypt
from fastapi import HTTPException, Request, status
from models.cliente_model import Cliente
from repositories.cliente_repo import ClienteRepo
from util.cookies import NOME_COOKIE_AUTH, adicionar_cookie_auth


async def obter_cliente_logado(request: Request) -> Optional[Cliente]:
    try:
        token = request.cookies[NOME_COOKIE_AUTH]
        if token.strip() == "":
            return None
        cliente = ClienteRepo.obter_por_token(token)
        return cliente
    except KeyError:
        return None


async def middleware_autenticacao(request: Request, call_next):
    cliente = await obter_cliente_logado(request)
    request.state.cliente = cliente
    response = await call_next(request)
    if response.status_code == status.HTTP_303_SEE_OTHER:
        return response
    if cliente:
        token = request.cookies[NOME_COOKIE_AUTH]
        adicionar_cookie_auth(response, token)
    return response


async def checar_permissao(request: Request):
    cliente = request.state.cliente if hasattr(request.state, "cliente") else None
    area_do_cliente = request.url.path.startswith("/cliente")
    area_do_admin = request.url.path.startswith("/admin")
    if (area_do_cliente or area_do_admin) and not cliente:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    # if area_do_cliente and cliente.perfil != 1:
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    # if area_do_admin and cliente.perfil != 2:
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)


def obter_hash_senha(senha: str) -> str:
    try:
        hashed = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())
        return hashed.decode()
    except ValueError:
        return ""


def conferir_senha(senha: str, hash_senha: str) -> bool:
    try:
        return bcrypt.checkpw(senha.encode(), hash_senha.encode())
    except ValueError:
        return False


def gerar_token(length: int = 32) -> str:
    try:
        return secrets.token_hex(length)
    except ValueError:
        return ""
