import time

if __name__ == "__main__":

    while True:
        time.sleep(1.0)

        with open('chess_move.txt', 'r') as f:
            try:
                line = f.readlines()[-1]
            except:
                line = f.readline()
                
        f.close()
        
        
        if line == "(0,0)":
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('a8')
            f.close()
        elif line == "(0,1)":
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('b8')
            f.close()
        elif line == "(0,2)":
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('c8')
            f.close()
        elif line == ('(0,3)'):
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('d8')
            f.close()
        elif line == ('(0,4)'):
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('e8')
            f.close()
        elif line == ("(0,5)"):
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('f8')
            f.close()
        elif line == ("(0,6)"):
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('g8')
            f.close()
        elif line == ('(0,7)'):
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('h8')
            f.close()
        elif line == "(1,0)":
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('a7')
            f.close()
        elif line == "(2,0)":
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('a6')
            f.close()
        elif line == "(3,0)":
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('a5')
            f.close()
        elif line == ('(4,0)'):
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('a4')
            f.close()
        elif line == ('(5,0)'):
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('a3')
            f.close()
        elif line == ("(6,0)"):
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('a2')
            f.close()
        elif line == ("(7,0)"):
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('a1')
            f.close()
        elif line == ('(1,1)'):
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('b7')
            f.close()
        elif line == "(1,2)":
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('c7')
            f.close()
        elif line == "(1,3)":
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('d7')
            f.close()
        elif line == "(1,4)":
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('e7')
            f.close()
        elif line == ('(1,5)'):
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('f7')
            f.close()
        elif line == ('(1,6)'):
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('g7')
            f.close()
        elif line == ("(1,7)"):
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('h7')
            f.close()
        elif line == ("(2,1)"):
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('b6')
            f.close()
        elif line == ('(2,2)'):
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('c6')
            f.close()
        elif line == "(2,3)":
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('d6')
            f.close()
        elif line == "(2,4)":
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('e6')
            f.close()
        elif line == "(2,5)":
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('f6')
            f.close()
        elif line == ('(2,6)'):
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('g6')
            f.close()
        elif line == ('(2,7)'):
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('h6')
            f.close()
        elif line == ("(3,1)"):
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('b5')
            f.close()
        elif line == ("(3,2)"):
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('c5')
            f.close()
        elif line == ('(3,3)'):
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('d5')
            f.close()
        elif line == "(3,4)":
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('e5')
            f.close()
        elif line == "(3,5)":
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('f5')
            f.close()
        elif line == ('(3,6)'):
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('g5')
            f.close()
        elif line == ('(3,7)'):
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('h5')
            f.close()
        elif line == ("(4,1)"):
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('b4')
            f.close()
        elif line == ("(4,2)"):
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('c4')
            f.close()
        elif line == ('(4,3)'):
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('d4')
            f.close()
        elif line == "(4,4)":
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('e4')
            f.close()
        elif line == "(4,5)":
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('f4')
            f.close()
        elif line == "(4,6)":
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('g4')
            f.close()
        elif line == ('(4,7)'):
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('h4')
            f.close()
        elif line == ('(5,1)'):
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('b3')
            f.close()
        elif line == ("(5,2)"):
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('c3')
            f.close()
        elif line == ("(5,3)"):
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('d3')
            f.close()
        elif line == ('(5,4)'):
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('e3')
            f.close()
        elif line == "(5,5)":
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('f3')
            f.close()
        elif line == "(5,6)":
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('g3')
            f.close()
        elif line == "(5,7)":
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('h3')
            f.close()
        elif line == ('(6,1)'):
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('b2')
            f.close()
        elif line == ('(6,2)'):
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('c2')
            f.close()
        elif line == ("(6,3)"):
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('d2')
            f.close()
        elif line == ("(6,4)"):
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('e2')
            f.close()
        elif line == ('(6,5)'):
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('f2')
            f.close()
        elif line == "(6,6)":
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('g2')
            f.close()
        elif line == "(6,7)":
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('h2')
            f.close()
        elif line == "(7,1)":
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('b1')
            f.close()
        elif line == ('(7,2)'):
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('c1')
            f.close()
        elif line == ('(7,3)'):
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('d1')
            f.close()
        elif line == ("(7,4)"):
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('e1')
            f.close()
        elif line == ("(7,5)"):
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('f1')
            f.close()
        elif line == ('(7,6)'):
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('g1')
            f.close()
        elif line == ('(7,7)'):
            f = open("chess_move.txt", "w")
            f.write("")
            f.write('h1')
            f.close()
        else:
            pass
        
        


