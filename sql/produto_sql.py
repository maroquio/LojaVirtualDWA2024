SQL_CRIAR_TABELA = """
    CREATE TABLE IF NOT EXISTS produto (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco FLOAT NOT NULL,
        descricao TEXT NOT NULL,
        estoque INTEGER NOT NULL)
"""

SQL_INSERIR = """
    INSERT INTO produto(nome, preco, descricao, estoque)
    VALUES (?, ?, ?, ?)
"""

SQL_OBTER_TODOS = """
    SELECT id, nome, preco, descricao, estoque
    FROM produto
    ORDER BY nome
"""

SQL_ALTERAR = """
    UPDATE produto
    SET nome=?, preco=?, descricao=?, estoque=?
    WHERE id=?
"""

SQL_EXCLUIR = """
    DELETE FROM produto    
    WHERE id=?
"""

SQL_OBTER_UM = """
    SELECT id, nome, preco, descricao, estoque
    FROM produto
    WHERE id=?
"""

SQL_OBTER_QUANTIDADE = """
    SELECT COUNT(*) FROM produto
"""

SQL_OBTER_BUSCA = """
    SELECT id, nome, preco, descricao, estoque
    FROM produto
    WHERE nome LIKE ? OR descricao LIKE ?
    ORDER BY #1
    LIMIT ? OFFSET ?
"""

SQL_OBTER_QUANTIDADE_BUSCA = """
    SELECT COUNT(*) FROM produto
    WHERE nome LIKE ? OR descricao LIKE ?
"""