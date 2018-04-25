from collections import namedtuple

# Defining C-like struct for card objects
CARD = namedtuple("CARD", "cost name expansion type imagePath")

# Defining dictionary which will contain all cards
CARDS = {}

# Defining all cards per Expansion
Dominion_base_cards = {
        'Adventurer':       CARD(6, "Adventurer", "Base", "Action", './pictures/dominion/adventurer.jpg'),
        'Bureaucrat':       CARD(4, "Bureaucrat", "Base", "Action - Attack", './pictures/dominion/bureaucrat.jpg'),
        'Cellar':           CARD(2, "Cellar", "Base", "Action", './pictures/dominion/cellar.jpg'),
        'Chancellor':       CARD(3, "Chancellor", "Base", "Action", './pictures/dominion/chancellor.jpg'),
        'Chapel':           CARD(2, "Chapel", "Base", "Action", './pictures/dominion/chapel.jpg'),
        'Councilroom':      CARD(5, "Councilroom", "Base", "Action", './pictures/dominion/councilroom.jpg'),
        'Feast':            CARD(4, "Feast", "Base", "Action", './pictures/dominion/feast.jpg'),
        'Festival':         CARD(5, "Festival", "Base", "Action", './pictures/dominion/festival.jpg'),
        'Gardens':          CARD(4, "Gardens", "Base", "Victory", './pictures/dominion/gardens.jpg'),
        'Laboratory':       CARD(5, "Laboratory", "Base", "Action", './pictures/dominion/laboratory.jpg'),
        'Library':          CARD(5, "Library", "Base", "Action", './pictures/dominion/library.jpg'),
        'Market':           CARD(5, "Market", "Base", "Action", './pictures/dominion/market.jpg'),
        'Militia':          CARD(4, "Militia", "Base", "Action - Attack", './pictures/dominion/militia.jpg'),
        'Mine':             CARD(5, "Mine", "Base", "Action", './pictures/dominion/mine.jpg'),
        'Moat':             CARD(2, "Moat", "Base", "Action - Reaction", './pictures/dominion/moat.jpg'),
        'Moneylender':      CARD(4, "Moneylender", "Base", "Action", './pictures/dominion/moneylender.jpg'),
        'Remodel':          CARD(4, "Remodel", "Base", "Action", './pictures/dominion/remodel.jpg'),
        'Smithy':           CARD(4, "Smithy", "Base", "Action", './pictures/dominion/smithy.jpg'),
        'Spy':              CARD(4, "Spy", "Base", "Action - Attack", './pictures/dominion/spy.jpg'),
        'Thief':            CARD(4, "Thief", "Base", "Action - Attack", './pictures/dominion/thief.jpg'),
        'Throneroom':       CARD(4, "Throneroom", "Base", "Action", './pictures/dominion/throneroom.jpg'),
        'Village':          CARD(3, "Village", "Base", "Action", './pictures/dominion/village.jpg'),
        'Witch':            CARD(5, "Witch", "Base", "Action - Attack", './pictures/dominion/witch.jpg'),
        'Woodcutter':       CARD(3, "Woodcutter", "Base", "Action", './pictures/dominion/woodcutter.jpg'),
        'Workshop':         CARD(3, "Workshop", "Base", "Action", './pictures/dominion/workshop.jpg')
}
Intrigue_cards = {
        'Baron':            CARD(4, "Baron", "Intrigue", "Action", './pictures/Intrigue/baron.jpg'),
        'Bridge':           CARD(4, "Bridge", "Intrigue", "Action", './pictures/Intrigue/bridge.jpg'),
        'Conspirator':      CARD(4, "Conspirator", "Intrigue", "Action", './pictures/Intrigue/conspirator.jpg'),
        'Coppersmith':      CARD(4, "Coppersmith", "Intrigue", "Action", './pictures/Intrigue/coppersmith.jpg'),
        'Courtyard':        CARD(2, "Courtyard", "Intrigue", "Action", './pictures/Intrigue/courtyard.jpg'),
        'Duke':             CARD(5, "Duke", "Intrigue", "Victory", './pictures/Intrigue/duke.jpg'),
        'GreatHall':        CARD(3, "Great Hall", "Intrigue", "Action - Victory", './pictures/Intrigue/greathall.jpg'),
        'Harem':            CARD(6, "Harem", "Intrigue", "Treasure - Victory", './pictures/Intrigue/harem.jpg'),
        'Ironworks':        CARD(4, "Ironworks", "Intrigue", "Action", './pictures/Intrigue/ironworks.jpg'),
        'Masquerade':       CARD(3, "Masquerade", "Intrigue", "Action", './pictures/Intrigue/masquerade.jpg'),
        'MiningVillage':    CARD(4, "Mining Village", "Intrigue", "Action", './pictures/Intrigue/miningvillage.jpg'),
        'Minion':           CARD(5, "Minion", "Intrigue", "Action - Attack", './pictures/Intrigue/minion.jpg'),
        'Nobles':           CARD(6, "Nobles", "Intrigue", "Action - Victory", './pictures/Intrigue/nobles.jpg'),
        'Pawn':             CARD(2, "Pawn", "Intrigue", "Action", './pictures/Intrigue/pawn.jpg'),
        'Saboteur':         CARD(5, "Saboteur", "Intrigue", "Action - Attack", './pictures/Intrigue/saboteur.jpg'),
        'Scout':            CARD(4, "Scout", "Intrigue", "Action", './pictures/Intrigue/scout.jpg'),
        'SecretChamber':    CARD(2, "Secret Chamber", "Intrigue", "Action - Reaction", './pictures/Intrigue/secretchamber.jpg'),
        'ShantyTown':       CARD(3, "Shanty Town", "Intrigue", "Action", './pictures/Intrigue/shantytown.jpg'),
        'Steward':          CARD(3, "Steward", "Intrigue", "Action", './pictures/Intrigue/steward.jpg'),
        'Swindler':         CARD(3, "Swindler", "Intrigue", "Action - Attack", './pictures/Intrigue/swindler.jpg'),
        'Torturer':         CARD(5, "Torturer", "Intrigue", "Action - Attack", './pictures/Intrigue/torturer.jpg'),
        'TradingPost':      CARD(5, "Trading Post", "Intrigue", "Action", './pictures/Intrigue/tradingpost.jpg'),
        'Tribute':          CARD(5, "Tribute", "Intrigue", "Action", './pictures/Intrigue/tribute.jpg'),
        'Upgrade':          CARD(5, "Upgrade", "Intrigue", "Action", './pictures/Intrigue/upgrade.jpg'),
        'WishingWell':      CARD(3, "Wishing Well", "Intrigue", "Action", './pictures/Intrigue/wishingwell.jpg')
}
Seaside_cards = {
        'Ambassador':       CARD(3, "Ambassador", "Seaside", "Action - Attack", './pictures/seaside/ambassador.jpg'),
        'Bazaar':           CARD(5, "Bazaar", "Seaside", "Action", './pictures/seaside/bazaar.jpg'),
        'Caravan':          CARD(4, "Caravan", "Seaside", "Action - Duration", './pictures/seaside/caravan.jpg'),
        'Cutpurse':         CARD(4, "Cutpurse", "Seaside", "Action - Attack", './pictures/seaside/cutpurse.jpg'),
        'Embargo':          CARD(2, "Embargo", "Seaside", "Action", './pictures/seaside/embargo.jpg'),
        'Explorer':         CARD(5, "Explorer", "Seaside", "Action", './pictures/seaside/explorer.jpg'),
        'FishingVillage':   CARD(3, "Fishing Village", "Seaside", "Action - Duration", './pictures/seaside/fishingvillage.jpg'),
        'GhostShip':        CARD(5, "Ghost Ship", "Seaside", "Action - Attack", './pictures/seaside/ghostship.jpg'),
        'Haven':            CARD(2, "Haven", "Seaside", "Action - Duration", './pictures/seaside/haven.jpg'),
        'Island':           CARD(4, "Island", "Seaside", "Action - Victory", './pictures/seaside/island.jpg'),
        'Lighthouse':       CARD(2, "Lighthouse", "Seaside", "Action - Duration", './pictures/seaside/lighthouse.jpg'),
        'Lookout':          CARD(3, "Lookout", "Seaside", "Action", './pictures/seaside/lookout.jpg'),
        'MerchantShip':     CARD(5, "Merchant Ship", "Seaside", "Action - Duration", './pictures/seaside/merchantship.jpg'),
        'NativeVillage':    CARD(2, "Native Village", "Seaside", "Action", './pictures/seaside/nativevillage.jpg'),
        'Navigator':        CARD(4, "Navigator", "Seaside", "Action", './pictures/seaside/navigator.jpg'),
        'Outpost':          CARD(5, "Outpost", "Seaside", "Action - Duration", './pictures/seaside/outpost.jpg'),
        'PearlDiver':       CARD(2, "Pearl Diver", "Seaside", "Action", './pictures/seaside/pearldiver.jpg'),
        'PirateShip':       CARD(4, "Pirate Ship", "Seaside", "Action - Attack", './pictures/seaside/pirateship.jpg'),
        'Salvager':         CARD(4, "Salvager", "Seaside", "Action", './pictures/seaside/salvager.jpg'),
        'SeaHag':           CARD(4, "Sea Hag", "Seaside", "Action - Attack", './pictures/seaside/seahag.jpg'),
        'Smuggler':         CARD(3, "Smuggler", "Seaside", "Action", './pictures/seaside/smugglers.jpg'),
        'Tactition':        CARD(5, "Tactition", "Seaside", "Action - Duration", './pictures/seaside/tactician.jpg'),
        'TreasureMap':      CARD(4, "Treasure Map", "Seaside", "Action", './pictures/seaside/treasuremap.jpg'),
        'Treasury':         CARD(5, "Treasury", "Seaside", "Action", './pictures/seaside/treasury.jpg'),
        'Warehouse':        CARD(3, "Warehouse", "Seaside", "Action", './pictures/seaside/warehouse.jpg'),
        'Wharf':            CARD(5, "Wharf", "Seaside", "Action - Duration", './pictures/seaside/wharf.jpg')
}
Alchemy_cards = {
        'Alchemist':        CARD(4, "Alchemist", "Alchemy", "Action", './pictures/alchemy/alchemist.jpg'),
        'Apothecary':       CARD(3, "Apothecary", "Alchemy", "Action", './pictures/alchemy/apothecary.jpg'),
        'Apprentice':       CARD(5, "Apprentice", "Alchemy", "Action", './pictures/alchemy/apprentice.jpg'),
        'Familiar':         CARD(4, "Familiar", "Alchemy", "Action - Attack", './pictures/alchemy/familiar.jpg'),
        'Golem':            CARD(5, "Golem", "Alchemy", "Action", './pictures/alchemy/golem.jpg'),
        'Herbalist':        CARD(2, "Herbalist", "Alchemy", "Action", './pictures/alchemy/herbalist.jpg'),
        'PhilosopherStone': CARD(3, "Philosopher Stone", "Alchemy", "Treasure", './pictures/alchemy/philosophersstone.jpg'),
        'Possession':       CARD(7, "Possession", "Alchemy", "Action", './pictures/alchemy/possession.jpg'),
        'ScryingPool':      CARD(3, "Scrying Pool", "Alchemy", "Action - Attack", './pictures/alchemy/scryingpool.jpg'),
        'Transmute':        CARD(3, "Transmute", "Alchemy", "Action", './pictures/alchemy/transmute.jpg'),
        'University':       CARD(3, "University", "Alchemy", "Action", './pictures/alchemy/university.jpg'),
        'Vineyard':         CARD(1, "Vineyard", "Alchemy", "Action - Attack", './pictures/alchemy/vineyard.jpg')
}
Prosperity_cards = {
        'Bank':             CARD(7, "Bank", "Prosperity", "Treasure", './pictures/prosperity/bank.jpg'),
        'Bishop':           CARD(4, "Bishop", "Prosperity", "Action", './pictures/prosperity/bishop.jpg'),
        'City':             CARD(5, "City", "Prosperity", "Action", './pictures/prosperity/city.jpg'),
        'Contraband':       CARD(5, "Contrabans", "Prosperity", "Treasure", './pictures/prosperity/contraband.jpg'),
        'CountingHouse':    CARD(5, "Counting House", "Prosperity", "Action", './pictures/prosperity/countinghouse.jpg'),
        'Expand':           CARD(7, "Expand", "Prosperity", "Action", './pictures/prosperity/expand.jpg'),
        'Forge':            CARD(7, "Forge", "Prosperity", "Action", './pictures/prosperity/forge.jpg'),
        'Goons':            CARD(6, "Goons", "Prosperity", "Action - Attack", './pictures/prosperity/goons.jpg'),
        'GrandMarket':      CARD(6, "Grand Market", "Prosperity", "Action", './pictures/prosperity/grandmarket.jpg'),
        'Hoard':            CARD(6, "Hoard", "Prosperity", "Treasure", './pictures/prosperity/hoard.jpg'),
        'KingsCourt':       CARD(7, "King's Court", "Prosperity", "Action", './pictures/prosperity/kingscourt.jpg'),
        'Loan':             CARD(3, "Loan", "Prosperity", "Treasure", './pictures/prosperity/loan.jpg'),
        'Mint':             CARD(5, "Mint", "Prosperity", "Action", './pictures/prosperity/mint.jpg'),
        'Monument':         CARD(4, "Monument", "Prosperity", "Action", './pictures/prosperity/monument.jpg'),
        'Mountebank':       CARD(5, "Mountebank", "Prosperity", "Action - Attack", './pictures/prosperity/mountebank.jpg'),
        'Peddler':          CARD(8, "Peddler", "Prosperity", "Action", './pictures/prosperity/peddler.jpg'),
        'Quarry':           CARD(4, "Quarry", "Prosperity", "Treasure", './pictures/prosperity/quarry.jpg'),
        'Rabble':           CARD(5, "Rabble", "Prosperity", "Action - Attack", './pictures/prosperity/rabble.jpg'),
        'RoyalSeal':        CARD(5, "Royal Seal", "Prosperity", "Treasure", './pictures/prosperity/royalseal.jpg'),
        'Talisman':         CARD(4, "Talisman", "Prosperity", "Treasure", './pictures/prosperity/talisman.jpg'),
        'TradeRoute':       CARD(3, "Trade Route", "Prosperity", "Action", './pictures/prosperity/traderoute.jpg'),
        'Vault':            CARD(5, "Vault", "Prosperity", "Action", './pictures/prosperity/vault.jpg'),
        'Venture':          CARD(5, "Venture", "Prosperity", "Treasure", './pictures/prosperity/venture.jpg'),
        'Watchtower':       CARD(3, "Watchtower", "Prosperity", "Action - Reaction", './pictures/prosperity/watchtower.jpg'),
        'WorkersVillage':   CARD(4, "Worker's Village", "Prosperity", "Action", './pictures/prosperity/workersvillage.jpg')
}
Cornucopia_cards = {
        'Fairgrounds':      CARD(6, "Fairgrounds", "Cornucopia", "Victory", './pictures/cornucopia/fairgrounds.jpg'),
        'FarmingVillage':   CARD(4, "Farming Village", "Cornucopia", "Action", './pictures/cornucopia/farmingvillage.jpg'),
        'FortuneTeller':    CARD(3, "Fortune Teller", "Cornucopia", "Action - Attack", './pictures/cornucopia/fortuneteller.jpg'),
        'Hamlet':           CARD(2, "Hamlet", "Cornucopia", "Action", './pictures/cornucopia/hamlet.jpg'),
        'Harvest':          CARD(5, "Harvest", "Cornucopia", "Action", './pictures/cornucopia/harvest.jpg'),
        'HornOfPlenty':     CARD(5, "Horn of Plenty", "Cornucopia", "Treasure", './pictures/cornucopia/hornofplenty.jpg'),
        'HorseTrader':      CARD(4, "Horse Trader", "Cornucopia", "Action - Reaction", './pictures/cornucopia/horsetraders.jpg'),
        'HuntingParty':     CARD(5, "Hunting Party", "Cornucopia", "Action", './pictures/cornucopia/huntingparty.jpg'),
        'Jester':           CARD(5, "Jester", "Cornucopia", "Action - Attack", './pictures/cornucopia/jester.jpg'),
        'Menagerie':        CARD(3, "Menagerie", "Cornucopia", "Action", './pictures/cornucopia/menagerie.jpg'),
        'Remake':           CARD(4, "Remake", "Cornucopia", "Action", './pictures/cornucopia/remake.jpg'),
        'Tournament':       CARD(4, "Tournament", "Cornucopia", "Action", './pictures/cornucopia/tournament.jpg'),
        'YoungWitch':       CARD(4, "Young Witch", "Cornucopia", "Action - Attack", './pictures/cornucopia/youngwitch.jpg')
}
Hinterlands_cards = {
        'BorderVillage':    CARD(6, "Border Village", "Hinterlands", "Action", './pictures/hinterlands/bordervillage.jpg'),
        'Cache':            CARD(4, "Cache", "Hinterlands", "Treasure", './pictures/hinterlands/cache.jpg'),
        'Cartographer':     CARD(5, "Cartographer", "Hinterlands", "Action", './pictures/hinterlands/cartographer.jpg'),
        'Crossroads':       CARD(2, "Crossroads", "Hinterlands", "Action", './pictures/hinterlands/crossroads.jpg'),
        'Develop':          CARD(3, "Develop", "Hinterlands", "Action", './pictures/hinterlands/develop.jpg'),
        'Duchess':          CARD(2, "Duchess", "Hinterlands", "Action", './pictures/hinterlands/duchess.jpg'),
        'Embassy':          CARD(5, "Embassy", "Hinterlands", "Action", './pictures/hinterlands/embassy.jpg'),
        'Farmland':         CARD(4, "Farmland", "Hinterlands", "Victory", './pictures/hinterlands/farmland.jpg'),
        'FoolsGold':        CARD(2, "Fool's Gold", "Hinterlands", "Treasure - Reaction", './pictures/hinterlands/foolsgold.jpg'),
        'Haggler':          CARD(5, "Haggler", "Hinterlands", "Action", './pictures/hinterlands/haggler.jpg'),
        'Highway':          CARD(5, "Highway", "Hinterlands", "Action", './pictures/hinterlands/highway.jpg'),
        'IllGottenGains':   CARD(5, "Ill-Gotten Gains", "Hinterlands", "Treasure", './pictures/hinterlands/illgottengains.jpg'),
        'Inn':              CARD(5, "Inn", "Hinterlands", "Action", './pictures/hinterlands/inn.jpg'),
        'JackOfAllTrades':  CARD(4, "Jack of all Trades", "Hinterlands", "Action", './pictures/hinterlands/jackofalltrades.jpg'),
        'Mandarin':         CARD(5, "Mandarin", "Hinterlands", "Action", './pictures/hinterlands/mandarin.jpg'),
        'Margrave':         CARD(5, "Margrave", "Hinterlands", "Action - Attack", './pictures/hinterlands/margrave.jpg'),
        'NobleBrigand':     CARD(4, "Noble Brigand", "Hinterlands", "Action - Attack", './pictures/hinterlands/noblebrigand.jpg'),
        'NomadCamp':        CARD(4, "Nomad Camp", "Hinterlands", "Action", './pictures/hinterlands/nomadcamp.jpg'),
        'Oasis':            CARD(3, "Oasis", "Hinterlands", "Action", './pictures/hinterlands/oasis.jpg'),
        'Oracle':           CARD(3, "Oracle", "Hinterlands", "Action - Attack", './pictures/hinterlands/oracle.jpg'),
        'Scheme':           CARD(3, "Scheme", "Hinterlands", "Action", './pictures/hinterlands/scheme.jpg'),
        'SilkRoad':         CARD(4, "Silk Road", "Hinterlands", "Victory", './pictures/hinterlands/silkroad.jpg'),
        'SpiceMerchant':    CARD(4, "Spice Merchant", "Hinterlands", "Action", './pictures/hinterlands/spicemerchant.jpg'),
        'Stables':          CARD(5, "Stables", "Hinterlands", "Action", './pictures/hinterlands/stables.jpg'),
        'Trader':           CARD(4, "Trader", "Hinterlands", "Action - Reaction", './pictures/hinterlands/trader.jpg'),
        'Tunnel':           CARD(3, "Tunnel", "Hinterlands", "Victory - Reaction", './pictures/hinterlands/tunnel.jpg')
}
DarkAges_cards = {
        'Altar':            CARD(6, "Altar", "Dark Ages", "Action", './pictures/darkages/altar.jpg'),
        'Armory':           CARD(4, "Armory", "Dark Ages", "Action", './pictures/darkages/armory.jpg'),
        'BanditCamp':       CARD(5, "Bandit Camp", "Dark Ages", "Action", './pictures/darkages/banditcamp.jpg'),
        'BandOfMisfits':    CARD(5, "Band of Misfits", "Dark Ages", "Action", './pictures/darkages/bandofmisfits.jpg'),
        'Beggar':           CARD(2, "Beggar", "Dark Ages", "Action - Reaction", './pictures/darkages/beggar.jpg'),
        'Catacombs':        CARD(5, "Catacombs", "Dark Ages", "Action", './pictures/darkages/catacombs.jpg'),
        'Count':            CARD(5, "Count", "Dark Ages", "Action", './pictures/darkages/count.jpg'),
        'Counterfeit':      CARD(5, "Counterfeit", "Dark Ages", "Treasure", './pictures/darkages/counterfeit.jpg'),
        'Cultist':          CARD(5, "Cultist", "Dark Ages", "Action - Attack", './pictures/darkages/cultist.jpg'),
        'DameAnna':         CARD(5, "Dame Anna", "Dark Ages", "Action - Attack", './pictures/darkages/dameanna.jpg'),
        'DameJosephine':    CARD(5, "Dame Josephine", "Dark Ages", "Action - Attack - Victory", './pictures/darkages/damejosephine.jpg'),
        'DameMolly':        CARD(5, "Dame Molly", "Dark Ages", "Action - Attack", './pictures/darkages/damemolly.jpg'),
        'DameNatalie':      CARD(5, "Dame Natalie", "Dark Ages", "Action - Attack", './pictures/darkages/damenatalie.jpg'),
        'DameSylvia':       CARD(5, "Dame Sylvia", "Dark Ages", "Action - Attack", './pictures/darkages/damesylvia.jpg'),
        'DeathCart':        CARD(4, "Death Cart", "Dark Ages", "Action", './pictures/darkages/deathcart.jpg'),
        'Feodum':           CARD(4, "Feodum", "Dark Ages", "Victory", './pictures/darkages/feodum.jpg'),
        'Forager':          CARD(3, "Forager", "Dark Ages", "Action", './pictures/darkages/forager.jpg'),
        'Fortress':         CARD(4, "Fortress", "Dark Ages", "Action", './pictures/darkages/fortress.jpg'),
        'Graverobber':      CARD(5, "Grave Robber", "Dark Ages", "Action", './pictures/darkages/graverobber.jpg'),
        'Hermit':           CARD(3, "Hermit", "Dark Ages", "Action", './pictures/darkages/hermit.jpg'),
        'Hovel':            CARD(1, "Hovel", "Dark Ages", "Reaction - Shelter", './pictures/darkages/hovel.jpg'),
        'Ironmonger':       CARD(4, "Ironmonger", "Dark Ages", "Action", './pictures/darkages/ironmonger.jpg'),
        'JunkDealer':       CARD(5, "Junk Dealer", "Dark Ages", "Action", './pictures/darkages/junkdealer.jpg'),
        'Marauder':         CARD(4, "Marauder", "Dark Ages", "Action - Attack", './pictures/darkages/marauder.jpg'),
        'MarketSquare':     CARD(3, "Market Square", "Dark Ages", "Action - Reaction", './pictures/darkages/marketsquare.jpg'),
        'Mystic':           CARD(5, "Mystic", "Dark Ages", "Action", './pictures/darkages/mystic.jpg'),
        'Necropolis':       CARD(1, "Necropolis", "Dark Ages", "Action - Shelter", './pictures/darkages/necropolis.jpg'),
        'OvergrownEstate':  CARD(1, "Overgrown Estate", "Dark Ages", "Victory - Shelter", './pictures/darkages/overgrownestate.jpg'),
        'Pillage':          CARD(5, "Pillage", "Dark Ages", "Action - Attack", './pictures/darkages/pillage.jpg'),
        'PoorHouse':        CARD(1, "Poor House", "Dark Ages", "Action", './pictures/darkages/poorhouse.jpg'),
        'Processtion':      CARD(4, "Processtion", "Dark Ages", "Action", './pictures/darkages/procession.jpg'),
        'Rats':             CARD(4, "Rats", "Dark Ages", "Action", './pictures/darkages/rats.jpg'),
        'Rebuild':          CARD(5, "Rebuild", "Dark Ages", "Action", './pictures/darkages/rebuild.jpg'),
        'Rogue':            CARD(5, "Rogue", "Dark Ages", "Action - Attack", './pictures/darkages/rogue.jpg'),
        'Sage':             CARD(3, "Sage", "Dark Ages", "Action", './pictures/darkages/sage.jpg'),
        'Scavenger':        CARD(4, "Scavenger", "Dark Ages", "Action", './pictures/darkages/scavenger.jpg'),
        'SirBailey':        CARD(5, "Sir Bailey", "Dark Ages", "Action - Attack", './pictures/darkages/sirbailey.jpg'),
        'SirDestry':        CARD(5, "Sir Destry", "Dark Ages", "Action - Attack", './pictures/darkages/sirdestry.jpg'),
        'SirMartin':        CARD(5, "Sir Martin", "Dark Ages", "Action - Attack", './pictures/darkages/sirmartin.jpg'),
        'SirMichael':       CARD(5, "Sir Michael", "Dark Ages", "Action - Attack", './pictures/darkages/sirmichael.jpg'),
        'SirVander':        CARD(5, "Sir Vander", "Dark Ages", "Action - Attack", './pictures/darkages/sirvander.jpg'),
        'Squire':           CARD(2, "Squire", "Dark Ages", "Action", './pictures/darkages/squire.jpg'),
        'Storeroom':        CARD(3, "Storeroom", "Dark Ages", "Action", './pictures/darkages/storeroom.jpg'),
        'Urchin':           CARD(3, "Urchin", "Dark Ages", "Action - Attack", './pictures/darkages/urchin.jpg'),
        'Vagrant':          CARD(2, "Vagrant", "Dark Ages", "Action", './pictures/darkages/vagrant.jpg'),
        'WanderingMinstrel':CARD(4, "Wandering Minstrel", "Dark Ages", "Action", './pictures/darkages/wanderingminstrel.jpg')
}
Guilds_cards = {
        'Advisor':          CARD(4, "Advisor", "Guilds", "Action", './pictures/guilds/advisor.jpg'),
        'Baker':            CARD(5, "Baker", "Guilds", "Action", './pictures/guilds/baker.jpg'),
        'Butcher':          CARD(5, "Butcher", "Guilds", "Action", './pictures/guilds/butcher.jpg'),
        'CandlestickMaker': CARD(2, "Candlestick Maker", "Guilds", "Action", './pictures/guilds/candlestickmaker.jpg'),
        'Doctor':           CARD(3, "Doctor", "Guilds", "Action", './pictures/guilds/doctor.jpg'),
        'Herald':           CARD(4, "Herald", "Guilds", "Action", './pictures/guilds/herald.jpg'),
        'Journeyman':       CARD(5, "Journeyman", "Guilds", "Action", './pictures/guilds/journeyman.jpg'),
        'Masterpiece':      CARD(3, "Masterpiece", "Guilds", "Treasure", './pictures/guilds/masterpiece.jpg'),
        'MerchantGuild':    CARD(5, "Merchant Guild", "Guilds", "Action", './pictures/guilds/merchantguild.jpg'),
        'Plaza':            CARD(4, "Plaza", "Guilds", "Action", './pictures/guilds/plaza.jpg'),
        'Soothsayer':       CARD(5, "Soothsayer", "Guilds", "Action - Attack", './pictures/guilds/soothsayer.jpg'),
        'Stonemason':       CARD(2, "Stonemason", "Guilds", "Action", './pictures/guilds/stonemason.jpg'),
        'Taxman':           CARD(4, "Taxman", "Guilds", "Action - Attack", './pictures/guilds/taxman.jpg')
}
Adventures_cards = {
        '':            CARD(4, "", "Adventures", "Action", './pictures/adventures/.jpg'),
        '':            CARD(4, "", "Adventures", "Action", './pictures/adventures/.jpg'),
        '':            CARD(4, "", "Adventures", "Action", './pictures/adventures/.jpg'),
        '':            CARD(4, "", "Adventures", "Action", './pictures/adventures/.jpg'),
}
Empires_cards = {
        '':            CARD(4, "", "Empires", "Action", './pictures/empires/.jpg'),
        '':            CARD(4, "", "Empires", "Action", './pictures/empires/.jpg'),
        '':            CARD(4, "", "Empires", "Action", './pictures/empires/.jpg'),
        '':            CARD(4, "", "Empires", "Action", './pictures/empires/.jpg'),
}
Nocturne_cards = {
        '':            CARD(4, "", "Nocturne", "Action", './pictures/nocturne/.jpg'),
        '':            CARD(4, "", "Nocturne", "Action", './pictures/nocturne/.jpg'),
        '':            CARD(4, "", "Nocturne", "Action", './pictures/nocturne/.jpg'),
        '':            CARD(4, "", "Nocturne", "Action", './pictures/nocturne/.jpg'),
        '':            CARD(4, "", "Nocturne", "Action", './pictures/nocturne/.jpg'),
}









# ADD all expansions to the CARDS dictionary.
CARDS.update(Dominion_base_cards)
CARDS.update(Intrigue_cards)
CARDS.update(Seaside_cards)
CARDS.update(Alchemy_cards)
CARDS.update(Prosperity_cards)
CARDS.update(Hinterlands_cards)

# Make a list with all the card names in alphabetical order.
CARDNAMES = []
for name in CARDS:
    CARDNAMES.append(CARDS[name].name)
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
