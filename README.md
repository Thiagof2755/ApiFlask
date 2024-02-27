## FlaskCRUD

FlaskCRUD é uma aplicação web simples utilizando Python com o framework Flask, que permite aos usuários criar, visualizar, editar e deletar registros de uma entidade específica em um banco de dados MySQL. A aplicação também deve ter uma interface básica utilizando HTML/CSS.

### Estrutura do Projeto

```
CRUD_COMPLETO_FLASK_PY/
│
├── app.py
├── controllers/
│   ├── produtosController.py
│   └── userController.py
│
├── models/
│   ├── produtosModel.py
│   └── userModel.py
│
├── routes/
│   └── Routes.py
│
├── static/
│   ├── estilo.css
│   └── scripts.js
│
├── templates/
│   ├── criar.html
│   ├── editar.html
│   ├── login.html
│   └── produtos.html
│
├── README.md
├── requirements.txt
└── sql.txt
```

### Explicação da Estrutura:

- **`app.py`**: Arquivo principal que inicia a aplicação Flask.
  
- **`controllers/`**: Pasta contendo os controladores da aplicação, responsáveis por controlar a lógica de negócios e interagir com os modelos de dados.

- **`models/`**: Pasta contendo os modelos de dados da aplicação, que representam as entidades do banco de dados.

- **`routes/`**: Pasta contendo os arquivos de rotas da aplicação, que definem as URLs e suas funções associadas.

- **`static/`**: Pasta para arquivos estáticos  CSS.

- **`templates/`**: Pasta para os arquivos de modelos HTML , usados para renderizar as páginas da web.

- **`README.md`**: Arquivo de documentação do projeto.

- **`requirements.txt`**: Arquivo contendo as dependências Python do projeto, que podem ser instaladas usando `pip`.

- **`sql.txt`**: Arquivo SQL com as instruções para criar o banco de dados e popular com alguns dados iniciais.

## Configuração e Execução

1. **Configurar o Banco de Dados**:
   - Use o XAMPP para configurar e iniciar um servidor MySQL local.
   - Execute o script `sql.txt` para criar o banco de dados e as tabelas, bem como inserir dados iniciais.

2. **Instalar Dependências**:
   - Instale as dependências do projeto listadas no arquivo `requirements.txt` usando o comando `pip install -r requirements.txt`.
   - Se você encontrar problemas durante a instalação das dependências usando o comando `pip install`, você pode tentar executar o comando em um terminal aberto como administrador (no Windows) ou com permissões elevadas (no Linux/macOS). Abra o terminal como administrador e execute o seguinte comando:

      ```
      pip install flask flask-SQLAlchemy mysql-connector-python mysqlclient requests
      ```


3. **Executar a Aplicação**:
   - Execute o arquivo `app.py` para iniciar a aplicação Flask.
   - Acesse a aplicação em http://localhost:5000/ no seu navegador.

Com essa estrutura e instruções, seu projeto estará pronto para ser executado e testado localmente. Certifique-se de personalizar cada parte do projeto de acordo com suas necessidades específicas.

## Exemplo de Uso

A seguir estão alguns exemplos simples de como utilizar a aplicação FlaskCRUD:

### Adicionar um Novo Produto

1. Acesse a página inicial da aplicação em http://localhost:5000/.
2. Clique no botão "Criar Novo Produto".
3. Preencha o formulário com o nome, descrição e preço do novo produto.
4. Clique no botão "Salvar" para adicionar o produto.
5. O novo produto será adicionado à lista de produtos exibida na página inicial.

### Editar um Produto Existente

1. Na lista de produtos exibida na página inicial, encontre o produto que deseja editar.
2. Clique no botão "Editar" ao lado do produto.
3. Será redirecionado para a página de edição do produto.
4. Faça as alterações desejadas nos campos de nome, descrição ou preço.
5. Clique no botão "Salvar" para confirmar as alterações.
6. O produto será atualizado com as informações editadas.

### Excluir um Produto

1. Na lista de produtos exibida na página inicial, encontre o produto que deseja excluir.
2. Clique no botão "Excluir" ao lado do produto.
3. Uma mensagem de confirmação será exibida.
4. Clique em "OK" para confirmar a exclusão do produto.
5. O produto será removido da lista de produtos.

Esses exemplos fornecem uma visão geral de como interagir com as funcionalidades de criação, edição e exclusão de produtos na aplicação FlaskCRUD. Experimente essas ações para explorar todas as capacidades da aplicação.

## Demonstração em Vídeo

- [Vídeo Demonstrativo](./FlaskCRUD.mp4)

