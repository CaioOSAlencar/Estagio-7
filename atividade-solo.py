"""
ATIVIDADE SOLO - Mapeamento de Elementos HTML
============================================

Site escolhido: Amazon (https://www.amazon.com.br)
Demonstração das principais estratégias de localização de elementos:

1. By.ID - Localizar por ID único
2. By.NAME - Localizar por atributo name
3. By.CLASS_NAME - Localizar por classe CSS
4. By.TAG_NAME - Localizar por tag HTML
5. By.CSS_SELECTOR - Localizar por seletor CSS
6. By.XPATH - Localizar por caminho XML
7. By.LINK_TEXT - Localizar por texto do link
8. By.PARTIAL_LINK_TEXT - Localizar por texto parcial do link

Autor: Estudante de Estágio
Data: Outubro 2024
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import json
from datetime import datetime

class EcommerceMappingDemo:
    def __init__(self, headless=False):
        """Inicializa o navegador para demonstração de mapeamento"""
        print("🛒 DEMONSTRAÇÃO DE MAPEAMENTO DE ELEMENTOS E-COMMERCE")
        print("=" * 60)
        
        chrome_options = Options()
        if headless:
            chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        
        self.service = Service()
        self.driver = webdriver.Chrome(service=self.service, options=chrome_options)
        self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        self.wait = WebDriverWait(self.driver, 15)
        self.mapping_results = []
        
        print("🚀 Navegador iniciado com sucesso!")
    
    def load_amazon_homepage(self):
        """Carrega a página inicial da Amazon Brasil"""
        try:
            print("\n🌐 Carregando Amazon Brasil...")
            self.driver.get("https://www.amazon.com.br")
            
            # Aguarda o carregamento da página
            self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
            print("✅ Amazon carregada com sucesso!")
            
            # Aguarda um pouco mais para garantir carregamento completo
            time.sleep(3)
            return True
            
        except TimeoutException:
            print("❌ Erro: Tempo limite para carregar a Amazon")
            return False
    
    def strategy_1_by_id(self):
        """Estratégia 1: Localização por ID"""
        print("\n🎯 ESTRATÉGIA 1: By.ID")
        print("-" * 40)
        
        try:
            # Tenta encontrar a barra de pesquisa por ID
            search_box = self.driver.find_element(By.ID, "twotabsearchtextbox")
            
            result = {
                'estrategia': 'By.ID',
                'elemento': 'Barra de Pesquisa',
                'localizador': 'twotabsearchtextbox',
                'encontrado': True,
                'tag_name': search_box.tag_name,
                'texto_placeholder': search_box.get_attribute('placeholder'),
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
            print(f"✅ Elemento encontrado: {search_box.tag_name}")
            print(f"   ID: {search_box.get_attribute('id')}")
            print(f"   Placeholder: {search_box.get_attribute('placeholder')}")
            
            # Demonstração: digita algo na busca
            search_box.clear()
            search_box.send_keys("smartphone")
            print("   💡 Demonstração: Texto 'smartphone' inserido na busca")
            time.sleep(1)
            search_box.clear()
            
        except NoSuchElementException:
            result = {
                'estrategia': 'By.ID',
                'elemento': 'Barra de Pesquisa',
                'localizador': 'twotabsearchtextbox',
                'encontrado': False,
                'erro': 'Elemento não encontrado',
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            print("❌ Elemento não encontrado por ID")
        
        self.mapping_results.append(result)
    
    def strategy_2_by_name(self):
        """Estratégia 2: Localização por NAME"""
        print("\n🎯 ESTRATÉGIA 2: By.NAME")
        print("-" * 40)
        
        try:
            # Procura por elementos com atributo name
            search_field = self.driver.find_element(By.NAME, "field-keywords")
            
            result = {
                'estrategia': 'By.NAME',
                'elemento': 'Campo de Palavras-chave',
                'localizador': 'field-keywords',
                'encontrado': True,
                'tag_name': search_field.tag_name,
                'type': search_field.get_attribute('type'),
                'name': search_field.get_attribute('name'),
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
            print(f"✅ Elemento encontrado: {search_field.tag_name}")
            print(f"   Name: {search_field.get_attribute('name')}")
            print(f"   Type: {search_field.get_attribute('type')}")
            
        except NoSuchElementException:
            result = {
                'estrategia': 'By.NAME',
                'elemento': 'Campo de Palavras-chave',
                'localizador': 'field-keywords',
                'encontrado': False,
                'erro': 'Elemento não encontrado',
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            print("❌ Elemento não encontrado por NAME")
        
        self.mapping_results.append(result)
    
    def strategy_3_by_class_name(self):
        """Estratégia 3: Localização por CLASS_NAME"""
        print("\n🎯 ESTRATÉGIA 3: By.CLASS_NAME")
        print("-" * 40)
        
        try:
            # Procura por botões ou elementos com classes específicas
            nav_elements = self.driver.find_elements(By.CLASS_NAME, "nav-line-1")
            
            if nav_elements:
                element = nav_elements[0]
                result = {
                    'estrategia': 'By.CLASS_NAME',
                    'elemento': 'Elemento de Navegação',
                    'localizador': 'nav-line-1',
                    'encontrado': True,
                    'quantidade_encontrada': len(nav_elements),
                    'tag_name': element.tag_name,
                    'texto': element.text,
                    'classes': element.get_attribute('class'),
                    'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                
                print(f"✅ {len(nav_elements)} elemento(s) encontrado(s)")
                print(f"   Primeiro elemento: {element.tag_name}")
                print(f"   Texto: '{element.text}'")
                print(f"   Classes: {element.get_attribute('class')}")
            else:
                raise NoSuchElementException()
                
        except NoSuchElementException:
            result = {
                'estrategia': 'By.CLASS_NAME',
                'elemento': 'Elemento de Navegação',
                'localizador': 'nav-line-1',
                'encontrado': False,
                'erro': 'Elemento não encontrado',
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            print("❌ Elemento não encontrado por CLASS_NAME")
        
        self.mapping_results.append(result)
    
    def strategy_4_by_tag_name(self):
        """Estratégia 4: Localização por TAG_NAME"""
        print("\n🎯 ESTRATÉGIA 4: By.TAG_NAME")
        print("-" * 40)
        
        try:
            # Procura por todas as imagens na página
            images = self.driver.find_elements(By.TAG_NAME, "img")
            
            result = {
                'estrategia': 'By.TAG_NAME',
                'elemento': 'Imagens',
                'localizador': 'img',
                'encontrado': True,
                'quantidade_total': len(images),
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
            print(f"✅ {len(images)} imagens encontradas na página")
            
            # Analisa as primeiras 3 imagens
            images_info = []
            for i, img in enumerate(images[:3]):
                img_info = {
                    'posicao': i + 1,
                    'src': img.get_attribute('src'),
                    'alt': img.get_attribute('alt'),
                    'width': img.get_attribute('width'),
                    'height': img.get_attribute('height')
                }
                images_info.append(img_info)
                print(f"   Imagem {i+1}: alt='{img.get_attribute('alt')}'")
            
            result['amostra_imagens'] = images_info
            
        except Exception as e:
            result = {
                'estrategia': 'By.TAG_NAME',
                'elemento': 'Imagens',
                'localizador': 'img',
                'encontrado': False,
                'erro': str(e),
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            print("❌ Erro ao buscar imagens por TAG_NAME")
        
        self.mapping_results.append(result)
    
    def strategy_5_by_css_selector(self):
        """Estratégia 5: Localização por CSS_SELECTOR"""
        print("\n🎯 ESTRATÉGIA 5: By.CSS_SELECTOR")
        print("-" * 40)
        
        try:
            # Usa seletor CSS complexo para encontrar botão de busca
            search_button = self.driver.find_element(By.CSS_SELECTOR, "input[type='submit'][value='Ir']")
            
            result = {
                'estrategia': 'By.CSS_SELECTOR',
                'elemento': 'Botão de Busca',
                'localizador': "input[type='submit'][value='Ir']",
                'encontrado': True,
                'tag_name': search_button.tag_name,
                'type': search_button.get_attribute('type'),
                'value': search_button.get_attribute('value'),
                'classes': search_button.get_attribute('class'),
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
            print(f"✅ Elemento encontrado: {search_button.tag_name}")
            print(f"   Type: {search_button.get_attribute('type')}")
            print(f"   Value: {search_button.get_attribute('value')}")
            print(f"   Classes: {search_button.get_attribute('class')}")
            
        except NoSuchElementException:
            # Tenta um seletor alternativo
            try:
                search_button = self.driver.find_element(By.CSS_SELECTOR, "#nav-search-submit-button")
                result = {
                    'estrategia': 'By.CSS_SELECTOR',
                    'elemento': 'Botão de Busca (alternativo)',
                    'localizador': "#nav-search-submit-button",
                    'encontrado': True,
                    'tag_name': search_button.tag_name,
                    'id': search_button.get_attribute('id'),
                    'type': search_button.get_attribute('type'),
                    'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                print(f"✅ Elemento encontrado (seletor alternativo): {search_button.tag_name}")
                print(f"   ID: {search_button.get_attribute('id')}")
            except NoSuchElementException:
                result = {
                    'estrategia': 'By.CSS_SELECTOR',
                    'elemento': 'Botão de Busca',
                    'localizador': "input[type='submit'][value='Ir']",
                    'encontrado': False,
                    'erro': 'Elemento não encontrado',
                    'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                print("❌ Elemento não encontrado por CSS_SELECTOR")
        
        self.mapping_results.append(result)
    
    def strategy_6_by_xpath(self):
        """Estratégia 6: Localização por XPATH"""
        print("\n🎯 ESTRATÉGIA 6: By.XPATH")
        print("-" * 40)
        
        try:
            # Usa XPath para encontrar links no menu de navegação
            nav_links = self.driver.find_elements(By.XPATH, "//div[@id='nav-main']//a[contains(@class, 'nav-a')]")
            
            if nav_links:
                result = {
                    'estrategia': 'By.XPATH',
                    'elemento': 'Links de Navegação',
                    'localizador': "//div[@id='nav-main']//a[contains(@class, 'nav-a')]",
                    'encontrado': True,
                    'quantidade_encontrada': len(nav_links),
                    'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                
                print(f"✅ {len(nav_links)} links de navegação encontrados")
                
                # Lista os primeiros 5 links
                links_info = []
                for i, link in enumerate(nav_links[:5]):
                    link_info = {
                        'posicao': i + 1,
                        'texto': link.text.strip(),
                        'href': link.get_attribute('href'),
                        'classes': link.get_attribute('class')
                    }
                    links_info.append(link_info)
                    if link.text.strip():
                        print(f"   Link {i+1}: '{link.text.strip()}'")
                
                result['amostra_links'] = links_info
            else:
                raise NoSuchElementException()
                
        except NoSuchElementException:
            result = {
                'estrategia': 'By.XPATH',
                'elemento': 'Links de Navegação',
                'localizador': "//div[@id='nav-main']//a[contains(@class, 'nav-a')]",
                'encontrado': False,
                'erro': 'Elemento não encontrado',
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            print("❌ Elementos não encontrados por XPATH")
        
        self.mapping_results.append(result)
    
    def strategy_7_by_data_attributes(self):
        """Estratégia 7: Localização por Atributos Data-* (CSS Selector)"""
        print("\n🎯 ESTRATÉGIA 7: By DATA ATTRIBUTES")
        print("-" * 40)
        
        # Procura por elementos com atributos data-* mais comuns na Amazon
        data_selectors = [
            "[data-nav-role]",
            "[data-cy]",
            "[aria-label]",
            "[role]",
            "[tabindex]"
        ]
        
        found_elements = []
        for selector in data_selectors:
            try:
                elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
                
                if elements:
                    first_element = elements[0]
                    element_info = {
                        'seletor': selector,
                        'encontrado': True,
                        'quantidade': len(elements),
                        'primeiro_elemento': {
                            'tag_name': first_element.tag_name,
                            'atributos_data': {attr: first_element.get_attribute(attr) 
                                             for attr in first_element.get_property('attributes') 
                                             if isinstance(first_element.get_property('attributes'), dict) and attr.startswith('data-')},
                            'texto': first_element.text[:50] if first_element.text else 'Sem texto'
                        }
                    }
                    found_elements.append(element_info)
                    print(f"✅ {len(elements)} elemento(s) encontrado(s) com {selector}")
                    print(f"   Tag: {first_element.tag_name}")
                else:
                    raise NoSuchElementException()
                    
            except (NoSuchElementException, Exception):
                element_info = {
                    'seletor': selector,
                    'encontrado': False,
                    'quantidade': 0,
                    'erro': 'Nenhum elemento encontrado'
                }
                found_elements.append(element_info)
                print(f"❌ Nenhum elemento encontrado com {selector}")
        
        result = {
            'estrategia': 'By.DATA_ATTRIBUTES',
            'elemento': 'Elementos com Data Attributes',
            'encontrados': len([elem for elem in found_elements if elem['encontrado']]),
            'total_testados': len(data_selectors),
            'detalhes': found_elements,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        self.mapping_results.append(result)
    
    def strategy_8_by_attribute_contains(self):
        """Estratégia 8: Localização por Atributos que Contêm Texto"""
        print("\n🎯 ESTRATÉGIA 8: By ATTRIBUTE CONTAINS")
        print("-" * 40)
        
        # Testa seletores que procuram por atributos que contenham texto específico
        attribute_selectors = [
            ("href", "amazon", "[href*='amazon']"),
            ("class", "nav", "[class*='nav']"),
            ("id", "search", "[id*='search']"),
            ("placeholder", "pesquis", "[placeholder*='pesquis' i]"),
            ("alt", "amazon", "[alt*='amazon' i]")
        ]
        
        found_by_attributes = []
        for attr_name, search_text, selector in attribute_selectors:
            try:
                elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
                
                if elements:
                    first_element = elements[0]
                    attr_info = {
                        'atributo': attr_name,
                        'texto_procurado': search_text,
                        'seletor': selector,
                        'encontrado': True,
                        'quantidade': len(elements),
                        'primeiro_elemento': {
                            'tag_name': first_element.tag_name,
                            'valor_atributo': first_element.get_attribute(attr_name),
                            'texto': first_element.text[:30] if first_element.text else 'Sem texto'
                        }
                    }
                    found_by_attributes.append(attr_info)
                    print(f"✅ {len(elements)} elemento(s) com {attr_name} contendo '{search_text}'")
                    print(f"   Valor: {first_element.get_attribute(attr_name)}")
                else:
                    raise NoSuchElementException()
                    
            except NoSuchElementException:
                attr_info = {
                    'atributo': attr_name,
                    'texto_procurado': search_text,
                    'seletor': selector,
                    'encontrado': False,
                    'quantidade': 0,
                    'erro': 'Nenhum elemento encontrado'
                }
                found_by_attributes.append(attr_info)
                print(f"❌ Nenhum elemento com {attr_name} contendo '{search_text}'")
        
        result = {
            'estrategia': 'By.ATTRIBUTE_CONTAINS',
            'elemento': 'Elementos por Atributos que Contêm Texto',
            'encontrados': len([attr for attr in found_by_attributes if attr['encontrado']]),
            'total_testados': len(attribute_selectors),
            'detalhes': found_by_attributes,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        self.mapping_results.append(result)
    
    def strategy_9_by_pseudo_selectors(self):
        """Estratégia 9: Localização por Pseudo-Seletores CSS"""
        print("\n🎯 ESTRATÉGIA 9: By PSEUDO SELECTORS")
        print("-" * 40)
        
        pseudo_selectors = [
            ("Primeiro link da página", "a:first-of-type"),
            ("Último item de lista", "li:last-child"),
            ("Elementos pares", "div:nth-child(even)"),
            ("Links com href", "a[href]:not([href=''])"),
            ("Inputs habilitados", "input:not([disabled])")
        ]
        
        pseudo_results = []
        for description, selector in pseudo_selectors:
            try:
                elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
                
                if elements:
                    first_element = elements[0]
                    pseudo_info = {
                        'descricao': description,
                        'seletor': selector,
                        'encontrado': True,
                        'quantidade': len(elements),
                        'primeiro_elemento': {
                            'tag_name': first_element.tag_name,
                            'texto': first_element.text[:40] if first_element.text else 'Sem texto',
                            'classes': first_element.get_attribute('class')
                        }
                    }
                    pseudo_results.append(pseudo_info)
                    print(f"✅ {len(elements)} elemento(s) - {description}")
                    print(f"   Tag: {first_element.tag_name}, Texto: '{first_element.text[:30]}'")
                else:
                    raise NoSuchElementException()
                    
            except NoSuchElementException:
                pseudo_info = {
                    'descricao': description,
                    'seletor': selector,
                    'encontrado': False,
                    'quantidade': 0,
                    'erro': 'Nenhum elemento encontrado'
                }
                pseudo_results.append(pseudo_info)
                print(f"❌ {description} não encontrado")
        
        result = {
            'estrategia': 'By.PSEUDO_SELECTORS',
            'elemento': 'Elementos por Pseudo-Seletores',
            'encontrados': len([p for p in pseudo_results if p['encontrado']]),
            'total_testados': len(pseudo_selectors),
            'detalhes': pseudo_results,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        self.mapping_results.append(result)
    
    def strategy_10_by_multiple_attributes(self):
        """Estratégia 10: Localização por Múltiplos Atributos Combinados"""
        print("\n🎯 ESTRATÉGIA 10: By MULTIPLE ATTRIBUTES")
        print("-" * 40)
        
        multi_selectors = [
            ("Botão de busca", "input[type='submit'][class*='nav']"),
            ("Links de navegação", "a[class*='nav'][href]"),
            ("Imagens com alt", "img[alt][src]"),
            ("Inputs de texto", "input[type='text'][name]"),
            ("Elementos visíveis", "div[style*='display'][class]")
        ]
        
        multi_results = []
        for description, selector in multi_selectors:
            try:
                elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
                
                if elements:
                    first_element = elements[0]
                    multi_info = {
                        'descricao': description,
                        'seletor': selector,
                        'encontrado': True,
                        'quantidade': len(elements),
                        'primeiro_elemento': {
                            'tag_name': first_element.tag_name,
                            'atributos': {
                                'id': first_element.get_attribute('id'),
                                'class': first_element.get_attribute('class'),
                                'name': first_element.get_attribute('name')
                            }
                        }
                    }
                    multi_results.append(multi_info)
                    print(f"✅ {len(elements)} elemento(s) - {description}")
                    print(f"   ID: {first_element.get_attribute('id')}")
                else:
                    raise NoSuchElementException()
                    
            except NoSuchElementException:
                multi_info = {
                    'descricao': description,
                    'seletor': selector,
                    'encontrado': False,
                    'quantidade': 0,
                    'erro': 'Nenhum elemento encontrado'
                }
                multi_results.append(multi_info)
                print(f"❌ {description} não encontrado")
        
        result = {
            'estrategia': 'By.MULTIPLE_ATTRIBUTES',
            'elemento': 'Elementos por Múltiplos Atributos',
            'encontrados': len([m for m in multi_results if m['encontrado']]),
            'total_testados': len(multi_selectors),
            'detalhes': multi_results,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        self.mapping_results.append(result)
    
    def strategy_11_by_xpath_advanced(self):
        """Estratégia 11: XPath Avançado com Condições"""
        print("\n🎯 ESTRATÉGIA 11: By XPATH ADVANCED")
        print("-" * 40)
        
        xpath_selectors = [
            ("Elementos com texto específico", "//*[contains(text(), 'Amazon') or contains(text(), 'Prime')]"),
            ("Links por posição", "//nav//a[position()<=3]"),
            ("Elementos com classe específica", "//div[contains(@class, 'nav') and @id]"),
            ("Elementos irmãos", "//input/following-sibling::*"),
            ("Elementos pais de imagens", "//img/parent::*")
        ]
        
        xpath_results = []
        for description, xpath in xpath_selectors:
            try:
                elements = self.driver.find_elements(By.XPATH, xpath)
                
                if elements:
                    first_element = elements[0]
                    xpath_info = {
                        'descricao': description,
                        'xpath': xpath,
                        'encontrado': True,
                        'quantidade': len(elements),
                        'primeiro_elemento': {
                            'tag_name': first_element.tag_name,
                            'texto': first_element.text[:40] if first_element.text else 'Sem texto',
                            'posicao': f"x:{first_element.location['x']}, y:{first_element.location['y']}"
                        }
                    }
                    xpath_results.append(xpath_info)
                    print(f"✅ {len(elements)} elemento(s) - {description}")
                    print(f"   Tag: {first_element.tag_name}")
                else:
                    raise NoSuchElementException()
                    
            except NoSuchElementException:
                xpath_info = {
                    'descricao': description,
                    'xpath': xpath,
                    'encontrado': False,
                    'quantidade': 0,
                    'erro': 'Nenhum elemento encontrado'
                }
                xpath_results.append(xpath_info)
                print(f"❌ {description} não encontrado")
        
        result = {
            'estrategia': 'By.XPATH_ADVANCED',
            'elemento': 'Elementos por XPath Avançado',
            'encontrados': len([x for x in xpath_results if x['encontrado']]),
            'total_testados': len(xpath_selectors),
            'detalhes': xpath_results,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        self.mapping_results.append(result)
    
    def strategy_12_by_text_content(self):
        """Estratégia 12: Localização por Conteúdo de Texto"""
        print("\n🎯 ESTRATÉGIA 12: By TEXT CONTENT")
        print("-" * 40)
        
        text_patterns = [
            ("Elementos com Login/Conta", "//*[contains(text(), 'Login') or contains(text(), 'Conta') or contains(text(), 'Entrar') or contains(text(), 'Olá')]"),
            ("Texto de Preço", "//*[contains(text(), 'R$') or contains(text(), 'reais') or contains(text(), '%')]"),
            ("Elementos de navegação", "//*[contains(text(), 'Livros') or contains(text(), 'Prime') or contains(text(), 'Casa')]"),
            ("Títulos de Seção", "//*[self::h1 or self::h2 or self::h3 or self::span][normalize-space(text())]"),
            ("Texto de Ofertas", "//*[contains(text(), 'oferta') or contains(text(), 'desconto') or contains(text(), 'off')]")
        ]
        
        text_results = []
        for description, xpath in text_patterns:
            try:
                elements = self.driver.find_elements(By.XPATH, xpath)
                
                if elements:
                    # Filtra elementos que realmente têm texto visível
                    visible_elements = [elem for elem in elements if elem.text.strip()]
                    
                    if visible_elements:
                        first_element = visible_elements[0]
                        text_info = {
                            'descricao': description,
                            'xpath': xpath,
                            'encontrado': True,
                            'quantidade': len(visible_elements),
                            'primeiro_elemento': {
                                'tag_name': first_element.tag_name,
                                'texto_completo': first_element.text,
                                'texto_resumido': first_element.text[:50] + '...' if len(first_element.text) > 50 else first_element.text
                            }
                        }
                        text_results.append(text_info)
                        print(f"✅ {len(visible_elements)} elemento(s) - {description}")
                        print(f"   Texto: '{first_element.text[:40]}'")
                    else:
                        raise NoSuchElementException()
                else:
                    raise NoSuchElementException()
                    
            except NoSuchElementException:
                text_info = {
                    'descricao': description,
                    'xpath': xpath,
                    'encontrado': False,
                    'quantidade': 0,
                    'erro': 'Nenhum elemento com texto encontrado'
                }
                text_results.append(text_info)
                print(f"❌ {description} não encontrado")
        
        result = {
            'estrategia': 'By.TEXT_CONTENT',
            'elemento': 'Elementos por Conteúdo de Texto',
            'encontrados': len([t for t in text_results if t['encontrado']]),
            'total_testados': len(text_patterns),
            'detalhes': text_results,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        self.mapping_results.append(result)
    
    def strategy_13_by_position_context(self):
        """Estratégia 13: Localização por Posição e Contexto"""
        print("\n🎯 ESTRATÉGIA 13: By POSITION CONTEXT")
        print("-" * 40)
        
        position_selectors = [
            ("Primeiro item do header", "header *:first-child, [role='banner'] *:first-child"),
            ("Último item do footer", "footer *:last-child, [role='contentinfo'] *:last-child"),
            ("Elementos centrais", "div:nth-child(even)"),
            ("Primeiros links de cada nav", "nav a:first-of-type"),
            ("Elementos após inputs", "input + *, input ~ *")
        ]
        
        position_results = []
        for description, selector in position_selectors:
            try:
                elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
                
                if elements:
                    first_element = elements[0]
                    position_info = {
                        'descricao': description,
                        'seletor': selector,
                        'encontrado': True,
                        'quantidade': len(elements),
                        'primeiro_elemento': {
                            'tag_name': first_element.tag_name,
                            'posicao_na_tela': first_element.location,
                            'tamanho': first_element.size,
                            'visivel': first_element.is_displayed()
                        }
                    }
                    position_results.append(position_info)
                    print(f"✅ {len(elements)} elemento(s) - {description}")
                    print(f"   Posição: {first_element.location}")
                else:
                    raise NoSuchElementException()
                    
            except NoSuchElementException:
                position_info = {
                    'descricao': description,
                    'seletor': selector,
                    'encontrado': False,
                    'quantidade': 0,
                    'erro': 'Nenhum elemento encontrado'
                }
                position_results.append(position_info)
                print(f"❌ {description} não encontrado")
        
        result = {
            'estrategia': 'By.POSITION_CONTEXT',
            'elemento': 'Elementos por Posição e Contexto',
            'encontrados': len([p for p in position_results if p['encontrado']]),
            'total_testados': len(position_selectors),
            'detalhes': position_results,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        self.mapping_results.append(result)
    
    def run_all_strategies(self):
        """Executa todas as estratégias de mapeamento"""
        if not self.load_amazon_homepage():
            return False
        
        print("\n🔍 INICIANDO DEMONSTRAÇÃO DE TODAS AS ESTRATÉGIAS")
        print("=" * 60)
        
        # Executa cada estratégia
        strategies = [
            self.strategy_1_by_id,
            self.strategy_2_by_name,
            self.strategy_3_by_class_name,
            self.strategy_4_by_tag_name,
            self.strategy_5_by_css_selector,
            self.strategy_6_by_xpath,
            self.strategy_7_by_data_attributes,
            self.strategy_8_by_attribute_contains,
            self.strategy_9_by_pseudo_selectors,
            self.strategy_10_by_multiple_attributes,
            self.strategy_11_by_xpath_advanced,
            self.strategy_12_by_text_content,
            self.strategy_13_by_position_context
        ]
        
        for strategy in strategies:
            try:
                strategy()
                time.sleep(2)  # Pausa entre estratégias
            except Exception as e:
                print(f"❌ Erro na estratégia: {str(e)}")
        
        return True
    
    def generate_report(self):
        """Gera relatório final da demonstração"""
        print("\n📊 RELATÓRIO FINAL DA DEMONSTRAÇÃO")
        print("=" * 60)
        
        # Conta estratégias bem-sucedidas considerando diferentes tipos de resultado
        successful_strategies = 0
        for result in self.mapping_results:
            if (result.get('encontrado', False) or 
                result.get('encontrados', 0) > 0 or
                any(item.get('encontrado', False) for item in result.get('detalhes', []))):
                successful_strategies += 1
        
        total_strategies = len(self.mapping_results)
        
        print(f"✅ Estratégias bem-sucedidas: {successful_strategies}/{total_strategies}")
        print(f"📈 Taxa de sucesso: {(successful_strategies/total_strategies)*100:.1f}%")
        
        print("\n📋 Resumo por Estratégia:")
        for i, result in enumerate(self.mapping_results, 1):
            # Determina se a estratégia foi bem-sucedida
            is_successful = (result.get('encontrado', False) or 
                           result.get('encontrados', 0) > 0 or
                           any(item.get('encontrado', False) for item in result.get('detalhes', [])))
            
            status = "✅" if is_successful else "❌"
            strategy_name = result.get('estrategia', 'Desconhecida')
            element_name = result.get('elemento', 'Elemento')
            
            # Adiciona contagem se disponível
            count_info = ""
            if result.get('encontrados', 0) > 0:
                count_info = f" ({result['encontrados']} encontrados)"
            elif result.get('quantidade_encontrada', 0) > 0:
                count_info = f" ({result['quantidade_encontrada']} encontrados)"
            
            print(f"  {i}. {status} {strategy_name}: {element_name}{count_info}")
        
        return True
    
    def save_results_to_json(self):
        """Salva os resultados em arquivo JSON"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"ecommerce_mapping_results_{timestamp}.json"
        
        report_data = {
            'metadata': {
                'site_testado': 'Amazon Brasil',
                'url': 'https://www.amazon.com.br',
                'data_execucao': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'total_estrategias': len(self.mapping_results),
                'estrategias_sucessos': len([r for r in self.mapping_results if r.get('encontrado', False)])
            },
            'resultados': self.mapping_results
        }
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(report_data, f, indent=2, ensure_ascii=False)
            
            print(f"\n💾 Relatório salvo em: {filename}")
            return True
            
        except Exception as e:
            print(f"❌ Erro ao salvar relatório: {str(e)}")
            return False
    
    def close(self):
        """Fecha o navegador"""
        print("\n🔒 Fechando navegador...")
        self.driver.quit()
        print("👋 Demonstração concluída!")

def main():
    """Função principal da demonstração"""
    print("🎯 ATIVIDADE SOLO - MAPEAMENTO DE ELEMENTOS HTML")
    print("Site: Amazon Brasil (E-commerce)")
    print("Estratégias: 13 diferentes métodos de localização")
    print("=" * 60)
    
    # Inicializa a classe de demonstração
    demo = EcommerceMappingDemo(headless=False)
    
    try:
        # Executa todas as estratégias
        if demo.run_all_strategies():
            # Gera relatório final
            demo.generate_report()
            
            # Salva resultados em JSON
            demo.save_results_to_json()
            
            print("\n🎉 DEMONSTRAÇÃO CONCLUÍDA COM SUCESSO!")
            print("Todos os métodos de mapeamento foram testados.")
            print("Verifique o arquivo JSON gerado para detalhes completos.")
        else:
            print("❌ Falha ao executar a demonstração")
            
    except KeyboardInterrupt:
        print("\n⚠️ Demonstração interrompida pelo usuário")
    except Exception as e:
        print(f"❌ Erro inesperado: {str(e)}")
    finally:
        demo.close()

if __name__ == "__main__":
    main()