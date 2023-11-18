_PLAYER = "O"
_COMPUTER = "X"


def display_board(board):
    """
    Muestra el tablero en pantalla.

    :param board: Lista con el estado del tablero.
    :return: None
    """
    print("+-------+-------+-------+")
    for row in range(1, 10, 3):
        print("|       |       |       |")
        row_values = [
            board[i] if board[i] != " " else str(i) for i in range(row, row + 3)
        ]
        print("|   " + "   |   ".join(row_values) + "   |")
        print("|       |       |       |")
        print("+-------+-------+-------+")


def is_valid_move(board, move):
    """
    Verifica si el movimiento es válido.

    :param board: Lista con el estado del tablero.
    :param move: Movimiento a verificar.
    :return: True si el movimiento es válido, False en caso contrario.
    """
    return move.isdigit() and int(move) in range(1, 10) and board[int(move)] == " "


def enter_move(board):
    """
    Permite al jugador humano ingresar su movimiento.

    :param board: Lista con el estado del tablero.
    :return: None
    """
    while True:
        move = input("Ingresa tu movimiento: ")
        if is_valid_move(board, move):
            board[int(move)] = _PLAYER
            break
        else:
            print("Movimiento incorrecto, vuelve a intentarlo.")


def make_list_of_free_fields(board):
    """
    Genera una lista con los movimientos posibles.
    :param board:  Lista con el estado del tablero.
    :return:  Lista con los movimientos posibles.
    """
    free = []
    for i in range(1, 10):
        if board[i] == " ":
            free.append(i)
    return free


def victory_for(board, sign):
    """
    Verifica si el jugador con el signo indicado ha ganado.

    :param board:  Lista con el estado del tablero.
    :param sign:  Signo del jugador a verificar.
    :return:  True si el jugador ha ganado, False en caso contrario.
    """
    if board[1] == sign and board[2] == sign and board[3] == sign:
        result = True
    elif board[4] == sign and board[5] == sign and board[6] == sign:
        result = True
    elif board[7] == sign and board[8] == sign and board[9] == sign:
        result = True
    elif board[1] == sign and board[4] == sign and board[7] == sign:
        result = True
    elif board[2] == sign and board[5] == sign and board[8] == sign:
        result = True
    elif board[3] == sign and board[6] == sign and board[9] == sign:
        result = True
    elif board[1] == sign and board[5] == sign and board[9] == sign:
        result = True
    elif board[3] == sign and board[5] == sign and board[7] == sign:
        result = True
    else:
        result = False
    return result


def draw_move(board):
    """
    Dibuja el movimiento en el tablero.

    :param board: Lista con el estado del tablero.
    :return: None
    """
    if len(make_list_of_free_fields(board)) == 9:
        board[5] = _COMPUTER  # Primer mov.
    else:
        free = make_list_of_free_fields(board)
        cnt = len(free)
        if cnt > 0:
            import random

            this_move = random.randrange(cnt)
            board[free[this_move]] = _COMPUTER


def main():
    """
    Función principal.
    :return:
    """
    while True:
        board = ["#", " ", " ", " ", " ", " ", " ", " ", " ", " "]
        human_turn = False

        while len(make_list_of_free_fields(board)) > 0:
            if len(make_list_of_free_fields(board)) != 9:
                display_board(board)
            if human_turn:
                enter_move(board)
                if victory_for(board, _PLAYER):
                    print("🎊🎊🎊 ¡Has ganado! 🎊🎊🎊")
                    break
            else:
                draw_move(board)
                if victory_for(board, _COMPUTER):
                    print("¡He ganado!")
                    break
            human_turn = not human_turn

        display_board(board)
        if not victory_for(board, _COMPUTER) and not victory_for(board, _PLAYER):
            print("¡Empate!")

        replay = input("¿Quieres jugar otra partida? (s/n): ").lower()
        if replay != "s":
            print("TicTacToe by Jonatan L.")
            break


if __name__ == "__main__":
    main()
