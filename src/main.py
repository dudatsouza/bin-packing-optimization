# src/main.py
import os
import sys
import csv
import glob
from parser import ler_instancia
from model import resolver_bpp_kantorovich
# src/main.py
import os
import sys
import csv
import glob
from parser import ler_instancia
from model import resolver_bpp_kantorovich

def main():
    print("==================================================")
    print(" Trabalho Final - Otimização Combinatória (1D-BPP)")
    print("==================================================")
    
    instances = {
        "1_u120": "data/Instances/1_Falkenauer/Falkenauer/Falkenauer U/Falkenauer_u120_*.txt",
        "1_t60": "data/Instances/1_Falkenauer/Falkenauer/Falkenauer T/Falkenauer_t60_*.txt",
        "2_n1c1w1": "data/Instances/2_Scholl/Scholl/Scholl_1/N1C1W1*.txt",
        "2_n1c2w1": "data/Instances/2_Scholl/Scholl/Scholl_2/N1W1B1R*.txt",
        "2_hard": "data/Instances/2_Scholl/Scholl/Scholl_3/HARD*.txt",
        "3_wascher": "data/Instances/3_Wäscher/Wäscher/Waescher_TEST*.txt",
        "4_schwerin_1": "data/Instances/4_Schwerin/Schwerin/Schwerin_1/Schwerin1_BPP*.txt",
        "4_schwerin_2": "data/Instances/4_Schwerin/Schwerin/Schwerin_2/Schwerin2_BPP*.txt",
        "5_hard28": "data/Instances/5_Hard28/Hard28/Hard28_BPP*.txt",
    }

    os.makedirs("results", exist_ok=True)
    arquivo_saida = "results/resultados_bpp.csv"
    
    print(f"\n[Etapa 1] Inicializando otimização em lote utilizando as classes mapeadas.")
    print(f"[Etapa 2] Os resultados serão salvos em {arquivo_saida}...\n")
    
    with open(arquivo_saida, mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        
        writer.writerow(['Classe', 'Instancia', 'Minimo_Caixas', 'Tempo_Segundos'])
        
        for nome_classe, caminho_padrao in instances.items():
            arquivos_instancias = sorted(glob.glob(caminho_padrao))[:10]
            
            if not arquivos_instancias:
                print(f"Aviso: Nenhuma instância encontrada para a classe '{nome_classe}'. Verifique o caminho.")
                continue
                
            print(f"\n>>> Iniciando bateria da classe: {nome_classe} ({len(arquivos_instancias)} arquivos)")
            
            for caminho_arquivo in arquivos_instancias:
                nome_instancia = os.path.basename(caminho_arquivo).replace('.txt', '')
                
                print(f"-> Processando: {nome_instancia}")
                
                n, capacidade, pesos = ler_instancia(caminho_arquivo)
                
                caixas_usadas, tempo = resolver_bpp_kantorovich(n, capacidade, pesos, nome_instancia)
                
                if caixas_usadas:
                    writer.writerow([nome_classe, nome_instancia, caixas_usadas, round(tempo, 4)])
                    csv_file.flush() 
                else:
                    writer.writerow([nome_classe, nome_instancia, 'Nao Resolvido', 'Timeout'])

    print("\n==================================================")
    print(" OTIMIZAÇÃO EM LOTE CONCLUÍDA COM SUCESSO!")
    print(f" Todos os resultados foram salvos em: {arquivo_saida}")
    print("==================================================")

if __name__ == "__main__":
    main()