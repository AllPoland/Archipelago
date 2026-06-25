from worlds.unbeatable_arcade.options import UNBEATABLEArcadeOptions

CHARACTER_NAMES = [
    "Beat",
    "Beat (Hoodie)",
    "Beat (Guitar)",
    "Beat (Nothing)",
    "Beat (Up)",
    "Clef",
    "Quaver",
    "Quaver (Acoustic)",
    "Quaver (CQC)",
    "Treble",
    "Rest",
    "Rest (OMF)",
    "Eve",
    "Grace"
]

BREAKOUT_CHARACTER_NAMES = [
    "Crest",
    "Crest (Maid)",
    "DC",
    "Poco",
    "Apoco",
    "Penny",
    "Sforzando"
]

all_characters = []
all_characters.extend(CHARACTER_NAMES)
all_characters.extend(BREAKOUT_CHARACTER_NAMES)

def get_included_characters(options: UNBEATABLEArcadeOptions) -> list:
    included_characters = []
    included_characters.extend(CHARACTER_NAMES)

    # Apply DLC
    if options.use_breakout:
        # Include the breakout edition characters if the user has the DLC
        included_characters.extend(BREAKOUT_CHARACTER_NAMES)

    return included_characters