from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle

class TargetRating(Range):
    """
    The star rating you need to achieve to complete the randomizer.
    This is also used to calculate your expected performance for logic.
    You should set this to just a bit lower than the rating you have right now.
    """

    display_name = "Target Rating"

    range_start = 3
    range_end = 13

    default = 6


class UseBreakout(Toggle):
    """
    Enables songs included in UNBEATABLE - Breakout Edition.
    This requires that you own the UNBEATABLE - Breakout Edition Upgrade DLC and have it installed.
    """

    display_name = "Include Breakout Songs"

    default = False


class MinDifficulty(Choice):
    """
    Sets the first unlocked difficulty. Lower difficulties than this will be inacessible.
    Higher difficulties must be unlocked by finding 'Progressive Difficulty' items.
    The more difficulties there are between this and the hardest difficulty you can play,
    the longer the game will generally be.
    (You use Star difficulty as the minimum because some songs don't have one)
    """

    display_name = "Minimum Difficulty"

    option_beginner = 0
    option_normal = 1
    option_hard = 2
    option_expert = 3
    option_unbeatable = 4

    default = option_beginner


class StartSongCount(Range):
    """
    Sets how many songs to start with.
    """

    display_name = "Starting Songs"

    range_start = 1
    range_end = 10
    
    default = 2


class StartCharacterCount(Range):
    """
    Sets how many characters to start with.
    These are currently filler items, but some challenges will require certain characters later.
    """

    display_name = "Starting Characters"

    range_start = 1
    range_end = 11

    default = 1


class AllowPfc(Toggle):
    """
    When enabled, logic may expect you to get 100% accuracy on low-difficulty maps.
    """

    display_name = "Allow PFC"

    default = False


class AccCurveBias(Range):
    """
    Adjusts the slope of the expected accuracy curve.
    Higher values lead to higher expected accuracy on low-difficulty maps.
    It's probably best to leave this unchanged.
    """

    display_name = "Accuracy Curve Bias"

    range_start = 1
    range_end = 10

    default = 5.4


class AccCurveCutoff(Range):
    """
    Sets when the expected accuracy value starts tapering off.
    Low values generally lead to higher expected scores on high-difficulty maps.
    It's probably best to leave this unchanged.
    """

    display_name = "Accuracy Curve Start Point"

    range_start = 0
    range_end = 1

    default = 0.8


@dataclass
class UNBEATABLEArcadeOptions(PerGameCommonOptions):
    target_rating: TargetRating
    use_breakout: UseBreakout
    min_difficulty: MinDifficulty
    start_song_count: StartSongCount
    start_char_count: StartCharacterCount

    allow_pfc: AllowPfc
    acc_curve_bias: AccCurveBias
    acc_curve_cutoff: AccCurveCutoff