import numpy as np

class Damas:
    def __init__(self):
        self.tabuleiro = self.inicializar_tabuleiro()
        self.jogador_atual = 'B'  # B para brancas, P para pretas

    def inicializar_tabuleiro(self):
        tabuleiro = np.full((8, 8), '.', dtype=str)
        for linha in range(3):
            for coluna in range(8):
                if (linha + coluna) % 2 == 1:
                    tabuleiro[linha, coluna] = 'P'
        for linha in range(5, 8):
            for coluna in range(8):
                if (linha + coluna) % 2 == 1:
                    tabuleiro[linha, coluna] = 'B'
        return tabuleiro

    def exibir_tabuleiro(self):
        print("  0 1 2 3 4 5 6 7")
        print(" +----------------")
        for i, linha in enumerate(self.tabuleiro):
            print(f"{i}| {' '.join(linha)}")
        print()

    def movimento_valido(self, linha_origem, coluna_origem, linha_destino, coluna_destino):
        if self.tabuleiro[linha_destino, coluna_destino] != '.':
            return False  # Espaço ocupado
        delta_linha = linha_destino - linha_origem
        delta_coluna = abs(coluna_destino - coluna_origem)
        if self.jogador_atual == 'B' and delta_linha != -1:
            return False  # Movimento inválido para brancas
        if self.jogador_atual == 'P' and delta_linha != 1:
            return False  # Movimento inválido para pretas
        return delta_coluna == 1

    def mover_peca(self, linha_origem, coluna_origem, linha_destino, coluna_destino):
        if self.movimento_valido(linha_origem, coluna_origem, linha_destino, coluna_destino):
            self.tabuleiro[linha_destino, coluna_destino] = self.jogador_atual
            self.tabuleiro[linha_origem, coluna_origem] = '.'
            self.trocar_turno()
        else:
            print("Movimento inválido!")

    def trocar_turno(self):
        self.jogador_atual = 'P' if self.jogador_atual == 'B' else 'B'

    def jogar(self):
        while True:
            self.exibir_tabuleiro()
            print(f"Vez do jogador {self.jogador_atual}")
            try:
                linha_origem = int(input("Linha da peça: "))
                coluna_origem = int(input("Coluna da peça: "))
                linha_destino = int(input("Linha destino: "))
                coluna_destino = int(input("Coluna destino: "))
                self.mover_peca(linha_origem, coluna_origem, linha_destino, coluna_destino)
            except ValueError:
                print("Entrada inválida. Tente novamente!")

if __name__ == "__main__":
    jogo = Damas()
    jogo.jogar()
