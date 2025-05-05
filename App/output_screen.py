from textual.screen import Screen
from textual.app import ComposeResult
from textual.widgets import Footer, Header, Button, Static, Markdown, ListView, ListItem, Label

# Tela de output
class OutputScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Static("OUTPUT")

        yield Footer(show_command_palette=False)