from .star_calculator import get_rating_from_play

diff_pow = 2
score_falloff_base = 0.965


def get_custom_rating_from_play(level: float, acc: float, fc: bool, fail: bool) -> float:
    # Apply a power scaling to the level
    # This makes unlocking higher difficulties more impactful on logic
    adjusted_level = pow(level, diff_pow)
    return get_rating_from_play(adjusted_level, acc, fc, fail)


def get_score_contribution(score_rating: float, score_idx: int) -> float:
    return (pow(score_falloff_base, score_idx) * score_rating)