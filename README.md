<a name="readme-topo"></a>

<h1 align='center'>
  Trabalho Final: Otimização Combinatória - 1D Bin Packing Problem (1D-BPP)
</h1>

<div align='center'>

[![SO][Zorin-OS-badge]][Zorin-OS-url]
[![IDE][vscode-badge]][vscode-url]
[![Python][Python-badge]][Python-url]

<b>
  Maria Eduarda Teixeira Souza<br>
</b>
  
<br>
Inteligência Computacional <br>
Engenharia de Computação <br>
CEFET-MG Campus V <br>
2026/1

</div>

## 📌 Sobre o Projeto

Este projeto apresenta um estudo prático focado no **Problema de Empacotamento Unidimensional (1D-BPP)**, classicamente classificado como NP-difícil. Baseando-se na revisão de literatura de Delorme, Iori e Martello (2016), foi implementada a formulação matemática de **Kantorovich**, referenciada na literatura como **BASIC ILP**. 

O objetivo principal é reproduzir os experimentos computacionais em classes de instâncias clássicas da literatura (como Falkenauer, Scholl e Hard28), validando o modelo utilizando a linguagem Python e o solver comercial **Gurobi**.

## 📄 Artigo Base
"Bin packing and cutting stock problems: Mathematical models and exact algorithms" (M. Delorme, S. Iori, S. Martello – European Journal of Operational Research, 2016).

