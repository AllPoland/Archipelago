# Dictionaries containing relevant info for each song in the game
# Each entry includes the name and the ratings for each difficulty (beginner, normal, hard, expert, unbeatable, star)
# Missing difficulties have a rating of -1

# All songs included with the base game
base_songs = [
    {"name":"<3", "b":3, "n":6, "h":9, "e":11, "u":15, "s":-1},
    {"name":"ball is infinite", "b":3, "n":8, "h":11, "e":13, "u":18, "s":-1},
    {"name":"bang", "b":5, "n":7, "h":10, "e":14, "u":18, "s":23},
    {"name":"beyond the heart (broken heart mix)", "b":2, "n":3, "h":8, "e":10, "u":14, "s":-1},
    {"name":"bookend song", "b":5, "n":10, "h":13, "e":17, "u":23, "s":-1},
    {"name":"bookend song - opening ver. -", "b":2, "n":5, "h":7, "e":10, "u":12, "s":-1},
    {"name":"call_home", "b":1, "n":5, "h":7, "e":10, "u":12, "s":-1},
    {"name":"ch2_dream1", "b":2, "n":6, "h":9, "e":11, "u":12, "s":-1},
    {"name":"ch2_dream2", "b":2, "n":5, "h":8, "e":10, "u":12, "s":-1},
    {"name":"ch2_dream3", "b":2, "n":4, "h":7, "e":9, "u":12, "s":-1},
    {"name":"ch4_dream1", "b":3, "n":7, "h":9, "e":11, "u":15, "s":-1},
    {"name":"ch4_dream2", "b":4, "n":7, "h":10, "e":12, "u":17, "s":-1},
    {"name":"cop trauma", "b":3, "n":7, "h":10, "e":13, "u":17, "s":-1},
    {"name":"cosmic starter", "b":2, "n":7, "h":10, "e":13, "u":20, "s":-1},
    {"name":"dialtone", "b":2, "n":8, "h":12, "e":15, "u":19, "s":-1},
    {"name":"disco disaster", "b":4, "n":7, "h":9, "e":12, "u":17, "s":-1},
    {"name":"done in love (from noisz sl)", "b":2, "n":7, "h":11, "e":14, "u":18, "s":-1},
    {"name":"drastic hammer", "b":3, "n":6, "h":9, "e":11, "u":13, "s":-1},
    {"name":"eating is living", "b":4, "n":6, "h":8, "e":11, "u":14, "s":22},
    {"name":"empty diary", "b":1, "n":4, "h":8, "e":10, "u":14, "s":-1},
    {"name":"empty diary - (soundcirclet rmx)", "b":4, "n":5, "h":10, "e":11, "u":16, "s":21},
    {"name":"familiar", "b":3, "n":4, "h":7, "e":11, "u":12, "s":-1},
    {"name":"familiar (acoustic)", "b":4, "n":6, "h":8, "e":10, "u":13, "s":-1},
    {"name":"familiar (brandon liew remix)", "b":4, "n":7, "h":11, "e":14, "u":20, "s":23},
    {"name":"familiar (live)", "b":1, "n":5, "h":8, "e":11, "u":15, "s":-1},
    {"name":"forever now", "b":1, "n":6, "h":10, "e":11, "u":15, "s":18},
    {"name":"forever now - (dog noise remix)", "b":5, "n":7, "h":9, "e":11, "u":17, "s":24},
    {"name":"forever when", "b":3, "n":7, "h":11, "e":12, "u":19, "s":-1},
    {"name":"future people", "b":2, "n":7, "h":9, "e":13, "u":14, "s":-1},
    {"name":"harm assault", "b":4, "n":8, "h":10, "e":13, "u":21, "s":-1},
    {"name":"infinity chase", "b":4, "n":9, "h":12, "e":15, "u":22, "s":-1},
    {"name":"k.moe (vip)", "b":4, "n":7, "h":9, "e":13, "u":16, "s":22},
    {"name":"loner", "b":2, "n":6, "h":8, "e":11, "u":14, "s":-1},
    {"name":"loner (live)", "b":3, "n":6, "h":8, "e":11, "u":15, "s":19},
    {"name":"low (nsr ending theme)", "b":5, "n":9, "h":11, "e":14, "u":17, "s":-1},
    {"name":"memorized", "b":3, "n":7, "h":10, "e":12, "u":15, "s":-1},
    {"name":"mirror", "b":2, "n":8, "h":9, "e":11, "u":16, "s":16},
    {"name":"mirror - kamome sano remix", "b":4, "n":9, "h":11, "e":13, "u":21, "s":-1},
    {"name":"neo elsewhere", "b":4, "n":7, "h":9, "e":12, "u":16, "s":-1},
    {"name":"no signal", "b":3, "n":7, "h":9, "e":12, "u":16, "s":-1},
    {"name":"om and on", "b":5, "n":9, "h":12, "e":15, "u":20, "s":22},
    {"name":"plastic hammer", "b":1, "n":5, "h":8, "e":10, "u":13, "s":-1},
    {"name":"pronto a molto", "b":3, "n":8, "h":11, "e":14, "u":21, "s":-1},
    {"name":"proper rhythm", "b":1, "n":4, "h":7, "e":10, "u":15, "s":-1},
    {"name":"proper rhythm - (must die! remix)", "b":3, "n":8, "h":9, "e":13, "u":17, "s":20},
    {"name":"proper rhythm (all there is to it)", "b":5, "n":9, "h":12, "e":15, "u":22, "s":24},
    {"name":"proper rhythm bootleg", "b":4, "n":8, "h":12, "e":15, "u":20, "s":24},
    {"name":"rest vs. beat", "b":5, "n":9, "h":12, "e":16, "u":23, "s":-1},
    {"name":"re-tuned", "b":1, "n":7, "h":12, "e":15, "u":20, "s":-1},
    {"name":"silent spiral", "b":4, "n":8, "h":11, "e":14, "u":21, "s":-1},
    {"name":"sleeping in", "b":2, "n":5, "h":11, "e":14, "u":18, "s":-1},
    {"name":"stolen", "b":2, "n":7, "h":10, "e":13, "u":17, "s":-1},
    {"name":"the adventures of clef the great, the coolest person you've ever met in your entire life, who you are only a speck of dust next to in the grand scheme of things, featuring treble sometimes. an-please, dear god, clef, this is not the final title of the song. we cannot put this on there. first of all, it's too long, and second of all, it's... i mean, this isn't a title. this is barely a collection of words you said out loud. uh yeah why is that a problem. it's... you know what, sure, yeah, okay, label guy, put this on there. literally print every word in our conversation. do you have a maximum length? you don't? what, really? we have other songs on this record. what's that g... you know what? no, it's fine. we're gonna do it, and keep this tape so that when she complains about it i can show her the evidence.", "b":3, "n":7, "h":9, "e":11, "u":14, "s":-1},
    {"name":"true (from noisz sl)", "b":5, "n":8, "h":10, "e":13, "u":21, "s":23},
    {"name":"twist sound", "b":4, "n":7, "h":9, "e":14, "u":17, "s":-1},
    {"name":"waiting", "b":2, "n":5, "h":8, "e":10, "u":14, "s":21},
    {"name":"waiting - lumena-tan remix", "b":1, "n":4, "h":7, "e":14, "u":19, "s":20},
    {"name":"war den", "b":5, "n":9, "h":12, "e":15, "u":19, "s":-1},
    {"name":"worn out tapes", "b":3, "n":6, "h":9, "e":13, "u":16, "s":-1},
    {"name":"worn out tapes [tally-ho! version]", "b":5, "n":7, "h":11, "e":14, "u":21, "s":25},
    {"name":"yeah yeah yeah yeah yeah yeah yeah yeah", "b":2, "n":7, "h":10, "e":13, "u":18, "s":20},
    {"name":"yeah yeah yeah yeah yeah yeah yeah yeah [trailer edit]", "b":2, "n":7, "h":11, "e":13, "u":20, "s":-1},
    {"name":"zero moment", "b":4, "n":8, "h":11, "e":15, "u":22, "s":25},
]

