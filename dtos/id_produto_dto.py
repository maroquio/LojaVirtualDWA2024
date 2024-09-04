from pydantic import BaseModel, field_validator

from util.validators import *


class IdProdutoDto(BaseModel):
    id_produto: int

    @field_validator("id_produto")
    def validar_id_produto(cls, v):
        msg = is_greater_than(v, "Id do Produto", 0)
        if msg: raise ValueError(msg)
        return v