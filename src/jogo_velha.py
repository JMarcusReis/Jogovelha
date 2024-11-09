from abc import ABC, abstractmethod
import random as r

class Tabuleiro:

    def __init__(self, casas: list[str]) -> None:
        """
        Cria um objeto na classe Tabuleiro

        Args:
            casas (list[str]): Uma lista com uma string de 9 elementos
        """
        self.casas = list(casas[0]) 
    
    def pegar_tabuleiro(self) -> list[list[str]]:
        """
        Constrói a representação 2D do tabuleiro

        Returns:
            list[list[str]]: O tabuleiro 3x3 como matriz
        """
        tabuleiro = [[], [], []]
        for i in range(3):
            for j in range(3):
                tabuleiro[i].append(self.casas[j + (i * 3)]) 
        return tabuleiro
    
    def marcar_casas(self, pos: tuple[int, int], valor: str) -> None:
        """
        Marca uma casa no tabuleiro com um valor dado

        Args:
            pos (tuple[int, int]): A posição (linha, coluna) da casa a ser marcada
            valor (str): O valor da casa
        """
        new_pos = (pos[0] - 1) * 3 + (pos[1] - 1)  
        self.casas[new_pos] = valor 

    def imprimir_tabuleiro(self) -> None:
        """
        Imprime o estado atual do tabuleiro no console
        """
        tabuleiro = self.pegar_tabuleiro() 
        for i in range(3):
            for j in range(3):
                print(f"|{tabuleiro[i][j]}|", end=' ')
            print('\n') 


class Jogador(ABC):

    def __init__(self, simbolo: str, nome: str) -> None:
        """
        Cria um objeto da classe Jogador

        Args:
            simbolo (str): O símbolo do jogador no tabuleiro
            nome (str): O nome do jogador
        """
        self.simbolo = simbolo
        self.nome = nome
    
    @abstractmethod
    def fazer_jogada(self, tabuleiro: Tabuleiro) -> tuple[int, int] | None:
        """
        Método abstrato para fazer uma jogada no tabuleiro

        Args:
            tabuleiro (Tabuleiro): O tabuleiro da jogada

        Returns:
            tuple[int, int]: A posição (linha, coluna) da jogada
        """
        pass


class JogadorHumano(Jogador):

    def __init__(self, simbolo: str, nome: str):
        """
        Cria um objeto da classe JogadorHumano

        Args:
            simbolo (str): O símbolo do jogador no tabuleiro
            nome (str): O nome do jogador
        """
        super().__init__(simbolo, nome)

    def fazer_jogada(self, tabuleiro: Tabuleiro) -> tuple[int, int] | None:
        """
        Solicita uma jogada do jogador

        Args:
            tabuleiro (Tabuleiro): O tabuleiro da jogada

        Returns:
            tuple[int, int]: A posição (linha, coluna) da jogada
        """
        message = 'Jogador atual: Humano\nJogada (linha coluna): '
        jogada = tuple(map(int, input(message).split()))
        if not tabuleiro.pegar_tabuleiro()[jogada[0] - 1][jogada[1] - 1] in ['1', '-1']:
            return jogada
        else:
            return None


class JogadorComputador(Jogador):

    def __init__(self, simbolo: str, nome: str, estrategia: str) -> None:
        """
        Instancia um objeto da classe JogadorComputador

        Args:
            simbolo (str): O símbolo do jogador no tabuleiro
            nome (str): O nome do jogador
            estrategia (str): A estratégia usada pelo computador
        """
        super().__init__(simbolo, nome)
        self.estrategia = estrategia if estrategia in ['aleatoria'] else 'aleatoria'

    def fazer_jogada(self, tabuleiro: Tabuleiro) -> tuple[int, int]:
        """
        Faz uma jogada aleatória no tabuleiro

        Args:
            tabuleiro (Tabuleiro): O tabuleiro da jogada

        Returns:
            tuple[int, int]: Uma posição aleatória possível
        """
        tab = tabuleiro.pegar_tabuleiro()
        possiveis_jogadas = [(i + 1, j + 1) for i in range(3) for j in range(3) if tab[i][j] not in ['1', '-1']]
        return r.choice(possiveis_jogadas)


class JogoVelha:

    def __init__(self, jogadores: list[Jogador], tabuleiro: Tabuleiro, turno: int = 1):
        """
        Cria um objeto da classe JogoVelha

        Args:
            jogadores (list[Jogador]): Lista de jogadores
            tabuleiro (Tabuleiro): O tabuleiro do jogo
            turno (int): O turno atual do jogo (padrão é 1)
        """
        self.jogadores = jogadores
        self.tabuleiro = tabuleiro
        self.turno = turno
    
    def checa_vitoria(self, jogador: Jogador) -> bool:
        """
        Verifica se um jogador ganhou o jogo

        Args:
            jogador (Jogador): O jogador que vai ser verificada

        Returns:
            bool: True ou False se o Jogador já ganhou
        """
        simbolo = jogador.simbolo
        tab = self.tabuleiro.pegar_tabuleiro()
        
        # Verifica linhas e colunas
        for i in range(3):
            if tab[i][0] == tab[i][1] == tab[i][2] == simbolo:
                return True
            if tab[0][i] == tab[1][i] == tab[2][i] == simbolo:
                return True
        
        # Verifica diagonais
        if tab[0][0] == tab[1][1] == tab[2][2] == simbolo:
            return True
        if tab[0][2] == tab[1][1] == tab[2][0] == simbolo:
            return True
        
        return False
    
    def checar_fim_de_jogo(self) -> str | None:
        """
        Verifica se o jogo terminou e retorna o vencedor

        Returns:
            str | None: 'Jogador0' ou 'Jogador1'
        """
        if self.checa_vitoria(self.jogadores[0]):
            return 'Jogador0'
        elif self.checa_vitoria(self.jogadores[1]):
            return 'Jogador1'
        return None  # Retorno padrão

    def jogador_atual(self) -> Jogador:
        """
        Retorna o jogador que vai jogar nesse turno

        Returns:
            Jogador: O jogador atual
        """
        return self.jogadores[1] if self.turno % 2 == 0 else self.jogadores[0]
    
    def jogar(self) -> None:
        """
        Inicia o jogo em loop, com as regras de um jogo da velha
        """
        while True:
            vencedor = self.checar_fim_de_jogo()
            if vencedor:
                print(f"FIM DE JOGO. VENCEDOR : {self.jogadores[0].nome if vencedor == 'Jogador0' else self.jogadores[1].nome}")
                break
            
            atual = self.jogador_atual()
            jogada = atual.fazer_jogada(self.tabuleiro)
            self.tabuleiro.marcar_casas((jogada[0], jogada[1]), atual.simbolo)
            self.tabuleiro.imprimir_tabuleiro()
            print(f"Jogador: {atual.nome}, jogada: {jogada[0]}, {jogada[1]}")
            self.turno += 1