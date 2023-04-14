import time
import pickle
import pygame as pg

pg.init()

# Assign constants to be used by PyGame
TILE_SIZE = 60
TILE_COLOR_1 = (205, 205, 205)
TILE_COLOR_2 = (155, 155, 155)

WHITE_COLOR = (240, 60, 60)
BLACK_COLOR = (60, 60, 240)

BOARD_SIZE = 8 * TILE_SIZE
WIN_WIDTH = BOARD_SIZE
WIN_HEIGHT = BOARD_SIZE

pg.display.set_caption("Chess")
WIN = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
WIN.fill((0, 0, 0))

bP_img = pg.image.load('images/bP.png')
wP_img = pg.image.load('images/wP.png')
bR_img = pg.image.load('images/bR.png')
wR_img = pg.image.load('images/wR.png')
bN_img = pg.image.load('images/bN.png')
wN_img = pg.image.load('images/wN.png')
bB_img = pg.image.load('images/bB.png')
wB_img = pg.image.load('images/wB.png')
bQ_img = pg.image.load('images/bQ.png')
wQ_img = pg.image.load('images/wQ.png')
bK_img = pg.image.load('images/bK.png')
wK_img = pg.image.load('images/wK.png')

class ChessPiece:
    """
    This class represents a piece in a game of chess, with an
    associated piece type, team, and board location.
    """
    def __init__(self, piece_type, team):
        """
        Initializes a chess piece with the specified piece type,
        team, coordinate, and movement status.
        :param piece_type: Type of piece: 'K', 'Q', 'R', 'B', 'N', or 'P'
        :type piece_type: str
        :param team: Team that the piece belongs to: 1 (White), or 2 (Black)
        :type team: int
        """
        self._piece_type = piece_type
        self._team = team
        self._coord = None
        self._moved = False

    def get_coord(self) -> tuple:
        """
        This method returns the coordinates this piece occupies.
        :return: Piece coordinates
        """
        return self._coord

    def set_coord(self, coord) -> None:
        """
        This method sets the piece's coordinates to the specified values.
        Can be set to 'None' to remove an associated coordinate.
        :type coord: tuple | None
        :return: None
        """
        self._coord = coord

    def is_in_play(self) -> bool:
        """
        This method returns True if the piece occupies a tile.
        :return: True if the piece is in play
        """
        if self._coord is None:
            return False
        return True

    def is_moved(self) -> bool:
        """
        This method returns True if the piece has been moved at least once from its initial position.
        If the piece is moved from, and subsequently back to its initial position, this method returns False.
        :return: Movement status as bool
        """
        return self._moved

    def get_piece_string(self) -> str:
        """
        This method returns a string representation of the piece, with a character 'w' (White)
        or 'b' (Black), followed by the piece type.
        :return: Piece as string
        """
        if self._team == 1:
            team_char = 'w'
        else:
            team_char = 'b'

        return team_char + self._piece_type

    def get_type(self) -> str:
        """
        This method returns the piece type for this piece.
        :return: Piece type
        """
        return self._piece_type

    def get_team(self) -> int:
        """
        This method returns the team this piece belongs to.
        :return: Piece team
        """
        return self._team

class ChessTile:
    """
    This class represents a tile on the board of a game of chess,
    with an associated coordinate on the board and piece occupying
    the tile.
    """
    def __init__(self, coord):
        """
        Initializes a tile with the given coordinate.
        :type coord: tuple
        """
        self._coord = coord
        self._piece = None

    def get_coord(self) -> tuple:
        """
        This method returns the coordinates of the tile.
        :return: Tuple coordinates
        """
        return self._coord

    def set_piece(self, piece) -> None:
        """
        This method sets a piece to occupy this tile. If the 'piece'
        argument is None, this removes any occupying piece.
        :param piece: The ChessPiece object to occupy this tile
        :type piece: ChessPiece | None
        :return: None
        """
        self._piece = piece

    def has_piece(self) -> bool:
        """
        This method returns True if there is a piece currently occupying
        this tile.
        :return:
        """
        if self._piece is None:
            return False
        return True

    def get_piece(self) -> ChessPiece:
        """
        This method returns the ChessPiece object occupying the tile.
        Returns None if no piece.
        :return: ChessPiece object
        """
        return self._piece


