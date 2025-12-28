from BaseClasses import Location, Region

from . import songs
from .items import get_item_count, MAX_ITEMS
from .world import UNBEATABLEArcadeWorld

LOCATION_NAME_TO_ID = {}

class UNBEATABLEArcadeLocation(Location):
    game = "UNBEATABLE Arcade"


def populate_location_ids() -> None:
    # Generate a generic location ID entry for each item
    # We want to generate one for the maximum possible number of items
    LOCATION_NAME_TO_ID.clear()

    for i in range(0, MAX_ITEMS):
        LOCATION_NAME_TO_ID[f"Rating Unlock {i}"] = i


def add_location(world: UNBEATABLEArcadeWorld, region: Region, name: str, id: int) -> None:
    new_location = UNBEATABLEArcadeLocation(
        world.player, name, id, region
    )
    region.locations.append(new_location)


def create_all_locations(world: UNBEATABLEArcadeWorld) -> None:
    # We need to generate locations based on the number of items
    # So first, calculate the number of items
    if len(LOCATION_NAME_TO_ID < MAX_ITEMS):
        populate_location_ids()

    songs.set_included_songs(world.options.use_breakout)

    # Count up how many items (and therefore checks) we need
    item_count = get_item_count(world)

    # This is where challenge board checks will go later

    # Generate all of our locations
    region = world.get_region(world.origin_region_name)
    for i in range(0, item_count):
        add_location(world, region, f"Rating Unlock {i}", i)