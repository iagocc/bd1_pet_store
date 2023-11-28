# Projeto Pet Store da cadeira de Banco de Dados 1 - Unichritus
O código deste repositório busca ser o mais didático possível, para ajudar o aluno a compreender a utilizar as técnicas desenvolvidar com o SQL ao longo do curso com a linguagem Python.

As dependências para este projeto rodar estão descritar no arquivo `requirements.txt` e pode ser instalado via o gerenciados de pacotes `pip`.
```sh
pip install -r requirements.txt
```
Vamos entender cada parte do código em sala de aula, mas para você conseguir rodar no seu ambiente, é necessário verificar cada arquivo e entender onde você deverá modificar para atender sua configuração.

Preste atenção no arquivo `server.py` que lá será necessário definir valores para a conexão com o banco de dados.

Além disso, as tabelas do banco encontra-se no arquivo `pet_db.sql`, sendo necessário criar o esquema antes.

Para rodar o código deste repositório é necessário utilizar o seguinte comando via linha de comando:
```sh
flask --app server --debug run 
```

