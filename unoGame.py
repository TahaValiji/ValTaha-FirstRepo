import random
import time

NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
COLOURS = ["Red", "Blue", "Green", "Yellow"]
WILDS = ["Wild", "Wild Draw Four"]
REMAINING_CARDS= ["Draw Two", "Reverse", "Skip"]
PLAYERWON = []

def buildDeck():
    """
    Builds the deck of cards for the game of Uno.

    Returns:
        list: A list of all the cards in the deck.
    """
    deck = []
    values = [*NUMBERS, *REMAINING_CARDS]
    for colour in COLOURS:
        for value in values:
            cardval = f"{colour} {value}"
            deck.append(cardval)
            if value != "0":
                deck.append(cardval)
    for _ in range(4):
        deck.append(WILDS[0])
        deck.append(WILDS[1])
    return deck

def shuffleDeck():
    """
    Shuffles the deck of Uno cards.

    Returns:
        list: A shuffled list of all the cards in the deck.
    """
    deck = buildDeck()
    random.shuffle(deck)
    return deck

def getPlayer():
    """
    Asks the user how many players are playing the game and returns that number.

    Returns:
        int: The number of players playing the game.
    """
    while True:
        TotalPlayer = input("Enter the number of players: ")
        if TotalPlayer.isdigit():
            TotalPlayer = int(TotalPlayer)
            if TotalPlayer > 1:
                break
            else:
                print("Number of players must be greater than 1.")
        else:
            print("Please Enter a number.")
    return TotalPlayer

def No_cards():
    """
    Asks the user how many cards each player will have and returns that number.

    Returns:
        int: The number of cards each player will have.
    """
    while True:
        TotalCards = input("Enter the number of cards: ")
        if TotalCards.isdigit():
            TotalCards = int(TotalCards)
            if TotalCards > 1:
                break
            else:
                print("Number of cards must be greater than 1.")
        else:
            print("Please Enter a number.")
    return TotalCards

def checkavailableCards():
    """
    Checks if the number of cards and players given are valid and can make a game of Uno.
    
    If the number of cards given multiplied by the number of players given exceeds 108,
    the function will call itself to ask for new input until valid input is given.
    
    Returns:
        tuple: A tuple containing the number of players and the number of cards each player has.
    """
    TotalCards = No_cards()
    TotalPlayer = getPlayer()
    check = TotalCards * TotalPlayer
    if check > 108:
        print("Number of cards is more than 108.")
        checkavailableCards()
    return TotalPlayer, TotalCards

def spreadCards():
    """
    Spreads the shuffled deck of cards among the players.

    Returns:
        tuple: A tuple containing the list of lists of cards each player has, the remaining deck of cards, and the order of play.
    """
    deck = shuffleDeck()
    TotalPlayer, TotalCards = checkavailableCards()
    playerTurn = []
    playerCards = []
    for i in list(range(TotalPlayer)):
        player = []
        playerTurn.append(i)
        for _ in list(range(TotalCards)):
            cardOut = deck.pop(0)
            player.append(cardOut)
        playerCards.append(player)
    return playerCards, deck, playerTurn

def drawCards(deck: list, numCards: int, discards: list, amt: int):
    """
    Draws a specified number of cards from the deck and returns them as a list.

    If the number of cards in the deck is less than the number of cards to draw,
    the function will update the deck by shuffling in the discard pile and then
    draw the cards from the updated deck.

    Args:
        deck (list): The list of cards in the deck.
        numCards (int): The number of cards to draw.
        discards (list): The list of discarded cards.
        amt (int): The number of cards in the deck.

    Returns:
        tuple: A tuple containing the list of drawn cards and the updated discard pile.
    """
    
    if len(deck) == 0 or len(deck) < amt:
        lastCard = discards[-1]
        deck.extend(discards[:-1])
        discards = [lastCard]
        random.shuffle(deck)
        print("The deck is reshuffled.")
        time.sleep(0.5)
        print("The deck is updated.\n")

    cardsDrawn = []
    for _ in range(numCards):
        card = deck.pop(0)
        cardsDrawn.append(card)
    return cardsDrawn, discards

