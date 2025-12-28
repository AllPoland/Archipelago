from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

from . import songs

if TYPE_CHECKING:
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

SONG_PREFIX = "Song: "
CHAR_PREFIX = "Character: "

# IDs are generated based on the lists so that it's not a nightmare to maintain game updates
ITEM_NAME_TO_ID = {}

def pre_calc_items() -> None:
    curr_id = 1
    for song in songs.all_songs:
        ITEM_NAME_TO_ID[f"{SONG_PREFIX}{song["name"]}"] = curr_id
        curr_id += 1

    for char in CHARACTER_NAMES:
        ITEM_NAME_TO_ID[f"{CHAR_PREFIX}{char}"] = curr_id
        curr_id += 1
    
    for trap in TRAP_NAMES:
        ITEM_NAME_TO_ID[trap] = curr_id
        curr_id += 1

    ITEM_NAME_TO_ID[PROG_DIFF_NAME] = curr_id
    curr_id += 1
    ITEM_NAME_TO_ID[FILLER_NAME] = curr_id

pre_calc_items()

ITEM_NAME_GROUPS = {
    "songs": set(),
    "characters": set(),
    "progression": set(),
    "traps": set()
}


class UNBEATABLEArcadeItem(Item):
    game = "UNBEATABLE Arcade"


def get_max_items():
    count = len(songs.all_songs)
    count += len(CHARACTER_NAMES)

    # There are a maximum of 5 progressive difficulties
    count += 5
    return count


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
    item_count = len(world.included_songs)
    item_count += len(CHARACTER_NAMES)
    
    # Min difficulty ranges from 0 - 4. We just need enough progressive
    # diffs to go from min difficulty to star
    progressive_diff_count = 5 - world.options.min_difficulty
    item_count += progressive_diff_count

    # Starting items are removed from the pool
    item_count -= world.options.start_song_count
    item_count -= world.options.start_char_count

    return item_count


def create_all_items(world: UNBEATABLEArcadeWorld) -> None:
    # Grant the player's starting songs
    start_song_count = world.options.start_song_count
    start_song_names = []
    for i in range(0, start_song_count):
        new_song_name = world.random.choice(world.included_songs)["name"]
        while new_song_name in start_song_names:
            # In case we roll the same song twice, just roll again
            new_song_name = world.random.choice(world.included_songs)["name"]

        start_song_names.append(new_song_name)

        song_item_name = f"{SONG_PREFIX}{new_song_name}"
        new_song = world.create_item(song_item_name)
        world.push_precollected(new_song)

    # Grant the player's starting characters
    start_char_count = world.options.start_char_count
    start_char_names = []
    for i in range(0, start_char_count):
        new_char_name = world.random.choice(CHARACTER_NAMES)
        while new_char_name in start_char_names:
            new_char_name = world.random.choice(CHARACTER_NAMES)

        start_char_names.append(new_char_name)

        char_item_name = f"{CHAR_PREFIX}{new_char_name}"
        new_char = world.create_item(char_item_name)
        world.push_precollected(new_char)

    songs: list[Item] = []
    for song in world.included_songs:
        if song["name"] in start_song_names:
            continue

        song_item_name = f"{SONG_PREFIX}{song["name"]}"
        songs.append(world.create_item(song_item_name))

    characters: list[Item] = []
    for char in CHARACTER_NAMES:
        if char in start_char_names:
            continue

        char_item_name = f"{CHAR_PREFIX}{char}"
        characters.append(world.create_item(char_item_name))

    # Min difficulty ranges from 0 - 4. We just need enough progressive
    # diffs to go from min difficulty to star
    progression: list[Item] = []
    progressive_diff_count = 5 - world.options.min_difficulty
    for i in range(0, progressive_diff_count):
        progression.append(world.create_item(PROG_DIFF_NAME))

    # Trap items to be added later

    # Create item groups
    ITEM_NAME_GROUPS["songs"] = set(songs)
    ITEM_NAME_GROUPS["characters"] = set(characters)
    ITEM_NAME_GROUPS["progression"] = set(progression)

    world.multiworld.itempool += songs + characters + progression