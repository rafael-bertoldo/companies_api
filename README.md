# CRUD de empresas

## Guia de execução:

- Faça o clone deste repositório;
- Em um terminal execute o seguinte comando:

```bash
cd companies_api
python -m venv .venv
```

Este comando iniciará um ambiente virtual para a instalação das dependências do projeto.

- Ainda no terminal execute:

  - Linux/Mac

  ```bash
  source .venv/bin/activate
  ```

  - Windows
    - Power Shell
      ```bash
      .\.venv\Scripts\activate
      ```
    - Git bash
      ```bash
      source .venv/Scripts/activate
      ```
Este comando entrará no ambiente virtual, para que não instalemos as dependências diretamente em nossa máquina;

- Com o ambiente virtual execute:

```bash
(.venv)
pip install -r requirements.txt
```

## Iniciar banco de dados SQLite

```bash
(.venv)
flask db init
```

## Executar Migrações
```bash
(.venv)
flask db migrate -m 'Nome da migração'

(.venv)
flask db upgrade
```

## Iniciar o servidor
```bash
flask run
```
Com este comando o servidor iniciará em `http://localhost:5000/`

Para acessar a documentação da api acesse: [http://localhost:5000/api/docs](http://localhost:5000/api/docs)