def ascii_art(result):
    win_art = """
__   _____  _   _  __        _____ _   _ _
\ \ / / _ \| | | | \ \      / /_ _| \ | | |
 \ V / | | | | | |  \ \ /\ / / | ||  \| | |
  | || |_| | |_| |   \ V  V /  | || |\  |_|
  |_| \___/ \___/     \_/\_/  |___|_| \_(_)
"""

    chance_art = """
  ____ _   _    _    _   _  ____ _____ _
 / ___| | | |  / \  | \ | |/ ___| ____| |
| |   | |_| | / _ \ |  \| | |   |  _| | |
| |___|  _  |/ ___ \| |\  | |___| |___|_|
 \____|_| |_/_/   \_\_| \_|\____|_____(_)
"""

    lose_art = """
__   _____  _   _   _     ___  ____  _____
\ \ / / _ \| | | | | |   / _ \/ ___|| ____|
 \ V / | | | | | | | |  | | | \___ \|  _|
  | || |_| | |_| | | |__| |_| |___) | |___ _ _ _
  |_| \___/ \___/  |_____\___/|____/|_____(_|_|_)
"""
    if result == 2:
        return win_art
    elif result == 1:
        return chance_art
    else:
        return lose_art

def cpu_art(num):
    patterns = {
        1: "          <<オートじゃんけん中！！！！>>          ",
        2: "         << オートじゃんけん中！！！！ >>         ",
        3: "        <<  オートじゃんけん中！！！！  >>        ",
        4: "       <<   オートじゃんけん中！！！！   >>       ",
        5: "      <<    オートじゃんけん中！！！！    >>      ",
        6: "     <<     オートじゃんけん中！！！！     >>     ",
        7: "    <<      オートじゃんけん中！！！！      >>    ",
        8: "   <<       オートじゃんけん中！！！！       >>   ",
        9: "  <<        オートじゃんけん中！！！！        >>  ",
        10: " <<         オートじゃんけん中！！！！         >> ",
    }
    return patterns[num]

if __name__ == "__main__":
    print(ascii_art(2))
