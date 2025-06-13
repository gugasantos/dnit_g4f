from PIL import Image, ImageDraw

# Abre a imagem base
imagem = Image.open("/app/imagens/imagensgrifadas.png").convert("RGBA")

# Cria uma camada transparente para marcações
marca = Image.new("RGBA", imagem.size, (255, 255, 255, 0))

draw = ImageDraw.Draw(marca)


# | Elemento         | Coordenadas `(x1, y1, x2, y2)` |
# | ---------------- | ------------------------------ |
# | `e-Carta`        | `(104, 135, 190, 150)`         |
# | `Número do Auto` | `(120, 408, 285, 430)`         |
# | `Infrator`       | `(125, 481, 490, 505)`         |

# x1 = X
# y1 = Y
# x2 = X + W
# y2 = Y + H



# Cor da marca-texto (amarelo translúcido)
cor_marca = (255, 255, 0, 100)

areas_para_destacar = [
    (0, 210, 60, 236),   # e-Carta
    (0, 515, 94, 543),   # Número do Auto
    (0, 662, 297, 688),   # Infrator
]

for x1, y1, x2, y2 in areas_para_destacar:
    draw.rectangle([x1, y1, x2, y2], fill=(255, 255, 0, 100))

# Mescla com a imagem original
imagem_marcada = Image.alpha_composite(imagem, marca)

# Salva o resultado
imagem_marcada.convert("RGB").save("/app/imagens/imagemgrifada.jpg", "JPEG")
