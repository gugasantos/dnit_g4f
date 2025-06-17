from PIL import Image

# Lista com os caminhos das imagens
imagens = ['/app/imagens/imagemgrifada.jpg', '/app/imagens/imagemgrifada2.jpg']

# Abrir todas as imagens e converter para RGB (necessário para PDF)
imagens_abertas = [Image.open(img).convert('RGB') for img in imagens]

# A primeira imagem será a capa do PDF
imagem_principal = imagens_abertas[0]

# As demais imagens serão adicionadas nas próximas páginas
outras_imagens = imagens_abertas[1:]

# Salvar no PDF (na mesma pasta onde estão as imagens)
imagem_principal.save('/app/imagens/saida.pdf', save_all=True, append_images=outras_imagens)
