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
Intrigue_cards = {
        'Baron':            CARD(4, "Intrigue", "Action", './pictures/Intrigue/baron.jpg'),
        'Bridge':           CARD(4, "Intrigue", "Action", './pictures/Intrigue/bridge.jpg'),
        'Conspirator':      CARD(4, "Intrigue", "Action", './pictures/Intrigue/conspirator.jpg'),
        'Coppersmith':      CARD(4, "Intrigue", "Action", './pictures/Intrigue/coppersmith.jpg'),
        'Courtyard':        CARD(2, "Intrigue", "Action", './pictures/Intrigue/courtyard.jpg'),
        'Duke':             CARD(5, "Intrigue", "Victory", './pictures/Intrigue/duke.jpg'),
        'GreatHall':        CARD(3, "Intrigue", "Action - Victory", './pictures/Intrigue/greathall.jpg'),
        'Harem':            CARD(6, "Intrigue", "Treasure - Victory", './pictures/Intrigue/harem.jpg'),
        'Ironworks':        CARD(4, "Intrigue", "Action", './pictures/Intrigue/ironworks.jpg'),
        'Masquerade':       CARD(3, "Intrigue", "Action", './pictures/Intrigue/masquerade.jpg'),
        'MiningVillage':    CARD(4, "Intrigue", "Action", './pictures/Intrigue/miningvillage.jpg'),
        'Minion':           CARD(5, "Intrigue", "Action - Attack", './pictures/Intrigue/minion.jpg'),
        'Nobles':           CARD(6, "Intrigue", "Action - Victory", './pictures/Intrigue/nobles.jpg'),
        'Pawn':             CARD(2, "Intrigue", "Action", './pictures/Intrigue/pawn.jpg'),
        'Saboteur':         CARD(5, "Intrigue", "Action - Attack", './pictures/Intrigue/saboteur.jpg'),
        'Scout':            CARD(4, "Intrigue", "Action", './pictures/Intrigue/scout.jpg'),
        'SecretChamber':    CARD(2, "Intrigue", "Action - Reaction", './pictures/Intrigue/secretchamber.jpg'),
        'ShantyTown':       CARD(3, "Intrigue", "Action", './pictures/Intrigue/shantytown.jpg'),
        'Steward':          CARD(3, "Intrigue", "Action", './pictures/Intrigue/steward.jpg'),
        'Swindler':         CARD(3, "Intrigue", "Action - Attack", './pictures/Intrigue/swindler.jpg'),
        'Torturer':         CARD(5, "Intrigue", "Action - Attack", './pictures/Intrigue/torturer.jpg'),
        'TradingPost':      CARD(5, "Intrigue", "Action", './pictures/Intrigue/tradingpost.jpg'),
        'Tribute':          CARD(5, "Intrigue", "Action", './pictures/Intrigue/tribute.jpg'),
        'Upgrade':          CARD(5, "Intrigue", "Action", './pictures/Intrigue/upgrade.jpg'),
        'WishingWell':      CARD(3, "Intrigue", "Action", './pictures/Intrigue/wishingwell.jpg')
        }
