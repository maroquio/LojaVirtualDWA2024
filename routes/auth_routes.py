from fastapi import APIRouter
from fastapi.responses import JSONResponse

from dtos.entrar_dto import EntrarDto
from dtos.problem_details_dto import ProblemDetailsDto
from repositories.usuario_repo import UsuarioRepo
from util.auth_jwt import conferir_senha, criar_token


router = APIRouter(prefix="/auth")


@router.post("/entrar")
async def entrar(entrar_dto: EntrarDto):
    cliente_entrou = UsuarioRepo.obter_por_email(entrar_dto.email)
    if ((not cliente_entrou)
        or (not cliente_entrou.senha)
        or (not conferir_senha(entrar_dto.senha, cliente_entrou.senha))):
        pd = ProblemDetailsDto("str", f"Credenciais inválidas. Certifique-se de que está cadastrado e de que sua senha está correta.", "value_not_found", ["body", "email", "senha"])
        return JSONResponse(pd.to_dict(), status_code=404)
    token = criar_token(cliente_entrou.id, cliente_entrou.nome, cliente_entrou.email, cliente_entrou.perfil)
    return JSONResponse({"token": token})