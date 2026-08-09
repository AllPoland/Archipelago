from worlds.unbeatable_arcade.options import UNBEATABLEArcadeOptions
from .song_list import base_songs, breakout_songs, content_companion_songs, breakout_content_songs, all_songs

# Contains alternate names for some songs for hinting/searching
song_aliases = [
    {"name":"the adventures of clef the great, the coolest person you've ever met in your entire life, who you are only a speck of dust next to in the grand scheme of things, featuring treble sometimes. an-please, dear god, clef, this is not the final title of the song. we cannot put this on there. first of all, it's too long, and second of all, it's...i mean, this isn't a title. this is barely a collection of words you said out loud. uh yeah why is that a problem. it's...you know what, sure. yeah, okay, label guy, put this on there. literally print every word in our conversation. do you have a maximum length? you don't? what, really? we have other songs on this record. what's that g...you know what? no, it's fine. we're gonna do it. and keep this tape so that when she complains about it i can show her the evidence.", "aliases":["the adventures of clef the great"]}
]

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


def get_included_songs(options: UNBEATABLEArcadeOptions) -> list:
    included_songs = []
    included_songs.extend(base_songs)

    breakout=False
    content_companion=False

    # Apply DLC
    for item_name in options.use_dlc.value:
        if item_name == "Breakout Edition":
            included_songs.extend(breakout_songs)
            breakout=True
        if item_name == "The Jamie Paige Content Companion":
            included_songs.extend(content_companion_songs)
            content_companion=True
    
    if(breakout and content_companion):
        included_songs.extend(breakout_content_songs)

    # Apply blacklist
    included_songs = list(filter(lambda song: song["name"] not in options.song_blacklist.value, included_songs))

    return included_songs
