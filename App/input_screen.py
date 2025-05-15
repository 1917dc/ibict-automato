from textual import on
from os import getcwd, listdir
from textual.screen import Screen
from textual.app import ComposeResult
from textual.widgets import Footer, Header, Button, Static, Markdown, Select, Label
from output_screen import OutputScreen

# Tela de input
class InputScreen(Screen):

    def __init__(self):
        super().__init__()
        self.file_name = None
        self.file_display = Static("")


    def compose(self) -> ComposeResult:

        with open("App/markdown/avisos.md", "r") as file:
            avisos_content = file.read()

        yield Static("INPUT")
        yield Select(((line[:-4], line) for line in listdir(getcwd() + "/inputs/") if line.endswith(".csv")), allow_blank = False)
        yield Markdown(avisos_content)
        yield Footer(show_command_palette=False)
        yield self.file_display

        yield Button("Enviar")
    
    @on(Select.Changed)
    def select_changed(self, event: Select.Changed) -> None:
        self.file_name = event.value
        self.file_display.update(f"Arquivo selecionado: {event.value}")

    @on(Button.Pressed)
    def button_pressed(self, event: Button.Pressed) -> None:
        self.app.push_screen(OutputScreen(self.file_name))

    
    def on_mount(self) -> None:
        return