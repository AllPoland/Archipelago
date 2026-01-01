from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle


class SkillRating(Range):
    """
    Your STAR rating.
    This is also used to calculate your expected accuracy on each map for logic.
    You should set this to just a little bit lower than the STAR rating you have in the vanilla game right now.
    NOTE: this represents the value multiplied by 100. For example, if want to set a rating of 5.63, set this to 563.
    """

    display_name = "Star Rating"

    range_start = 300
    range_end = 1300

    default = 600


class MaxDifficulty(Choice):
    """
    Sets the highest difficulty to unlock.
    Difficulties above this will be inaccessible during the randomizer.
    You should set this to the highest difficulty you can consistently pass.
    """

    display_name = "Maximum Difficulty"

    option_beginner = 0
    option_normal = 1
    option_hard = 2
    option_expert = 3
    option_unbeatable = 4
    option_star = 5

    default = option_star


class MinDifficulty(Choice):
    """
    Sets the first unlocked difficulty. Lower difficulties than this will be inacessible.
    Higher difficulties must be unlocked by finding 'Progressive Difficulty' items.
    The more difficulties there are between this and Maximum Difficulty,
    the longer the game will generally be.
    (You also can't use Star difficulty as the minimum because some songs don't have one.)
    """

    display_name = "Minimum Difficulty"

    option_beginner = 0
    option_normal = 1
    option_hard = 2
    option_expert = 3
    option_unbeatable = 4

    default = option_beginner


class CompletionPercent(Range):
    """
    Sets how much of the game you need to play to complete the randomizer.
    Lower values make logic more lenient but can lead to pacing issues.
    If you want a shorter randomizer, consider increasing Minimum Difficulty first.
    """

    display_name = "Completion Percentage"

    range_start = 1
    range_end = 100

    default = 90


class UseBreakout(Toggle):
    """
    Enables songs included in UNBEATABLE - Breakout Edition.
    This requires that you own the UNBEATABLE - Breakout Edition Upgrade DLC and have it installed.
    """

    display_name = "Include Breakout Songs"

    default = False


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

    default = True


class AccCurveBias(Range):
    """
    Adjusts the slope of the expected accuracy curve.
    Higher values lead to higher expected accuracy on low-difficulty maps.
    It's probably best to leave this unchanged.
    """

    display_name = "Accuracy Curve Bias"

    range_start = 0
    range_end = 1000

    default = 250


class AccCurveCutoff(Range):
    """
    Sets when the expected accuracy value starts tapering off.
    Low values tend to lead to higher expected accuracy on high-difficulty maps.
    It's probably best to leave this unchanged.
    """

    display_name = "Accuracy Curve Start Point"

    range_start = 0
    range_end = 100

    default = 80


@dataclass
class UNBEATABLEArcadeOptions(PerGameCommonOptions):
    use_breakout: UseBreakout
    max_difficulty: MaxDifficulty
    min_difficulty: MinDifficulty
    completion_percent: CompletionPercent
    start_song_count: StartSongCount
    start_char_count: StartCharacterCount

    skill_rating: SkillRating
    allow_pfc: AllowPfc
    acc_curve_bias: AccCurveBias
    acc_curve_cutoff: AccCurveCutoff


option_groups = [
    OptionGroup(
        "Gameplay Options",
        [MaxDifficulty, MinDifficulty, CompletionPercent, StartSongCount, StartCharacterCount, UseBreakout]
    ),
    OptionGroup(
        "Difficulty Options",
        [SkillRating, AllowPfc]
    ),
    OptionGroup(
        "Advanced Options",
        [AccCurveBias, AccCurveCutoff]
    )
]