class ChessBoard:
    """
    This class represents a chessboard with associated tiles and pieces,
    coordinating the ChessTile and ChessPiece objects.
    """
    def __init__(self):
        # The board is a list of lists of ChessTile objects.
        self._board = []
        for i in range(0, 8):
            row_list = []
            for j in range(0, 8):
                tile = ChessTile((i, j))
                row_list.append(tile)
            self._board.append(row_list)

        self.set_up_board()

    def set_up_board(self) -> None:
        """
        This method sets up the initial positions of the pieces on the board.
        :return: None
        """
        initial_rows = [['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'], []]
        for i in range(0, 8):
            initial_rows[1].append('P')

        self.set_up_row(0, initial_rows[0], 2)
        self.set_up_row(1, initial_rows[1], 2)
        self.set_up_row(6, initial_rows[1], 1)
        self.set_up_row(7, initial_rows[0], 1)

    def set_up_row(self, row, format_list, team) -> None:
        """
        This method sets up the pieces in a row with the given format on the given team's side.
        :param row: The row to set up
        :type row: int
        :param format_list: A list containing the string characters representing the order the pieces appear in a row.
        :type format_list: list
        :param team: An integer 1 (White) or 2 (Black)
        :type team: int
        :return: None
        """
        for i in range(0, 8):
            new_piece = ChessPiece(format_list[i], team)
            self.set_piece_coord(new_piece, (row, i))

    def get_tile(self, coord) -> ChessTile:
        """
        This method returns the ChessTile object with the speicifed coordinates.
        :type coord: tuple
        :return: ChessTile object
        """
        return self._board[coord[0]][coord[1]]

    def set_piece_coord(self, piece, coord) -> None:
        """
        This method sets a piece's coordinates to the specified value. It also
        updates the tile that the piece occupies, and removes it from the
        tile that it previously occupied. If the tile at the specified coordinate
        is already occupied by a piece, that piece is overwritten.
        :param piece: ChessPiece object
        :type piece: ChessPiece
        :param coord: Coordinate to set to
        :type coord: tuple
        :return: None
        """
        new_tile = self.get_tile(coord)

        # If there is a piece at the given coordinates, remove its coordinates
        if new_tile.has_piece():
            new_tile.get_piece().set_coord(None)

        # Remove the given piece from its current Tile object, if possible
        if piece.get_coord() is not None:
            current_tile = self.get_tile(piece.get_coord())
            current_tile.set_piece(None)

        # Add piece to new tile
        new_tile.set_piece(piece)
        piece.set_coord(coord)

    def get_board(self) -> list:
        """
        This method returns the board as a list of lists of ChessTile objects.
        :return: Board list
        """
        return self._board

    def is_in_bounds(self, coord) -> bool:
        """
        This method returns False if the provided coordinates are outside of the playable board space.
        :param coord: Coordinates
        :type coord: tuple
        :return: True if in bounds
        """
        for i in range(0, 2):
            if coord[i] < 0 or coord[i] > 7:
                return False
        return True


class ChessGame:
    """
    This class represents a game of chess with its associated board and game state.
    """
    def __init__(self):
        """
        This method initializes a game of chess.
        """
        self.b = ChessBoard()
        self.moves_stack = []

    def get_board(self) -> list:
        """
        This method returns the board as a list of lists of ChessTile objects.
        :return: Board list
        """
        return self.b.get_board()


class ConsoleCommand:
    """
    This class represents a command to be executed by the ChessConsole object.
    """
    def __init__(self, cmd_name, cmd_arg_count, cmd_help_string, cmd_detail_string, cmd_function):
        """
        Initializes a command with the command name, number of arguments taken, and help string.
        :param cmd_name: Name of the command
        :type cmd_name: str
        :param cmd_arg_count: Number of arguments accepted (including the command itself)
        :type cmd_arg_count: int
        :param cmd_help_string: Short description of command
        :type cmd_help_string: str
        :param cmd_extend_string: Extended description of command
        :type cmd_extend_string: str
        """
        self.cmd_name = cmd_name
        self.cmd_arg_count = cmd_arg_count
        self.cmd_help_string = cmd_help_string
        self.cmd_detail_string = cmd_detail_string
        self.cmd_function = cmd_function