🔗 [Link para o artigo](https://www.sciencedirect.com/science/article/abs/pii/S0377221716302491)

## 🧮 Formulação Matemática (BASIC ILP)

A modelagem do problema (Kantorovich) é construída a partir dos seguintes elementos:

**Parâmetros:**
* $n$: número total de itens disponíveis para empacotamento;
* $C$: capacidade máxima (homogênea) de cada caixa;
* $w_j$: peso associado ao item $j$, tal que $w_j > 0$.

**Variáveis de Decisão:**
* $y_i \in \{0, 1\}$: variável binária que assume o valor 1 se a caixa $i$ for utilizada na solução, e 0 caso contrário, para $i \in \{1, \dots, n\}$;
* $x_{ij} \in \{0, 1\}$: variável binária que assume o valor 1 se o item $j$ for alocado na caixa $i$, e 0 caso contrário, para $i, j \in \{1, \dots, n\}$.

**Função Objetivo:**
Minimizar o número total de caixas utilizadas:
$$ \min \sum_{i=1}^{n} y_i $$

**Restrições Operacionais:**
1. **Garantia de alocação única:** Assegura que cada item $j$ seja processado e atribuído a exatamente uma única caixa.
   $$ \sum_{i=1}^{n} x_{ij} = 1 \quad \forall j \in \{1, \dots, n\} $$

2. **Respeito à capacidade limite:** Garante que o somatório dos pesos dos itens alocados em uma caixa não exceda a sua respectiva capacidade $C$.
   $$ \sum_{j=1}^{n} w_j x_{ij} \leq C y_i \quad \forall i \in \{1, \dots, n\} $$

## 📚 Arquitetura do Projeto

Visando assegurar a organização estrutural, a reprodutibilidade e a escalabilidade dos experimentos, a arquitetura do código-fonte foi segmentada da seguinte forma:

```text
trabalho-otimizacao-bpp/
│
├── data/                   # Diretório para os dados públicos (instâncias BPPLIB)
│   └── falkenauer/         # Ex: Instâncias clássicas de Falkenauer
│       └── t60_00.txt      # Arquivo de texto puro com os dados
│
├── src/                    # Código-fonte principal em Python
│   ├── parser.py           # Leitura e Pré-processamento: ingestão dos arquivos .txt
│   ├── model.py            # Modelagem Matemática: instanciação do BASIC ILP no Gurobi
│   ├── main.py             # Execução e Exportação: automatização e execução em lote
│   └── analysis.py         # Análise de Dados e Visualização: estatísticas e gráficos
│
├── results/                # Resultados gerados e logs do solver
│   ├── resultados_bpp.csv  # Dados consolidados das execuções
│   ├── medias_bpp.csv      # Tabela de médias por classe
│   └── solver_logs.txt     # Logs do solver Gurobi
│
├── docs/                   # Documentação
│   ├── Trabalho_Final____Pesquisa_Operacional.pdf # O relatório e artigo do trabalho
│   └── artigo_base.pdf     # O PDF do artigo do Delorme (para consulta)
│
├── requirements.txt        # Dependências do Python
├── .gitignore              # Arquivos que o Git deve ignorar
└── README.md               # Este arquivo
```

## 🛠️ Dependências e Configuração
O projeto foi desenvolvido em Python 3.10. A principal biblioteca externa necessária para a execução do modelo é a API do Gurobi (`gurobipy`).

Para instalar as dependências, execute:

```bash
pip install -r requirements.txt
```

> [!NOTE]
> É necessário possuir uma licença ativa (acadêmica ou comercial) do **Gurobi** configurada na sua máquina.

<p align="right">(<a href="#readme-topo">voltar ao topo</a>)</p>

## 🚀 Como Executar

Para rodar o processamento em lote nas instâncias configuradas:

```bash
python src/main.py
```
*(As rotinas de análise e compilação gráfica podem ser executadas chamando `python src/analysis.py` posteriormente).*

## 📊 Resultados e Conclusões

Os experimentos demonstraram que o modelo BASIC ILP apresenta tempos computacionais significativamente menores para instâncias computacionalmente tratáveis, como *Falkenauer U* e *Scholl 1*, especialmente devido ao avanço tecnológico do hardware atual. Notavelmente, a classe *Falkenauer T* obteve prova de otimalidade em 90% das amostras na nossa execução, superando a dificuldade relatada no artigo de 2016.

No entanto, o limite prático do modelo foi evidenciado em instâncias críticas (*Scholl 3*, *Wäscher* e *Hard28*), cuja alta complexidade (por capacidades elevadas e simetria) esgotou o tempo de CPU estipulado de 300 segundos, confirmando a conclusão do artigo base de que a fraca qualidade da relaxação linear da matriz de Kantorovich impõe dificuldades aos métodos exatos.

## 🧪 Ambiente de Compilação e Execução

<div align="justify">
  O trabalho foi desenvolvido e testado no seguinte ambiente computacional, que influencia diretamente na performance apresentada:
</div>

<div align='center'>

| *Componente* | *Especificação* |
|:------------:|:-------------------:|
| *Máquina*   | Dell Inspiron 13 5330 |
| *Processador* | Intel Core i7-1360P |
| *Memória RAM* | 16 GB DDR5 |
| *Placa de Vídeo* | Intel Iris Xe Graphics |
| *Sistema Operacional* | Zorin OS |

</div>

> [!IMPORTANT] 
> Para que os testes tenham validade metodológica e comparativa, considere as especificações
> do ambiente de execução e as versões dos pacotes.

<p align="right">(<a href="#readme-topo">voltar ao topo</a>)</p>

## 📨 Contato

<div align="center">  
  
  <br><br>
     <i>Maria Eduarda Teixeira Souza - Graduando - 7º Período de Engenharia de Computação @ CEFET-MG</i>
  <br><br>
  
  [![Gmail][gmail-badge]][gmail-autor2]
  [![Linkedin][linkedin-badge]][linkedin-autor2]
  [![Telegram][telegram-badge]][telegram-autor2]

</div>

<p align="right">(<a href="#readme-topo">voltar ao topo</a>)</p>


<a name="referencias">📚 Referências</a>

1. <a name="ref1"></a>SOUZA, Maria E. T. **Trabalho Final: Otimização Combinatória - 1D Bin Packing Problem (1D-BPP)**. Repositório GitHub, 2026. Disponível em: <https://github.com/dudatsouza/bin-packing-optimization>. Acesso em: 03 jul. 2026.

2. <a name="ref2"></a>DELORME, M.; IORI, M.; MARTELLO, S. Bin packing and cutting stock problems: Mathematical models and exact algorithms. **European Journal of Operational Research**, v. 255, p. 1-20, 2016.

3. <a name="ref3"></a>GUROBI OPTIMIZATION, LLC. **Gurobi Optimizer Reference Manual**. 2026. Disponível em: <https://www.gurobi.com>. Acesso em: 03 jul. 2026.

4. <a name="ref4"></a> DELORME, M. **BPPLIB: A benchmark library for the one-dimensional bin packing problem**. 2018. Disponível em: <https://github.com/mdelorme2/BPPLIB>. Acesso em: 03 jul. 2026.

[vscode-badge]: https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white
[vscode-url]: https://code.visualstudio.com/docs/?dv=linux64_deb
[make-badge]: https://img.shields.io/badge/_-MAKEFILE-427819.svg?style=for-the-badge
[make-url]: https://www.gnu.org/software/make/manual/make.html
[cpp-badge]: https://img.shields.io/badge/c++-%2300599C.svg?style=for-the-badge&logo=c%2B%2B&logoColor=white
[cpp-url]: https://en.cppreference.com/w/cpp
[trabalho-url]: https://drive.google.com/file/d/1-IHbGaA1BIC6_CMBydOC-NbV2bCERc8r/view?usp=sharing
[github-prof]: https://github.com/mpiress
[main-ref]: src/main.cpp
[branchAMM-url]: https://github.com/alvarengazv/trabalhosAEDS1/tree/AlgoritmosMinMax
[makefile]: ./makefile
[bash-url]: https://www.hostgator.com.br/blog/o-que-e-bash/
[lenovo-badge]: https://img.shields.io/badge/lenovo%20laptop-E2231A?style=for-the-badge&logo=lenovo&logoColor=white
[Zorin-OS-badge]: https://img.shields.io/badge/-Zorin%20OS-%2310AAEB?style=for-the-badge&logo=zorin&logoColor=white
[Zorin-OS-url]: https://zorin.com/
[ryzen5500-badge]: https://img.shields.io/badge/AMD%20Ryzen_5_5500U-ED1C24?style=for-the-badge&logo=amd&logoColor=white
[ryzen3500-badge]: https://img.shields.io/badge/AMD%20Ryzen_5_3500X-ED1C24?style=for-the-badge&logo=amd&logoColor=white
[windows-badge]: https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white
[gcc-badge]: https://img.shields.io/badge/GCC-5C6EB8?style=for-the-badge&logo=gnu&logoColor=white
[Python-badge]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/


[linkedin-autor1]: https://www.linkedin.com/in/guilherme-alvarenga-de-azevedo-959474201/
[telegram-autor1]: https://t.me/alvarengazv
[gmail-autor1]: mailto:gui.alvarengas234@gmail.com

[linkedin-autor2]: https://www.linkedin.com/in/dudatsouza/
[telegram-autor2]: https://t.me/dudat_18
[gmail-autor2]: mailto:dudateixeirasouza@gmail.com

[linkedin-badge]: https://img.shields.io/badge/-LinkedIn-0077B5?style=for-the-badge&logo=Linkedin&logoColor=white
[telegram-badge]: https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white
[gmail-badge]: https://img.shields.io/badge/-Gmail-D14836?style=for-the-badge&logo=Gmail&logoColor=white
