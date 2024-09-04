from pydantic import BaseModel, field_validator

from models.pedido_model import EstadoPedido
from util.validators import is_greater_than


class AlterarPedidoDto(BaseModel):
    id: int
    estado: EstadoPedido

    @field_validator("id")
    def validar_id(cls, v):
        msg = is_greater_than(v, "Id", 0)
        if msg: raise ValueError(msg)
        return v    