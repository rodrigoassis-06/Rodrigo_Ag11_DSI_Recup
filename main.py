from colorama import init, Fore, Style

# Inicializacao da biblioteca colorama
init()

# Lista com os niveis e situacoes do reservatorio
niveis_reservatorio = [
    {"nivel": 1, "situacao": "Muito baixo (critico)"},
    {"nivel": 2, "situacao": "Baixo"},
    {"nivel": 3, "situacao": "Medio"},
    {"nivel": 4, "situacao": "Alto"},
    {"nivel": 5, "situacao": "Muito alto (alerta)"}
]

def obter_cor_nivel(nivel):
    """
    Funcao responsavel por definir a cor correspondente
    ao nivel informado conforme a especificacao do projeto.
    """
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE

def exibir_monitoramento(niveis):
    print("SISTEMA DE MONITORAMENTO DO RESERVATORIO DE AGUA")
    print("-" * 50)
    for item in niveis:
        nivel = item["nivel"]
        situacao = item["situacao"]
        cor = obter_cor_nivel(nivel)
        print(f"{cor}[Nivel {nivel}] Situacao: {situacao}{Style.RESET_ALL}")
    print("-" * 50)

if __name__ == "__main__":
    exibir_monitoramento(niveis_reservatorio)