def seperatePlayerCards(playerCards: list):
    """
    Separates the player cards into a dictionary with player names as keys
    and a list of their cards as values.

    Args:
        playerCards (list): The list of lists of cards each player has.

    Returns:
        tuple: A tuple containing the dictionary of player cards and the list of player names.
    """
    playerNumber = []
    playerDict = {}

    for i in range(len(playerCards)):
        name = input(f"Enter Name no.{i+1}: ").lower().title()
        playerNumber.append(name)

    playerDict = dict(zip(playerNumber, playerCards))
    return playerDict, playerNumber

def firstCard(deck: list):
    """
    Pops the first card from the deck and checks if it is a special card.
    If it is, it is put back in the deck and the process is repeated until
    a non-special card is drawn.

    Args:
        deck (list): The list of cards in the deck.

    Returns:
        tuple: A tuple containing the first card drawn from the deck and the updated deck.
    """
    while True:
        FirstCard = deck.pop(0)
        notAllowedCards = ["Draw Two", "Reverse", "Skip", "Wild"]
        for i in notAllowedCards:
            if i in FirstCard:
                deck.append(FirstCard)
                break
        else:
            break
    return FirstCard, deck

def firstPlay(FirstCard: str):
    """
    Returns the colour and value of the first card drawn from the deck.
    
    Args:
        FirstCard (str): The first card drawn from the deck.
    
    Returns:
        tuple: A tuple containing the colour and value of the first card drawn.
    """
    Firstcard = FirstCard.split(" ")
    currentColour = Firstcard[0]
    cardval = Firstcard[1]
    return currentColour, cardval

def showHand(player: str, playerHand: list):
    """
    Prints out the cards in the player's hand with their respective numbers.

    Args:
        player (str): The name of the player.
        playerHand (list): The list of cards in the player's hand.
    """
    time.sleep(0.5)
    print(f"==> {player}'s Turn.")
    print("------------------")
    for i, card in enumerate(playerHand):
        print(f"{i+1}) {card}")
    print("------------------")

def canplay(player: list, colour: str, value: str):
    """
    Checks if a player can play a card based on the given colour and value.

    If the player has only one card left, the function checks if the card is a special card.
    If the card is a special card, the function will return False, indicating that the player
    cannot play the card. If the card is not a special card, the function will check if the
    card matches the given colour or value. If the card matches, the function will return True,
    indicating that the player can play the card. If the card does not match, the function will
    return False.

    If the player has more than one card left, the function will check if any of the cards match
    the given colour or value. If a card matches, the function will return True, indicating that
    the player can play the card. If no cards match, the function will return False.

    Args:
        player (list): The list of cards in the player's hand.
        colour (str): The colour of the card to check.
        value (str): The value of the card to check.

    Returns:
        bool: True if the player can play a card, False otherwise.
    """
    if len(player) == 1:        # Checking for UNO situation.
        for card in player:
            if "Wild" in card:
                return False
            elif "Reverse" in card:
                return False
            elif "Skip" in card:
                return False
            elif "Draw Two" in card:
                return False
            else:
                if colour in card or value in card:
                    return True
                return False
    elif len(player) > 1:
        for card in player:
            if "Wild" in card:
                return True
            elif colour in card or value in card:
                return True
        return False

def canplay2(player: list, colour: str, cardval: str):
    """
    Checks if a player can play a card based on the given colour and value.

    If the player has a Wild card, the function will return True, indicating that
    the player can play the card.

    If the player has a Reverse, Skip, or Draw Two card and the colour matches the
    given colour, the function will return True, indicating that the player can play
    the card.

    If the player has a card that matches the given colour or value, the function
    will return True, indicating that the player can play the card. If the player
    does not have a matching card, the function will return False.

    Args:
        player (list): The list of cards in the player's hand.
        colour (str): The colour of the card to check.
        value (str): The value of the card to check.

    Returns:
        bool: True if the player can play a card, False otherwise.
    """
    if "Wild" in player:
        return True
    if (("Reverse" in player) or ("Skip" in player) or ("Draw Two" in player)) and (colour in player):
        return True
    if colour in player or cardval in player:
        return True
    return False

