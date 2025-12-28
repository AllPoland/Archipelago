from BaseClasses import CollectionState

from . import star_calculator
from ..items import PROG_DIFF_NAME, SONG_PREFIX
from ..options import UNBEATABLEArcadeOptions

rating_per_map = 2 / 25


def difficulty_key_from_rank(difficulty: int) -> str:
    if difficulty <= 0:
        return "b"
    elif difficulty == 1:
        return "n"
    elif difficulty == 2:
        return "h"
    elif difficulty == 3:
        return "e"
    elif difficulty == 4:
        return "u"
    else:
        return "s"


def get_songs_with_ratings(songs: list, options: UNBEATABLEArcadeOptions) -> dict[str, list[float]]:
    rated_songs = {}

    target_rating = options.target_rating

    diff_count = 5 - options.min_difficulty

    allow_pfc = options.allow_pfc
    acc_curve_cutoff = options.acc_curve_cutoff
    acc_curve_bias = options.acc_curve_bias

    # Calculate the expected rating to be earned from each song in the list
    for song in songs:
        new_rating = []
        # Populate the rating entries with only the difficulties we'll unlock in the AP
        # This makes it easy to index the expected ratings by Progressive Difficulty inventory count
        for i in range(0, diff_count):
            diff_rank = options.min_difficulty + i
            diff_key = difficulty_key_from_rank(diff_rank)

            diff_level = song[diff_key]
            if diff_level < 0:
                # Negative values represent a nonexistent difficulty, so we can't get rating from this
                new_rating[i] = 0
                continue

            new_rating[i] = star_calculator.get_expected_acc_curve(
                target_rating, song[diff_key], acc_curve_cutoff, acc_curve_bias, allow_pfc
            )

        rated_songs[f"{SONG_PREFIX}{song["name"]}"] = new_rating

    return rated_songs


def get_max_rating(rated_songs: dict[str, list[float]], state: CollectionState, player: int) -> float:
    unlocked_difficulties = state.count(PROG_DIFF_NAME, player)

    # TODO: Find out how tf to make this work

    return 0