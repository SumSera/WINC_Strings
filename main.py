# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
"""Assignment: Strings
PART 1"""

# 1. players that scored in this final.
scorer_name_0 = 'Ruud Gullit'
scorer_name_1 = 'Marco van Basten'

# 2. time the goals were scored (in playtime minutes).
goal_0 = 32
goal_1 = 54

# 3. here is the string
scorers = scorer_name_0 + ' '+ str(goal_0)+ ', ' + scorer_name_1 + ' ' + str(goal_1)
#print(scorers)

# 4.
report = f'{scorer_name_0} scored in the {goal_0}nd minute\n{scorer_name_1} scored in the {goal_1}th minute'

print(report)

#PART 2
# 1. choose a player
player = 'Adri van Tiggelen'

# 2. get his first name.
first_name = player[0: (player.find(' '))]

#3. what is the player's last name length
last_name_len = len(player[(player.find(' ')):-1])

#4.
name_short = player[0]+'.'+ player[(player.find(' ')):]

#5.
chant = (first_name +'! ') * (len(first_name) - 1) + (first_name +'!')

#6. good chant when statement this is true
""" Vind het laatste character. Als dit geen spatie is, dan is de chant goed.
    Door van de lengte van de chant-string 1 af te trekken, krijg je de index van die laatste plek.
    Die vergelijk je vervolgens met een spatie. Is het geen spatie, dan is de statement true en is het een goede chant.
"""
good_chant = (chant[(len(chant)-1)] != ' ')


