from datetime import datetime
import sqlite3
from typing import List, Optional
from models.pedido_model import EstadoPedido, Pedido
from repositories.item_pedido_repo import ItemPedidoRepo
from sql.pedido_sql import *
from util.database import obter_conexao


class PedidoRepo:

    @classmethod
    def criar_tabela(cls):
        with obter_conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute(SQL_CRIAR_TABELA)

    @classmethod
    def inserir(cls, pedido: Pedido) -> Optional[Pedido]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(
                    SQL_INSERIR,
                    (
                        pedido.data_hora,
                        pedido.valor_total,
                        pedido.endereco_entrega,
                        pedido.estado,
                        pedido.id_cliente,
                    ),
                )
                if cursor.rowcount > 0:
                    pedido.id = cursor.lastrowid
                    return pedido
        except sqlite3.Error as ex:
            print(ex)
            return None

    @classmethod
    def alterar_data_hora(cls, id: int, nova_data_hora: datetime) -> bool:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(
                    SQL_ALTERAR_DATA_HORA,
                    (
                        nova_data_hora,
                        id,
                    ),
                )
                return cursor.rowcount > 0
        except sqlite3.Error as ex:
            print(ex)
            return False

    @classmethod
    def alterar_estado(cls, id: int, novo_estado: str) -> bool:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(
                    SQL_ALTERAR_ESTADO,
                    (
                        novo_estado,
                        id,
                    ),
                )
                return cursor.rowcount > 0
        except sqlite3.Error as ex:
            print(ex)
            return False

    @classmethod
    def atualizar_para_fechar(
        cls, id: int, endereco_entrega: str, valor_total: float
    ) -> bool:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(
                    SQL_ATUALIZAR_PARA_FECHAR,
                    (
                        endereco_entrega,
                        valor_total,
                        id,
                    ),
                )
                return cursor.rowcount > 0
        except sqlite3.Error as ex:
            print(ex)
            return False
        
    @classmethod
    def atualizar_valor_total(
        cls, id: int, valor_total: float = 0
    ) -> bool:
        if not valor_total:
            itens = ItemPedidoRepo.obter_por_pedido(id)
            if itens:
                valor_total = sum([item.valor_item for item in itens])
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(
                    SQL_ATUALIZAR_VALOR_TOTAL,
                    (
                        valor_total,
                        id,
                    ),
                )
                return cursor.rowcount > 0
        except sqlite3.Error as ex:
            print(ex)
            return False

    @classmethod
    def excluir(cls, id: int) -> bool:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(SQL_EXCLUIR, (id,))
                return cursor.rowcount > 0
        except sqlite3.Error as ex:
            print(ex)
            return False

    @classmethod
    def obter_por_id(cls, id: int) -> Optional[Pedido]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                tupla = cursor.execute(SQL_OBTER_POR_ID, (id,)).fetchone()
                if not tupla: return None
                pedido = Pedido(*tupla)
                return pedido
        except sqlite3.Error as ex:
            print(ex)
            return None

    @classmethod
    def obter_quantidade(cls, id_cliente: int) -> Optional[int]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                tupla = cursor.execute(SQL_OBTER_QUANTIDADE, (id_cliente,)).fetchone()
                return int(tupla[0])
        except sqlite3.Error as ex:
            print(ex)
            return None

    @classmethod
    def obter_por_periodo(
        cls, id_cliente: int, data_inicial: datetime, data_final: datetime
    ) -> List[Pedido]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                tuplas = cursor.execute(
                    SQL_OBTER_POR_PERIODO,
                    (
                        id_cliente,
                        data_inicial,
                        data_final,
                    ),
                ).fetchall()
                pedidos = [Pedido(*t) for t in tuplas]
                return pedidos
        except sqlite3.Error as ex:
            print(ex)
            return None

    @classmethod
    def obter_quantidade_por_periodo(
        cls, id_cliente: int, data_inicial: datetime, data_final: datetime
    ) -> Optional[int]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                tupla = cursor.execute(
                    SQL_OBTER_QUANTIDADE_POR_PERIODO,
                    (
                        id_cliente,
                        data_inicial,
                        data_final,
                    ),
                ).fetchone()
                return int(tupla[0])
        except sqlite3.Error as ex:
            print(ex)
            return None

    @classmethod
    def obter_por_estado(cls, id_cliente: int, estado: int) -> List[Pedido]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                tuplas = cursor.execute(
                    SQL_OBTER_POR_ESTADO,
                    (
                        id_cliente,
                        estado,
                    ),
                ).fetchall()
                pedidos = [Pedido(*t) for t in tuplas]
                return pedidos
        except sqlite3.Error as ex:
            print(ex)
            return None
        
    @classmethod
    def obter_todos_por_estado(cls, estado: int) -> List[Pedido]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                tuplas = cursor.execute(
                    SQL_OBTER_TODOS_POR_ESTADO, (estado,),
                ).fetchall()
                pedidos = [Pedido(*t) for t in tuplas]
                return pedidos
        except sqlite3.Error as ex:
            print(ex)
            return None