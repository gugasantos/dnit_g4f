# Usar uma imagem oficial do Python
FROM python:3.12-slim

# Definir o diretório de trabalho
WORKDIR /app

# Copiar o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt .

# Instalar as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código fonte da aplicação
COPY . .

# Definir o comando para rodar o script Python
CMD ["python", "transformaimg.py"]
