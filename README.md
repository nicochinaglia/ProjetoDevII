# Projeto Cadastro de Alunos

O projeto tem como objetivo utilizar o framework Django, pertencente a linguágem de programação Python para criar uma operação simples de CRUD. <br>
O Django utiliza a arquitetura MVT (Model, View, Template). <br>
O tema escolhido foi um cadastro de alunos da Fatec, onde é possível inserir, deletar, vez e atualizar os dados. <br>

Caso deseje baixar o projeto em sua máquina certifique-se de rodar os comandos dentro da pasta do projeto para provisionar o banco de dados.

    ./manage.py makemigrations
    ./manage.py migrate

Após realizar as migrações, rode o comanhdo para inicializar o servidor do projeto:

    ./manage.py runserver
    
Certifique-se de que quando acessar a URL http://127.0.0.1:8000/ insira o nome aluno após a barra.    
______________________________________________________________________________________________________________________________________

Caso deseje iniciar um novo aplicativo no projeto insira o comando no terminal dentro da pasta do projeto:

    ./manage.py startapp myapp
    
______________________________________________________________________________________________________________________________________    

## Estrutura do projeto

![Estrutura do projeto](https://github.com/nicochinaglia/ProjetoDevII/tree/master/imagens/github.jpg)

______________________________________________________________________________________________________________________________________ 

## Referência

O código de referência para o projeto foi retirado da internet com customizações para atender o objetivo do projeto.
Página usada de referência:
https://rayed.com/posts/2018/05/django-crud-create-retrieve-update-delete/
