branco = " "
token = ["X", "O"]

def criarBoard():
    board = [
        [branco,branco,branco],
        [branco,branco,branco],
        [branco,branco,branco],
    ]
    return board

def printBoard(board):
   for i in range(3):
       print("|".join(board[i]))
       if i < 2:
         print("---------")


def getInputValido(mensagem):
    try:
        n = int(input(mensagem))
        if(n >= 1 and n <= 3):
            return n -1
            print("Sucesso ", n)
        else:
            print("O numero precisa estar entre 1 e 3")
            return getInputValido(mensagem)
    except:
        print("Numero nao valido")
        getInputValido(mensagem)

def verificaMovimento(board, i, j):
    if(board[i][j] == branco):
        return True
    else:
        return False

def fazMovimento(board, i, j, jogador):
    board[i][j] = token[jogador]

def verificaGanhador(board):
    return False
