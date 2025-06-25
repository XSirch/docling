import fitz  # PyMuPDF
import base64
import requests
import os
import hashlib

# Dicionário que funcionará como cache: chave = hash da imagem, valor = resultado da consulta
cache_resultados = {}

def calcular_hash(imagem_bytes):
    """Calcula o hash SHA-256 dos bytes da imagem."""
    return hashlib.sha256(imagem_bytes).hexdigest()

def extract_images_from_pdf(pdf_path, output_folder):
    """
    Extrai imagens de um arquivo PDF e as salva no diretório especificado.
    Retorna uma lista dos caminhos das imagens extraídas.
    """
    doc = fitz.open(pdf_path)
    image_paths = []
    image_counter = 1
    for i in range(len(doc)):
        for img in doc.get_page_images(i):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            # Use a global counter to avoid naming conflicts
            image_path = os.path.join(output_folder, f"image_{image_counter:03d}.{image_ext}")
            with open(image_path, "wb") as img_file:
                img_file.write(image_bytes)
            image_paths.append(image_path)
            image_counter += 1
    return image_paths

def enviar_imagem_ao_modelo(image_base64, model="llava:latest", prompt="Analise a imagem fornecida e retorne apenas uma frase curta e genérica. "
        "Se a imagem contiver elementos sensiveis como logotipos ou assinaturas, responda apenas com uma mensagem generica, por exemplo, "
        "'Aqui há um logotipo' ou 'Aqui há uma assinatura'. Não inclua detalhes adicionais. A resposta não deve ser longa, no máximo 5 palavras. Responda sempre em português."):
    """
    Envia a imagem codificada para a API do Ollama com o prompt especificado
    e retorna a resposta.
    """
    payload = {
        "model": model,
        "prompt": prompt,
        "images": [image_base64],
        "stream": False
    }
    response = requests.post("http://localhost:11434/api/generate", json=payload)
    if response.status_code == 200:
        result = response.json()
        # Usando a chave "response" conforme o retorno visto nos logs
        return result.get("response", "Descrição não disponível.")
    else:
        return "Erro ao obter descrição da imagem."

def get_image_description(image_path):
    """
    Obtém a descrição de uma imagem usando o servidor Ollama, utilizando cache.
    Se a imagem já estiver processada, retorna o resultado armazenado.
    """
    with open(image_path, "rb") as img_file:
        image_data = img_file.read()
    imagem_hash = calcular_hash(image_data)
    
    if imagem_hash in cache_resultados:
        print(f"{image_path}: Resultado em cache.")
        return cache_resultados[imagem_hash]
    else:
        image_base64 = base64.b64encode(image_data).decode("utf-8")
        prompt = (
            "Analise a imagem fornecida e retorne apenas uma frase curta e genérica. "
            "Se a imagem contiver elementos como logotipos ou assinaturas, responda com uma mensagem curta, "
            "por exemplo, 'Aqui há um logotipo' ou 'Aqui há uma assinatura'. Não inclua detalhes adicionais."
        )
        print(f"{image_path}: Enviando imagem para o modelo...")
        resultado = enviar_imagem_ao_modelo(image_base64, prompt=prompt)
        cache_resultados[imagem_hash] = resultado
        return resultado

def process_pdf_to_markdown_with_image_descriptions(pdf_path, output_folder):
    """
    Processa um arquivo PDF, extrai as imagens, obtém suas descrições e
    gera um conteúdo em Markdown com as descrições das imagens.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    image_paths = extract_images_from_pdf(pdf_path, output_folder)
    markdown_content = f"# Conteúdo do PDF: {os.path.basename(pdf_path)}\n\n"
    
    for image_path in image_paths:
        description = get_image_description(image_path)
        markdown_content += f"![{description}]({image_path})\n\n"
    
    return markdown_content
