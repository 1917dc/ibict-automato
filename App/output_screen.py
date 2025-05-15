from textual.screen import Screen
from textual.app import ComposeResult
from textual.widgets import Footer, Header, Button, Static, Markdown, ListView, ListItem, Label

# Tela de output
class OutputScreen(Screen):
    
    def __init__(self, file_name: str):
        super().__init__()
        self.file_name = file_name

    def compose(self) -> ComposeResult:
        yield Static("OUTPUT")
        yield Static(f"{self.file_name}")

        yield Footer(show_command_palette=False)