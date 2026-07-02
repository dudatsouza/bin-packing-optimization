def ler_instancia(caminho_arquivo):
    with open(caminho_arquivo, 'r') as f:
        linhas = f.readlines()
        
    linhas = [linha.strip() for linha in linhas if linha.strip()]
    
    n = int(linhas[0])
    capacidade = int(linhas[1])
    
    pesos = [int(linha) for linha in linhas[2:2+n]]
    
    print(f"Instância carregada com sucesso!")
    print(f"Total de Itens: {n} | Capacidade da Caixa: {capacidade}")
    
    return n, capacidade, pesos