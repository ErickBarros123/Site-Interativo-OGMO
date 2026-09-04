import os
import json
from datetime import datetime
import requests
from bs4::BeautifulSoup import BeautifulSoup # type: ignore
import time
from bs4 import BeautifulSoup

# Base de dados embutida diretamente no código Python
BANCO_DADOS_INICIAL = [
  {
    "Matrícula": 900001,
    "Nome": "ADEÍLSON PEREIRA DA SILVA FILHO",
    "GUINCHO": 0,
    "BLOCO": 0,
    "AJUDANTE": 0,
    "Total Geral": 0
  },
  {
    "Matrícula": 900002,
    "Nome": "ALEX DA SILVA OLIVEIRA",
    "GUINCHO": 0,
    "BLOCO": 0,
    "AJUDANTE": 0,
    "Total Geral": 0
  },
  {
    "Matrícula": 900003,
    "Nome": "ALEXSANDRO MARCOS SALES",
    "GUINCHO": 0,
    "BLOCO": 0,
    "AJUDANTE": 0,
    "Total Geral": 0
  },
  {
    "Matrícula": 900004,
    "Nome": "ÁLVARO AUGUSTO VIANA BRAGA TORRES",
    "GUINCHO": 0,
    "BLOCO": 0,
    "AJUDANTE": 0,
    "Total Geral": 0
  },
  {
    "Matrícula": 900005,
    "Nome": "ANDERSEN FERREIRA DIAS DA SILVA",
    "GUINCHO": 0,
    "BLOCO": 0,
    "AJUDANTE": 0,
    "Total Geral": 0
  },
  {
    "Matrícula": 900006,
    "Nome": "ANDERSON LIMA DA SILVA",
    "GUINCHO": 0,
    "BLOCO": 0,
    "AJUDANTE": 0,
    "Total Geral": 0
  },
  {
    "Matrícula": 900007,
    "Nome": "ANDRÉ LUIZ PINHEIRO ARAUJO DA SILVA",
    "GUINCHO": 0,
    "BLOCO": 0,
    "AJUDANTE": 0,
    "Total Geral": 0
  },
  {
    "Matrícula": 900008,
    "Nome": "ANDRÉ LUIZ VITURINO CABRAL",
    "GUINCHO": 0,
    "BLOCO": 0,
    "AJUDANTE": 0,
    "Total Geral": 0
  },
  {
    "Matrícula": 900009,
    "Nome": "ANTONIO VINICIUS DE FREITAS MATIAS",
    "GUINCHO": 0,
    "BLOCO": 0,
    "AJUDANTE": 0,
    "Total Geral": 0
  },
  {
    "Matrícula": 900010,
    "Nome": "BRUNO HENRIQUE SEVERO DA SILVA",
    "GUINCHO": 0,
    "BLOCO": 0,
    "AJUDANTE": 0,
    "Total Geral": 0
  },
  {
    "Matrícula": 900011,
    "Nome": "CAINÃ FERREIRA DOS SANTOS",
    "GUINCHO": 0,
    "BLOCO": 0,
    "AJUDANTE": 0,
    "Total Geral": 0
  },
  {
    "Matrícula": 900012,
    "Nome": "CARLOS ANTONIO DA SILVA CARNEIRO",
    "GUINCHO": 0,
    "BLOCO": 0,
    "AJUDANTE": 0,
    "Total Geral": 0
  },
  {
    "Matrícula": 900013,
    "Nome": "CHRISTYAN LEANDRO MEIRELES DE SOUZA",
    "GUINCHO": 0,
    "BLOCO": 0,
    "AJUDANTE": 0,
    "Total Geral": 0
  },
  {
    "Matrícula": 900014,
    "Nome": "CLÁUDIO HENRIQUE RIBEIRO",
    "GUINCHO": 0,
    "BLOCO": 0,
    "AJUDANTE": 0,
    "Total Geral": 0
  },
  {
    "Matrícula": 900015,
    "Nome": "DARIO PEREIRA DOS SANTOS",
    "GUINCHO": 0,
    "BLOCO": 0,
    "AJUDANTE": 0,
    "Total Geral": 0
  },
  {
    "Matrícula": 900016,
    "Nome": "DAVID DAYVISON DOS SANTOS LINS",
    "GUINCHO": 0,
    "BLOCO": 0,
    "AJUDANTE": 0,
    "Total Geral": 0
  },
  {
    "Matrícula": 900017,
    "Nome": "DOUGLAS ANDERSON MARTINS CRUZ",
    "GUINCHO": 0,
    "BLOCO": 0,
    "AJUDANTE": 0,
    "Total Geral": 0
  },
  {
    "Matrícula": 900018,
    "Nome": "EDUARDO CABRAL",
    "GUINCHO": 0,
    "BLOCO": 0,
    "AJUDANTE": 0,
    "Total Geral": 0
  },
  {
    "Matrícula": 900019,
    "Nome": "ELIAS ALFREDO DOS SANTOS",
    "GUINCHO": 0,
    "BLOCO": 0,
    "AJUDANTE": 0,
    "Total Geral": 0
  },
  {
    "Matrícula": 900020,
    "Nome": "EMERSON REIS RAMOS",
    "GUINCHO": 0,
    "BLOCO": 0,
    "AJUDANTE": 0,
    "Total Geral": 0
  },
  {
    "Matrícula": 900021,
    "Nome": "ENES ALBERTINO DA SILVA JUNIOR",
    "GUINCHO": 0,
    "BLOCO": 0,
    "AJUDANTE": 0,
    "Total Geral": 0
  },
  {
    "Matrícula": 900022,
    "Nome": "ERICK BARROS DA SILVA",
    "GUINCHO": 0,
    "BLOCO": 0,
    "AJUDANTE": 0,
    "Total Geral": 0
  },
  {
    "Matrícula": 900023,
    "Nome": "ERIGLEYDSON HENRIQUE DA SILVA NASCIMENTO",
    "GUINCHO": 0,
    "BLOCO": 0,
    "AJUDANTE": 0,
    "Total Geral": 0
  },
  {
    "Matrícula": 900024,
    "Nome": "ÉRLITON FERNANDES DE ALBUQUERQUE LUCAS",
    "GUINCHO": 0,
    "BLOCO": 0,
    "AJUDANTE": 0,
    "Total Geral": 0
  },
  {
    "Matrícula": 900025,
    "Nome": "EVERALDO DA SILVA NEPOMUCENO",
    "GUINCHO": 0,
    "BLOCO": 0,
    "AJUDANTE": 0,
    "Total Geral": 0
  },
  {
    "Matrícula": 900026,
    "Nome": "FELIPE CHESSINE TAN",
    "GUINCHO": 0,
    "BLOCO": 0,
    "AJUDANTE": 0,
    "Total Geral": 0
  },
  {
    "Matrícula": 900027,
    "Nome": "FELIPE IRINEU SANTIAGO",
    "GUINCHO": 0,
    "BLOCO": 0,
    "AJUDANTE": 0,
    "Total Geral": 0
  },
  {
    "Matrícula": 900028,
    "Nome": "FELIPE PEREIRA GUIMARÃES",
    "GUINCHO": 0,
    "BLOCO": 0,
    "AJUDANTE": 0,
    "Total Geral": 0
  },
  {
    "Matrícula": 900029,
    "Nome": "HENRIQUE PEREIRA PARANHOS GOUVEIA DE MELO",
    "GUINCHO": 0,
    "BLOCO": 0,
    "AJUDANTE": 0,
    "Total Geral": 0
  },
  {
    "Matrícula": 900030,
    "Nome": "HENRIQUE VIANA BRANDÃO",
    "GUINCHO": 0,
    "BLOCO": 0,
    "AJUDANTE": 0,
    "Total Geral": 0
  },
  {
    "Matrícula": 900031,
    "Nome": "IZABELLY DOS SANTOS CORREIA",
    "GUINCHO": 0,
    "BLOCO": 0,
    "AJUDANTE": 0,
    "Total Geral": 0
  },
  {
    "Matrícula": 900032,
    "Nome": "IZAQUE DOS SANTOS LIMA",
    "GUINCHO": 0,
    "BLOCO": 0,
    "AJUDANTE": 0,
    "Total Geral": 0
  },
  {
    "Matrícula": 900033,
    "Nome": "JADSON DA SILVA SANTANA",
    "GUINCHO": 0,
    "BLOCO": 0,
    "AJUDANTE": 0,
    "Total Geral": 0
  },
  {
    "Matrícula": 900034,
    "Nome": "JOAO MANOEL DA SILVA JUNIOR",
    "GUINCHO": 0,
    "BLOCO": 0,
    "AJUDANTE": 0,
    "Total Geral": 0
  },
  {
    "Matrícula": 900035,
    "Nome": "JOSEVANIO FERNANDES JUNIOR",
    "GUINCHO": 0,
    "BLOCO": 0,
    "AJUDANTE": 0,
    "Total Geral": 0
  },
  {
    "Matrícula": 900036,
    "Nome": "JOSIAS MARTINS SANTOS",
    "GUINCHO": 0,
    "BLOCO": 0,
    "AJUDANTE": 0,
    "Total Geral": 0
  },
  {
    "Matrícula": 900037,
    "Nome": "JULIO ALEXANDRE DUARTE DA SILVA",
    "GUINCHO": 0,
    "BLOCO": 0,
    "AJUDANTE": 0,
    "Total Geral": 0
  },
  {
    "Matrícula": 900038,
    "Nome": "LUCAS CAVALCANTE DE FREITAS",
    "GUINCHO": 0,
    "BLOCO": 0,
    "AJUDANTE": 0,
    "Total Geral": 0
  },
  {
    "Matrícula": 900039,
    "Nome": "LUCAS MADRUGA DOS SANTOS",
    "GUINCHO": 0,
    "BLOCO": 0,
    "AJUDANTE": 0,
    "Total Geral": 0
  },
  {
    "Matrícula": 900040,
    "Nome": "LUIZ PEDRO GONÇALVES DA SILVA",
    "GUINCHO": 0,
    "BLOCO": 0,
    "AJUDANTE": 0,
    "Total Geral": 0
  },
  {
    "Matrícula": 900041,
    "Nome": "MARCIA KELLY DA SILVA SOUZA",
    "GUINCHO": 0,
    "BLOCO": 0,
    "AJUDANTE": 0,
    "Total Geral": 0
  },
  {
    "Matrícula": 900042,
    "Nome": "MARCO TULLIO FERNANDES GUIMARAES",
    "GUINCHO": 0,
    "BLOCO": 0,
    "AJUDANTE": 0,
    "Total Geral": 0
  },
  {
    "Matrícula": 900043,
    "Nome": "PABLO RENILDO DA SILVA LINO",
    "GUINCHO": 0,
    "BLOCO": 0,
    "AJUDANTE": 0,
    "Total Geral": 0
  },
  {
    "Matrícula": 900044,
    "Nome": "PAULO RAFAEL FERREIRA DE MORAIS",
    "GUINCHO": 0,
    "BLOCO": 0,
    "AJUDANTE": 0,
    "Total Geral": 0
  },
  {
    "Matrícula": 900045,
    "Nome": "PAULO ROBERTO DE ASSIS PEREIRA SILVA",
    "GUINCHO": 0,
    "BLOCO": 0,
    "AJUDANTE": 0,
    "Total Geral": 0
  },
  {
    "Matrícula": 900046,
    "Nome": "PAULO YGOR VILAS BÔAS DE VASCONCELOS",
    "GUINCHO": 0,
    "BLOCO": 0,
    "AJUDANTE": 0,
    "Total Geral": 0
  },
  {
    "Matrícula": 900047,
    "Nome": "RAFAEL CARLOS DE ALMEIDA VICENTE",
    "GUINCHO": 0,
    "BLOCO": 0,
    "AJUDANTE": 0,
    "Total Geral": 0
  },
  {
    "Matrícula": 900048,
    "Nome": "RAFAEL COSTA NASCIMENTO",
    "GUINCHO": 0,
    "BLOCO": 0,
    "AJUDANTE": 0,
    "Total Geral": 0
  },
  {
    "Matrícula": 900049,
    "Nome": "RAFAEL HENRIQUE SILVEIRA DE LIMA",
    "GUINCHO": 0,
    "BLOCO": 0,
    "AJUDANTE": 0,
    "Total Geral": 0
  },
  {
    "Matrícula": 900050,
    "Nome": "RANIERE TIBURCIO DA SILVA",
    "GUINCHO": 0,
    "BLOCO": 0,
    "AJUDANTE": 0,
    "Total Geral": 0
  },
  {
    "Matrícula": 900051,
    "Nome": "RODOLFO JOSÉ DOS SANTOS CAMELO",
    "GUINCHO": 0,
    "BLOCO": 0,
    "AJUDANTE": 0,
    "Total Geral": 0
  },
  {
    "Matrícula": 900052,
    "Nome": "SAVIO HENRIQUE BATISTA MAIA",
    "GUINCHO": 0,
    "BLOCO": 0,
    "AJUDANTE": 0,
    "Total Geral": 0
  },
  {
    "Matrícula": 900053,
    "Nome": "SÉRGIO HIGINO MORAES DE OLIVEIRA",
    "GUINCHO": 0,
    "BLOCO": 0,
    "AJUDANTE": 0,
    "Total Geral": 0
  },
  {
    "Matrícula": 900054,
    "Nome": "THALES GOUVEIA GAMA",
    "GUINCHO": 0,
    "BLOCO": 0,
    "AJUDANTE": 0,
    "Total Geral": 0
  },
  {
    "Matrícula": 900055,
    "Nome": "VINICIUS DA COSTA SILVA",
    "GUINCHO": 0,
    "BLOCO": 0,
    "AJUDANTE": 0,
    "Total Geral": 0
  },
  {
    "Matrícula": 900056,
    "Nome": "VINICIUS LEANDRO CAVALCANTI VINHAS",
    "GUINCHO": 0,
    "BLOCO": 0,
    "AJUDANTE": 0,
    "Total Geral": 0
  }
]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_DATABASE = os.path.join(BASE_DIR, "novo_data.json") 

