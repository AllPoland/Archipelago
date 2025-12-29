from .star_calculator import get_rating_from_play

diff_pow = 2

# An extra divisor to bring the rating ranges closer to vanilla
custom_divisor = 15


def get_custom_rating_from_play(level: float, acc: float, fc: bool, fail: bool) -> float:
    # Apply a power scaling to the level
    # This makes unlocking higher difficulties more impactful on logic
    adjusted_level = pow(level, diff_pow)
    return get_rating_from_play(adjusted_level, acc, fc, fail) / custom_divisor