from collections.abc import Mapping
from typing import Any

from BaseClasses import CollectionState, Item, ItemClassification, Region
from worlds.AutoWorld import World

from . import songs, items, locations, rules, web_world
from .game_info import GAME_NAME
from .options import UNBEATABLEArcadeOptions
from .ratings import ratings_logic

class UNBEATABLEArcadeWorld(World):
    """
    UNBEATABLE is a rhythm game where music is illegal and you do crimes.
    UNBEATABLE Arcade Mode is a gamemode separate from the story mode, where you can play songs from the game (and other places) to your heart's content.
    """

    game = GAME_NAME

    web = web_world.UNBEATABLEArcadeWebWorld()

    options_dataclass = UNBEATABLEArcadeOptions
    options: UNBEATABLEArcadeOptions

    location_name_to_id = locations.LOCATION_NAME_TO_ID

    item_name_to_id = items.ITEM_NAME_TO_ID
    item_name_groups = items.ITEM_NAME_GROUPS

    origin_region_name = "Arcade"

    included_songs: list
    rated_songs: dict[str, dict[int, float]]


    def generate_early(self) -> None:
        # Since this is the first stage of generation, add our included songs here
        self.included_songs = songs.get_included_songs(self.options.use_breakout)

        # Precalculate the expected rating gains per-map
        # This is stored as a dictionary indexed by song item names,
        # then a list of ratings indexed by Progressive Difficulty count
        self.rated_songs = ratings_logic.get_songs_with_ratings(self.included_songs, self.options)


    def create_regions(self) -> None:
        # Only a single region for this world
        self.multiworld.regions += [Region(self.origin_region_name, self.player, self.multiworld)]
        locations.create_all_locations(self)


    def set_rules(self) -> None:
        rules.set_all_rules(self)
    

    def create_items(self) -> None:
        items.create_all_items(self)
    

    def create_item(self, name: str) -> items.UNBEATABLEArcadeItem:
        return items.create_item_with_classification(self, name)


    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)


    def fill_slot_data(self) -> Mapping[str, Any]:
        return self.options.as_dict(
            "target_rating",
            "use_breakout",
            "min_difficulty"
        )
    

    def collect(self, state: CollectionState, item: Item) -> bool:
        change = super().collect(state, item)

        if change:
            if item.name in self.item_name_groups["songs"]:
                print(f"Added: {item.name}")
                ratings_logic.add_song(state, self.player, self.rated_songs, item.name)
                print(ratings_logic.get_max_rating(state, self.player))
                # print(list(reversed(state.unbeatable_sorted_scores[self.player])))
        
        return change
    

    def remove(self, state: CollectionState, item: Item) -> bool:
        change = super().remove(state, item)

        if change:
            if item.name in self.item_name_groups["songs"]:
                ratings_logic.remove_song(state, self.player, item.name)
        
        return change