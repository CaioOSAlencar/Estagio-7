# 🎯 Estágio 7 - Automação Web com Selenium

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Concluído-success.svg)

## 📋 Descrição do Projeto

Este projeto demonstra técnicas avançadas de automação web utilizando Selenium WebDriver em Python. O foco está em estratégias de localização de elementos DOM e extração de dados de páginas web, apresentando duas atividades práticas complementares.

### 🎯 Objetivos de Aprendizado

- **Mapeamento de Elementos DOM**: Demonstração de 13 estratégias diferentes para localizar elementos em páginas web
- **Extração de Dados**: Automatização da coleta e processamento de dados estruturados
- **Interação Web**: Simulação de ações do usuário em interfaces web
- **Boas Práticas**: Implementação de código limpo e tratamento de exceções

---

## 🚀 Atividades Desenvolvidas

### 📊 **Atividade Solo**: Mapeamento de Elementos E-commerce
**Arquivo**: [`atividade-solo.py`](./atividade-solo.py)

Demonstração completa de localização de elementos no site da Amazon Brasil, utilizando:

#### 🔍 Estratégias de Localização Implementadas:

1. **By.ID** - Localização por identificador único
2. **By.NAME** - Localização por atributo name
3. **By.CLASS_NAME** - Localização por classe CSS
4. **By.TAG_NAME** - Localização por tag HTML
5. **By.CSS_SELECTOR** - Seletores CSS simples e complexos
6. **By.XPATH** - Caminhos XML básicos e avançados
7. **Data Attributes** - Elementos com atributos data-*
8. **Attribute Contains** - Atributos que contêm texto específico
9. **Pseudo Selectors** - Seletores CSS pseudo-classes
10. **Multiple Attributes** - Combinação de múltiplos atributos
11. **XPath Advanced** - XPath com condições complexas
12. **Text Content** - Localização por conteúdo de texto
13. **Position Context** - Localização por posição e contexto

#### ✨ Funcionalidades:
- Análise automática de elementos da página
- Geração de relatórios detalhados em JSON
- Tratamento robusto de exceções
- Interface de linha de comando informativa

### 🎮 **Atividade Squad**: Challenge DOM Interactive
**Arquivo**: [`atividade-squad.py`](./atividade-squad.py)

Automação interativa do site "The Internet - Challenging DOM", focando em:

#### 🛠️ Funcionalidades Principais:
- **Extração de Dados**: Coleta automática de dados tabulares
- **Interação com Botões**: Cliques automatizados em elementos de ação
- **Modo Interativo**: Interface de usuário no terminal
- **Exportação de Dados**: Suporte a CSV e JSON
- **Recarregamento Dinâmico**: Atualização de dados em tempo real

#### 📱 Interface Interativa:
```
🎮 MODO INTERATIVO - Escolha uma opção:
1. Mostrar dados da tabela
2. Clicar em botão Edit de uma linha
3. Clicar em botão Delete de uma linha
4. Salvar dados em CSV
5. Salvar dados em JSON
6. Recarregar página
0. Sair
```

---

## 🛠️ Tecnologias Utilizadas

### 🔧 Dependências Principais
```python
selenium==4.15.0+     # WebDriver para automação web
webdriver-manager     # Gerenciamento automático de drivers
```

### 📚 Bibliotecas Padrão
- `json` - Manipulação de dados JSON
- `csv` - Processamento de arquivos CSV
- `datetime` - Timestamp e controle temporal
- `time` - Controle de delays e timeouts

### 🌐 Navegador Suportado
- **Google Chrome** (ChromeDriver gerenciado automaticamente)

---

## 📦 Instalação e Configuração

### 1️⃣ **Pré-requisitos**
```bash
# Python 3.7 ou superior
python --version

# Google Chrome instalado
```

### 2️⃣ **Instalação das Dependências**
```bash
# Clone o repositório
git clone https://github.com/CaioOSAlencar/Estagio-7.git
cd Estagio-7

# Instale as dependências
pip install selenium webdriver-manager
```

### 3️⃣ **Configuração Alternativa com Requirements**
```bash
# Se houver arquivo requirements.txt
pip install -r requirements.txt
```

---

## 🚀 Como Executar

### 🎯 **Atividade Solo** (Mapeamento E-commerce)
```bash
python atividade-solo.py
```

**Saída Esperada:**
- Análise de 13 estratégias de localização
- Relatório detalhado no terminal
- Arquivo JSON com resultados completos

### 🎮 **Atividade Squad** (Challenge DOM)
```bash
python atividade-squad.py
```

**Recursos Disponíveis:**
- Extração automática de dados tabulares
- Modo interativo no terminal
- Exportação para CSV/JSON
- Cliques automatizados em botões

---

