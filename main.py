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
scorers = f'{scorer_name_0} {str(goal_0)}, {scorer_name_1} {str(goal_1)}'

# 4.
report = f'{scorer_name_0} scored in the {goal_0}nd minute \n{scorer_name_1} scored in the {goal_1}th minute'

print(report)

#PART 2
# 1. choose a player
player = 'Adri van Tiggelen'

# 2. get his first name (assumes it's at te beginning).
first_name = player[(player.find('Adri')):4]

#3. what is the player's last name length
last_name_len = len(player[(player.find('van Tiggelen')):])

#4.
name_short = player[(player.find('Adri')):1]+'. '+ player[5:]

#5.
chant = (first_name +'! ') * (len(first_name) - 1) + (first_name +'!')

#6. good chant when statement this is true
good_chant = ((first_name +'! ') * (len(first_name)) != chant)
