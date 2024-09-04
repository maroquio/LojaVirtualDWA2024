SQL_CRIAR_TABELA = """
    CREATE TABLE IF NOT EXISTS pedido (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data_hora DATETIME NOT NULL,
        valor_total FLOAT NOT NULL,
        endereco_entrega TEXT NOT NULL,
        estado TEXT NOT NULL,
        id_cliente INTEGER NOT NULL,
        FOREIGN KEY (id_cliente) REFERENCES cliente(id))
"""

SQL_INSERIR = """
    INSERT INTO pedido(data_hora, valor_total, endereco_entrega, estado, id_cliente)
    VALUES (?, ?, ?, ?, ?)
"""

SQL_ALTERAR_DATA_HORA = """
    UPDATE pedido
    SET data_hora=?
    WHERE id=?
"""

SQL_ALTERAR_ESTADO = """
    UPDATE pedido
    SET estado=?
    WHERE id=?
"""

SQL_ATUALIZAR_PARA_FECHAR = """
    UPDATE pedido
    SET endereco_entrega=?, valor_total=?
    WHERE id=?
"""

SQL_ATUALIZAR_VALOR_TOTAL = """
    UPDATE pedido
    SET valor_total=?
    WHERE id=?
"""

SQL_EXCLUIR = """
    DELETE FROM pedido
    WHERE id=?
"""

SQL_OBTER_POR_ID = """
    SELECT id, data_hora, valor_total, endereco_entrega, estado, id_cliente
    FROM pedido
    WHERE id=?
"""

SQL_OBTER_QUANTIDADE = """
    SELECT COUNT(*) 
    FROM pedido
    WHERE id_cliente=?
"""

SQL_OBTER_POR_PERIODO = """
    SELECT id, data_hora, valor_total, endereco_entrega, estado, id_cliente
    FROM pedido
    WHERE (id_cliente = ?) AND (data_hora BETWEEN ? AND ?)
    ORDER BY data_hora DESC
"""

SQL_OBTER_QUANTIDADE_POR_PERIODO = """
    SELECT COUNT(*) 
    FROM pedido
    WHERE (id_cliente = ?) AND (data_hora BETWEEN ? AND ?)
"""

SQL_OBTER_POR_ESTADO = """
    SELECT id, data_hora, valor_total, endereco_entrega, estado, id_cliente
    FROM pedido
    WHERE (id_cliente = ?) AND (estado = ?)
"""

SQL_OBTER_TODOS_POR_ESTADO = """
    SELECT id, data_hora, valor_total, endereco_entrega, estado, id_cliente
    FROM pedido
    WHERE (estado = ?)
"""