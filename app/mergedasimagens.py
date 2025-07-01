from PIL import Image

# Caminhos das imagens PNG
imagem1 = Image.open("/app/imagens/filial.png").convert("RGB")
imagem2 = Image.open("/app/imagens/matriz.png").convert("RGB")

# Lista com as imagens que vão para o PDF (exceto a primeira)
imagens = [imagem2]

# Salva como PDF
imagem1.save("/app/imagens/matriz_filial.pdf", save_all=True, append_images=imagens)