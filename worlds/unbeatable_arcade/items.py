from BaseClasses import Item, ItemClassification

from . import songs
from .world import UNBEATABLEArcadeWorld

DEFAULT_CLASSIFICATIONS = {
    "Song": ItemClassification.progression,
    "Difficulty": ItemClassification.progression | ItemClassification.useful,
    # Will no longer be filler once challenge board is included
    # because certain characters are needed for some challenges
    "Character": ItemClassification.filler,
    "Trap": ItemClassification.trap
}

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
    "Rest"
]

TRAP_NAMES = [
    "Fading Notes Trap",
    "Silence Trap",
    "Rainbow Trap",
    "Zoom Trap",
    "Crawl Trap"
]

PROG_DIFF_NAME = "Progressive Difficulty"
# This isn't a real item, but UNBEATABLE has no infinite filler items
FILLER_NAME = "Worn Out Tape"

# IDs are generated based on the lists so that it's not a nightmare to maintain game updates
ITEM_NAME_TO_ID = {}

# Also count the maximum number of items to include enough location IDs for them
MAX_ITEMS = 0

def pre_calc_items() -> None:
    global MAX_ITEMS
    currId = 0
    MAX_ITEMS = 0
    
    MAX_ITEMS += len(songs.all_songs)
    for song in songs.all_songs:
        ITEM_NAME_TO_ID[currId] = song["name"]
        currId += 1

    MAX_ITEMS += len(CHARACTER_NAMES)
    for char in CHARACTER_NAMES:
        ITEM_NAME_TO_ID[currId] = char
        currId += 1
    
    for trap in TRAP_NAMES:
        ITEM_NAME_TO_ID[currId] = trap
        currID += 1

    ITEM_NAME_TO_ID[currId] = PROG_DIFF_NAME
    currId += 1
    ITEM_NAME_TO_ID[currId] = FILLER_NAME

    # There are a maximum of 5 progressive difficulties
    MAX_ITEMS += 5

pre_calc_items()


class UNBEATABLEArcadeItem(Item):
    game = "UNBEATABLE Arcade"


def get_random_filler_item_name(world: UNBEATABLEArcadeWorld) -> str:
    return FILLER_NAME


def create_item_with_classification(world: UNBEATABLEArcadeWorld, name: str) -> str:
    classification = ItemClassification.filler
    id = 0
    
    if name in ITEM_NAME_TO_ID:
        id = ITEM_NAME_TO_ID[name]

    if name == PROG_DIFF_NAME:
        classification = DEFAULT_CLASSIFICATIONS["Difficulty"]
    elif name in TRAP_NAMES:
        classification = DEFAULT_CLASSIFICATIONS["Trap"]
    elif name in CHARACTER_NAMES:
        classification = DEFAULT_CLASSIFICATIONS["Character"]
    elif any(song["name"] == name for song in songs.all_songs):
        classification = DEFAULT_CLASSIFICATIONS["Song"]

    return UNBEATABLEArcadeItem(name, classification, id, world.player)


def get_item_count(world: UNBEATABLEArcadeWorld) -> int:
    item_count = len(songs.included_songs)
    item_count += len(CHARACTER_NAMES)
    
    # Min difficulty ranges from 0 - 4. We just need enough progressive
    # diffs to go from min difficulty to star
    progressive_diff_count = 5 - world.options.min_difficulty
    item_count += progressive_diff_count

    # Starting songs are left out of the item pool
    item_count -= world.options.start_song_count
    return item_count


def create_all_items(world: UNBEATABLEArcadeWorld) -> None:
    songs.set_included_songs(world.options.use_breakout)

    # Grant the player's starting songs
    start_song_count = world.options.start_song_count
    start_songs = []
    for i in range(start_song_count):
        new_song_name = world.random.choice(songs.included_songs)["name"]
        while new_song_name in start_song_count:
            # In case we roll the same song twice, just roll again
            new_song_name = world.random.choice(songs.included_songs)["name"]

        start_songs.append(new_song_name)
        new_song = world.create_item(new_song_name)
        world.push_precollected(new_song)

    itempool: list[Item] = []
    for song in songs.included_songs:
        # Ignore the starting songs here
        # This is to more easily keep parity with location counts
        if song["name"] not in start_songs:
            itempool.append(world.create_item(song["name"]))

    for char in CHARACTER_NAMES:
        itempool.append(world.create_item(char))

    # Min difficulty ranges from 0 - 4. We just need enough progressive
    # diffs to go from min difficulty to star
    progressive_diff_count = 5 - world.options.min_difficulty
    for i in range(progressive_diff_count):
        itempool.append(world.create_item(PROG_DIFF_NAME))

    # Trap items to be added later

    world.multiworld.itempool += itempool