# import random
import logging
from prettytable import PrettyTable
from copy import deepcopy
from math import floor

def deckMaker():
    # 1 is an Ace
    # 11 is a Jack
    # 12 is a Queen
    # 13 is a King
    # This is a tuple, not a list.
    deck = ({'faceValue': 1, 'suit': 'Spades'},{'faceValue': 1, 'suit': 'Hearts'},{'faceValue': 1, 'suit': 'Clubs'},{'faceValue': 1, 'suit': 'Diamonds'},
            {'faceValue': 2, 'suit': 'Spades'},{'faceValue': 2, 'suit': 'Hearts'},{'faceValue': 2, 'suit': 'Clubs'},{'faceValue': 2, 'suit': 'Diamonds'},
            {'faceValue': 3, 'suit': 'Spades'},{'faceValue': 3, 'suit': 'Hearts'},{'faceValue': 3, 'suit': 'Clubs'},{'faceValue': 3, 'suit': 'Diamonds'},
            {'faceValue': 4, 'suit': 'Spades'},{'faceValue': 4, 'suit': 'Hearts'},{'faceValue': 4, 'suit': 'Clubs'},{'faceValue': 4, 'suit': 'Diamonds'},
            {'faceValue': 5, 'suit': 'Spades'},{'faceValue': 5, 'suit': 'Hearts'},{'faceValue': 5, 'suit': 'Clubs'},{'faceValue': 5, 'suit': 'Diamonds'},
            {'faceValue': 6, 'suit': 'Spades'},{'faceValue': 6, 'suit': 'Hearts'},{'faceValue': 6, 'suit': 'Clubs'},{'faceValue': 6, 'suit': 'Diamonds'},
            {'faceValue': 7, 'suit': 'Spades'},{'faceValue': 7, 'suit': 'Hearts'},{'faceValue': 7, 'suit': 'Clubs'},{'faceValue': 7, 'suit': 'Diamonds'},
            {'faceValue': 8, 'suit': 'Spades'},{'faceValue': 8, 'suit': 'Hearts'},{'faceValue': 8, 'suit': 'Clubs'},{'faceValue': 8, 'suit': 'Diamonds'},
            {'faceValue': 9, 'suit': 'Spades'},{'faceValue': 9, 'suit': 'Hearts'},{'faceValue': 9, 'suit': 'Clubs'},{'faceValue': 9, 'suit': 'Diamonds'},
            {'faceValue': 10, 'suit': 'Spades'},{'faceValue': 10, 'suit': 'Hearts'},{'faceValue': 10, 'suit': 'Clubs'},{'faceValue': 10, 'suit': 'Diamonds'},
            {'faceValue': 11, 'suit': 'Spades'},{'faceValue': 11, 'suit': 'Hearts'},{'faceValue': 11, 'suit': 'Clubs'},{'faceValue': 11, 'suit': 'Diamonds'},
            {'faceValue': 12, 'suit': 'Spades'},{'faceValue': 12, 'suit': 'Hearts'},{'faceValue': 12, 'suit': 'Clubs'},{'faceValue': 12, 'suit': 'Diamonds'},
            {'faceValue': 13, 'suit': 'Spades'},{'faceValue': 13, 'suit': 'Hearts'},{'faceValue': 13, 'suit': 'Clubs'},{'faceValue': 13, 'suit': 'Diamonds'}        
    )
    return deck


def testStackTableaus():
    # This is an ordered tuple, not a list.
    tableaus = ([ 
                    {'faceValue': 13, 'suit': 'Diamonds'},{'faceValue': 12, 'suit': 'Clubs'},
                    {'faceValue': 11, 'suit': 'Diamonds'},{'faceValue': 10, 'suit': 'Clubs'},
                    {'faceValue': 9, 'suit': 'Hearts'},{'faceValue': 8, 'suit': 'Clubs'},
                    {'faceValue': 7, 'suit': 'Hearts'},{'faceValue': 6, 'suit': 'Spades'},
                    {'faceValue': 5, 'suit': 'Diamonds'},{'faceValue': 4, 'suit': 'Clubs'},
                    {'faceValue': 3, 'suit': 'Diamonds'},{'faceValue': 2, 'suit': 'Spades'},
                    {'faceValue': 1, 'suit': 'Diamonds'}
                ],
               [ {'faceValue': 2, 'suit': 'Spades'} ],
               [    
                    {'faceValue': 6, 'suit': 'Diamonds'},{'faceValue': 5, 'suit': 'Spades'},
                    {'faceValue': 4, 'suit': 'Hearts'},{'faceValue': 3, 'suit': 'Spades'} 
                    ],
               [ ],
               [ {'faceValue': 6, 'suit': 'Hearts'},{'faceValue': 5, 'suit': 'Spades'},{'faceValue': 7, 'suit': 'Hearts'} ],
               [ {'faceValue': 9, 'suit': 'Hearts'},{'faceValue': 8, 'suit': 'Hearts'} ],
               [ {'faceValue': 11, 'suit': 'Hearts'},{'faceValue': 10, 'suit': 'Diamonds'},{'faceValue': 9, 'suit': 'Clubs'},{'faceValue': 8, 'suit': 'Clubs'} ],
               [ {'faceValue': 11, 'suit': 'Hearts'},{'faceValue': 10, 'suit': 'Diamonds'},{'faceValue': 9, 'suit': 'Clubs'} ] 
    )
    return tableaus

