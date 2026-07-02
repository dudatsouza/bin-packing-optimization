import gurobipy as gp
from gurobipy import GRB

def resolver_bpp_kantorovich(n, capacidade, pesos, nome_instancia="Instancia"):
    print(f"\n--- Construindo o Modelo para: {nome_instancia} ---")
    
    model = gp.Model(f"1D_BPP_{nome_instancia}")
    
    model.setParam('TimeLimit', 300)
    model.setParam('MIPGap', 0.0)

    # VARIÁVEIS DE DECISÃO
    # y[i] = 1 se a caixa i for usada, 0 caso contrário
    y = model.addVars(n, vtype=GRB.BINARY, name="y")
    
    # x[i, j] = 1 se o item j for colocado na caixa i, 0 caso contrário
    x = model.addVars(n, n, vtype=GRB.BINARY, name="x")

    # FUNÇÃO OBJETIVO
    # Minimizar o número total de caixas usadas
    model.setObjective(gp.quicksum(y[i] for i in range(n)), GRB.MINIMIZE)

    # RESTRIÇÕES 
    # Regra 1: Cada item 'j' deve ser colocado em exatamente uma caixa 'i'
    for j in range(n):
        model.addConstr(gp.quicksum(x[i, j] for i in range(n)) == 1, name=f"item_{j}_alocado")

    # Regra 2: A soma dos pesos dos itens na caixa 'i' não pode exceder a capacidade C
    for i in range(n):
        model.addConstr(gp.quicksum(pesos[j] * x[i, j] for j in range(n)) <= capacidade * y[i], name=f"cap_caixa_{i}")

    # RESOLUÇÃO
    print("Iniciando o Branch-and-Bound (Gurobi)...")
    model.optimize()

    # EXTRAÇÃO DE RESULTADOS
    if model.status == GRB.OPTIMAL or model.status == GRB.TIME_LIMIT:
        caixas_usadas = int(model.ObjVal)
        tempo = model.Runtime
        return caixas_usadas, tempo
    else:
        print("O solver não conseguiu encontrar uma solução.")
        return None, None