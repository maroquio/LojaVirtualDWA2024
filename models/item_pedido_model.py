from dataclasses import dataclass
from typing import Optional


@dataclass
class ItemPedido:
    id_pedido: Optional[int] = None
    id_produto: Optional[int] = None
    nome_produto: Optional[str] = None
    valor_produto: Optional[float] = None
    quantidade: Optional[int] = None
    valor_item: Optional[float] = None
