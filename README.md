# Fundamentos de Python para Automação e IA

Bem-vindo ao repositório: **Fundamentos de Python para Automação e IA**!

Este módulo foi desenhado para fornecer uma base sólida e prática na linguagem Python, essencial para quem deseja criar soluções nas áreas de automação de processos e desenvolvimento de aplicações com Inteligência Artificial Generativa (GenAI). Todo o conteúdo é apresentado através de Jupyter Notebooks, combinando explicações conceituais com exemplos práticos e relevantes para o tema do programa.

## Objetivos de Aprendizagem do Módulo

Ao concluir este módulo, você será capaz de:

*   Dominar a sintaxe fundamental do Python e seus tipos de dados essenciais.
*   Utilizar operadores para construir expressões lógicas e aritméticas.
*   Controlar o fluxo de execução de seus programas com condicionais e laços.
*   Escrever código modular e reutilizável através da definição e uso de funções.
*   Trabalhar eficientemente com as principais estruturas de dados do Python: listas, tuplas, conjuntos e dicionários.
*   Entender como organizar e reutilizar código com módulos e pacotes.
*   Aplicar os conceitos básicos de Programação Orientada a Objetos (POO).
*   Implementar tratamento de erros robusto para criar scripts mais confiáveis.
*   Interagir com APIs externas utilizando a biblioteca `requests`.
*   Realizar operações básicas de manipulação de arquivos.
*   Adotar boas práticas de codificação, depuração e gerenciamento de dependências com ambientes virtuais.

## Pré-requisitos

*   Conhecimentos básicos de informática e navegação em sistemas operacionais.
*   Não é necessário conhecimento prévio de programação Python, pois este módulo cobre os fundamentos.
*   Git instalado (para clonar este repositório).
*   Python 3.8 ou superior.

## Como Configurar o Ambiente e Executar os Notebooks

Siga os passos abaixo para configurar seu ambiente de desenvolvimento:

1.  **Clone o repositório:**
 

