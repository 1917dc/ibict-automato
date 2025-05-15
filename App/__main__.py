from os import listdir, getcwd
from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.binding import Binding
from textual.containers import Vertical
from textual.widgets import Footer, Header, Button, Static, Markdown, ListView, ListItem, Label
from input_screen import InputScreen
from output_screen import OutputScreen

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
            id="menu_landing"
        )
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "input_button":
            self.push_screen(InputScreen())
            

    def on_mount(self) -> None:
        self.theme = "gruvbox"
        self.title = "Automato"
        self.sub_title = " Uma colaboração entre UnDF & IBICT"

app = App()
app.run()
