from os import getcwd, listdir
from textual.screen import Screen
from textual.app import ComposeResult
from textual.widgets import Footer, Header, Button, Static, Markdown, ListView, ListItem, Label

# Tela de input
class InputScreen(Screen):
    def compose(self) -> ComposeResult:

        AVISOS = """
# Formatação
**A tabela deve ser frormatada com as seguintes colunas:**
- Data de Ocorrência
- Monitoramento
- Servico
- Manifestações Quantidade
- Usuário
- Título
- Conteúdo
- Link
- Tipo Conteudo
- Manifestacoes Detalhado
- data_ultima_atualizacao
- datacoleta

# Observações

- Atualmente aceitamos apenas arquivos em formato ".csv"
- Coloque os arquivos que devem ser usados para a análise dentro da pasta inputs"
        """        

        yield Static("INPUT")
        yield ListView(
            *[ListItem(Label(item)) for item in listdir(getcwd() + "/inputs/")]
        )
        yield Markdown(AVISOS)

        yield Footer(show_command_palette=False)
    
    def on_mount(self) -> None:
        return