def carregar_banco_dados():
    # Se o arquivo JSON externo não existir, ele cria automaticamente usando a lista embutida acima
    if not os.path.exists(JSON_DATABASE):
        salvar_banco_dados(BANCO_DADOS_INICIAL)
        return BANCO_DADOS_INICIAL
    
    with open(JSON_DATABASE, "r", encoding="utf-8") as f:
        try:
            dados = json.load(f)
            if not dados:  # Se estiver vazio por algum motivo, usa o embutido
                return BANCO_DADOS_INICIAL
            return dados
        except json.JSONDecodeError:
            return BANCO_DADOS_INICIAL

def salvar_banco_dados(dados):
    with open(JSON_DATABASE, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)

def puxar_escala_todos_turnos():
    data_hoje = datetime.now().strftime("%Y-%m-%d")
    turnos = [1, 2, 3, 4, 5, 6, 7]
    
    banco = carregar_banco_dados()
    mapa_matriculas = {str(trabalhador["Matrícula"]): idx for idx, trabalhador in enumerate(banco)}
    
    total_geral_atualizados = 0
    escala_geral_dia = []

    print(f"\n[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Iniciando varredura automatizada para o dia {data_hoje}...")

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    for turno in turnos:
        url = f"http://tpa.ogmosuape.com.br/web/listagem_turno?d={data_hoje}&t={turno}"
        print(f"-> Verificando Turno {turno}...")
        
        try:
            resposta = requests.get(url, headers=headers, timeout=15)
            resposta.raise_for_status()

            soup = BeautifulSoup(resposta.text, "html.parser")
            linhas = soup.find_all("tr")
            escalados_no_turno = 0

            for linha in linhas:
                colunas = linha.find_all("td")
                if len(colunas) >= 3:
                    registro_site = colunas[0].text.strip()
                    funcao_site = colunas[1].text.strip().upper()
                    nome_site = colunas[2].text.strip()

                    if registro_site in mapa_matriculas:
                        idx = mapa_matriculas[registro_site]
                        
                        if funcao_site in banco[idx]:
                            banco[idx][funcao_site] += 1
                        
                        banco[idx]["Total Geral"] += 1
                        total_geral_atualizados += 1
                        escalados_no_turno += 1
                        
                        escala_geral_dia.append(f"Turno {turno} | {nome_site} ({funcao_site}) - Matrícula: {registro_site}")

            print(f"   Sucesso! {escalados_no_turno} trabalhadores do nosso banco pontuados no Turno {turno}.")
        except Exception as e:
            print(f"   Erro ao processar o Turno {turno}: {e}")

    salvar_banco_dados(banco)
    print(f"\nVarredura concluída. Total de apontamentos somados hoje: {total_geral_atualizados}")
    
    if len(escala_geral_dia) == 0:
        print(f"[AVISO] Nenhum trabalhador da base foi encontrado nas escalas da data de hoje ({data_hoje}).")

if __name__ == "__main__":
    INTERVALO_SEGUNDOS = 3600 
    
    print("=== Robô OGMO de Monitoramento Geral Iniciado ===")
    while True:
        puxar_escala_todos_turnos()
        print(f"\nAguardando próxima checagem automática em {INTERVALO_SEGUNDOS // 60} minutos... (Pressione Ctrl+C para encerrar)\n")
        time.sleep(INTERVALO_SEGUNDOS)