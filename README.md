# Projeto Python Tech News! :newspaper:
Projeto desenvolvido por mim durante o curso de Desenvolvimento Web na Trybe. Divulgado aqui como portfólio de aprendizado.

<details>
<summary><strong>Objetivos do projeto:</strong></summary>
 
  * Desenvolver um gerador de relatórios. Deve receber arquivos contendo informações sobre um estoque e produzir um relatório abrangente com base nesses dados.
  * Verificar se sou capaz de:
    * Aplicar conceitos de Programação Orientada a Objetos em Python.
    * Implementar leitura e escrita de arquivos CSV e JSON em Python.
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
