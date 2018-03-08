# https://en.wikipedia.org/wiki/War_(card_game)
import random;
class Deck():
    suits = "H D S C".split();
    values = "A K Q J 10 9 8 7 6 5 4 3 2".split();
    highs = ["J","Q","K","A"];
    cards = [];
    def __init__(self):
        self.prepare_deck();

    def prepare_deck(self):
        for suit in self.suits:
            for value in self.values:
                self.cards.append(suit+":"+value);

    def shuffle_deck(self):
        random.shuffle(self.cards);

    def compare_cards(self,card1,card2):
        card1_value = card1.split(":")[1];
        card2_value = card2.split(":")[1];
        #print("{} and {}".format(card1_value,card2_value));
        if(card1_value in self.highs and not card2_value in self.highs):
            #print("24");
            return 1;
        elif(card2_value in self.highs and not card1_value in self.highs):
            #print("27");
            return -1;
        elif(card1_value in self.highs and card2_value in self.highs):
            #print("30");
            return self.highs.index(card1_value) - self.highs.index(card2_value);
        #print("32");
        return int(card1_value) - int(card2_value);

class Hand():

    def __init__(self):
        self.card_stack = [];
        self.cards_in_hand = [];

    def draw_card(self):
        return self.cards_in_hand.pop(0);

    def put_in_stack(self,cards):
        self.card_stack.extend(cards);

class Player():
    def __init__(self,name):
        self.name = name;
        self.hand = Hand();
        self.next_card = "";

    def show_next_card(self):
        card = self.hand.cards_in_hand.pop(0);
        print("Player {} has {}".format(self.name,card));
        self.next_card = card;
        return card;

    def put_card_on_table(self):
        return self.hand.cards_in_hand.pop(0);

class Table():
    status_battle = 1;
    status_war = 2;

    def __init__(self):
        self.face_up_cards = [];
        self.face_down_cards = [];
        self.deck = Deck();

    def clear_table(self):
        del self.face_up_cards[:];
        del self.face_down_cards[:];

    def take_hidden_card(self,card):
        self.face_down_cards.append(card);

    def take_shown_card(self,card):
        self.face_up_cards.append(card);

    def determine_winner(self,player1,player2):
        #print("comparing {} and {} ".format(player1.next_card,player2.next_card));
        result = self.deck.compare_cards(player1.next_card,player2.next_card);
        #print("result:",result);
        if(result == 0):
            return self.status_war;
        elif(result>0):
            print("Player {} Gets the cards".format(player1.name));
            player1.hand.card_stack.extend(self.face_down_cards);
            player1.hand.card_stack.extend(self.face_up_cards);
        else:
            print("Player {} Gets the cards".format(player2.name));
            player2.hand.card_stack.extend(self.face_down_cards);
            player2.hand.card_stack.extend(self.face_up_cards);

        self.clear_table();
        print();
        return self.status_battle;

print("Let's Play");

player2 = Player("Computer");
print("Player {} is ready".format(player2.name));

name = input("Enter your name : ");
player1 = Player(name);

table = Table();
print("Shuffling deck");
table.deck.shuffle_deck();

player1.hand.cards_in_hand = table.deck.cards[:26];
player2.hand.cards_in_hand = table.deck.cards[26:];
print("Cards are distributed.");

table.face_up_cards = [player2.show_next_card()];
table.face_up_cards = [player1.show_next_card()];
status = table.determine_winner(player1,player2);

while (len(player1.hand.cards_in_hand) != 0 and len(player2.hand.cards_in_hand) != 0):
    if(status == table.status_war):
        print("It's WAR!");
        table.take_hidden_card(player2.put_card_on_table());
        table.take_hidden_card(player1.put_card_on_table());
        table.take_shown_card(player2.show_next_card());
        input("continue");
        table.take_shown_card(player1.show_next_card());

    elif(status == table.status_battle):
        print("Battle!");
        table.take_shown_card(player2.show_next_card());
        input("continue");
        table.take_shown_card(player1.show_next_card());

    status = table.determine_winner(player1,player2);

if(len(player1.hand.card_stack) == len(player2.hand.card_stack)):
    print("IT'S A DRAW !!");
elif(len(player1.hand.card_stack)> len(player2.hand.card_stack)):
    print("Player {} Wins !!".format(player1.name));
else:
    print("Player {} Wins !!".format(player2.name));

print("Player {} collected : ".format(player1.name));
print(player1.hand.card_stack);
print("Player {} collected : ".format(player2.name));
print(player2.hand.card_stack);
