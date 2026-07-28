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

CONTENT_COMPANION_CHARACTER_NAMES = [
    "JamieP",
    "Quaver (Shrimp)"
]

all_characters = []
all_characters.extend(CHARACTER_NAMES)
all_characters.extend(BREAKOUT_CHARACTER_NAMES)
all_characters.extend(CONTENT_COMPANION_CHARACTER_NAMES)

def get_included_characters(options: UNBEATABLEArcadeOptions) -> list:
    included_characters = []
    included_characters.extend(CHARACTER_NAMES)

    # Apply DLC
    for item_name in options.use_dlc.value:
        if item_name == "Breakout Edition":
            included_characters.extend(BREAKOUT_CHARACTER_NAMES)
        if item_name == "The Jamie Paige Content Companion":
            included_characters.extend(CONTENT_COMPANION_CHARACTER_NAMES)

    return included_characters