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
# I used +1 because I guess we don't want to count the first space as part of the last name.
last_name_len = len(player[(player.find(' ') + 1):])

#4. geen spatie achter de punt in de '.' string, want die wordt door de slice/find al geselecteerd 
name_short = player[0]+'.'+ player[(player.find(' ')):]
#print(name_short)
#5.
chant = (first_name +'! ') * (len(first_name) - 1) + (first_name +'!')

#6. good chant when statement this is true (shortest version;)
good_chant = (chant[-1] != ' ')