def testDiscardTableaus():
    # This is an ordered tuple, not a list.
    tableaus = ([ ],
               [ 
                   {'faceValue': 13, 'suit': 'Diamonds'},{'faceValue': 12, 'suit': 'Diamonds'},
                    {'faceValue': 11, 'suit': 'Diamonds'},{'faceValue': 10, 'suit': 'Diamonds'},
                    {'faceValue': 9, 'suit': 'Diamonds'},{'faceValue': 8, 'suit': 'Diamonds'},
                    {'faceValue': 7, 'suit': 'Diamonds'},{'faceValue': 6, 'suit': 'Diamonds'},
                    {'faceValue': 5, 'suit': 'Diamonds'},{'faceValue': 4, 'suit': 'Diamonds'},
                    {'faceValue': 3, 'suit': 'Diamonds'},{'faceValue': 2, 'suit': 'Diamonds'},
                    {'faceValue': 1, 'suit': 'Diamonds'}
                 ],
               [    
                    {'faceValue': 5, 'suit': 'Spades'},{'faceValue': 1, 'suit': 'Spades'},
                    ],
               [  ],
               [ {'faceValue': 2, 'suit': 'Hearts'} ],
               [ {'faceValue': 3, 'suit': 'Spades'},{'faceValue': 2, 'suit': 'Spades'} ],
               [ {'faceValue': 11, 'suit': 'Hearts'},{'faceValue': 10, 'suit': 'Diamonds'},{'faceValue': 9, 'suit': 'Clubs'},{'faceValue': 8, 'suit': 'Clubs'} ],
               [ {'faceValue': 1, 'suit': 'Clubs'},{'faceValue': 1, 'suit': 'Hearts'} ] 
    )
    return tableaus

# I wanted to get every possible permutation of a deck.
# not used due to MemoryError with a 52 card deck, lol
# https://stackoverflow.com/questions/464864/get-all-possible-2n-combinations-of-a-list-s-elements-of-any-length
def comboSequence(deck):
        if len(deck) == 0:
             return [[]]
        sequence = []
        for combo in comboSequence(deck[1:]):
             sequence += [combo, combo + [deck[0]]]
        return sequence


# I wanted to get every possible permutation of a deck.
# not used due to MemoryError with a 52 card deck, lol

# all possible permutations without analags number 1.75x10^64
# UTF Char	4	bytes
# 1 permuation of a deck	945	chars
# 1 permutaiton of a deck	3780	bytes
# number of distict deals without analogs	1.75E+64	
# Size of all permutations on disk	6.615E+67	bytes
# Size of all permutations on disk	6.615E+55	Terabytes
#  from itertools import permutations
def deckPermutations(deck):
    permutationObject = permutations(deck)        # all possible orderings, no repeated elements
    hand = tuple(permutationObject)
    return(hand)


def dealCards(deck):
    foundations = [None,None,None,None]
    cells = [None,None,None,None]  
    tableaus = ([ deck[0],deck[8],deck[16],deck[24],deck[32],deck[40],deck[48] ],        # This is an ordered tuple, not a list.
               [ deck[1],deck[9],deck[17],deck[25],deck[33],deck[41],deck[49] ],        # empty tableaus should be an empty list []
               [ deck[2],deck[10],deck[18],deck[26],deck[34],deck[42],deck[50] ],
               [ deck[3],deck[11],deck[19],deck[27],deck[35],deck[43],deck[51] ],
               [ deck[4],deck[12],deck[20],deck[28],deck[36],deck[44] ],
               [ deck[5],deck[13],deck[21],deck[29],deck[37],deck[45] ],
               [ deck[6],deck[14],deck[22],deck[30],deck[38],deck[46] ],
               [ deck[7],deck[15],deck[23],deck[31],deck[39],deck[47] ] 
    )
    gameState = {'tableaus': tableaus,'cells': cells,'foundations': foundations}
    return gameState


