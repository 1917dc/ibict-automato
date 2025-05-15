from os import listdir, getcwd
from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.binding import Binding
from textual.containers import Horizontal, Vertical
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
        yield Header(icon="🤖")

        IBICT_ASCII = r"""

        
            .--..                         ...             
            .*%%%*-...              ...:==-..             
            .*%%%%%%#+:...      ...-=**=..::.             
            .*%%%%%%%%%#*=:...:-+##*-.:-=-:..             
            .*%%%%%%%%%%%%%###%%*=-=**=:..--.             
            .*%%%%%%%%%%%%%%%#=+#%*-..=*+:.               
            .*%%%%%%%%%%%%%%#%#*=-+##=:.:-+=.             
            .+%%%%%%%%%%%%%%#*+#%*=:-+**-.....           
             .:+#%%%%%%%%%%%%#*++*##=:.-==-..            
           :=:...:+#%%%%%%%%##%%#=:-*#*-....-=-..        
        .=+...*#:.  .=#%%%%%%*-=%%%*:  .:+%%%%%%%+..     
  ....:=-..-*+:.=#*=....=#%%%%%#+:...-+#%%%%%%%%%%%#+:..
....:=-..=*=::+#+:-*%#=:...-=-:...-*%%%%%%%%%%%%%%%%%%#+-.
.:==:..=+-.:**=:=##=-+#%#+:.  .=*%%%%%%%%%%%%%%%%%%%%%%*-.
  ..-**-.:+#=-=##+=*%#++#%%: .*%#%%%%%%%%%%%%%%%%%%%#=:.. 
      .+%#=.-#%+-*%%**%%%%%-.:#%+#%#%%%%%%%%%%%%%%+..     
       ..=#%#+-*#%**%%%%%%%-.:#%-##*%##%%%%%%%##:.        
          .:+#%#*#%%%%%%%%%-.:##:#*+%+*#*#%%*-.           
           ..-#%%%%%%%%%%%%-.:#+:#++%=*#+#%=.             
             .*%%%%%%%%%%%%-.:#-:#==#:**=##:.             
             .*%%%%%%%%%%%%- :*::#-=#.++-##.              
             .*%%%%%%%%%%%%- :*.:*:=+.++-#*.              
             .+%%%%%%%%%%%%- :=.:+.+-.+=:#=               
             .=%%%%%%%%%%%#. ::.:-.=:.+-:#:               
             .-%%%%%%%%#+:.     ...-..=::*.               
             .:%%%%%#=..          ....-.:=.               
             .:#%#=..                ....-.               
              .:..                      ..                

"""

        yield Horizontal(
             Static(IBICT_ASCII, id="logo"),
            Vertical(
                Static("Menu", id="menu_top"),
                Static("Páginas", id="title_landing"),
                Vertical(
                    Button("INPUT", id="input_button"),
                    id="menu_button_box"
                ),
                id="menu_landing"
            ),
            id="layout"
        )

        yield Footer(show_command_palette=False)
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "input_button":
            self.push_screen(InputScreen())
            

    def on_mount(self) -> None:
        self.theme = "gruvbox"
        self.title = "Automato"
        self.sub_title = " Uma colaboração entre UnDF & IBICT"

app = App()
app.run()
