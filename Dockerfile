# Usar imagem oficial do Python
FROM python:3.12-slim

# Instalar Tesseract com suporte ao idioma português
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    tesseract-ocr-por \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Definir diretório de trabalho
WORKDIR /app

# Copiar e instalar dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Garantir que Pillow e pytesseract estão presentes
RUN pip install --no-cache-dir pillow pytesseract

# Copiar a aplicação
COPY . .

# Definir o comando de execução
CMD ["python", "transformaimg.py"]
