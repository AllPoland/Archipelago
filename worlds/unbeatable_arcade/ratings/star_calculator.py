

def get_acc_power(acc: float) -> float:
    if acc <= 50:
        # Acc below 50 would result in weird negative stuff
        return 0
    
    return pow(acc - 50, 1.12)

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
    # Flat divisor applied to make ratings in the ranges the devs wanted
    divisor = 5625

    accPower = get_acc_power(acc)
    gradeBonus = get_grade_bonus(acc, fc, fail)

    rating = float(level) * (accPower + gradeBonus)
    return rating / divisor