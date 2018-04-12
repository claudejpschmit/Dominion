from collections import namedtuple

# Defining C-like struct for card objects
CARD = namedtuple("CARD", "cost expansion type imagePath")

# Defining dictionary which will contain all cards
CARDS = {}

# Defining all cards per Expansion
Dominion_base_cards = {
        'Adventurer':       CARD(6, "Base", "Action", './pictures/dominion/adventurer.jpg'),
        'Bureaucrat':       CARD(4, "Base", "Action - Attack", './pictures/dominion/bureaucrat.jpg'),
        'Cellar':           CARD(2, "Base", "Action", './pictures/dominion/cellar.jpg'),
        'Chancellor':       CARD(3, "Base", "Action", './pictures/dominion/chancellor.jpg'),
        'Chapel':           CARD(2, "Base", "Action", './pictures/dominion/chapel.jpg'),
        'Councilroom':      CARD(5, "Base", "Action", './pictures/dominion/councilroom.jpg'),
        'Feast':            CARD(4, "Base", "Action", './pictures/dominion/feast.jpg'),
        'Festival':         CARD(5, "Base", "Action", './pictures/dominion/festival.jpg'),
        'Gardens':          CARD(4, "Base", "Victory", './pictures/dominion/gardens.jpg'),
        'Laboratory':       CARD(5, "Base", "Action", './pictures/dominion/laboratory.jpg'),
        'Library':          CARD(5, "Base", "Action", './pictures/dominion/library.jpg'),
        'Market':           CARD(5, "Base", "Action", './pictures/dominion/market.jpg'),
        'Militia':          CARD(4, "Base", "Action - Attack", './pictures/dominion/militia.jpg'),
        'Mine':             CARD(5, "Base", "Action", './pictures/dominion/mine.jpg'),
        'Moat':             CARD(2, "Base", "Action - Reaction", './pictures/dominion/mine.jpg'),
        'Moneylender':      CARD(4, "Base", "Action", './pictures/dominion/moneylender.jpg'),
        'Remodel':          CARD(4, "Base", "Action", './pictures/dominion/remodel.jpg'),
        'Smithy':           CARD(4, "Base", "Action", './pictures/dominion/smithy.jpg'),
        'Spy':              CARD(4, "Base", "Action - Attack", './pictures/dominion/spy.jpg'),
        'Thief':            CARD(4, "Base", "Action - Attack", './pictures/dominion/thief.jpg'),
        'Throneroom':       CARD(4, "Base", "Action", './pictures/dominion/throneroom.jpg'),
        'Village':          CARD(3, "Base", "Action", './pictures/dominion/village.jpg'),
        'Witch':            CARD(5, "Base", "Action - Attack", './pictures/dominion/witch.jpg'),
        'Woodcutter':       CARD(3, "Base", "Action", './pictures/dominion/woodcutter.jpg'),
        'Workshop':         CARD(3, "Base", "Action", './pictures/dominion/workshop.jpg')
        }

# ADD all expansions to the CARDS dictionary.
CARDS.update(Dominion_base_cards)

# Make a list with all the card names in alphabetical order.
CARDNAMES = []
for name in CARDS:
    CARDNAMES.append(name)
CARDNAMES.sort()
