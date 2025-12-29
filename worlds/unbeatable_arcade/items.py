from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

from . import songs
from .game_info import GAME_NAME
from .songs import difficulty_key_from_rank

if TYPE_CHECKING:
    from .world import UNBEATABLEArcadeWorld

DEFAULT_CLASSIFICATIONS = {
    "Song": ItemClassification.progression_deprioritized_skip_balancing,
    # "Difficulty": ItemClassification.progression,
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

# PROG_DIFF_NAME = "Progressive Difficulty"
# This isn't a real item, but UNBEATABLE has no infinite filler items
FILLER_NAME = "Worn Out Tape"

SONG_PREFIX = "Progressive Song: "
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

    # ITEM_NAME_TO_ID[PROG_DIFF_NAME] = curr_id
    # curr_id += 1
    ITEM_NAME_TO_ID[FILLER_NAME] = curr_id

pre_calc_items()

ITEM_NAME_GROUPS = {
    "songs": set(f"{SONG_PREFIX}{entry["name"]}" for entry in songs.all_songs),
    "characters": set(CHARACTER_NAMES),
    # "progression": {PROG_DIFF_NAME},
    "traps": set(TRAP_NAMES),
    "filler": {FILLER_NAME}
}


class UNBEATABLEArcadeItem(Item):
    game = GAME_NAME


def get_max_items():
    # There are a maximum of 5 progressive difficulties
    count = len(songs.all_songs) * 5
    count += len(CHARACTER_NAMES)

    return count


def get_random_filler_item_name(world: UNBEATABLEArcadeWorld) -> str:
    return FILLER_NAME


def create_item_with_classification(world: UNBEATABLEArcadeWorld, name: str) -> UNBEATABLEArcadeItem:
    classification = ItemClassification.filler
    item_id = 0
    
    if name in ITEM_NAME_TO_ID:
        item_id = ITEM_NAME_TO_ID[name]

    # if name == PROG_DIFF_NAME:
    #     classification = DEFAULT_CLASSIFICATIONS["Difficulty"]
    if name in TRAP_NAMES:
        classification = DEFAULT_CLASSIFICATIONS["Trap"]
    elif name in CHARACTER_NAMES:
        classification = DEFAULT_CLASSIFICATIONS["Character"]
    elif any(f"{SONG_PREFIX}{song["name"]}" == name for song in songs.all_songs):
        classification = DEFAULT_CLASSIFICATIONS["Song"]

    return UNBEATABLEArcadeItem(name, classification, item_id, world.player)


def get_item_count(world: UNBEATABLEArcadeWorld) -> int:
    # Min difficulty ranges from 0 - 4. We just need enough progressive
    # diffs to go from min difficulty to star
    progressive_diff_count = 5 - world.options.min_difficulty

    item_count = 0
    for song in world.included_songs:
        for i in range(0, progressive_diff_count):
            # Damn you off by one error
            diff_rank = i + world.options.min_difficulty + 1
            diff_key = difficulty_key_from_rank(diff_rank)
            if song[diff_key] < 0:
                continue
            
            item_count += 1

    item_count += len(CHARACTER_NAMES)
    
    # item_count += progressive_diff_count

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

    item_pool: list[Item] = []

    # Min difficulty ranges from 0 to 4. We just need enough progressive
    # diffs to go from min difficulty to star
    progressive_diff_count = 5 - world.options.min_difficulty

    # for i in range(0, progressive_diff_count):
    #     item_pool.append(world.create_item(PROG_DIFF_NAME))

    for song in world.included_songs:
        song_item_name = f"{SONG_PREFIX}{song["name"]}"
        for i in range(0, progressive_diff_count):
            if i == 0 and song["name"] in start_song_names:
                continue

            # Damn you off by one error
            diff_rank = i + world.options.min_difficulty + 1
            diff_key = difficulty_key_from_rank(diff_rank)
            if song[diff_key] < 0:
                continue
            
            item_pool.append(world.create_item(song_item_name))

    for char in CHARACTER_NAMES:
        if char in start_char_names:
            continue

        char_item_name = f"{CHAR_PREFIX}{char}"
        item_pool.append(world.create_item(char_item_name))

    # Trap items to be added later

    # Forcing a progressive difficulty helps with the restrictive start inherent to this AP
    # world.multiworld.local_early_items[world.player][PROG_DIFF_NAME] = 1

    world.multiworld.itempool += item_pool