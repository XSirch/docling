# Conversor de Arquivos para Markdown

Uma aplicação web moderna desenvolvida com Streamlit para conversão inteligente de documentos (PDF, DOCX, XLSX) para formato Markdown, com recursos avançados de processamento de imagens usando IA.

## 🚀 Funcionalidades Principais

### 📄 **Conversão de Documentos**
- **PDF**: Conversão completa com extração e descrição automática de imagens via Ollama AI
- **DOCX**: Conversão de documentos Word preservando formatação e estrutura
- **XLSX**: Processamento de planilhas Excel com remoção automática de fórmulas

### 🖼️ **Processamento Inteligente de Imagens**
- Extração automática de imagens de arquivos PDF
- Geração de descrições em português usando modelo LLaVA via Ollama
- Sistema de cache para otimizar performance e evitar processamento duplicado
- Integração das descrições no markdown final

### 🔐 **Sistema de Autenticação**
- Login seguro com hash de senhas usando bcrypt
- Banco de dados SQLite para gerenciamento de usuários
- Interface protegida para upload e conversão de documentos

### ⚡ **Recursos Técnicos**
- Interface web responsiva com Streamlit
- Processamento em tempo real com feedback visual
- Download direto dos arquivos convertidos
- Suporte a múltiplos formatos de entrada

## 📋 Requisitos

### **Sistema**
- Python 3.8 ou superior
- Windows, macOS ou Linux
- Ollama instalado e configurado (para processamento de imagens)

### **Dependências Principais**
- Streamlit (interface web)
- Docling (conversão de documentos)
- PyMuPDF (processamento de PDF)
- OpenPyXL (manipulação de Excel)
- Requests (comunicação com Ollama API)
- BCrypt (segurança de senhas)

## 🛠️ Instalação

### **1. Pré-requisitos**
Instale o Ollama para processamento de imagens:
```bash
# Windows/macOS/Linux
curl -fsSL https://ollama.ai/install.sh | sh

# Instale o modelo LLaVA
ollama pull llava:latest
```

### **2. Clone o repositório**
```bash
git clone https://github.com/XSirch/docling
cd docling
```

### **3. Configure o ambiente virtual**
```bash
# Crie o ambiente virtual
python -m venv .venv

# Ative o ambiente virtual
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
```

### **4. Instale as dependências**
```bash
pip install streamlit docling PyMuPDF openpyxl requests bcrypt sqlite3
```

## 🚀 Como Usar

### **1. Inicie a aplicação**
```bash
# Certifique-se de que o ambiente virtual está ativo
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # macOS/Linux

# Inicie o servidor Streamlit
streamlit run app.py
```

### **2. Acesse a aplicação**
- Abra seu navegador em `http://localhost:8501`
- Faça login com suas credenciais (crie uma conta se necessário)

### **3. Converta documentos**
1. **Upload**: Selecione um arquivo PDF, DOCX ou XLSX
2. **Conversão**: Clique em "Converter" e aguarde o processamento
3. **Download**: Baixe o arquivo Markdown gerado

## 📁 Estrutura do Projeto

```
📁 docling/
├── 📄 app.py                 # Aplicação principal consolidada
├── 📁 imagepdf/
│   ├── 📄 __init__.py
│   └── 📄 imagepdf2.py      # Módulo de processamento de imagens
├── 📁 .streamlit/
│   └── 📄 config.toml       # Configurações do Streamlit
├── 📁 uploads/              # Arquivos enviados pelos usuários
├── 📁 converted/            # Arquivos convertidos
├── 📁 images/               # Imagens extraídas de PDFs
├── 📄 users.db             # Banco de dados de usuários
└── 📄 README.md            # Esta documentação
```

## 🔧 Configuração Avançada

### **Ollama API**
- **Endpoint**: `http://localhost:11434/api/generate`
- **Modelo**: `llava:latest`
- **Prompt personalizado**: Configurado para descrições em português

### **Streamlit**
- **Porta padrão**: 8501
- **Configurações**: `.streamlit/config.toml`
- **Modo de desenvolvimento**: Desabilitado por padrão

## 🔍 Funcionalidades Detalhadas

### **Processamento de PDF**
- ✅ Extração de texto e tabelas via Docling
- ✅ Extração automática de imagens via PyMuPDF
- ✅ Descrição de imagens via IA (Ollama + LLaVA)
- ✅ Cache inteligente para evitar reprocessamento
- ✅ Integração de imagens no markdown final

### **Processamento de Excel**
- ✅ Remoção automática de fórmulas
- ✅ Preservação de valores calculados
- ✅ Suporte a múltiplas planilhas
- ✅ Conversão para markdown via Docling

### **Processamento de Word**
- ✅ Conversão direta via Docling
- ✅ Preservação de formatação
- ✅ Suporte a tabelas e listas

## 🐛 Solução de Problemas

### **Ollama não responde**
```bash
# Verifique se o Ollama está rodando
ollama list

# Reinicie o serviço se necessário
ollama serve
```

### **Erro de importação**
```bash
# Reinstale as dependências
pip install --upgrade streamlit docling PyMuPDF openpyxl
```

### **Problemas de permissão**
- Certifique-se de que as pastas `uploads/`, `converted/` e `images/` têm permissão de escrita

## 📊 Status do Projeto

- ✅ **Aplicação consolidada** - Código unificado em `app.py`
- ✅ **Processamento de imagens** - Integração completa com Ollama
- ✅ **Sistema de cache** - Otimização de performance
- ✅ **Suporte multi-formato** - PDF, DOCX, XLSX
- ✅ **Interface moderna** - Streamlit responsivo
- ✅ **Segurança** - Autenticação com hash de senhas

## 🤝 Contribuição

Contribuições são bem-vindas! Para contribuir:

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👨‍💻 Autor

Desenvolvido com ❤️ para facilitar a conversão e processamento inteligente de documentos.