def strCard(card):                # convert a card object to an easily printable string
    suit = ''
    if card == None: 
        return 'None'
    elif card == []:
        return '[]'
    elif card == ():
        return '()'
    
    elif card['suit'] == 'Spades':
        suit = '♠'
    elif card['suit'] == 'Hearts':
        suit = '♥'
    elif card['suit'] == 'Clubs':
        suit = '♣'
    elif card['suit'] == 'Diamonds':
        suit = '♦'
    else:
        logging.ERROR('printCard(card) Suite not found.')
    
    value = ''
    if card['faceValue'] == 1:
        value = 'A'
    elif card['faceValue'] == 11:
        value = 'J'
    elif card['faceValue'] == 12:
        value = 'Q'
    elif card['faceValue'] == 13:
        value = 'K'
    else:
        value = str(card['faceValue'])
    
    return (value + suit)

def printTableau(tableauInput):        
    tableau = deepcopy(tableauInput)    # Print tableau needs a seperate object so it can reformat it.
    maxCascadeLength = 0
    for cascade in tableau:
         if len(cascade) > maxCascadeLength:
              maxCascadeLength = len(cascade)

    col = 0
    for cascade in tableau:
        row = 0
        for card in cascade:
            tableau[col][row] = strCard(card)
            row = row + 1
        col = col + 1    

    table = PrettyTable()
    cascadeIter = 0
    for cascade in tableau: 
        if len(cascade) < maxCascadeLength:     # in order to print in a table, I have to add spaces so each cascade list is the same length.
            missingLength = maxCascadeLength - len(cascade)
            for j in range(missingLength):
                cascade.append(' ')
        table.add_column(str(cascadeIter),cascade)
        cascadeIter = cascadeIter + 1
    
    print(table)


def printGameState(gameState):
    foundations = gameState['foundations']
    cells = gameState['cells']
    print("Foundations:",strCard(foundations[0]),strCard(foundations[1]),strCard(foundations[2]),strCard(foundations[3]))
    print("Cells:",strCard(cells[0]),strCard(cells[1]),strCard(cells[2]),strCard(cells[3]))
    printTableau(gameState['tableaus'])


def isOppositeColor(baseCardSuit,movedCardSuit):
    if baseCardSuit == 'Clubs' or baseCardSuit == 'Spades':
        # logging.debug("Black Base")
        if movedCardSuit == 'Clubs' or movedCardSuit == 'Spades':
            # logging.debug("Black movedCardSuit")
            return False
        elif movedCardSuit == 'Hearts' or movedCardSuit == 'Diamonds':
            # logging.debug("Red movedCardSuit")
            return True
        else:
            logging.error("Error: invalid movedCardSuit for isOppositeColor().")
            return False

    elif baseCardSuit == 'Hearts' or baseCardSuit == 'Diamonds':
        # logging.debug("Red Base")
        if movedCardSuit == 'Hearts' or movedCardSuit == 'Diamonds':
            # logging.debug("Red movedCardSuit")
            return False
        elif movedCardSuit == 'Clubs' or movedCardSuit == 'Spades':
            # logging.debug("black movedCardSuit")
            return True
        else:
            logging.error("Error: invalid movedCardSuit for isOppositeColor().")
            return False

    else:
        logging.error("Error: invalid faceCardSuit for isOppositeColor().")
        return False


def isFaceOneHigher(higherCard,lowerCard):
    # logging.debug("isFaceOneHigher(" + str(baseCardFace) + "," + str(movedCardFace))
    if (higherCard - 1) == lowerCard:
        # logging.debug("isFaceOneHigher(" + str(higherCard) + "," + str(lowerCard) + "," + "True)")
        return True
    else:
        # logging.debug("isFaceOneHigher() False")
        return False


def canStack(baseCardObj,movedCardObj):
    baseCardFace = int(baseCardObj['faceValue'])
    baseCardSuit = baseCardObj['suit']
    movedCardFace = int(movedCardObj['faceValue'])
    movedCardSuit = movedCardObj['suit']
    
    if isOppositeColor(baseCardSuit,movedCardSuit):
        # logging.debug(strCard(baseCardObj) +" " + strCard(movedCardObj) + " isOppositeColor()-> True")
        result = isFaceOneHigher(baseCardFace,movedCardFace) 
        return result
    else:
        return False