2.  **Crie e ative um ambiente virtual** (altamente recomendado):
    Isso isola as dependências do projeto. Na pasta raiz do projeto:

    *   **Windows:**
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```
    *   **macOS/Linux:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    Você saberá que o ambiente virtual está ativo pois o nome dele (`venv`) aparecerá no início do seu prompt do terminal.

3.  **Instale as dependências:**
    Com o ambiente virtual ativo, instale as bibliotecas Python necessárias:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Inicie o Jupyter Lab (ou Jupyter Notebook):**
    Ainda no terminal, com o ambiente virtual ativo e na pasta raiz do projeto, execute:
    ```bash
    jupyter lab
    ```
    Seu navegador padrão deverá abrir com a interface do Jupyter.

5.  **Navegue e execute os notebooks:**
    *   Na interface do Jupyter, clique na pasta `notebooks/`.
    *   Os notebooks são numerados para sugerir uma ordem de estudo. Comece pelo `00_introducao_ambiente_jupyter.ipynb`.
    *   Abra um notebook e execute as células de código (geralmente pressionando `Shift + Enter`).



## Conteúdo dos Notebooks (Módulo 1)

1.  `00_introducao_ambiente_jupyter.ipynb`: Familiarização com o ambiente Jupyter Notebook e uma primeira visão do Python.
2.  `01_variaveis_tipos_dados.ipynb`: Conceitos de variáveis e os tipos de dados fundamentais do Python.
3.  `02_operadores_expressoes.ipynb`: Operadores aritméticos, de atribuição, comparação e lógicos.
4.  `03_controle_fluxo_condicionais.ipynb`: Tomada de decisão com `if`, `elif` e `else`.
5.  `04_controle_fluxo_lacos.ipynb`: Repetição de tarefas com laços `for` e `while`.
6.  `05_funcoes.ipynb`: Definindo e utilizando funções para modularidade e reutilização de código.
7.  `06_estruturas_dados_listas_tuplas.ipynb`: Trabalhando com listas e tuplas.
8.  `07_estruturas_dados_conjuntos_dicionarios.ipynb`: Explorando conjuntos e a importância dos dicionários.
9.  `08_modulos_pacotes.ipynb`: Utilizando módulos da biblioteca padrão e introdução ao gerenciamento de pacotes com `pip`.
10. `09_introducao_poo_classes_objetos.ipynb`: Introdução à Programação Orientada a Objetos: classes e objetos.
11. `10_poo_heranca_polimorfismo.ipynb`: Conceitos de herança e polimorfismo na POO.
12. `11_tratamento_excecoes.ipynb`: Lidando com erros e exceções para criar código robusto.
13. `12_manipulacao_arquivos.ipynb`: Lendo e escrevendo em arquivos de texto.
14. `13_json_csv.ipynb`: Trabalhando com arquivos nos formatos JSON e CSV.
15. `14_datas_horas_datetime.ipynb`: Manipulando datas e horas com o módulo `datetime`.
16. `15_expressoes_regulares_re.ipynb`: Utilizando expressões regulares para busca e manipulação de padrões em texto com o módulo `re`.
17. `16_trabalhando_apis_requests.ipynb`: Fazendo requisições HTTP para APIs web com a biblioteca `requests`.
18. `17_depuracao_boas_praticas_ambientes_virtuais.ipynb`: Técnicas de depuração, boas práticas de codificação (PEP 8) e a importância dos ambientes virtuais.

## Desafios Práticos de Programação

Além dos notebooks, você encontrará desafios práticos na pasta `/desafio`. Estes desafios são projetados para aplicar os conceitos aprendidos em cenários mais complexos e prepará-lo para problemas do mundo real.

### Como Trabalhar nos Desafios:

1.  **Localize os Arquivos:**
    *   Cada desafio está contido em sua própria subpasta dentro de `/desafio` ou diretamente como arquivos nomeados `desafio_XX.py` e `test_desafio_XX.py`.
    *   O arquivo `desafio_XX.py` (por exemplo, `desafio_01.py`) é onde você deverá escrever sua solução. Ele virá com uma estrutura inicial ou funções que você precisa completar.
    *   O arquivo `test_desafio_XX.py` (por exemplo, `test_desafio_01.py`) contém os testes automatizados que verificarão se sua solução está correta.

2.  **Implemente sua Solução:**
    *   Abra o arquivo `desafio_XX.py` em seu editor de código preferido.
    *   Leia atentamente os comentários e as instruções dentro do arquivo para entender o que precisa ser feito.
    *   Escreva seu código Python para resolver o problema proposto.

3.  **Teste sua Solução com `pytest`:**
    *   Após implementar sua solução, você precisará testá-la. Utilizamos a ferramenta `pytest` para isso.
    *   Certifique-se de que seu ambiente virtual (`venv`) está ativo.
    *   No terminal, navegue até a pasta raiz do projeto (`python_fundamentals`).
    *   Para rodar os testes de um desafio específico, você pode usar o comando:
        ```bash
        python -m pytest desafio/test_desafio_XX.py
        ```
        (Substitua `XX` pelo número do desafio, por exemplo: `python -m pytest desafio/test_desafio_01.py`)
    *   Alternativamente, para rodar todos os testes que contenham o nome do desafio no arquivo (útil se houver múltiplos arquivos de teste para um desafio ou para rodar apenas um conjunto específico):
        ```bash
        python -m pytest -k desafio_XX
        ```
        (Substitua `XX` pelo número do desafio, por exemplo: `python -m pytest -k desafio_01`)

4.  **Analise os Resultados:**
    *   `pytest` mostrará quais testes passaram (geralmente marcados com um ponto `.`) e quais falharam (marcados com `F`).
    *   Se houver falhas, `pytest` fornecerá detalhes sobre o erro, incluindo a linha no arquivo de teste e, muitas vezes, a diferença entre o valor esperado e o valor que sua função retornou.
    *   Seu objetivo é fazer com que todos os testes para o desafio em questão passem!

5.  **Itere e Refine:**
    *   Se os testes falharem, volte ao seu arquivo `desafio_XX.py`, revise sua lógica, corrija os erros e tente rodar os testes novamente.
    *   Continue este processo até que todos os testes passem.

Estes desafios são uma parte crucial do seu aprendizado. Eles ajudarão a solidificar seu entendimento e a desenvolver suas habilidades de resolução de problemas em Python.

---

Aproveite o curso! Se encontrar problemas ou tiver sugestões, sinta-se à vontade para abrir uma "Issue" neste repositório.