class ChessConsole:
    """
    This class handles the console used to interact with the game.
    """
    def __init__(self, game):
        """
        Initializes the console and associated commands.
        :param game: ChessGame object
        :type game: ChessGame
        """
        self.game = game

        self._command_dict = {}

        self._command_dict["help"] = (ConsoleCommand(
            "help",
            2,
            "Provide usage information for commands. 'help [command]' for specific command details.",
            "Provide usage information for commands. 'help [command]' for details on command; "
            "'help all' for an overview of all available commands.",
            self.cmd_help
        ))

        self._command_dict["board"] = (ConsoleCommand(
            "board",
            1,
            "Prints the board to the console.",
            "Prints the board to the console in a visual format.",
            self.cmd_board
        ))

        self._command_dict["move"] = (ConsoleCommand(
            "move",
            3,
            "Move a piece.",
            "Attempts to move a piece from the coordinates of the first argument to that of the second argument.\n"
            "Usage: 'move a7 a5'",
            self.cmd_move
        ))

        self._command_dict["newgame"] = (ConsoleCommand(
            "newgame",
            1,
            "Reset the board.",
            "Starts a new game of chess, with all pieces set back to their initial positions."
            " The status of the ongoing game is also cleared.",
            self.cmd_newgame
        ))

        self._command_dict["save"] = (ConsoleCommand(
            "save",
            1,
            "Saves the game.",
            "Saves the game to the 'save_file' file.\nOnly one save file is available, and "
            "any existing saved data is overwritten by this command.",
            self.cmd_save
        ))

        self._command_dict["load"] = (ConsoleCommand(
            "load",
            1,
            "Loads a game.",
            "Loads the existing 'save_file' data as a game.\nOnly one save file is available, and "
            "any ongoing game will be overwritten.",
            self.cmd_load
        ))

        self._command_dict["undo"] = (ConsoleCommand(
            "undo",
            1,
            "Undoes the last move.",
            "Undoes the most recently played move, restoring the previous game state.",
            self.cmd_undo
        ))

        self._command_dict["exit"] = (ConsoleCommand(
            "exit",
            1,
            "Exit the program.",
            "Exits the program without saving.",
            self.cmd_exit
        ))

    def get_input(self, user_input, input_string=None) -> int:
        """
        This method takes a boolean value to determine whether a command will be passed directly
        to this function or if the function should request user input in the console. This input is then parsed
        and passed to the execute_command function to execute the command.
        :param user_input: True to provide user input
        :type user_input: bool
        :param input_string: String to parse for command
        :return: 0 if successful
        """
        if user_input:
            input_string = input("Enter a command ('help all' for available commands):\n>")

        if len(input_string) == 0:
            print("Error: No input found")
            return -1

        arguments = input_string.split()

        if arguments[0] in self._command_dict:
            command = self._command_dict[arguments[0]]
        else:
            print("Error: Command not recognized: " + arguments[0])
            return -1

        if len(arguments) != command.cmd_arg_count:
            print("Error: Argument count error")
            return -1

        del arguments[0]

        # Execute the command's associated function
        command_function = command.cmd_function
        return command_function(arguments)

    def cmd_help(self, arguments) -> int:
        """
        Provide usage information for commands. Takes one argument: 'all' to display all commands,
        or the name of a specific command for a more detailed description.
        :param arguments:
        :return: 0 if successful
        """
        if arguments[0] == 'all':
            for i in self._command_dict:
                command = self._command_dict[i]
                print("'" + command.cmd_name + "' -> " + command.cmd_help_string)
        elif arguments[0] in self._command_dict:
            command = self._command_dict[arguments[0]]
            print("'" + command.cmd_name + "' -> " + command.cmd_detail_string)
        else:
            print("Command not recognized: '" + arguments[0] + "'")
            return -1
        return 0

    def cmd_board(self, arguments) -> int:
        """
        This function prints a visual representation of the board to the console.
        :return: 0 if successful
        """
        letters = "abcdefgh"
        final_row = ""
        for i in range(0, 8):
            row = self.game.get_board()[i]
            print_row = []
            for tile in row:
                if not tile.has_piece():
                    print_row.append("..")
                    #print_row.append(str(tile.get_coord()[0]) + str(tile.get_coord()[1]))
                else:
                    print_row.append(tile.get_piece().get_piece_string())
            print(str(8 - i) + " " + str(print_row))
            final_row = final_row + "     " + str(letters[i])
        print(final_row)
        return 0

    def cmd_move(self, arguments) -> int:
        """
        Attempts to move a piece from the first argument to the second argument.
        :param arguments: list containing selection and destination coords at index 0 and 1, respectively
        :return: 0 on success
        """
        # Check that the provided arguments are of valid notation
        if self.notation_to_coord(arguments[0]) == -1 or self.notation_to_coord(arguments[1]) == -1:
            print("Enter 'help move' for proper usage")
            return -1

        # Check that the first coord contains a piece to move
        piece_coord = self.notation_to_coord(arguments[0])
        piece = self.game.get_board()[piece_coord[0]][piece_coord[1]].get_piece()
        if piece is None:
            print("Tile '" + arguments[0] + "' does not contain a piece.")
            return -1

        # Check whether or not a piece will be captured, such that we can save it for use in the moves stack
        destination_coord = self.notation_to_coord(arguments[1])
        if self.game.get_board()[destination_coord[0]][destination_coord[1]].has_piece():
            destination_piece = self.game.get_board()[destination_coord[0]][destination_coord[1]].get_piece()
        else:
            destination_piece = None

        # Move the piece to the destination
        self.game.b.set_piece_coord(piece, destination_coord)

        # Display message
        print("Piece " + piece.get_piece_string() + " moved from " +
              self.ms_get_coord_to_notation(self.notation_to_coord(arguments[0])) + " to "
              + self.ms_get_coord_to_notation(self.notation_to_coord(arguments[1])))

        # Save the move to the moves stack
        self.game.moves_stack.append([piece_coord, destination_coord, destination_piece])
        return 0

    def notation_to_coord(self, notation) -> tuple:
        """
        This method takes a string of chess coordinate notation and returns its equivalent as a tuple. Returns -1
        on error.
        :param notation: Chess notation coordinate (e.g. 'a7')
        :return: Tuple coordinate, or -1 on failure
        """
        # Verify the length of the notation (must be 2)
        if len(notation) > 2:
            print("Error: Notation '" + notation + "' is invalid")
            return -1

        # Convert the first character letter to its equivalent number
        tuple_0 = None
        letters = "abcdefgh"
        for i in range(0, len(letters)):
            if letters[i] == notation[0]:
                tuple_0 = i
        if not notation[1].isnumeric():
            print("Error: Notation '" + notation + "' is invalid")
            return -1

        # Convert the second character to its coordinate equivalent
        tuple_1 = 8 - int(notation[1])

        # Verify that these new values are legitimate
        if tuple_0 is None or (tuple_1 < 0 or tuple_1 > 7):
            print("Error: Notation '" + notation + "' is invalid")
            return -1

        return int(tuple_1), int(tuple_0)

    def ms_get_coord_to_notation(self, coord) -> str:
        """
        This method utilizes a text-file based microservice to convert a coordinate to chessboard notation.
        :type coord: tuple
        :return:
        """
        # Parse the coordinate such that it is readable by the translator
        with open('Microservice/chess_move.txt', 'w') as outfile:
            outfile.write("(" + str(coord[0]) + "," + str(coord[1]) + ")")

        # Wait for the translator to process the coordinate
        time.sleep(0.3)

        # Read the file for the translated coordinate
        with open('Microservice/chess_move.txt', 'r') as infile:
            line = infile.readline()
            line = line.strip()
        return line

    def cmd_newgame(self, arguments) -> int:
        """
        Resets the board and starts a new game.
        :return: 0 if successful
        """
        user_confirm = input("Start a new game? Current game will not be saved. (y / n):\n>")
        if user_confirm == 'y':
            self.game = ChessGame()
            return 0
        elif user_confirm != 'n':
            print("Error: Input not recognized")
            return -1
        return 0

    def cmd_undo(self, arguments) -> int:
        """
        This method undoes the last move.
        :return: 0 if successful
        """
        if len(self.game.moves_stack) < 1:
            print("No moves to undo")
            return -1

        last_move = self.game.moves_stack.pop()
        last_move_select_coord = last_move[0]
        last_move_dest_coord = last_move[1]
        last_move_captured_piece = last_move[2]

        moved_piece = self.game.get_board()[last_move_dest_coord[0]][last_move_dest_coord[1]].get_piece()

        self.game.b.set_piece_coord(moved_piece, last_move_select_coord)
        if last_move_captured_piece is not None:
            self.game.b.set_piece_coord(last_move_captured_piece, last_move_dest_coord)

        print("'move " + self.ms_get_coord_to_notation(last_move_select_coord) + " " +
              self.ms_get_coord_to_notation(last_move_dest_coord) + "' undone")
        return 0

    def cmd_save(self, arguments) -> int:
        """
        Saves the current game via pickle dump to the file 'save_file'.
        :return: 0 on success
        """
        user_confirm = input("Save? Existing save file will be overwritten. (y / n):\n>")
        if user_confirm == 'n':
            return 0
        if user_confirm != 'y':
            print("Error: Input not recognized")
            return -1

        outfile = open('save_file', 'wb')
        pickle.dump(self.game, outfile)
        outfile.close()
        print("Save successful")
        return 0

    def cmd_load(self, arguments):
        """
        Loads the save file from the 'save_file' file using pickle and overwrites the ongoing game.
        :return: 0 on success
        """
        user_confirm = input("Load? Ongoing game will be overwritten. (y / n):\n>")
        if user_confirm == 'n':
            return 0
        if user_confirm != 'y':
            print("Error: Input not recognized")
            return -1

        infile = open('save_file', 'rb')
        game = pickle.load(infile)
        infile.close()

        self.game = game
        print("Load successful")
        return 0

    def cmd_exit(self, arguments):
        """
        Prompts the user to quit the program without saving, then exits the program with user confirmation.
        :return: str 'EXIT' to exit, 0 if user declines, -1 on unrecognized input
        """
        user_confirm = input("Exit? Current game will not be saved. (y / n):\n>")
        if user_confirm == 'y':
            return 'EXIT'
        elif user_confirm != 'n':
            print("Error: Input not recognized")
            return -1
        return 0


