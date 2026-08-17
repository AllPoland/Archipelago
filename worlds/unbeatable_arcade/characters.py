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
    if "Breakout Edition" in options.use_dlc.value:
        included_characters.extend(BREAKOUT_CHARACTER_NAMES)

    if "The Jamie Paige Content Companion" in options.use_dlc.value:
        included_characters.extend(CONTENT_COMPANION_CHARACTER_NAMES)

    return included_characters