ChargeGrid Intelligence
Sobre o Projeto

O ChargeGrid Intelligence é uma prova de conceito desenvolvida para o GoodWe Challenge, com o objetivo de demonstrar uma solução para gerenciamento inteligente de estações de recarga de veículos elétricos em ambientes comerciais.

A aplicação simula a distribuição de energia entre carregadores, realiza cálculos de tarifação e utiliza uma lógica de inteligência artificial para otimizar o uso da energia disponível, evitando sobrecargas na rede elétrica.

Problema

Com a expansão dos carregadores de veículos elétricos para ambientes comerciais, surgem desafios relacionados ao gerenciamento eficiente da energia disponível.

Os principais problemas identificados foram:

Sobrecarga da rede elétrica em horários de pico;
Distribuição inadequada da potência entre carregadores;
Necessidade de tarifação automatizada;
Integração entre carregadores de diferentes fabricantes;
Otimização do consumo energético.
Solução Proposta

A solução desenvolvida consiste em um sistema desktop que simula uma estação de carregamento inteligente.

O sistema permite:

Definir o limite de energia disponível;
Informar a demanda de três carregadores;
Distribuir a energia automaticamente;
Calcular o custo da recarga;
Exibir informações em um dashboard;
Gerar relatórios da operação.
Funcionalidades
Controle Inteligente de Demanda

O sistema monitora a demanda dos carregadores e verifica se ela ultrapassa o limite de energia disponível.

Caso a demanda seja superior ao limite, a energia é redistribuída proporcionalmente entre os carregadores.

Inteligência Artificial Simulada

Uma lógica de decisão analisa o cenário atual.

Durante horários de pico, a potência disponível pode ser reduzida para evitar sobrecarga da rede.

Tarifação

O sistema calcula automaticamente o valor da recarga com base na energia distribuída.

Interoperabilidade

A aplicação simula a integração de carregadores de diferentes fabricantes por meio de protocolos abertos.

Relatórios

Após a simulação, é possível gerar um relatório contendo os resultados da operação.

Tecnologias Utilizadas
Python
Tkinter
Matplotlib
Programação Orientada a Objetos
Estrutura do Projeto
chargegrid-intelligence/

├── main.py
├── demand_manager.py
├── ai_manager.py
├── billing.py
├── requirements.txt
└── README.md
Arquitetura da Solução
Usuário
    │
    ▼
Interface Tkinter
    │
    ▼
Controle de Demanda
    │
    ▼
Inteligência Artificial
    │
    ▼
Distribuição de Energia
    │
    ▼
Tarifação
    │
    ▼
Dashboard e Relatórios
Como Executar
Instalar Dependências
pip install matplotlib
Executar o Projeto
python main.py
Exemplo de Simulação
Entrada
Limite de Energia: 100 kW

Carregador 1: 50 kW
Carregador 2: 40 kW
Carregador 3: 30 kW
Resultado
Demanda Total: 120 kW

Energia redistribuída automaticamente

Carregador 1: 41.67 kW
Carregador 2: 33.33 kW
Carregador 3: 25.00 kW
Objetivos Atendidos
Controle de demanda
Tarifação e pagamento
Interoperabilidade
Inteligência artificial
Dashboard de monitoramento
Geração de relatórios
Prova de conceito funcional
Melhorias Futuras
Integração com banco de dados
Cadastro de usuários
Histórico de recargas
Comunicação em tempo real com carregadores
Implementação de algoritmos avançados de Machine Learning
Dashboard web
Equipe

Projeto desenvolvido para o GoodWe Challenge como atividade acadêmica da disciplina de Ciência da Computação.

Licença

Projeto desenvolvido exclusivamente para fins educacionais.
