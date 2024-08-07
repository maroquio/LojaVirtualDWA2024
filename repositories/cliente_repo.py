import json
import sqlite3
from typing import List, Optional
from models.cliente_model import Cliente
from sql.cliente_sql import *
from util.database import obter_conexao


class ClienteRepo:

    @classmethod
    def criar_tabela(cls):
        with obter_conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute(SQL_CRIAR_TABELA)

    @classmethod
    def inserir(cls, cliente: Cliente) -> Optional[Cliente]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(
                    SQL_INSERIR,
                    (
                        cliente.nome,
                        cliente.cpf,
                        cliente.data_nascimento,
                        cliente.endereco,
                        cliente.telefone,
                        cliente.email,
                        cliente.senha,
                    ),
                )
                if cursor.rowcount > 0:
                    cliente.id = cursor.lastrowid
                    return cliente
        except sqlite3.Error as ex:
            print(ex)
            return None

    @classmethod
    def obter_todos(cls) -> List[Cliente]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                tuplas = cursor.execute(SQL_OBTER_TODOS).fetchall()
                clientes = [Cliente(*t) for t in tuplas]
                return clientes
        except sqlite3.Error as ex:
            print(ex)
            return None

    @classmethod
    def alterar(cls, cliente: Cliente) -> bool:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(
                    SQL_ALTERAR,
                    (
                        cliente.nome,
                        cliente.cpf,
                        cliente.data_nascimento,
                        cliente.endereco,
                        cliente.telefone,
                        cliente.email,
                        cliente.id,
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
    def obter_por_id(cls, id: int) -> Optional[Cliente]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                tupla = cursor.execute(SQL_OBTER_POR_ID, (id,)).fetchone()
                cliente = Cliente(*tupla)
                return cliente
        except sqlite3.Error as ex:
            print(ex)
            return None

    @classmethod
    def obter_quantidade(cls) -> Optional[int]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                tupla = cursor.execute(SQL_OBTER_QUANTIDADE).fetchone()
                return int(tupla[0])
        except sqlite3.Error as ex:
            print(ex)
            return None

    @classmethod
    def inserir_clientes_json(cls, arquivo_json: str):
        if ClienteRepo.obter_quantidade() == 0:
            with open(arquivo_json, "r", encoding="utf-8") as arquivo:
                clientes = json.load(arquivo)
                for cliente in clientes:
                    ClienteRepo.inserir(Cliente(**cliente))

    @classmethod
    def obter_busca(cls, termo: str, pagina: int, tamanho_pagina: int) -> List[Cliente]:
        termo = "%" + termo + "%"
        offset = (pagina - 1) * tamanho_pagina
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                tuplas = cursor.execute(
                    SQL_OBTER_BUSCA, (termo, termo, tamanho_pagina, offset)
                ).fetchall()
                clientes = [Cliente(*t) for t in tuplas]
                return clientes
        except sqlite3.Error as ex:
            print(ex)
            return None

    @classmethod
    def obter_quantidade_busca(cls, termo: str) -> Optional[int]:
        termo = "%" + termo + "%"
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                tupla = cursor.execute(
                    SQL_OBTER_QUANTIDADE_BUSCA, (termo, termo)
                ).fetchone()
                return int(tupla[0])
        except sqlite3.Error as ex:
            print(ex)
            return None

    @classmethod
    def obter_por_email(cls, email: str) -> Optional[Cliente]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                tupla = cursor.execute(SQL_OBTER_POR_EMAIL, (email,)).fetchone()
                if tupla:
                    cliente = Cliente(*tupla)
                    return cliente
                else:
                    return None
        except sqlite3.Error as ex:
            print(ex)
            return None

    @classmethod
    def alterar_token(cls, id: int, token: str) -> bool:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(SQL_ALTERAR_TOKEN, (token, id))
                return cursor.rowcount > 0
        except sqlite3.Error as ex:
            print(ex)
            return False

    @classmethod
    def obter_por_token(cls, token: str) -> Optional[Cliente]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                tupla = cursor.execute(SQL_OBTER_POR_TOKEN, (token,)).fetchone()
                if tupla:
                    cliente = Cliente(*tupla)
                    return cliente
                else:
                    return None
        except sqlite3.Error as ex:
            print(ex)
            return None

    @classmethod
    def alterar_senha(cls, id: int, senha: str) -> bool:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(SQL_ALTERAR_SENHA, (senha, id))
                return cursor.rowcount > 0
        except sqlite3.Error as ex:
            print(ex)
            return False
