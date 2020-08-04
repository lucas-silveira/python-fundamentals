# Criando ambiente virtual (isolado da nossa máquina)

Para criar um virtual env em nosso projeto, executamos o comando:
```
python -m venv name_of_venv
```

Para ativar o virtual env, acessamos o arquivo activate do venv:
```
. /venv/bin/activate or source /venv/bin/activate
```

Para sair do virtual env, basta digitar no console:
```
deactivate
```

# Comandos

Listar os pacotes instalados em nosso virtual env:
```
pip freeze
```

Criar arquivo requirements.txt:
```
pip freeze > requirements.txt
```

Instalar pacotes listados no arquivo requirements:
```
pip install -r requirements.txt
```