def testCanStack(deck):
    print('## testCanStack(deck) ##')
    baseCard = deck[0]
    movedCard = deck[0]
    for baseCard in deck:
        for movedCard in deck:       
            if canStack(baseCard,movedCard):
                print(strCard(baseCard),strCard(movedCard),str(canStack(baseCard,movedCard)))


def maxStackMoveOccupied(freeCells,freeFoundations):    # max number of stacked cards you can move onto another stack.
    return (2 ** freeFoundations * (freeCells + 1))
    

def maxStackMoveEmpty(freeCells,freeFoundations):    # max number of stacked cards you can move into an empty tableau.
    return (int(floor(maxStackMoveOccupied(freeCells,freeFoundations) / 2)))


def countFreecells():
    return


def countFreeFoundations():
    return


def countMoveableStackSize():
    return


def testMaxStacks():
    print('## testMaxStacks() ##')
    fcs = [0,1,2,3,4]
    ffs = [0,1,2,3,4]
    print("freeCells","freeFoundations","maxStackMoveOccupied","maxStackMoveEmpty")
    for fc in fcs:
        for ff in ffs:
            print(fc,ff,maxStackMoveOccupied(fc,ff),maxStackMoveEmpty(fc,ff))

def isFaceOneLower(lesserCardFace,greaterCardFace):
        if lesserCardFace + 1 == greaterCardFace:
            return True
        else:
            return False    


def isCardTop(tableau,row):
    if len(tableau) - 1 == row:
        return True
    elif tableau == [] or tableau == None: 
        return False
    else:        
        return False


def testIsCardTop(tableaus):
    print("## testIsCardTop(tableaus) ##")
    print("card","row","isCardTop")
    count = 0
    for tableau in tableaus:
        row = 0
        for card in tableau:
            result = isCardTop(tableau,row)
            print(strCard(card),row,result)
            row = row + 1
            if result:
                count = count + 1
    correctCount = 7
    print("Count:",count)
    return


def canDiscard(foundation,card):
    if foundation == None and card['faceValue'] == 1:
        return True        
    elif foundation == None:
        return False
    elif foundation['suit'] == card['suit']:
        # logging.debug("same suite: " + strCard(foundation) + ", " + strCard(card))
        return isFaceOneLower(foundation['faceValue'],card['faceValue'])
    else:
        return False


def testCanDiscard(deck):
    print('## testCanDiscard(deck) ##')
    foundations = [None,{'faceValue': 1, 'suit': 'Spades'},{'faceValue': 2, 'suit': 'Spades'},{'faceValue': 3, 'suit': 'Spades'}]
    card = {'faceValue': 1, 'suit': 'Spades'}
    result = True
    for foundation in deck:
        for card in deck:
            result = canDiscard(foundation,card)
            if result:
                print(strCard(foundation),strCard(card),result)

    foundation = None
    for card in deck:
        result = canDiscard(foundation,card)
        if result:
            print(strCard(foundation),strCard(card),result)


def isCardStacked(bottomCard,topCard):     # Is the pile of cards a moveable stack?
    if isOppositeColor(bottomCard['suit'],topCard['suit']):
        # logging.debug(strCard(bottomCard) + " "  + strCard(topCard) + "  isOppositeColor()")
        return isFaceOneHigher(bottomCard['faceValue'],topCard['faceValue'])
    return False


def testIsStacked(deck):
    print('## testIsStacked(deck) ##')
    count = 0
    result = True
    for bottomCard in deck:
        for topCard in deck:
            result = isCardStacked(bottomCard,topCard)
            if result:
                print(strCard(bottomCard),strCard(topCard),result)
                count = count + 1

    print("totalCount:",count)  # 96
    correctCount = 96
    if count == correctCount:
        return True


def isTableauStacked(tableau):        # check if top two cards are stacked
    if len(tableau) >= 2:
        # logging.debug(strCard(tableau[-2]) + " "  + strCard(tableau[-1]))
        return isCardStacked(tableau[-2],tableau[-1])
    else:
        return False


