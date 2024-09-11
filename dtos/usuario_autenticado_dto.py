from dataclasses import dataclass
from typing import Optional


@dataclass
class UsuarioAutenticadoDto: 
    id: Optional[int] = None   
    nome: Optional[str] = None
    email: Optional[str] = None
    perfil: Optional[int] = None