from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import CollectionState
from worlds.generic.Rules import add_rule, set_rule

from . import songs
from .items import get_item_count
from .ratings.ratings_logic import get_songs_with_ratings, get_max_rating

if TYPE_CHECKING:
    from .world import UNBEATABLEArcadeWorld


def set_all_rules(world: UNBEATABLEArcadeWorld) -> None:
    # Precalculate the expected rating gains per-map
    # This is stored as a dictionary indexed by song item names,
    # then a list of ratings indexed by Progressive Difficulty count
    rated_songs = get_songs_with_ratings(world.included_songs, world.options)
    
    target_rating = world.options.target_rating
    world.multiworld.completion_condition[world.player] = lambda state: get_max_rating(rated_songs, state) >= target_rating