class GameDisplay():
    """
    This class handles the display of the game in the window using PyGame.
    """
    def __init__(self, board):
        """
        Initializes a GameDisplay object to handle the given board
        :type board: ChessBoard
        """
        self.chessboard = board
        self.tile_dict = self.draw_board_tiles()

    def draw_all(self):
        """
        Draws all elements to the window: Tiles and pieces
        :return:
        """
        self.draw_board_tiles()

        self.draw_pieces()

    def draw_board_tiles(self) -> dict:
        """
        Draws the tiles as Rects in the window.
        """
        tiles = {}
        board = self.chessboard.get_board()
        x_tile_offset = 0
        swap_colors = False
        for i in board:
            y_tile_offset = 0
            for j in i:
                tile = pg.Rect(x_tile_offset, y_tile_offset, TILE_SIZE, TILE_SIZE)
                tiles[j.get_coord()] = tile
                if swap_colors:
                    pg.draw.rect(WIN, TILE_COLOR_1, tile)
                else:
                    pg.draw.rect(WIN, TILE_COLOR_2, tile)

                y_tile_offset += TILE_SIZE
                swap_colors = not swap_colors
            swap_colors = not swap_colors
            x_tile_offset += TILE_SIZE
        return tiles

    def draw_pieces(self) -> None:
        """
        This method draws the pieces onto the tiles.
        :return:
        """
        board = self.chessboard.get_board()
        for i in board:
            for j in i:
                if j.has_piece():
                    piece_type = j.get_piece().get_type()
                    piece_team = j.get_piece().get_team()
                    if piece_type == 'P':
                        if piece_team == 1:
                            img = wP_img
                        else:
                            img = bP_img
                    elif piece_type == 'R':
                        if piece_team == 1:
                            img = wR_img
                        else:
                            img = bR_img
                    elif piece_type == 'N':
                        if piece_team == 1:
                            img = wN_img
                        else:
                            img = bN_img
                    elif piece_type == 'B':
                        if piece_team == 1:
                            img = wB_img
                        else:
                            img = bB_img
                    elif piece_type == 'Q':
                        if piece_team == 1:
                            img = wQ_img
                        else:
                            img = bQ_img
                    elif piece_type == 'K':
                        if piece_team == 1:
                            img = wK_img
                        else:
                            img = bK_img

                    coord = j.get_coord()
                    x_offset = (TILE_SIZE * coord[1]) + 10
                    y_offset = (TILE_SIZE * coord[0]) + 10
                    WIN.blit(img, (x_offset, y_offset))


if __name__ == "__main__":
    c = ChessGame()
    gd = GameDisplay(c.b)
    console = ChessConsole(c)
    run = True
    while run:
        pg.event.pump()
        gd.draw_all()
        pg.display.update()
        if console.get_input(True) == "EXIT":
            run = False

