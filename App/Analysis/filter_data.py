import pandas as pd
from enelvo import normaliser

# Classe feita para desempenhar o papel de análise de dados dentro da aplicação.

# dadas essas colunas:

# Data de Ocorrência
# Monitoramento
# Servico
# Manifestações Quantidade
# Usuário
# Título
# Conteúdo
# Link
# Tipo Conteudo
# Manifestacoes Detalhado
# data_ultima_atualizacao
# datacoleta

# os dados pertinentes para o momento sao:
# Titulo, Conteudo, Manifestacoes

class DataFilter():
    def data_normaliser(file_name: str) -> None:

        data = pd.read_csv(f"inputs/{file_name}.csv")
        norm = normaliser.Normaliser()

        conteudo_norm = []

        for conteudo in data["Conteúdo"]:
            conteudo_norm.append(norm.normalise(str(conteudo)))

        for tweet in conteudo_norm:
            print(tweet)




if __name__ == "__main__":
    data = DataFilter

    data.data_normaliser("dados_500")
