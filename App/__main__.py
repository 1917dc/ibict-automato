from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.widgets import Footer, Header 

class App(App[str]):
    CSS_PATH = "app.tcss"
    BINDINGS = [
        Binding(key = "ctrl+q", action="quit", description="Fechar aplicativo"),
        Binding(key = "j", action="down", description="Rolar para baixo"),
        Binding(key = "k", action="up", description="Rolar para cima"),
    ]

    def compose(self) -> ComposeResult:
        yield Header(icon="🤖")
        yield Footer(show_command_palette=False)
    
    def on_mount(self) -> None:
        self.theme = "gruvbox"
        self.title = "Automato"
        self.sub_title = " Uma colaboração entre UnDF & IBICT"


if __name__ == "__main__":
    app = App()
    app.run()
