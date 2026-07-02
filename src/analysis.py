import csv
import os
import matplotlib.pyplot as plt

def gerar_analise():
    print("==================================================")
    print(" Gerando Análise de Resultados e Gráficos")
    print("==================================================")
    
    caminho_entrada = 'results/resultados_bpp.csv'
    caminho_medias = 'results/medias_bpp.csv'
    caminho_grafico = 'results/grafico_resultados.png'

    if not os.path.exists(caminho_entrada):
        print(f"Erro: O arquivo {caminho_entrada} não foi encontrado.")
        print("Certifique-se de que o main.py já terminou de rodar e gerou os resultados.")
        return

    dados_classe = {}

    # Passo 1: Leitura dos dados brutos
    with open(caminho_entrada, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            classe = row['Classe']
            tempo = float(row['Tempo_Segundos'])
            status = row['Minimo_Caixas']
            
            if classe not in dados_classe:
                dados_classe[classe] = {'total_tempo': 0.0, 'qtd': 0, 'resolvidos': 0, 'timeouts': 0}
            
            dados_classe[classe]['total_tempo'] += tempo
            dados_classe[classe]['qtd'] += 1
            
            # Se o status é não resolvido ou bateu no teto de ~300s, conta como timeout
            if status == 'Nao Resolvido' or tempo >= 300:
                dados_classe[classe]['timeouts'] += 1
            else:
                dados_classe[classe]['resolvidos'] += 1

    # Passo 2: Calcular médias e salvar no novo CSV
    classes = []
    tempos_medios = []
    taxas_timeout = []

    with open(caminho_medias, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        # Cabeçalho da nova tabela de médias
        writer.writerow(['Classe', 'Total_Instancias', 'Resolvidos', 'Timeouts', 'Taxa_Timeout_Perc', 'Tempo_Medio_Segundos'])
        
        for classe, dados in dados_classe.items():
            qtd = dados['qtd']
            tempo_medio = dados['total_tempo'] / qtd
            taxa_timeout = (dados['timeouts'] / qtd) * 100
            
            classes.append(classe)
            tempos_medios.append(tempo_medio)
            taxas_timeout.append(taxa_timeout)
            
            # Salva no arquivo CSV
            writer.writerow([classe, qtd, dados['resolvidos'], dados['timeouts'], round(taxa_timeout, 2), round(tempo_medio, 4)])

    print(f"[Sucesso] Arquivo de médias gerado em: {caminho_medias}")

    # Passo 3: Gerar o Gráfico
    # Cria uma figura com dois gráficos lado a lado
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Gráfico 1: Tempo Médio de Execução (Barras Azuis)
    ax1.barh(classes, tempos_medios, color='#3498db', edgecolor='black')
    ax1.set_xlabel('Tempo Médio (s)', fontsize=12)
    ax1.set_title('Tempo Médio de Execução por Classe', fontsize=14, fontweight='bold')
    ax1.set_xlim(0, 320)
    ax1.grid(axis='x', linestyle='--', alpha=0.7)

    # Gráfico 2: Taxa de Timeout (Barras Vermelhas)
    ax2.barh(classes, taxas_timeout, color='#e74c3c', edgecolor='black')
    ax2.set_xlabel('Taxa de Timeout (%)', fontsize=12)
    ax2.set_title('Porcentagem de Timeouts por Classe', fontsize=14, fontweight='bold')
    ax2.set_xlim(0, 110)
    ax2.grid(axis='x', linestyle='--', alpha=0.7)

    # Ajusta o layout para não cortar os nomes das classes e salva a imagem
    plt.tight_layout()
    plt.savefig(caminho_grafico, dpi=300) # dpi=300 garante alta qualidade para o PDF
    print(f"[Sucesso] Gráfico em alta resolução salvo em: {caminho_grafico}")

if __name__ == "__main__":
    gerar_analise()