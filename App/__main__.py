from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.binding import Binding
from textual.containers import Vertical
from textual.widgets import Footer, Header, Button, Static, Label, Markdown

# Obs:
# Encapsular melhor as telas para diminuir a quantidade de código apenas nessa tela

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
        yield Markdown(AVISOS)

        yield Footer(show_command_palette=False)
        
# Tela de input
class OutputScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Static("OUTPUT")

        yield Footer(show_command_palette=False)

# Classe que é responsável por rodar o app
class App(App[str]):
    CSS_PATH = "app.tcss"
    BINDINGS = [
        Binding(key = "ctrl+q", action="quit", description="Fechar aplicativo"),
        Binding(key = "j", action="down", description="Rolar para baixo"),
        Binding(key = "k", action="up", description="Rolar para cima"),
    ]

    def compose(self) -> ComposeResult:
        yield Static("MENU")
        yield Header(icon="🤖")
        yield Footer(show_command_palette=False)

        yield Vertical(
            Static("PÁGINAS", id="title_landing"),
            Button("INPUT", id="input_button"), 
            Button("OUTPUT", id="output_button"),   
            id="menu_landing"
        )
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "input_button":
            self.push_screen(InputScreen())
        elif event.button.id == "output_button":
            self.push_screen(OutputScreen())
            

    def on_mount(self) -> None:
        self.theme = "gruvbox"
        self.title = "Automato"
        self.sub_title = " Uma colaboração entre UnDF & IBICT"

app = App()
app.run()