# All songs included with the breakout edition
breakout_songs = [
    {"name":"abab kababbab", "b":2, "n":8, "h":11, "e":14, "u":20, "s":-1},
    {"name":"afterburn", "b":1, "n":6, "h":9, "e":13, "u":17, "s":21},
    {"name":"afterburner", "b":4, "n":8, "h":11, "e":16, "u":22, "s":25},
    {"name":"binary reasoning", "b":3, "n":7, "h":10, "e":14, "u":18, "s":-1},
    {"name":"dear diary", "b":2, "n":5, "h":8, "e":11, "u":14, "s":-1},
    {"name":"forward operating bass", "b":3, "n":9, "h":12, "e":15, "u":22, "s":-1},
    {"name":"goin' crazy", "b":4, "n":8, "h":10, "e":13, "u":19, "s":-1},
    {"name":"hotel room 215 (feat. tenchio and postergirlxoxo)", "b":4, "n":7, "h":10, "e":12, "u":17, "s":20},
    {"name":"misery index", "b":4, "n":8, "h":12, "e":14, "u":17, "s":21},
    {"name":"square up", "b":4, "n":8, "h":11, "e":12, "u":18, "s":-1},
    {"name":"welcome to slamtown", "b":2, "n":7, "h":10, "e":13, "u":19, "s":-1},
]

# Contains alternate names for each song for hinting/searching
song_aliases = [
    {"name":"beyond the heart (broken heart mix)", "aliases":["beyond the heart"]},
    {"name":"done in love (from noisz sl)", "aliases":["done in love"]},
    {"name":"k.moe (vip)", "aliases":["k.moe"]},
    {"name":"the adventures of clef the great, the coolest person you've ever met in your entire life, who you are only a speck of dust next to in the grand scheme of things, featuring treble sometimes. an-please, dear god, clef, this is not the final title of the song. we cannot put this on there. first of all, it's too long, and second of all, it's... i mean, this isn't a title. this is barely a collection of words you said out loud. uh yeah why is that a problem. it's... you know what, sure, yeah, okay, label guy, put this on there. literally print every word in our conversation. do you have a maximum length? you don't? what, really? we have other songs on this record. what's that g... you know what? no, it's fine. we're gonna do it, and keep this tape so that when she complains about it i can show her the evidence.", "aliases":["the adventures of clef the great"]},
]

# All the songs in the entire game, this is used for defining IDs
all_songs = []
all_songs.extend(base_songs)
all_songs.extend(breakout_songs)


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


def get_included_songs(breakout: bool) -> list:
    included_songs = []
    included_songs.extend(base_songs)

    if breakout:
        # Include the breakout edition songs if the user has the DLC
        included_songs.extend(breakout_songs)

    return included_songs