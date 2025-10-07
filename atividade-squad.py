from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import csv
import json
from datetime import datetime

class ChallengeDOM:
    def __init__(self, headless=False):
        """Inicializa o navegador com configurações otimizadas"""
        chrome_options = Options()
        if headless:
            chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        
        self.service = Service()
        self.driver = webdriver.Chrome(service=self.service, options=chrome_options)
        self.wait = WebDriverWait(self.driver, 10)
        self.data = []
        
        print("🚀 Navegador iniciado com sucesso!")
    
    def load_page(self):
        """Carrega a página e aguarda elementos estarem prontos"""
        try:
            print("🌐 Carregando página...")
            self.driver.get("https://the-internet.herokuapp.com/challenging_dom")
            
            # Aguarda a tabela carregar
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "table")))
            print("✅ Página carregada com sucesso!")
            return True
        except TimeoutException:
            print("❌ Erro: Tempo limite para carregar a página")
            return False
    
    def extract_table_data(self):
        """Extrai todos os dados da tabela de forma estruturada"""
        try:
            print("📊 Extraindo dados da tabela...")
            
            table = self.driver.find_element(By.CSS_SELECTOR, "table")
            thead = table.find_element(By.TAG_NAME, "thead")
            headers = [th.text.strip() for th in thead.find_elements(By.TAG_NAME, "th")]
            
            tbody = table.find_element(By.TAG_NAME, "tbody")
            rows = tbody.find_elements(By.TAG_NAME, "tr")
            
            print(f"📋 Encontradas {len(rows)} linhas com {len(headers)} colunas: {headers}")
            
            self.data = []
            for i, row in enumerate(rows, 1):
                cells = row.find_elements(By.TAG_NAME, "td")
                
                # Extrai dados das células (exceto a última que contém botões)
                row_data = {
                    'linha': i,
                    'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                
                # Mapeia cada célula com seu cabeçalho correspondente
                for j, cell in enumerate(cells[:-1]):  # Ignora a última célula (botões)
                    if j < len(headers) - 1:  # Ignora a coluna "Action"
                        row_data[headers[j]] = cell.text.strip()
                
                # Extrai informações dos botões
                action_cell = cells[-1]
                buttons = action_cell.find_elements(By.TAG_NAME, "a")
                row_data['botoes_disponiveis'] = [btn.text.strip() for btn in buttons]
                row_data['edit_href'] = None
                row_data['delete_href'] = None
                
                for btn in buttons:
                    href = btn.get_attribute('href')
                    if 'edit' in href:
                        row_data['edit_href'] = href
                    elif 'delete' in href:
                        row_data['delete_href'] = href
                
                self.data.append(row_data)
                print(f"  📝 Linha {i}: {list(row_data.values())[2:-3]}...")  # Mostra principais dados
            
            print(f"✅ Extração concluída! {len(self.data)} registros coletados.")
            return True
            
        except Exception as e:
            print(f"❌ Erro ao extrair dados: {str(e)}")
            return False
    
    def click_button(self, linha, tipo_botao='edit'):
        """Clica em um botão específico de uma linha"""
        try:
            print(f"🖱️  Clicando no botão '{tipo_botao}' da linha {linha}...")
            
            tbody = self.driver.find_element(By.TAG_NAME, "tbody")
            rows = tbody.find_elements(By.TAG_NAME, "tr")
            
            if linha > len(rows):
                print(f"❌ Erro: Linha {linha} não existe (máximo: {len(rows)})")
                return False
            
            row = rows[linha - 1]
            action_cell = row.find_elements(By.TAG_NAME, "td")[-1]
            buttons = action_cell.find_elements(By.TAG_NAME, "a")
            
            for btn in buttons:
                if tipo_botao.lower() in btn.get_attribute('href').lower():
                    btn.click()
                    print(f"✅ Botão '{tipo_botao}' da linha {linha} clicado!")
                    time.sleep(1)  # Aguarda possível mudança na página
                    return True
            
            print(f"❌ Botão '{tipo_botao}' não encontrado na linha {linha}")
            return False
            
        except Exception as e:
            print(f"❌ Erro ao clicar no botão: {str(e)}")
            return False
    
    def save_to_csv(self, filename=None):
        """Salva os dados extraídos em arquivo CSV"""
        if not self.data:
            print("❌ Nenhum dado para salvar")
            return False
        
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"challenge_dom_data_{timestamp}.csv"
        
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = list(self.data[0].keys())
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(self.data)
            
            print(f"💾 Dados salvos em: {filename}")
            return True
        except Exception as e:
            print(f"❌ Erro ao salvar CSV: {str(e)}")
            return False
    
    def save_to_json(self, filename=None):
        """Salva os dados extraídos em arquivo JSON"""
        if not self.data:
            print("❌ Nenhum dado para salvar")
            return False
        
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"challenge_dom_data_{timestamp}.json"
        
        try:
            with open(filename, 'w', encoding='utf-8') as jsonfile:
                json.dump(self.data, jsonfile, indent=2, ensure_ascii=False)
            
            print(f"💾 Dados salvos em: {filename}")
            return True
        except Exception as e:
            print(f"❌ Erro ao salvar JSON: {str(e)}")
            return False
    
    def interactive_mode(self):
        """Modo interativo para explorar a tabela"""
        while True:
            print("\n" + "="*50)
            print("🎮 MODO INTERATIVO - Escolha uma opção:")
            print("1. Mostrar dados da tabela")
            print("2. Clicar em botão Edit de uma linha")
            print("3. Clicar em botão Delete de uma linha")
            print("4. Salvar dados em CSV")
            print("5. Salvar dados em JSON")
            print("6. Recarregar página")
            print("0. Sair")
            print("="*50)
            
            choice = input("Digite sua escolha: ").strip()
            
            if choice == '1':
                self.show_data_summary()
            elif choice == '2':
                linha = input("Digite o número da linha (1-10): ").strip()
                try:
                    linha_num = int(linha)
                    self.click_button(linha_num, 'edit')
                except ValueError:
                    print("❌ Número inválido")
            elif choice == '3':
                linha = input("Digite o número da linha (1-10): ").strip()
                try:
                    linha_num = int(linha)
                    self.click_button(linha_num, 'delete')
                except ValueError:
                    print("❌ Número inválido")
            elif choice == '4':
                self.save_to_csv()
            elif choice == '5':
                self.save_to_json()
            elif choice == '6':
                self.load_page()
                self.extract_table_data()
            elif choice == '0':
                break
            else:
                print("❌ Opção inválida")
    
    def show_data_summary(self):
        """Mostra um resumo dos dados coletados"""
        if not self.data:
            print("❌ Nenhum dado coletado")
            return
        
        print(f"\n📊 RESUMO DOS DADOS ({len(self.data)} registros):")
        print("-" * 80)
        for item in self.data:
            print(f"Linha {item['linha']:2d}: {item.get('Lorem', 'N/A'):10s} | "
                  f"{item.get('Ipsum', 'N/A'):10s} | {item['botoes_disponiveis']}")
    
    def close(self):
        """Fecha o navegador"""
        print("🔒 Fechando navegador...")
        self.driver.quit()
        print("👋 Sessão encerrada!")

def main():
    """Função principal com demo completo"""
    print("🎯 CHALLENGE DOM - Automação Avançada")
    print("=====================================")
    
    # Inicializa a classe
    challenge = ChallengeDOM(headless=False)
    
    try:
        # Carrega a página
        if not challenge.load_page():
            return
        
        # Extrai dados da tabela
        if not challenge.extract_table_data():
            return
        
        # Demonstração: clica em alguns botões
        print("\n🎬 DEMONSTRAÇÃO: Clicando em botões...")
        challenge.click_button(1, 'edit')
        time.sleep(2)
        challenge.click_button(3, 'delete')
        time.sleep(2)
        
        # Salva dados automaticamente
        challenge.save_to_csv()
        challenge.save_to_json()
        
        # Modo interativo
        print("\n🎮 Iniciando modo interativo...")
        challenge.interactive_mode()
        
    except KeyboardInterrupt:
        print("\n⚠️  Interrompido pelo usuário")
    except Exception as e:
        print(f"❌ Erro inesperado: {str(e)}")
    finally:
        challenge.close()

if __name__ == "__main__":
    main()