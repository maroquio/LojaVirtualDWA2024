from PIL import Image


def transformar_em_quadrada(imagem_original, tamanho_maximo=480):
    # captura largura e altura da imagem original
    largura, altura = imagem_original.size
    # obtém a menor das arestas (altura ou largura)
    tamanho_quadrado = min(largura, altura)
    # cria uma imagem quadrada branca com lado
    # do tamanho da menor aresta
    imagem_quadrada = Image.new(
        "RGB", (tamanho_quadrado, tamanho_quadrado), (255, 255, 255)
    )
    # computa o deslocamento vertical ou horizontal para
    # centralizar a imagem original na imagem quadrada
    x_offset = (tamanho_quadrado - largura) // 2
    y_offset = (tamanho_quadrado - altura) // 2
    # cola a imagem original na imagem quadrada considerando
    # os deslocamentos computados acima
    imagem_quadrada.paste(imagem_original, (x_offset, y_offset))
    # caso o lado da imagem quadrada seja maior que o tamanho máximo
    if imagem_quadrada.size[0] > tamanho_maximo:
        # redimensiona a imagem para que seu lado tenha o tamanho máximo
        imagem_quadrada = imagem_quadrada.resize(
            (tamanho_maximo, tamanho_maximo), Image.Resampling.LANCZOS
        )
    # retorna a imagem quadrada e redimensionada (quando necessário)
    return imagem_quadrada