## 📊 Arquivos de Saída

### 📄 **Relatórios Gerados**

| Arquivo | Descrição | Formato |
|---------|-----------|---------|
| `ecommerce_mapping_results_*.json` | Resultados do mapeamento de elementos | JSON |
| `challenge_dom_data_*.csv` | Dados extraídos da tabela DOM | CSV |
| `challenge_dom_data_*.json` | Dados extraídos em formato estruturado | JSON |

### 📋 **Estrutura dos Dados JSON** (Atividade Solo)
```json
{
  "metadata": {
    "site_testado": "Amazon Brasil",
    "data_execucao": "2024-10-07 14:16:48",
    "total_estrategias": 13,
    "estrategias_sucessos": 11
  },
  "resultados": [
    {
      "estrategia": "By.ID",
      "elemento": "Barra de Pesquisa",
      "encontrado": true,
      "localizador": "twotabsearchtextbox"
    }
  ]
}
```

---

## 🎯 Conceitos Técnicos Demonstrados

### 🔧 **Selenium WebDriver**
- Inicialização e configuração do navegador
- Gerenciamento de timeouts e waits
- Localização de elementos por múltiplas estratégias
- Interação com elementos (cliques, digitação)

### 🧹 **Boas Práticas**
- **Tratamento de Exceções**: Captura e manejo de erros específicos
- **Código Limpo**: Funções bem definidas e documentadas
- **Configuração Flexível**: Opções de execução (headless, timeouts)
- **Logging Detalhado**: Feedback visual do progresso

### 📊 **Processamento de Dados**
- Extração estruturada de dados web
- Serialização em múltiplos formatos
- Timestamping para controle de versão

---

## 🎨 Recursos Visuais

### 🎭 **Interface Terminal**
```
🛒 DEMONSTRAÇÃO DE MAPEAMENTO DE ELEMENTOS E-COMMERCE
============================================================
🚀 Navegador iniciado com sucesso!
🌐 Carregando Amazon Brasil...
✅ Amazon carregada com sucesso!

🎯 ESTRATÉGIA 1: By.ID
----------------------------------------
✅ Elemento encontrado: input
   ID: twotabsearchtextbox
   Placeholder: Pesquise Amazon.com.br
   💡 Demonstração: Texto 'smartphone' inserido na busca
```

### 📊 **Relatório de Resultados**
```
📊 RELATÓRIO FINAL DA DEMONSTRAÇÃO
============================================================
✅ Estratégias bem-sucedidas: 11/13
📈 Taxa de sucesso: 84.6%

📋 Resumo por Estratégia:
  1. ✅ By.ID: Barra de Pesquisa
  2. ✅ By.NAME: Campo de Palavras-chave
  3. ✅ By.CLASS_NAME: Elemento de Navegação (3 encontrados)
  4. ✅ By.TAG_NAME: Imagens (127 encontrados)
  ...
```

---

## 🔧 Configurações Avançadas

### ⚙️ **Opções do Chrome**
```python
chrome_options = Options()
chrome_options.add_argument('--headless')          # Execução sem interface
chrome_options.add_argument('--no-sandbox')        # Bypass de sandbox
chrome_options.add_argument('--disable-dev-shm-usage')  # Otimização de memória
```

### ⏱️ **Timeouts e Waits**
```python
wait = WebDriverWait(driver, 15)  # Timeout de 15 segundos
wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
```

---

## 📚 Estrutura do Projeto

```
Estagio-7/
├── 📄 README.md                          # Documentação principal
├── 🐍 atividade-solo.py                  # Mapeamento de elementos
├── 🎮 atividade-squad.py                 # Challenge DOM interativo
├── 📊 challenge_dom_data_*.csv           # Dados exportados (CSV)
├── 📋 challenge_dom_data_*.json          # Dados exportados (JSON)
├── 📈 ecommerce_mapping_results_*.json   # Relatórios de mapeamento
└── 📂 .git/                             # Controle de versão
```

---

## 🤝 Contribuições

Este projeto foi desenvolvido como parte do programa de estágio, demonstrando competências em:

- **Automação Web**: Selenium WebDriver
- **Python Avançado**: OOP, tratamento de exceções, manipulação de dados
- **Documentação**: Código limpo e bem documentado
- **Boas Práticas**: Estrutura modular e reutilizável

---

## 📞 Contato e Informações

**Desenvolvedor**: Caio Alencar  
**Projeto**: Estágio 7 - Automação Web  
**Data**: Outubro 2024  
**Tecnologia Principal**: Python + Selenium WebDriver

---

## 📜 Licença

Este projeto é desenvolvido para fins educacionais e de demonstração técnica.

---

**⭐ Se este projeto foi útil para você, considere dar uma estrela no repositório!**