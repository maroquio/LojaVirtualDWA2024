from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Optional


class EstadoPedido(Enum):
    CARRINHO = "carrinho"
    PENDENTE = "pendente"
    PAGO = "pago"
    FATURADO = "faturado"
    SEPARADO = "separado"
    ENVIADO = "enviado"
    ENTREGUE = "entregue"
    CANCELADO = "cancelado"


@dataclass
class Pedido:
    id: Optional[int] = None
    data_hora: Optional[datetime] = None
    valor_total: Optional[float] = None
    endereco_entrega: Optional[str] = None
    estado: Optional[EstadoPedido] = None
    id_cliente: Optional[int] = None
