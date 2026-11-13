# ATV09 - Sistema Web com Django

## Identificação da Dupla
- **Maedja Andrade**
- **Sarah Beatriz**

## Descrição do Projeto
Aplicação web desenvolvida em Django para a Atividade 09, contendo páginas dinâmicas gerenciadas pelo painel administrativo (Capa, Currículos, Temas e Link Externo no menu lateral).

## Tecnologias Utilizadas
- Python 3
- Django 6
- HTML5 e CSS3
- SQLite3

## Como Executar o Projeto

### 1. Criação e ativação do ambiente virtual
    python3 -m venv .venv
    source .venv/bin/activate

### 2. Instalação das dependências
    pip install django

### 3. Execução das migrations
    python manage.py migrate

### 4. Criação do superusuário
    python manage.py createsuperuser

### 5. Execução do servidor
    python manage.py runserver

### 6. Acesso à aplicação e ao Django Admin
- **Aplicação:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Django Admin:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
