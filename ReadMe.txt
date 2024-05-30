#Pipeline Action Task - Projeto

Exercício 1: Criando uma Pipeline de CI/CD com GitHub Actions e Testes Automatizados

### Pré-requisitos

- Python 3.x
- pip

##Instalação e execução

1. Clone o repositório:
	git clone https://github.com/clr-c/pipeline-action-task.git
   
2. Abra o diretório do projeto
	cd pipeline-action-task

3. Crie e ative o ambiente virtual:
	python -m venv venv
	source venv/bin/activate	#Linux/Mac
	.\venv\Scripts\activate		#Windows

4. Instale as dependências do projeto
	pip install -r requirements.txt

5. Inicie o servidor Flask e execute o teste:
	python app.py
	pytest

6. Crie um arquivo '.gitignore' para python cache