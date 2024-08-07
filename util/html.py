def ler_html(nome_arquivo: str) -> str:
    with open(f"html/{nome_arquivo}.html", "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()        
        return conteudo