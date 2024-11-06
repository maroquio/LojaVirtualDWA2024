SQL_CRIAR_TABELA = """
    CREATE TABLE IF NOT EXISTS usuario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cpf TEXT NOT NULL UNIQUE,
        data_nascimento DATE NOT NULL,
        endereco TEXT NOT NULL,
        telefone TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL UNIQUE,
        perfil INTEGER DEFAULT 1,
        senha TEXT NOT NULL,
        token TEXT)
"""

SQL_INSERIR = """
    INSERT INTO usuario(nome, cpf, data_nascimento, endereco, telefone, email, perfil, senha)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
"""

SQL_OBTER_TODOS_POR_PERFIL = """
    SELECT id, nome, cpf, data_nascimento, endereco, telefone, email
    FROM usuario
    WHERE perfil=?
    ORDER BY nome
"""

SQL_OBTER_TODOS = """
    SELECT id, nome, cpf, data_nascimento, endereco, telefone, email
    FROM usuario
    ORDER BY nome
"""

SQL_ALTERAR = """
    UPDATE usuario
    SET nome=?, cpf=?, data_nascimento=?, endereco=?, telefone=?, email=?
    WHERE id=?
"""

SQL_ALTERAR_TOKEN = """
    UPDATE usuario
    SET token=?
    WHERE id=?
"""

SQL_ALTERAR_SENHA = """
    UPDATE usuario
    SET senha=?
    WHERE id=?
"""

SQL_EXCLUIR = """
    DELETE FROM usuario    
    WHERE id=?
"""

SQL_OBTER_POR_ID = """
    SELECT id, nome, cpf, data_nascimento, endereco, telefone, email, perfil
    FROM usuario
    WHERE id=?
"""

SQL_OBTER_POR_EMAIL = """
    SELECT id, nome, cpf, data_nascimento, endereco, telefone, email, perfil, senha
    FROM usuario
    WHERE email=?
"""

SQL_OBTER_POR_TOKEN = """
    SELECT id, nome, cpf, data_nascimento, endereco, telefone, email, perfil
    FROM usuario
    WHERE token=?
"""

SQL_OBTER_QUANTIDADE_POR_PERFIL = """
    SELECT COUNT(*)
    FROM usuario
    WHERE perfil=?
"""

SQL_OBTER_BUSCA = """
    SELECT id, nome, cpf, data_nascimento, endereco, telefone, email
    FROM usuario
    WHERE nome LIKE ? OR cpf LIKE ?
    ORDER BY nome
    LIMIT ? OFFSET ?
"""

SQL_OBTER_QUANTIDADE_BUSCA = """
    SELECT COUNT(*) FROM usuario
    WHERE nome LIKE ? OR cpf LIKE ?
"""
