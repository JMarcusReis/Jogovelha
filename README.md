# Jogovelha
Cria um jogo da velha em python

## Libs usadas:
 - random
 - abc

## Files:
 - Functios-jogo_velha.py : Contém o código de todas as funções

## Instalação:
 - Vá no seu terminal e digite : "python -m pip install --upgrade pip setuptools wheel".
 - Depois digite : "python setup.py install"

## Estrutura do Código

### Classes Principais

1. **Tabuleiro**
   - Representa o tabuleiro do jogo.
   - **Métodos:**
     - `__init__(casas: list[str])`: Inicializa o tabuleiro com uma lista que contém uma string.
     - `pegar_tabuleiro() -> list[list[str]]`: Retorna a representação 2D do tabuleiro.
     - `marcar_casas(pos: tuple[int, int], valor: str)`: Marca uma casa no tabuleiro com as coordenadas fornecidas.
     - `imprimir_tabuleiro()`: Imprime o estado atual do tabuleiro.

2. **Jogador (Abstrata)**
   - Classe base para jogadores, que define a interface que todos os jogadores devem implementar.
   - **Métodos:**
     - `__init__(simbolo: str, nome: str)`: Inicializa um jogador com seu símbolo no jogo e seu nome.
     - `fazer_jogada(tabuleiro: Tabuleiro) -> tuple[int, int] | None`: Método abstrato para a jogada que será feita pelo jogador.

3. **JogadorHumano**
   - Extende a classe `Jogador` para implementar um jogador humano.
   - **Métodos:**
     - `fazer_jogada(tabuleiro: Tabuleiro) -> tuple[int, int]`: Solicita a jogada do jogador através de um input do usuário.

4. **JogadorComputador**
   - Extende a classe `Jogador` para implementar um jogador controlado pelo computador.
   - **Métodos:**
     - `fazer_jogada(tabuleiro: Tabuleiro) -> tuple[int, int]`: Realiza uma jogada aleatória nas casas livres no tabuleiro.

5. **JogoVelha**
   - Controla o jogo e a interação entre os jogadores.
   - **Métodos:**
     - `__init__(jogadores: list[Jogador, Jogador], tabuleiro: Tabuleiro, turno: int = 1)`: Inicializa o jogo com jogadores e um tabuleiro.
     - `checa_vitoria(jogador: Jogador) -> bool`: Verifica se o jogador venceu.
     - `checar_fim_de_jogo() -> str | None`: Verifica se o jogo terminou e retorna o vencedor.
     - `jogador_atual() -> Jogador`: Retorna o jogador que está jogando no turno atual.
     - `jogar() -> None`: Inicia o loop do jogo.

## Exemplos
```python
from Functions import jogovelha as jv

tabuleiro = jv.Tabuleiro(['         '])
jogadores = [jv.JogadorHumano('X', 'João Marcus'), 
            jv.JogadorComputador('O', 'Roboto')]
jogo = jv.JogoVelha(jogadores, tabuleiro, 1)
jogo.jogar()
```
## License:
 - MIT license