def tableauStackDepth(tableau):        # returns from 1 to 12. a stack depth of 1 is a single card.
    i = -1
    depth = 1
    while i > -1*len(tableau):          # iterate over tableau list backwards
        isOppositeColorBool = isOppositeColor(tableau[i-1]['suit'],tableau[i]['suit'])
        isFaceOneHigherBool = isFaceOneHigher(tableau[i-1]['faceValue'],tableau[i]['faceValue'])
        # logging.debug(strCard(tableau[i-1]) + " " + strCard(tableau[i]) + " " + str(i) + " " + str(depth) + " " + str(isOppositeColorBool) + " " + str(isFaceOneHigherBool))
        if isOppositeColorBool and isFaceOneHigherBool:
            depth = depth + 1
        else: 
            break
        i = i - 1
    return depth


def testTableauStacks(tableaus):
    countIsStacked = 0
    for tableau in tableaus:
        result = isTableauStacked(tableau)
        depth = tableauStackDepth(tableau)
        print(tableau,result,depth)
        if result:
            countIsStacked = countIsStacked + 1
    correctCountIsStacked = 3

    if countIsStacked == correctCountIsStacked:
        return True


def isStackMovable(tableau,row):
    if len(tableau) - 1 == row:
        return True
    elif tableau == [] or tableau == None: 
        return False
    elif isTableauStacked(tableau):
        depth = tableauStackDepth(tableau)
        if len(tableau) - row - 1 < depth:
            return True
        else:
            return False
    else:        
        return False


def testIsStackMovable(tableaus):
    print("## testIsCardMovable(tableaus) ##")
    print("card","row","isCardMovable")
    for tableau in tableaus:
        row = 0
        for card in tableau:
            result = isStackMovable(tableau,row)
            print(strCard(card),row,result)
            row = row + 1
    return


def canPlaceCard(bottomCard,topCard):
    if topCard is None:
        logging.ERROR("canPlaceCard() invalid topCard: None")
        return False
    if bottomCard is None: 
        return True
    else:
        return(isCardStacked(bottomCard,topCard))


def testCanPlaceCard(deck):
    print('## testCanPlaceCard(deck) ##')
    count = 0
    for bottomCard in deck:
        for topCard in deck:
            result = canPlaceCard(bottomCard,topCard)
            if result:
                print(strCard(bottomCard),strCard(topCard),result)
                count = count + 1

    bottomCard = None
    for topCard in deck:
        result = canPlaceCard(bottomCard,topCard)
        if result:
            print(strCard(bottomCard),strCard(topCard),result)
            count = count + 1

    print("totalCount:",count)
    correctCount = 148
    if count == correctCount:
        return True


def doDiscard(gameState,col,row):
    card = gameState['tableaus'][col][row]
    tableau = gameState['tableaus'][col]
    changed = False
    # print(card)
    i = 0
    for foundation in gameState['foundations']:
        isCardTopBool = isCardTop(tableau,row)
        canDiscardBool = canDiscard(foundation,card)
        if isCardTopBool and canDiscardBool:
            logging.debug(strCard(foundation) + " " + strCard(card) + " doDiscard( "+ str(col) + ", " + str(row) + ")" )
            gameState['foundations'][i] = tableau[row]
            tableau.remove(card)
            gameState['changed'] = True
            return gameState
        i = i + 1
    return gameState


def testDoDiscard(gameState):
    tableaus = testDiscardTableaus()
    gameState['tableaus'] = tableaus

    col = len(tableaus) - 1 
    while col >= 0:
        row = len(tableaus[col]) - 1
        while row >= 0:
            gameState['changed'] = False
            gameState = doDiscard(gameState,col,row)
            if gameState['changed']:
                printGameState(gameState)   
            row = row - 1
        col = col - 1
    return 


def doMoveStack():
    return


def isGameWon():
    return


def isGameOver():
    return


def play():
    # every cycle first check if you can move the aces or 2's over.
    # Create an API, so an AI can try to access the card game.
    return


def unitTests(gameState):
    deck = deckMaker()
    # testCanStack(deck)
    # testMaxStacks()
    # testCanDiscard(deck)
    # testIsStacked(deck)
    # testCanPlaceCard(deck)

    tableaus = testStackTableaus()
    gameState['tableaus'] = tableaus
    # printTableaus = deepcopy(tableaus)           
    printGameState(gameState)
    # testTableauStacks(tableaus)
    # testIsCardMovable(tableaus)
    # testDoDiscard(gameState)
    # testIsCardTop(tableaus)


    testDoDiscard(gameState)
    # printGameState(gameState)
    return


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    deck = [{}]
    deck = list(deckMaker())
    # random.shuffle(deck)
    gameState = dealCards(deck)
    unitTests(gameState)

