def ler_instancia(caminho_arquivo):
    """
    Lê o arquivo de texto da instância do 1D-BPP (Formato Falkenauer).
    
    Retorna:
        n (int): Número de itens
        capacidade (int): Capacidade de cada caixa
        pesos (list): Lista com o peso de cada item
    """
    with open(caminho_arquivo, 'r') as f:
        linhas = f.readlines()
        
    # Limpa espaços em branco e quebras de linha
    linhas = [linha.strip() for linha in linhas if linha.strip()]
    
    # Extrai os dados do cabeçalho
    n = int(linhas[0])
    capacidade = int(linhas[1])
    
    # Lê os pesos a partir da terceira linha até o final dos itens
    pesos = [int(linha) for linha in linhas[2:2+n]]
    
    print(f"Instância carregada com sucesso!")
    print(f"Total de Itens: {n} | Capacidade da Caixa: {capacidade}")
    
    return n, capacidade, pesos