#include <iostream>
#include <vector>
#include <string>
#include <random>
#include <algorithm>
#include <cstdlib>

using namespace std;

// Global Variables for Card Attributes
vector<string> COLORS = {"Red", "Blue", "Green", "Yellow"};
vector<string> NUMBERS = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"};
vector<string> SPECIALS = {"Skip", "Reverse", "Draw Two"};
vector<string> WILDS = {"Wild", "Wild Draw Four"};

// Card Structure
struct Card {
    string color;
    string value;

    // Constructor
    Card(string c, string v) : color(c), value(v) {}

    // Display the card
    void display() const {
        if (color.empty()) {
            cout << value; // Wild cards have no color
        } else {
            cout << color << " " << value;
        }
    }
};

// Function to Build the Deck
vector<Card> buildDeck() {
    vector<Card> deck;

    // Add number and special cards
    for (const string& color : COLORS) {
        for (const string& number : NUMBERS) {
            deck.emplace_back(color, number);
            if (number != "0") deck.emplace_back(color, number); // Two of each except "0"
        }
        for (const string& special : SPECIALS) {
            deck.emplace_back(color, special);
            deck.emplace_back(color, special); // Two of each special card
        }
    }

    // Add wild cards
    for (const string& wild : WILDS) {
        for (int i = 0; i < 4; ++i) {
            deck.emplace_back("", wild);
        }
    }

    return deck;
}

// Function to Shuffle the Deck
void shuffleDeck(vector<Card>& deck) {
    random_device rd;
    mt19937 g(rd());
    shuffle(deck.begin(), deck.end(), g);
}

// Function to Get the Number of Players
int getNumberOfPlayers() {
    int players;
    while (true) {
        cout << "Enter the number of players (2 or more): ";
        cin >> players;
        if (players >= 2) break;
        cout << "Invalid input. Number of players must be 2 or more.\n";
    }
    return players;
}

// Function to Get the Number of Cards per Player
int getCardsPerPlayer(int numPlayers) {
    int cards;
    while (true) {
        cout << "Enter the number of cards per player: ";
        cin >> cards;
        if (cards > 0) {
            int maxCards = 108 / numPlayers;
            if (cards <= maxCards) {
                break;
            } else {
                cout << "Too many cards per player. Maximum allowed: " << maxCards << "\n";
            }
        } else {
            cout << "Number of cards must be greater than 0.\n";
        }
    }
    return cards;
}

// Function to Deal Cards to Players
vector<vector<Card>> dealCards(vector<Card>& deck, int numPlayers, int cardsPerPlayer) {
    vector<vector<Card>> hands(numPlayers);
    for (int i = 0; i < numPlayers; ++i) {
        for (int j = 0; j < cardsPerPlayer; ++j) {
            hands[i].push_back(deck.back());
            deck.pop_back();
        }
    }
    return hands;
}

// Function to Display a Player's Hand
void displayHand(const vector<Card>& hand) {
    for (size_t i = 0; i < hand.size(); ++i) {
        cout << i + 1 << ") ";
        hand[i].display();
        cout << "\n";
    }
}

// Function to Check if a Card Can Be Played
bool canPlay(const Card& card, const Card& topCard) {
    return card.color == topCard.color || card.value == topCard.value || card.color.empty(); // Wild cards
}

// Function to Play a Turn
void playTurn(int player, vector<Card>& hand, Card& topCard, vector<Card>& deck) {
    cout << "Player " << player + 1 << "'s turn.\n";
    cout << "Top card: ";
    topCard.display();
    cout << "\n";

    displayHand(hand);

    // Check if the player has a playable card
    bool hasPlayableCard = false;
    for (const Card& card : hand) {
        if (canPlay(card, topCard)) {
            hasPlayableCard = true;
            break;
        }
    }

    if (!hasPlayableCard) {
        cout << "No playable card. Drawing a card...\n";
        if (!deck.empty()) {
            hand.push_back(deck.back());
            deck.pop_back();
        } else {
            cout << "The deck is empty. Skipping turn.\n";
        }
        return;
    }

    // Prompt the player to choose a card
    int choice;
    while (true) {
        cout << "Choose a card to play (1-" << hand.size() << "): ";
        cin >> choice;
        if (choice >= 1 && choice <= (int)hand.size() && canPlay(hand[choice - 1], topCard)) {
            break;
        }
        cout << "Invalid choice. Try again.\n";
    }

    // Play the chosen card
    topCard = hand[choice - 1];
    hand.erase(hand.begin() + choice - 1);

    // Handle special cards
    if (topCard.value == "Reverse") {
        cout << "Reverse card played! Reversing turn order.\n";
    } else if (topCard.value == "Skip") {
        cout << "Skip card played! Next player is skipped.\n";
    } else if (topCard.value == "Draw Two") {
        cout << "Draw Two card played! Next player draws two cards.\n";
    } else if (topCard.value == "Wild") {
        cout << "Wild card played! Choose a color (Red, Blue, Green, Yellow): ";
        cin >> topCard.color;
    } else if (topCard.value == "Wild Draw Four") {
        cout << "Wild Draw Four card played! Choose a color (Red, Blue, Green, Yellow): ";
        cin >> topCard.color;
    }
}

// Main Function
int main() {
    cout << "Welcome to UNO!\n";

    // Set up the game
    int numPlayers = getNumberOfPlayers();
    int cardsPerPlayer = getCardsPerPlayer(numPlayers);

    vector<Card> deck = buildDeck();
    shuffleDeck(deck);

    vector<vector<Card>> hands = dealCards(deck, numPlayers, cardsPerPlayer);

    Card topCard = deck.back();
    deck.pop_back();

    int currentPlayer = 0;
    bool gameOver = false;

    while (!gameOver) {
        playTurn(currentPlayer, hands[currentPlayer], topCard, deck);

        if (hands[currentPlayer].empty()) {
            cout << "Player " << currentPlayer + 1 << " wins!\n";
            gameOver = true;
        } else {
            // Move to the next player
            currentPlayer = (currentPlayer + 1) % numPlayers;
        }
    }

    cout << "Game over. Thanks for playing UNO!\n";
    return 0;
}
