from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import CollectionState, MultiWorld
from worlds.AutoWorld import LogicMixin
from worlds.generic.Rules import set_rule

from .game_info import GAME_NAME
from .items import get_item_count
from .locations import RATE_LOC_PREFIX
from .ratings.ratings_logic import get_target_rating, get_max_rating

if TYPE_CHECKING:
    from .world import UNBEATABLEArcadeWorld

class RatingState(LogicMixin):
    unbeatable_sorted_scores: dict[int, list]

    unbeatable_max_rating: dict[int, float]
    unbeatable_is_dirty: dict[int, bool]


    def init_mixin(self, multiworld: MultiWorld) -> None:
        self.unbeatable_sorted_scores = {
            player: [] for player in multiworld.get_game_players(GAME_NAME)
        }

        self.unbeatable_max_rating = {
            player: 0 for player in multiworld.get_game_players(GAME_NAME)
        }
        self.unbeatable_is_dirty = {
            player: False for player in multiworld.get_game_players(GAME_NAME)
        }

    
    def copy_mixin(self, new_state: CollectionState) -> CollectionState:
        new_state.unbeatable_sorted_scores = {
            player: list(entry.copy() for entry in scores) for player, scores in self.unbeatable_sorted_scores.items()
        }

        new_state.unbeatable_max_rating = {
            player: rating for player, rating in self.unbeatable_max_rating.items()
        }
        new_state.unbeatable_is_dirty = {
            player: dirty for player, dirty in self.unbeatable_is_dirty.items()
        }
        return new_state


def set_all_rules(world: UNBEATABLEArcadeWorld) -> None:
    target_rating = get_target_rating(world)

    item_count = get_item_count(world)
    player = world.player

    rating_step = target_rating / item_count
    curr_rating = rating_step

    for i in range(0, item_count):
        location = world.get_location(f"{RATE_LOC_PREFIX}{i + 1}")
        # print(f"{RATE_LOC_PREFIX}{i + 1}: {curr_rating}")
        set_rule(
            location,
            lambda state, loc_rating = curr_rating: get_max_rating(state, player) >= loc_rating
        )

        curr_rating += rating_step

    world.multiworld.completion_condition[world.player] = lambda state: state.can_reach_location(f"{RATE_LOC_PREFIX}{item_count}", player)