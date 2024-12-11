#include <SFML/Graphics.hpp>
#include <SFML/Window.hpp>
#include <SFML/System.hpp>
#include <iostream>
#include <vector>
#include <string>
#include <ctime>
#include <cstdlib>
#include <algorithm>
#include <random>

using namespace std;
using namespace sf;

// Global Constants
const int WINDOW_WIDTH = 1280;
const int WINDOW_HEIGHT = 720;
const int CARD_WIDTH = 100;
const int CARD_HEIGHT = 150;

// Struct to represent a Card
struct Card {
    string color;
    string value;

    Card(string c, string v) : color(c), value(v) {}
};

// Function to create the deck
vector<Card> createDeck() {
    vector<Card> deck;
    vector<string> colors = {"Red", "Blue", "Green", "Yellow"};
    vector<string> values = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "Skip", "Reverse", "Draw Two"};
    vector<string> wilds = {"Wild", "Wild Draw Four"};

    for (const auto& color : colors) {
        for (const auto& value : values) {
            deck.emplace_back(color, value);
            if (value != "0") deck.emplace_back(color, value);
        }
    }

    for (const auto& wild : wilds) {
        for (int i = 0; i < 4; i++) deck.emplace_back("", wild);
    }

    return deck;
}

// Function to shuffle the deck
void shuffleDeck(vector<Card>& deck) {
    random_device rd;
    mt19937 g(rd());
    shuffle(deck.begin(), deck.end(), g);
}

// Helper function to draw a card as a rectangle with text
void drawCard(RenderWindow& window, const Card& card, float x, float y) {
    RectangleShape cardShape(Vector2f(CARD_WIDTH, CARD_HEIGHT));
    cardShape.setPosition(x, y);

    // Set card color
    if (card.color == "Red") cardShape.setFillColor(Color::Red);
    else if (card.color == "Blue") cardShape.setFillColor(Color::Blue);
    else if (card.color == "Green") cardShape.setFillColor(Color::Green);
    else if (card.color == "Yellow") cardShape.setFillColor(Color::Yellow);
    else cardShape.setFillColor(Color::Black);

    // Draw the card background
    window.draw(cardShape);

    // Draw the card text
    Font font;
    font.loadFromFile("arial.ttf");
    Text cardText(card.value, font, 20);
    cardText.setFillColor(Color::White);
    cardText.setPosition(x + 10, y + 10);

    window.draw(cardText);
}

// Function to display player hand
void displayPlayerHand(RenderWindow& window, const vector<Card>& hand, float startX, float startY) {
    for (size_t i = 0; i < hand.size(); ++i) {
        drawCard(window, hand[i], startX + i * (CARD_WIDTH + 10), startY);
    }
}

// Function to display the top card
void displayTopCard(RenderWindow& window, const Card& topCard) {
    drawCard(window, topCard, WINDOW_WIDTH / 2 - CARD_WIDTH / 2, WINDOW_HEIGHT / 2 - CARD_HEIGHT / 2);
}

// Main function
int main() {
    RenderWindow window(VideoMode(WINDOW_WIDTH, WINDOW_HEIGHT), "UNO Game");

    // Load resources
    Font font;
    if (!font.loadFromFile("arial.ttf")) {
        cerr << "Error loading font!" << endl;
        return -1;
    }

    // Initialize the deck
    vector<Card> deck = createDeck();
    shuffleDeck(deck);

    // Distribute cards to players
    int players = 2;
    int cardsPerPlayer = 7;
    vector<vector<Card>> playerHands(players);
    for (int i = 0; i < players; ++i) {
        for (int j = 0; j < cardsPerPlayer; ++j) {
            playerHands[i].push_back(deck.back());
            deck.pop_back();
        }
    }

    // Set up initial top card
    Card topCard = deck.back();
    deck.pop_back();

    // Game loop
    while (window.isOpen()) {
        Event event;
        while (window.pollEvent(event)) {
            if (event.type == Event::Closed) {
                window.close();
            }
        }

        // Clear the window
        window.clear(Color::White);

        // Display the top card
        displayTopCard(window, topCard);

        // Display player hands
        displayPlayerHand(window, playerHands[0], 100, WINDOW_HEIGHT - 200);
        displayPlayerHand(window, playerHands[1], 100, 50);

        // Display text for instructions
        Text instructionText("Click on a card to play!", font, 24);
        instructionText.setFillColor(Color::Black);
        instructionText.setPosition(20, WINDOW_HEIGHT - 40);
        window.draw(instructionText);

        // Display the window
        window.display();
    }

    return 0;
}
