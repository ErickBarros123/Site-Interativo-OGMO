from datetime import datetime
import json
import requests
from bs4 import BeautifulSoup
import time
import os
import json

JSON_DATABASE = "novo_data.json"

def carregar_banco_dados():
    if not os.path.exists(JSON_DATABASE):
        # Cria uma lista vazia automaticamente se o arquivo não existir
        with open(JSON_DATABASE, "w", encoding="utf-8") as f:
            json.dump([], f)
    with open(JSON_DATABASE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def salvar_banco_dados(dados):
    with open(JSON_DATABASE, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)

def puxar_escala_todos_turnos():
    # Pega a data de hoje de forma dinâmica
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

                    # Cruza com a base de dados de todos os 56 trabalhadores
                    if registro_site in mapa_matriculas:
                        idx = mapa_matriculas[registro_site]
                        
                        # Atualiza a contagem da função específica se existir na chave, senão soma no total
                        if funcao_site in banco[idx]:
                            banco[idx][funcao_site] += 1
                        
                        banco[idx]["Total Geral"] += 1
                        total_geral_atualizados += 1
                        escalados_no_turno += 1
                        
                        escala_geral_dia.append(f"Turno {turno} | {nome_site} ({funcao_site}) - Matrícula: {registro_site}")

            print(f"   Sucesso! {escalados_no_turno} trabalhadores do nosso banco pontuados no Turno {turno}.")
        except Exception as e:
            print(f"   Erro ao processar o Turno {turno}: {e}")

    # Salva todas as pontuações acumuladas no JSON em tempo real
    salvar_banco_dados(banco)
    print(f"\nVarredura concluída. Total de apontamentos somados hoje: {total_geral_atualizados}")
    
    if len(escala_geral_dia) == 0:
        print(f"[AVISO] Nenhum trabalhador da base foi encontrado nas escalas da data de hoje ({data_hoje}).")

if __name__ == "__main__":
    # Configuração de Tempo Real: Roda sozinho periodicamente (ex: a cada 1 hora = 3600 segundos)
    INTERVALO_SEGUNDOS = 3600 
    
    print("=== Robô OGMO de Monitoramento Geral Iniciado ===")
    while True:
        puxar_escala_todos_turnos()
        print(f"\nAguardando próxima checagem automática em {INTERVALO_SEGUNDOS // 60} minutos... (Pressione Ctrl+C para encerrar)\n")
        time.sleep(INTERVALO_SEGUNDOS)