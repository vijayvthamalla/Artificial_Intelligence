import sys
import time
from MaxConnect4Game import *

def oneMoveGame(currentGame, depth):
    if currentGame.pieceCount == 42:  
        print ('BOARD FULL\n\nGame Over!\n')
        sys.exit(0)

    if depth == 0:
        print ('Give a depth greater than 0')
        sys.exit(0)

    currentGame.aiPlay(depth, currentGame.currentTurn)

    print ('Game state after move:')
    currentGame.printGameBoard()

    currentGame.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))

    if currentGame.currentTurn == 1:
        currentGame.currentTurn = 2
    elif currentGame.currentTurn == 2:
        currentGame.currentTurn = 1

    currentGame.printGameBoardToFile()
    currentGame.gameFile.close()


def interactiveGame(currentGame, depth, computer):
    if currentGame.pieceCount == 42:
        currentGame.countScore()
        if computer == 1:
            print('Score: Computer (Player 1) = %d, Human (Player 2) = %d\n' % (currentGame.player1Score, currentGame.player2Score))
            if currentGame.player1Score < currentGame.player2Score:
                print ("Congratulations, you WIN!")
            elif currentGame.player1Score > currentGame.player2Score:
                print ("Oops, you lost")
            else:
                print ("You were good. It is a draw")
        else:
            print('Score: Human (Player 1) = %d, Computer (Player 2) = %d\n' % (currentGame.player1Score, currentGame.player2Score))
            if currentGame.player1Score > currentGame.player2Score:
                print ("Congratulations, you WIN!")
            elif currentGame.player1Score < currentGame.player2Score:
                print ("Oops, you lost")
            else:
                print ("You were good. It is a draw")

        print ('BOARD FULL\n\nGame Over!\n')
        sys.exit(0)

    if depth == 0:
        print ('Give a depth greater than 0')
        sys.exit(0)

    if computer == currentGame.currentTurn:
        outFile = "computer.txt"
        currentGame.aiPlay(depth, computer)
        currentGame.printGameBoard()
        currentGame.countScore()
        if computer == 1:
            print('Score: Computer (Player 1) = %d, Human (Player 2) = %d\n' % (currentGame.player1Score, currentGame.player2Score))
        else:
            print('Score: Human (Player 1) = %d, Computer (Player 2) = %d\n' % (currentGame.player1Score, currentGame.player2Score))
    else:
        outFile = "human.txt"
        try: 
            column = int(input("What column do you want to play at(from 1 to 7): "))
            if type(column) == int:
                if column > 0 and column <= 7:
                    result = currentGame.playPiece(column - 1)
                    if not result:
                        print ("No moves on column "+ str(column) + ". Try Again")
                        interactiveGame(currentGame, depth, computer)
                    else:
                        if computer == 1:
                            print('Score: Computer (Player 1) = %d, Human (Player 2) = %d\n' % (currentGame.player1Score, currentGame.player2Score))
                        else:
                            print('Score: Human (Player 1) = %d, Computer (Player 2) = %d\n' % (currentGame.player1Score, currentGame.player2Score))
                else:
                    print ("Invalid Move. Try Again")
                    interactiveGame(currentGame, depth, computer)
        except:
            sys.exit('Aborting. Wrong input given. The current state of the program is saved in ' + outFile)
    try:
        currentGame.gameFile = open(outFile, 'w')
    except:
        sys.exit('Error opening output file.')

    currentGame.printGameBoardToFile()

    nextGame = maxConnect4Game()
    nextGame.gameBoard = copy.deepcopy(currentGame.gameBoard)
    nextGame.pieceCount = currentGame.pieceCount
    nextGame.evaluation = 0
    currentGame.gameFile.close()

    if currentGame.currentTurn == 1:
        nextGame.currentTurn = 2
        currentGame.currentTurn = 2
    else:
        nextGame.currentTurn = 1
        currentGame.currentTurn = 1

    interactiveGame(nextGame, depth, computer)

def main(argv):
    if len(argv) != 5:
        print ('Four command-line arguments are needed:')
        print('Usage: %s interactive [input_file] [computer-next/human-next] [depth]' % argv[0])
        print('or: %s one-move [input_file] [output_file] [depth]' % argv[0])
        sys.exit(2)

    game_mode, inFile = argv[1:3]

    if not game_mode == 'interactive' and not game_mode == 'one-move':
        print('%s is an unrecognized game mode' % game_mode)
        sys.exit(2)

    currentGame = maxConnect4Game()
    try:
        currentGame.gameFile = open(inFile, 'r')
    except IOError:
        sys.exit("\nError opening input file.\nCheck file name.\n")
    file_lines = currentGame.gameFile.readlines()
    currentGame.gameBoard = [[int(char) for char in line[0:7]] for line in file_lines[0:-1]]
    currentGame.currentTurn = int(file_lines[-1][0])
    currentGame.evaluation = 0
    currentGame.gameFile.close()

    print ('\nMaxConnect-4 game\n')
    print ('Game state before move:')
    currentGame.printGameBoard()
    currentGame.checkPieceCount()
    currentGame.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))

    if game_mode == 'interactive':
        if argv[3] == "computer-next":
            computer = currentGame.currentTurn
        elif argv[3] == "human-next":
            if currentGame.currentTurn == 1:
                computer = 2
            else:
                computer = 1
        interactiveGame(currentGame, int(argv[4]),computer)
    else:
        outFile = argv[3]
        try:
            currentGame.gameFile = open(outFile, 'w')
        except:
            sys.exit('Error opening output file.')
        oneMoveGame(currentGame, int(argv[4]))


if __name__ == '__main__':
    start_time = time.time()
    main(sys.argv)
    end_time = time.time()
    total_time = end_time-start_time
    print(f"Execution time: {total_time} seconds")