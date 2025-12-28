import math

# Flat divisor applied to make ratings in the ranges the devs wanted
rating_divisor = 5625
acc_pow = 1.12

# Maximum rating value it's possible to earn - used for curving expected acc
max_score_rating = pow(50, acc_pow) + 25

# The minimum and maximum rating values for each grade
rating_ranges = [
    {"min":10, "max":pow(15, acc_pow) + 10, "gmod":10},                    # D or HOW
    {"min":pow(15, acc_pow) + 12, "max":pow(25, acc_pow) + 12, "gmod":12}, # C
    {"min":pow(25, acc_pow) + 15, "max":pow(35, acc_pow) + 15, "gmod":15}, # B
    {"min":pow(35, acc_pow) + 20, "max":pow(40, acc_pow) + 20, "gmod":20}, # A
    {"min":pow(40, acc_pow) + 25, "max":float("inf"), "gmod":25}  # S
]


def get_acc_power(acc: float) -> float:
    if acc <= 50:
        # Acc below 50 would result in weird negative stuff
        return 0
    
    return pow(acc - 50, acc_pow)


def get_grade_bonus(acc: float, fc: bool, fail: bool) -> int:
    if fail:
        # No grade bonus for an F
        return 0

    if fc:
        # Game gives a 1% accuracy bonus for this part if you FC
        acc += 1
    
    if acc > 90:
        return 25
    elif acc > 85:
        # A rank
        return 20
    elif acc > 75:
        # B rank
        return 15
    elif acc > 65:
        # C rank
        return 12
    else:
        # D or HOW rank
        return 10


def get_rating_from_play(level: int, acc: float, fc: bool, fail: bool) -> float:

    accPower = get_acc_power(acc)
    gradeBonus = get_grade_bonus(acc, fc, fail)

    rating = float(level) * (accPower + gradeBonus)
    return rating / rating_divisor


def get_expected_acc(target_rating: float, level: int) -> float:
    # The portion of rating that must come from song scores
    # 2 stars come from flat completion, the rest come from 25 top plays
    required_rating_from_songs = float(rating_divisor) * (target_rating - 2) / 25
    required_score_rating = required_rating_from_songs / level
    
    # Check the grade ranges to determine which grade bonus we're working with
    required_acc_rating = 0
    for grade in rating_ranges:
        if grade["min"] >= required_score_rating:
            # Our required score falls inside a gap, so just use this minimum
            required_acc_rating = grade["min"] - grade["gmod"]
            break

        if grade["max"] >= required_score_rating:
            required_acc_rating = required_score_rating - grade["gmod"]
            break

    # Now that we know how much acc rating we need, we can calculate the exact acc
    return pow(required_acc_rating, 1 / acc_pow) + 50


def get_expected_acc_curve(target_rating: float, level: int, curve_cutoff: float, bias: float, allow_pfc: bool) -> float:
    raw_acc = get_expected_acc(target_rating, level) / 100

    # Apply a curve based on the maximum rating possible on the map
    # The curve starts linear until a certain point, then it turns to an exponential with a vertical asymptote
    # This avoids expecting the player to get over 100%, which isn't possible
    # and adds some leniency so the player doesn't get skill stuck as much
    max_acc = 1 if allow_pfc else 0.99
    acc_epsilon = 1 - max_acc

    curve_range = 1 - curve_cutoff - acc_epsilon

    # range + cutoff - range * e^( -bias(acc01 - cutoff) )
    exponent = -bias * (raw_acc - curve_cutoff)
    return curve_range + curve_cutoff - (curve_range * math.exp(exponent))