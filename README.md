# ibict-automacao
Projeto para automação de processos de NLP dentro do IBICT

# Como desenvolver dentro do projeto

Caso tenha clonado o projeto e queira rodar localmente siga o seguinte passo a passo:

### Entrar no ambiente de desenvolvimento
```bash
# Linux
source .venv/bin/activate

# Windows
. .venv\bin\Activate.ps1
```

### Instalação de dependências
```bash
pip install -r requirements.txt
```

### Acoplar dependências novas ao projeto (faça isso apenas caso adicione algum depêndencia nova)
```bash
pip freeze > requirements.txt
```
