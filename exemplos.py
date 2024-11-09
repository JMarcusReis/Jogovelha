from src import jogovelha as jv

tabuleiro = jv.Tabuleiro(['         '])
nome_1 = int(input("Digite o nome do seu jogador\nNome: "))
jogadores = [jv.JogadorHumano('X', 'João Marcus'), 
            jv.JogadorComputador('O', 'Roboto')]
jogo = jv.JogoVelha(jogadores, tabuleiro, 1)
jogo.jogar()