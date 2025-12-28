from collections.abc import Mapping
from typing import Any

from BaseClasses import Region
from worlds.AutoWorld import World

from . import items
# Order here is important
# Locations and rules rely on data generated from importing items.py
from . import locations, rules
from . import options as unbeatable_arcade_options

class UNBEATABLEArcadeWorld(World):
    """
    UNBEATABLE is a rhythm game where music is illegal and you do crimes.
    UNBEATABLE Arcade Mode is a gamemode separate from the story mode, where you can play songs from the game (and other places) to your heart's content.
    """

    game = "UNBEATABLE Arcade"

    options_dataclass = unbeatable_arcade_options.UNBEATABLEArcadeOptions
    options: unbeatable_arcade_options.UNBEATABLEArcadeOptions

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    origin_region_name = "Arcade"

    def create_regions(self) -> None:
        # Only a single region for this world
        self.multiworld.regions = [Region(self.origin_region_name, self.player, self.multiworld)]
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