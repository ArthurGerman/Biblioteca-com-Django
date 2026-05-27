# Projeto Biblioteca com Django
- Aluno: Arthur Germano da Cunha Silva
- Ferramenta escolhida: Django
- Descrição da atividade: Crud de uma Biblioteca com relacionamento 1:n entre duas entidades: Autor e Livro. Cada autor pode ter vários livros, mas cada livro tem apenas um autor.

## Clonando o projeto

Para rodar o projeto, siga estes passos

```bash
# 1. Clonando o projeto
git clone https://github.com/ArthurGerman/Biblioteca-com-Django
cd crud_django

# 2. Criar e ativar o virtualenv
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 3. Instalar as dependências
pip install -r requirements.txt

# 4. Rodar as migrations
python manage.py migrate

# 5. Rodar o servidor
python manage.py runserver


```