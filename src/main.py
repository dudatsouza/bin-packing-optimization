# src/main.py
import os
import sys
from parser import ler_instancia
from model import resolver_bpp_kantorovich

def main():
    print("==================================================")
    print(" Trabalho Final - Otimização Combinatória (1D-BPP)")
    print("==================================================")
    
    # Caminho do arquivo que acabamos de copiar
    caminho_instancia = "data/Falkenauer_U/Falkenauer_u120_00.txt"
    nome_instancia = "Falkenauer_u120_00"
    
    # Trava de segurança para garantir que você está rodando do lugar certo
    if not os.path.exists(caminho_instancia):
        print(f"\nErro: O arquivo não foi encontrado no caminho: {caminho_instancia}")
        print("Certifique-se de executar o script a partir da raiz do projeto (trabalho-otimizacao-bpp)")
        sys.exit(1)
        
    print("\n[Etapa 1] Realizando a leitura da base de dados...")
    n, capacidade, pesos = ler_instancia(caminho_instancia)
    
    print("\n[Etapa 2] Inicializando a API do Gurobi e montando o modelo...")
    caixas_usadas, tempo = resolver_bpp_kantorovich(n, capacidade, pesos, nome_instancia)
    
    if caixas_usadas:
        print("\n==================================================")
        print(" OTIMIZAÇÃO CONCLUÍDA COM SUCESSO!")
        print("==================================================")
        print("Estes são os valores para colocar na tabela do relatório:")
        print(f"-> Instância: {nome_instancia}")
        print(f"-> Solução Ótima (Mínimo de Caixas): {caixas_usadas}")
        print(f"-> Tempo Computacional: {tempo:.4f} segundos")
        print("==================================================")

if __name__ == "__main__":
    main()