Seaside_cards = {
        'Ambassador':       CARD(3, "Seaside", "Action - Attack", './pictures/seaside/ambassador.jpg'),
        'Bazaar':           CARD(5, "Seaside", "Action", './pictures/seaside/bazaar.jpg'),
        'Caravan':          CARD(4, "Seaside", "Action - Duration", './pictures/seaside/caravan.jpg'),
        'Cutpurse':         CARD(4, "Seaside", "Action - Attack", './pictures/seaside/cutpurse.jpg'),
        'Embargo':          CARD(2, "Seaside", "Action", './pictures/seaside/embargo.jpg'),
        'Ambassador':       CARD(3, "Seaside", "Action - Attack", './pictures/seaside/ambassador.jpg'),
        'Ambassador':       CARD(3, "Seaside", "Action - Attack", './pictures/seaside/ambassador.jpg'),
        'Ambassador':       CARD(3, "Seaside", "Action - Attack", './pictures/seaside/ambassador.jpg'),
        'Ambassador':       CARD(3, "Seaside", "Action - Attack", './pictures/seaside/ambassador.jpg'),
        'Ambassador':       CARD(3, "Seaside", "Action - Attack", './pictures/seaside/ambassador.jpg'),
        'Ambassador':       CARD(3, "Seaside", "Action - Attack", './pictures/seaside/ambassador.jpg'),
        'Ambassador':       CARD(3, "Seaside", "Action - Attack", './pictures/seaside/ambassador.jpg'),
        'Ambassador':       CARD(3, "Seaside", "Action - Attack", './pictures/seaside/ambassador.jpg'),
        'Ambassador':       CARD(3, "Seaside", "Action - Attack", './pictures/seaside/ambassador.jpg'),
        'Ambassador':       CARD(3, "Seaside", "Action - Attack", './pictures/seaside/ambassador.jpg'),
        'Ambassador':       CARD(3, "Seaside", "Action - Attack", './pictures/seaside/ambassador.jpg'),
        'Ambassador':       CARD(3, "Seaside", "Action - Attack", './pictures/seaside/ambassador.jpg'),
        'Ambassador':       CARD(3, "Seaside", "Action - Attack", './pictures/seaside/ambassador.jpg'),
        'Ambassador':       CARD(3, "Seaside", "Action - Attack", './pictures/seaside/ambassador.jpg'),
        'Ambassador':       CARD(3, "Seaside", "Action - Attack", './pictures/seaside/ambassador.jpg'),
        'Ambassador':       CARD(3, "Seaside", "Action - Attack", './pictures/seaside/ambassador.jpg'),
        'Ambassador':       CARD(3, "Seaside", "Action - Attack", './pictures/seaside/ambassador.jpg'),
        'Ambassador':       CARD(3, "Seaside", "Action - Attack", './pictures/seaside/ambassador.jpg'),
        'Ambassador':       CARD(3, "Seaside", "Action - Attack", './pictures/seaside/ambassador.jpg')
        }

# ADD all expansions to the CARDS dictionary.
CARDS.update(Dominion_base_cards)
CARDS.update(Intrigue_cards)

# Make a list with all the card names in alphabetical order.
CARDNAMES = []
for name in CARDS:
    CARDNAMES.append(name)
CARDNAMES.sort()

# Make a dict of all the Dominion Expansions with some descriptive attributes
EXPANSION = namedtuple("EXPANSION", "Name Number StandAlone Year Description")

EXPANSIONS = {
        'Base':         EXPANSION("Base", 1, True, 2008, "The Dominion base game."), 
        'Intrigue':     EXPANSION("Intrigue", 2, True, 2009, "The First Expansion."), 
        'Seaside':      EXPANSION("Seaside", 3, False, 2009, "The Second Expansion."), 
        'Alchemy':      EXPANSION("Alchemy", 4, False, 2010, "The Third Expansion."),
        'Prosperity':   EXPANSION("Prosperity", 5, False, 2010, "The Fourth Expansion."), 
        'Cornucopia':   EXPANSION("Cornucopia", 6, False, 2011, "The Fifth Expansion."), 
        'Hinterlands':  EXPANSION("Hinterlands", 7, False, 2011, "The Sixth Expansion."), 
        'DarkAges':     EXPANSION("Dark Ages", 8, False, 2012, "The Seventh Expansion."), 
        'Guilds':       EXPANSION("Guilds", 9, False, 2013, "The Eigth Expansion."), 
        'Adventures':   EXPANSION("Adventures", 10, False, 2015, "The Ninth Expansion."),
        'Empires':      EXPANSION("Empires", 11, False, 2016, "The Tenth Expansion."), 
        'Nocturne':     EXPANSION("Nocturne", 12, False, 2017, "The Eleventh Expansion.") 
        }

tmp = []
for name in EXPANSIONS:
    tmp.append((name, EXPANSIONS[name].Number))
tmp.sort(key=lambda tup: tup[1])

EXPANSION_NAMES_CHR = []
for tup in tmp:
    EXPANSION_NAMES_CHR.append(tup[0])
