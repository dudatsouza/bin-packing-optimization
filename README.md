<a name="readme-topo"></a>

<h1 align='center'>
  Trabalho Final: Otimização Combinatória - 1D Bin Packing Problem (1D-BPP)
</h1>

<div align='center'>

[![SO][Ubuntu-badge]][Ubuntu-url]
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

## Artigo Base
"Bin packing problems: mathematical models and exact algorithms" (M. Delorme, S. Iori, S. Martello – European Journal of Operational Research, 2016).

https://www.sciencedirect.com/science/article/abs/pii/S0377221716302491


## 📚 O Projeto
Para manter a organização e facilitar a execução do solver, o projeto está estruturado da seguinte forma:

```
trabalho-otimizacao-bpp/
│
├── data/                   # Diretório para os dados públicos (instâncias)
│   └── falkenauer/         # Ex: Instâncias clássicas de Falkenauer
│       └── t60_00.txt      # Arquivo de texto puro com os dados
│
├── src/                    # Código-fonte principal em Python
│   ├── main.py             # Script principal que orquestra o fluxo
│   ├── parser.py           # Função para ler os arquivos .txt da pasta 'data'
│   └── model.py            # A implementação do Modelo de Kantorovich no Gurobi
│
├── results/                # Onde salvaremos os logs e saídas do Gurobi
│   └── solver_logs.txt
│
├── docs/                   # Documentação
│   ├── relatorio_final.pdf # O relatório que será entregue
│   └── artigo_base.pdf     # O PDF do artigo do Delorme (para consulta)
│
├── requirements.txt        # Dependências do Python (gurobipy)
├── .gitignore              # Arquivos que o Git deve ignorar
└── README.md               # Este arquivo


```

## 🛠️ Dependências e Configuração
O projeto foi desenvolvido em Python 3. A única biblioteca externa necessária para a execução do modelo é a API do Gurobi.

Para instalar as dependências, execute:

```
pip install -r requirements.txt
```


> [!NOTE]
> É necessário possuir uma licença acadêmica ativa do Gurobi configurada na máquina

<p align="right">(<a href="#readme-topo">voltar ao topo</a>)</p>

## 🚀 Como Executar

Para rodar o modelo em uma instância específica, basta executar o arquivo principal:

```
python src/main.py
```



## 🧪 Ambiente de Compilação e Execução

<div align="justify">

  O trabalho foi desenvolvido e testado em várias configurações de hardware. Podemos destacar algumas configurações de Sistema Operacional e Compilador, pois as demais configurações não influenciam diretamente no desempenho do programa.

</div>

<div align='center'>

[![SO][Ubuntu-badge]][Ubuntu-url]
[![IDE][vscode-badge]][vscode-url]
[![Python][Python-badge]][Python-url]

| *Hardware* | *Especificações* |
|:------------:|:-------------------:|
| *Laptop*   | Dell Inspiron 13 5330 |
| *Processador* | Intel Core i7-1360P |
| *Memória RAM* | 16 GB DDR5 |
| *Sistema Operacional* | Ubuntu 24.04 |
| *IDE* | Visual Studio Code |
| *Placa de Vídeo* | Intel Iris Xe Graphics |

</div>

> [!IMPORTANT] 
> Para que os testes tenham validade, considere as especificações
> do ambiente de compilação e execução do programa.

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

1. <a name="ref1"></a>SOUZA, Maria E. T. Otimização Combinatória - 1D Bin Packing Problem (1D-BPP). 2026. Disponível em: [https://github.com/dudatsouza/bin-packing-optimization) Acesso em: 02 jul. 2026.




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
[ubuntu-badge]: https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white
[Ubuntu-url]: https://ubuntu.com/
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
