import bisect

from BaseClasses import CollectionState

from . import star_calculator
from ..items import SONG_PREFIX
from ..options import UNBEATABLEArcadeOptions
from ..songs import difficulty_key_from_rank

rating_per_map = 2 / 25
expected_fail_threshold = 55


def get_songs_with_ratings(songs: list, options: UNBEATABLEArcadeOptions) -> dict[str, dict[int, float]]:
    rated_songs = {}

    target_rating = float(options.target_rating) / 100
    skill_rating = target_rating + (float(options.actual_rating_diff) / 100)

    diff_count = 5 - options.min_difficulty

    allow_pfc = options.allow_pfc
    acc_curve_cutoff = float(options.acc_curve_cutoff) / 100
    acc_curve_bias = float(options.acc_curve_bias) / 100

    # Calculate the expected rating to be earned from each song in the list
    for song in songs:
        new_rating = {}
        # Populate the rating entries with only the difficulties we'll unlock in the AP
        # This makes it easy to index the expected ratings by Progressive Difficulty inventory count
        for i in range(0, diff_count + 1):
            diff_rank = options.min_difficulty + i
            diff_key = difficulty_key_from_rank(diff_rank)

            diff_level = song[diff_key]
            if diff_level < 0:
                # Negative values represent a nonexistent difficulty, so we can't get rating from this
                new_rating[diff_rank] = -1
                continue

            expected_acc = star_calculator.get_expected_acc_curve(
                skill_rating, diff_level, acc_curve_cutoff, acc_curve_bias, allow_pfc
            )
            expected_rating = star_calculator.get_rating_from_play(
                diff_level, expected_acc, False, expected_acc < expected_fail_threshold
            )
            new_rating[diff_rank] = expected_rating

        rated_songs[f"{SONG_PREFIX}{song["name"]}"] = new_rating

    return rated_songs


def set_state_dirty(state: CollectionState, player: int) -> None:
    state.unbeatable_is_dirty[player] = True


def get_max_rating(state: CollectionState, player: int) -> float:
    if not state.unbeatable_is_dirty[player]:
        return state.unbeatable_max_rating[player]
    
    scores = state.unbeatable_sorted_scores[player]

    unlocked_difficulties = 0
    score_rating = 0
    for entry in reversed(scores):
        unlocked_difficulties += 1
        score_rating += entry["rating"]
        if unlocked_difficulties >= 25:
            # Only the top 25 difficulties count
            break

    progress_rating = min(unlocked_difficulties, 25) * rating_per_map

    max_rating = score_rating + progress_rating
    state.unbeatable_max_rating[player] = max_rating
    state.unbeatable_is_dirty[player] = False

    return max_rating


def add_song(state: CollectionState, player: int, rated_songs: dict[str, dict[int, float]], song_name: str) -> None:
    # Insert all the difficulties added by the song
    unlocked_rank = state.count(song_name, player)

    rated_song = rated_songs[song_name]
    rating = rated_song[unlocked_rank]

    # Add this difficulty to our unlocked scores, in ascending order
    # This format makes it easiest to calculate our max rating
    new_entry = {
        "name": song_name,
        "rank": unlocked_rank,
        "rating": rating
    }
    bisect.insort(state.unbeatable_sorted_scores[player], new_entry, key=lambda x: x["rating"])

    set_state_dirty(state, player)


def remove_song(state: CollectionState, player: int, song_name: str) -> None:
    removed_rank = state.count(song_name, player) + 1

    to_remove = None
    for entry in state.unbeatable_sorted_scores[player]:
        if entry["name"] == song_name and entry["rank"] == removed_rank:
            to_remove = entry
            break

    if to_remove:
        # Remove the entry while we aren't traversing the target list
        state.unbeatable_sorted_scores[player].remove(to_remove)

    set_state_dirty(state, player)