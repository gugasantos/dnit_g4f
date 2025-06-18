from PIL import Image, ImageDraw
import pytesseract

# Abre imagem
imagem = Image.open("/app/imagens/imagensgrifadas.png").convert("RGBA")

# OCR com coordenadas
ocr = pytesseract.image_to_data(imagem, lang='por', output_type=pytesseract.Output.DICT)

# Frases a serem grifadas
alvos = [
    "Data de Postagem",
    "Situação",
    "Serviço de Expedição",
    "SNE",
    "Número do Auto"
]
alvos = [a.lower() for a in alvos]

# Inicializa marcação
marca = Image.new("RGBA", imagem.size, (255, 255, 255, 0))
draw = ImageDraw.Draw(marca)

n = len(ocr["text"])
valor_extraido = None

for i in range(n):
    palavras = []
    coords = []
    for j in range(i, min(i + 5, n)):  # Tenta formar frases de até 5 palavras
        palavra = ocr["text"][j].strip()
        if palavra == "":
            break
        palavras.append(palavra.lower())
        coords.append(j)
        frase = " ".join(palavras)

        if frase in alvos:
            # Grifa a frase
            x1 = min([ocr["left"][k] for k in coords])
            y1 = min([ocr["top"][k] for k in coords])
            x2 = max([ocr["left"][k] + ocr["width"][k] for k in coords])
            y2 = max([ocr["top"][k] + ocr["height"][k] for k in coords])
            draw.rectangle([x1, y1, x2, y2], fill=(255, 255, 0, 100))

            # Se for a frase "número do auto", procura o valor abaixo
            if frase == "número do auto":
                centro_x = (x1 + x2) / 2
                base_y = y2
                menor_dist = float("inf")
                valor_abaixo = None
                coord_valor = None

                for k in range(n):
                    if ocr["text"][k].strip() == "":
                        continue
                    x = ocr["left"][k]
                    y = ocr["top"][k]
                    w = ocr["width"][k]
                    h = ocr["height"][k]
                    centro_palavra = x + w / 2

                    if abs(centro_palavra - centro_x) < 60 and y > base_y:
                        dist = y - base_y
                        if dist < menor_dist:
                            menor_dist = dist
                            valor_abaixo = ocr["text"][k].strip()
                            coord_valor = (x, y, x + w, y + h)

                if valor_abaixo and coord_valor:
                    draw.rectangle(coord_valor, fill=(255, 255, 0, 100))
                    valor_extraido = valor_abaixo
            break

# Salva imagem final
imagem_marcada = Image.alpha_composite(imagem, marca)
imagem_marcada.convert("RGB").save("/app/imagens/imagemgrifada.jpg", "JPEG")

# Exibe valor extraído
if valor_extraido:
    print(f"[{valor_extraido}]")
