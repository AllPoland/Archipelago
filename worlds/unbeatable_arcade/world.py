from collections.abc import Mapping
from typing import Any

from BaseClasses import Region
from worlds.AutoWorld import World

from . import songs, items, locations, rules, web_world
from .options import UNBEATABLEArcadeOptions

class UNBEATABLEArcadeWorld(World):
    """
    UNBEATABLE is a rhythm game where music is illegal and you do crimes.
    UNBEATABLE Arcade Mode is a gamemode separate from the story mode, where you can play songs from the game (and other places) to your heart's content.
    """

    game = "UNBEATABLE Arcade"

    web = web_world.UNBEATABLEArcadeWebWorld()

    options_dataclass = UNBEATABLEArcadeOptions
    options: UNBEATABLEArcadeOptions

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    
    item_name_to_id = items.ITEM_NAME_TO_ID
    item_name_groups = items.ITEM_NAME_GROUPS

    origin_region_name = "Arcade"

    def create_regions(self) -> None:
        # Since this is the first stage of generation, add our included songs here
        self.included_songs = songs.get_included_songs(self.options.use_breakout)

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