class JogoDamas:
    def __init__(self):
        self.tabuleiro = self.inicializar_tabuleiro()
        self.jogador_atual = 'B'  # 'B' para brancas, 'P' para pretas

    def inicializar_tabuleiro(self):
        tabuleiro = [['.' for _ in range(8)] for _ in range(8)]
        for linha in range(3):
            for coluna in range(8):
                if (linha + coluna) % 2 == 1:
                    tabuleiro[linha][coluna] = 'P'
        for linha in range(5, 8):
            for coluna in range(8):
                if (linha + coluna) % 2 == 1:
                    tabuleiro[linha][coluna] = 'B'
        return tabuleiro

    def imprimir_tabuleiro(self):
        for linha in self.tabuleiro:
            print(' '.join(linha))
        print("Jogador atual:", self.jogador_atual)

    def selecionar_peca(self, linha, coluna):
        if self.tabuleiro[linha][coluna] == self.jogador_atual:
            return (linha, coluna)
        return None

    def movimento_valido(self, linha_origem, coluna_origem, linha_destino, coluna_destino):
        if self.tabuleiro[linha_destino][coluna_destino] != '.':
            return False
        delta_linha = linha_destino - linha_origem
        delta_coluna = abs(coluna_destino - coluna_origem)
        if self.jogador_atual == 'B' and delta_linha != -1:
            return False
        if self.jogador_atual == 'P' and delta_linha != 1:
            return False
        return delta_coluna == 1

    def mover_peca(self, linha_origem, coluna_origem, linha_destino, coluna_destino):
        if self.movimento_valido(linha_origem, coluna_origem, linha_destino, coluna_destino):
            self.tabuleiro[linha_destino][coluna_destino] = self.jogador_atual
            self.tabuleiro[linha_origem][coluna_origem] = '.'
            self.jogador_atual = 'P' if self.jogador_atual == 'B' else 'B'

# Criar o jogo
damas = JogoDamas()

# Predefinir movimentos (substituir a entrada interativa)
movimentos = [
    (2, 1, 3, 2),
    (5, 0, 4, 1),
    (2, 3, 3, 4),
    (5, 2, 4, 3),
]

# Loop principal
for movimento in movimentos:
    linha_origem, coluna_origem, linha_destino, coluna_destino = movimento
    damas.imprimir_tabuleiro()
    print(f"Movendo de ({linha_origem}, {coluna_origem}) para ({linha_destino}, {coluna_destino})")
    damas.mover_peca(linha_origem, coluna_origem, linha_destino, coluna_destino)

print("Jogo Finalizado.")