def checkColour(player: list, colour: str, value: str):
    """
    Asks the player which card they want to play and checks if the chosen card is valid.

    The function will ask the player to enter a number corresponding to the card they want to play.
    The function will then check if the chosen card is valid by calling the canplay2 function.
    If the chosen card is not valid, the function will print an error message and continue to ask the player to enter a number.
    If the chosen card is valid, the function will return the colour of the chosen card and the chosen card's index.

    Args:
        player (list): The list of cards in the player's hand.
        colour (str): The colour of the card to check.
        value (str): The value of the card to check.

    Returns:
        tuple: A tuple containing the colour of the chosen card and the chosen card's index.
    """
    while True:
        cardChosen = input("Which card do you want to play? ")
        if cardChosen.isdigit():
            cardChosen = int(cardChosen)
            if 1 <= cardChosen <= len(player):
                if not canplay2(player[cardChosen-1], colour, value):
                    print(f"Not a valid card.\nYour card should have colour: {colour} or value: {value}")
                    continue
                break
            else:
                print(f"Invalid option. Please enter a number between (1-{len(player)})")

    if "Wild" not in player[int(cardChosen)-1]:
        cardInfo = player[int(cardChosen) - 1].split(" ")
        for card in player:
            if cardInfo[0] in card:
                return cardInfo[0], cardChosen
            elif cardInfo[1] in card:
                return cardInfo[0], cardChosen
            
    return colour, cardChosen
    
def checkWin(playerNumber: list, playerCards: list, playerDict: dict, playerTurn: list, turn: int):
    """
    Checks if a player has won the game and updates the game state accordingly.

    This function is called when a player has only one card left in their hand.
    The function will remove the player from the game, append the player's name to the PLAYERWON list,
    and update the playerTurn list.

    Args:
        playerNumber (list): The list of player names.
        playerCards (list): The list of lists of cards each player has.
        playerDict (dict): The dictionary of player cards.
        playerTurn (list): The list of player turns.
        turn (int): The current turn.

    Returns:
        tuple: A tuple containing the updated PLAYERWON list, playerNumber list, playerCards list, playerDict dictionary, playerTurn list, and turn.
    """
    turn = playerTurn[turn]
    del playerDict[playerNumber[turn]]
    playerCards.pop(turn)
    name =  playerNumber.pop(turn)
    PLAYERWON.append(name)

    if playerTurn[0] == 0:
        playerTurn = []
        for i in range(len(playerCards)):
            playerTurn.append(i)
    elif playerTurn[0] != 0:
        playerTurn = []
        for i in sorted(range(len(playerCards)), reverse=True):
            playerTurn.append(i)

    turn-=1
    print(f"\n{name} has finished at position {len(PLAYERWON)}\n")
    return PLAYERWON, playerNumber, playerCards, playerDict, playerTurn, turn

