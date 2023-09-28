# Projeto Python Tech News! :newspaper:
Projeto desenvolvido por mim durante o curso de Desenvolvimento Web na Trybe. Divulgado aqui como portfólio de aprendizado.

<details>
<summary><strong>Objetivos do projeto:</strong></summary>
 
  * Desenvolver uma aplicação que faz consultas em notícias sobre tecnologia utilizando a raspagem de dados no [blog da trybe](https://blog.betrybe.com).
  * Verificar se sou capaz de:
    * Utilizar o terminal interativo do Python
    * Escrever seus próprios módulos e importá-los em outros códigos
    * Aplicar técnicas de raspagem de dados
    * Extrair dados de conteúdo HTML
    * Armazenar os dados obtidos em um banco de dados.
</details>
<details>
<summary><strong> Requisitos do projeto:</strong></summary>

  *  Testar o construtor/inicializador do objeto Produto.
  *  Testar o relatório individual gerado por Produto.
  *  Criar a Interface `Importer`.
  *  Criar a classe `JsonImporter`.
  *  Criar a classe `Inventory`.
  *  Criar o protocolo `Report`.
  *  Criar o relatório `SimpleReport`.
</details>
  
## Rodando o projeto localmente

Para rodar o projeto em sua máquina, abra seu terminal, crie um diretório no local de sua preferência com o comando `mkdir` e acesse o diretório criado com o comando `cd`:

```bash
mkdir meu-diretorio &&
cd meu-diretorio
```

Clone o projeto com o comando `git clone`:

```bash
git clone git@github.com:marcosadrianoti/tb-python-inventory-report.git
```

Acesse o diretório do projeto com o comando `cd`:

```bash
cd tb-python-inventory-report
```

crie o ambiente virtual:
```bash
python3 -m venv .venv
```

Ative o ambiente virtual:
```bash
source .venv/bin/activate
```

Instale as dependências no ambiente virtual:
```bash
python3 -m pip install -r dev-requirements.txt
```

Execute os testes com:
```bash
python3 -m pytest
```
