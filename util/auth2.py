from datetime import datetime
from datetime import timedelta
import os
import bcrypt
from fastapi import HTTPException, Request, status
import jwt

NOME_COOKIE_AUTH = "auth"

async def obter_usuario_logado(request: Request) -> dict:
    try:
        token = request.cookies[NOME_COOKIE_AUTH]
        if token.strip() == "":
            return None
        dados = validar_token(token)
        return dados
    except KeyError:
        return None
    

async def checar_autenticacao(request: Request, call_next):
    usuario = await obter_usuario_logado(request)
    request.state.usuario = usuario
    response = await call_next(request)
    if response.status_code == status.HTTP_307_TEMPORARY_REDIRECT:
        return response
    if usuario:
        token = request.cookies[NOME_COOKIE_AUTH]
        criar_cookie_auth(response, token)
    return response
    

async def checar_autorizacao(request: Request):
    usuario = request.state.usuario if hasattr(request.state, "usuario") else None
    area_do_aluno = request.url.path.startswith("/aluno")
    area_do_professor = request.url.path.startswith("/professor")
    if (area_do_aluno or area_do_professor) and not usuario:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    if area_do_aluno and usuario.perfil != 1:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    if area_do_professor and usuario.perfil != 2:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)


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
    

def criar_token(email: str, perfil: int) -> str:
    payload = {
        "email": email,
        "perfil": perfil,
        "exp": datetime.now() + timedelta(minutes=60)
    }
    return jwt.encode(payload, 
        os.getenv("JWT_SECRET"),
        os.getenv("JWT_ALGORITHM"))


def validar_token(token: str) -> dict:
    try:
        return jwt.decode(token, 
            os.getenv("JWT_SECRET"),
            os.getenv("JWT_ALGORITHM"))
    except jwt.ExpiredSignatureError:
        return {"mensagem": "Token expirado"}
    except jwt.InvalidTokenError:
        return {"mensagem": "Token inválido"}
    except Exception as e:
        return {"mensagem": f"Erro: {e}"}
    

def criar_cookie_auth(response, token):
    response.set_cookie(
        key=NOME_COOKIE_AUTH,
        value=token,
        max_age=1800,
        httponly=True,
        samesite="lax",
    )
    return response


def configurar_swagger_auth(app):
    app.openapi_schema = app.openapi()
    app.openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
        }
    }
    app.openapi_schema["security"] = [{"BearerAuth": []}]