def main():
    """
    The main function is the entry point of the Uno game.

    It is responsible for shuffling the deck, spreading the cards among the players, and
    starting the game loop. The game loop will continue until only one player has cards
    left in their hand.

    Args:
        None

    Returns:
        None
    """
    originalDeck = shuffleDeck()
    playerCards, shuffled_deck, playerTurn = spreadCards()
    playerDict, playerNumber = seperatePlayerCards(playerCards)
    FirstCard, deck = firstCard(shuffled_deck)

    # Start The Game
    discards = [FirstCard]
    playing = True
    currentColour, cardval = firstPlay(FirstCard)
    turn = 0

    # Game loop
    while playing:
        print(f"Card on top of pile: {discards[-1]}")
        showHand(playerNumber[playerTurn[turn]], playerCards[playerTurn[turn]])

        # Check if only one player is left
        if len(playerTurn) == 1:
            PLAYERWON, playerNumber, playerCards, playerDict, playerTurn, turn = checkWin(playerNumber, playerCards, playerDict, playerTurn, turn)
            playing = False

        # Check if player can play
        elif canplay(playerCards[playerTurn[turn]], currentColour, cardval):

            # Check if colour is changed or not.
            currentColour, cardChosen = checkColour(playerCards[playerTurn[turn]], currentColour, cardval)
            discards.append(playerCards[playerTurn[turn]].pop(cardChosen - 1))

            # Check for only 1 card left condition(UNO)
            if len(playerCards[playerTurn[turn]]) == 1:
                print('\n"UNO"\n')

            print(f"Current Colour: {currentColour}")                 

            # Check for special cards
            if discards[-1] == "Wild Draw Four":
                cardType = "Wild Draw Four"
                cardval = "Any"
            elif "Draw Two" in discards[-1]:
                cardType = "Draw Two"
                cardval = "Draw Two"
            elif "Wild" in discards[-1]:
                cardType = "Wild"
                cardval = "Any"
            else:
                splitCard = discards[-1].split(" ")
                cardType = splitCard[1]
                cardval = cardType

            if cardType == "Wild":
                ask = input("Do you want to change colour? (y/n): ").lower()
                if ask == "y":
                    while True:
                        for i,colour in enumerate(COLOURS):
                            print(f"{i}) {colour}")
                        askColour = input("Which colour do you want to change to? ").lower().title()
                        if askColour in COLOURS:
                            currentColour = askColour
                            print(f"Current Colour: {currentColour}")
                            break
                        else:
                            print("Invalid option.")
                continue

            elif cardType == "Reverse":
                if playerTurn[0] == 0:
                    playerTurn = playerTurn[::-1]
                    turn = playerTurn[turn]
                elif playerTurn[0] != 0:
                    turn = playerTurn[turn]
                    playerTurn = playerTurn[::-1]
                cardval = "Reverse"

            elif cardType == "Draw Two":
                amt = 2
                cardsDrawn, discards = drawCards(deck,2,discards,amt)
                if turn >= len(playerNumber) - 1:
                    playerDict[playerNumber[playerTurn[0]]].extend(cardsDrawn)
                elif turn < len(playerNumber) - 1:
                    playerDict[playerNumber[playerTurn[turn+1]]].extend(cardsDrawn)

            elif cardType == "Skip":
                turn += 1
                if turn > (len(playerNumber)-1):
                    turn = 0

            elif cardType == "Wild Draw Four":
                amt = 4
                ask = input("Do you want to change colour? (y/n): ").lower()
                if ask == "y":
                    while True:
                        for i,colour in enumerate(COLOURS):
                            print(f"{i}) {colour}")
                        askColour = input("Which colour do you want to change to? ").lower().title()
                        if askColour in COLOURS:
                            currentColour = askColour
                            print(f"Current Colour: {currentColour}")
                            break
                        else:
                            print("Invalid option.")

                cardsDrawn, discards = drawCards(deck,4,discards,amt)
                if turn >= (len(playerNumber) - 1):
                    playerDict[playerNumber[playerTurn[0]]].extend(cardsDrawn)
                elif turn < (len(playerNumber)-1):
                    playerDict[playerNumber[playerTurn[turn+1]]].extend(cardsDrawn)
                continue

            # Check if player won
            if len(playerCards[playerTurn[turn]]) == 0:
                PLAYERWON, playerNumber, playerCards, playerDict, playerTurn, turn = checkWin(playerNumber, playerCards, playerDict, playerTurn, turn)

            # Change Turns
            turn += 1
            if turn > (len(playerNumber)-1):
                turn = 0

        else:
            time.sleep(1)
            amt = 1
            if (("Wild" in playerCards[playerTurn[turn]][0]) or ("Reverse" in playerCards[playerTurn[turn]][0]) or ("Skip" in playerCards[playerTurn[turn]][0]) or ("Draw Two" in playerCards[playerTurn[turn]][0])) and (len(playerCards[playerTurn[turn]]) == 1):
                print(f'Sorry cannot accept "{playerCards[playerTurn[turn]][0]}" at the end.\n')
            NewCard, discards = drawCards(deck,1,discards,amt)
            playerDict[playerNumber[playerTurn[turn]]].extend(NewCard)
            print(f"You can't play, you have to draw a card!    Card Drawn: {NewCard[0]}")
            print(f"Current Colour: {currentColour}")
            if canplay(playerCards[playerTurn[turn]], currentColour, cardval):
                continue
            turn += 1
            if turn > (len(playerNumber)-1):
                turn = 0

    print("Game Over!\n")
    print("The winners are: ")
    for i,name in enumerate(PLAYERWON):
        print(f"{i+1}) {name}")

if __name__ == "__main__":
    print("Welcome To UNO Game!")
    main()