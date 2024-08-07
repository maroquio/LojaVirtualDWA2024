SQL_CRIAR_TABELA = """
    CREATE TABLE IF NOT EXISTS cliente (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cpf TEXT NOT NULL UNIQUE,
        data_nascimento DATE NOT NULL,
        endereco TEXT NOT NULL,
        telefone TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL UNIQUE,
        senha TEXT NOT NULL,
        token TEXT)
"""

SQL_INSERIR = """
    INSERT INTO cliente(nome, cpf, data_nascimento, endereco, telefone, email, senha)
    VALUES (?, ?, ?, ?, ?, ?, ?)
"""

SQL_OBTER_TODOS = """
    SELECT id, nome, cpf, data_nascimento, endereco, telefone, email
    FROM cliente
    ORDER BY nome
"""

SQL_ALTERAR = """
    UPDATE cliente
    SET nome=?, cpf=?, data_nascimento=?, endereco=?, telefone=?, email=?
    WHERE id=?
"""

SQL_ALTERAR_TOKEN = """
    UPDATE cliente
    SET token=?
    WHERE id=?
"""

SQL_ALTERAR_SENHA = """
    UPDATE cliente
    SET senha=?
    WHERE id=?
"""

SQL_EXCLUIR = """
    DELETE FROM cliente    
    WHERE id=?
"""

SQL_OBTER_POR_ID = """
    SELECT id, nome, cpf, data_nascimento, endereco, telefone, email
    FROM cliente
    WHERE id=?
"""

SQL_OBTER_POR_EMAIL = """
    SELECT id, nome, cpf, data_nascimento, endereco, telefone, email, senha
    FROM cliente
    WHERE email=?
"""

SQL_OBTER_POR_TOKEN = """
    SELECT id, nome, cpf, data_nascimento, endereco, telefone, email
    FROM cliente
    WHERE token=?
"""

SQL_OBTER_QUANTIDADE = """
    SELECT COUNT(*) FROM cliente
"""

SQL_OBTER_BUSCA = """
    SELECT id, nome, cpf, data_nascimento, endereco, telefone, email
    FROM cliente
    WHERE nome LIKE ? OR cpf LIKE ?
    ORDER BY nome
    LIMIT ? OFFSET ?
"""

SQL_OBTER_QUANTIDADE_BUSCA = """
    SELECT COUNT(*) FROM cliente
    WHERE nome LIKE ? OR cpf LIKE ?
"""
