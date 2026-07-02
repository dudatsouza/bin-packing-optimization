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
    
    # Caminho das instâncias, para u120 use o caminho abaixo, para u250 use o caminho comentado
    caminho_pasta = "data/Falkenauer_U/Falkenauer_u120_*.txt"
    # caminho_pasta = "data/Falkenauer_U/Falkenauer_u250_*.txt"
    arquivos_instancias = glob.glob(caminho_pasta)
    
    if not arquivos_instancias:
        print(f"\nErro: Nenhuma instância encontrada no padrão: {caminho_pasta}")
        print("Certifique-se de executar o script a partir da raiz do projeto.")
        sys.exit(1)
        
    os.makedirs("results", exist_ok=True)

    # Nome do arquivo de saída, para u120 use o nome abaixo, para u250 use o nome comentado
    arquivo_saida = "results/resultados_bpp_120.csv"
    # arquivo_saida = "results/resultados_bpp_250.csv"
    
    print(f"\n[Etapa 1] Encontradas {len(arquivos_instancias)} instâncias para processar.")
    print(f"[Etapa 2] Iniciando otimização em lote e salvando em {arquivo_saida}...\n")
    
    with open(arquivo_saida, mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        
        writer.writerow(['Instancia', 'Minimo_Caixas', 'Tempo_Segundos'])
        
        for caminho_arquivo in sorted(arquivos_instancias):
            nome_instancia = os.path.basename(caminho_arquivo).replace('.txt', '')
            
            print(f"\n-> Processando: {nome_instancia}")
            
            n, capacidade, pesos = ler_instancia(caminho_arquivo)
            
            caixas_usadas, tempo = resolver_bpp_kantorovich(n, capacidade, pesos, nome_instancia)
            
            if caixas_usadas:
                writer.writerow([nome_instancia, caixas_usadas, round(tempo, 4)])
                csv_file.flush() 
            else:
                writer.writerow([nome_instancia, 'Nao Resolvido', 'Timeout'])

    print("\n==================================================")
    print(" OTIMIZAÇÃO EM LOTE CONCLUÍDA COM SUCESSO!")
    print(f" Todos os resultados foram salvos em: {arquivo_saida}")
    print("==================================================")

if __name__ == "__main__":
    main()