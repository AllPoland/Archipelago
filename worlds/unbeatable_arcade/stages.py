from worlds.unbeatable_arcade.options import UNBEATABLEArcadeOptions

STAGE_NAMES = [
    "train_station.",
    "stadium_(past).",
    "stadium_(present).",
    "dreamscape.",
    "prison_yard.",
    "train.",
    "lighthouse_show.",
    "city_hideout.",
    "recording_studio.",
    "overpass.",
    "city_center.",
    "underground_show.",
    "alleyway_show.",
    "warehouse_show.",
    "harm_hq_lobby.",
    "zero_moment_array.",
    "zm_test_chamber.",
    "graveyard.",
    "nsr.",
    "greenscreen.",
    "playback."
]
#Placeholder until DLC releases
CONTENT_COMPANION_STAGE_NAMES = [
    "Apple Orchard",
    "Wrestling Arena"
]

all_stages = []
all_stages.extend(STAGE_NAMES)
all_stages.extend(CONTENT_COMPANION_STAGE_NAMES)

def get_included_stages(options: UNBEATABLEArcadeOptions) -> list:
    included_stages = []
    included_stages.extend(STAGE_NAMES)

    # Apply DLC
    for item_name in options.use_dlc.value:
        if item_name == "The Jamie Paige Content Companion":
            included_stages.extend(CONTENT_COMPANION_STAGE_NAMES)

    return included_stages
