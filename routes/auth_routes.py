from fastapi import APIRouter
from fastapi.responses import JSONResponse

from dtos.entrar_dto import EntrarDto
from dtos.problem_details_dto import ProblemDetailsDto
from repositories.usuario_repo import UsuarioRepo
from util.auth_jwt import conferir_senha, criar_token


router = APIRouter(prefix="/auth")


@router.post("/entrar", status_code=200)
async def entrar(entrar_dto: EntrarDto):
    usuario = UsuarioRepo.obter_por_email(entrar_dto.email)
    if ((not usuario)
        or (not usuario.senha)
        or (not conferir_senha(entrar_dto.senha, usuario.senha))):
        pd = ProblemDetailsDto("str", f"Credenciais inválidas. Certifique-se de que está cadastrado e de que sua senha está correta.", "value_not_found", ["body", "email", "senha"])
        return JSONResponse(pd.to_dict(), status_code=404)
    token = criar_token(usuario.id, usuario.nome, usuario.email, usuario.perfil)
    return JSONResponse({"token": token}, status_code=200)