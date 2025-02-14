import fitz  # PyMuPDF
import base64
import requests
import os

def extract_images_from_pdf(pdf_path, output_folder):
    """
    Extrai imagens de um arquivo PDF e as salva no diretório especificado.
    Retorna uma lista dos caminhos das imagens extraídas.
    """
    doc = fitz.open(pdf_path)
    image_paths = []
    for i in range(len(doc)):
        for img in doc.get_page_images(i):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            image_path = os.path.join(output_folder, f"image_{i+1}.{image_ext}")
            with open(image_path, "wb") as img_file:
                img_file.write(image_bytes)
            image_paths.append(image_path)
    return image_paths

def get_image_description(image_path):
    """
    Obtém a descrição de uma imagem usando o servidor Ollama.
    """
    with open(image_path, "rb") as img_file:
        image_data = img_file.read()
    image_base64 = base64.b64encode(image_data).decode('utf-8')
    payload = {
        "model": "llava",
        "prompt": "Descreva esta imagem:",
        "images": [image_base64],
        "stream": False
    }
    response = requests.post("http://localhost:11434/api/generate", json=payload)
    if response.status_code == 200:
        result = response.json()
        return result.get("message", {}).get("content", "Descrição não disponível.")
    else:
        return "Erro ao obter descrição da imagem."

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
