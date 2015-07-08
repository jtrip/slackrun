from sys import argv

from Character import get_data
from dice import d6, check
import private
import slacker


def runner(action_info):

    slack = slacker.Slacker(private.sixthWorld)

    # last is used in buiding the description, to use = at the end not +
    last = len(action_info['modifiers']) - 1 
    
    # caluclate total modifier bonus
    mod_bonus = 0
    for key, value in action_info['modifiers'].items():
        mod_bonus += value
    
    # get character dictionary
    character = get_data(action_info['character_name'])
    
    # create die pool based on Attribute, Skill, Skill Group
    die_pool = 0
    if (action_info['attribute'] and action_info['skill'] != ''):
        die_pool    += character[action_info['attribute']] 
        die_pool    += character[action_info['skill']] + mod_bonus
    elif (action_info['skill'] == ''):
        die_pool    += character[action_info['attribute']]
    else:
        print('Error, action_info must have an attribute defined')
        

    # create good looking description
    # Name, Action, Attribute and Skill information
    description = ''
    description += (
        '_' + character['Name'] + ' ' + action_info['action_name'] + '_\n' +
        action_info['attribute'] + 
        "(" + str(character[action_info['attribute']]) + ")  + " +
        action_info['skill'] + 
        "(" + str(character[action_info['skill']]) + ") + "
        )

    # Modifier information
    for i, key in enumerate(action_info['modifiers']):
        if i == last:
            operator = '= '
        else:
            operator = '+ '
        description += (
            str(key) + 
            "(" + str(action_info['modifiers'][key]) + ") "
            + operator
            )

    # Die pool
    description += ("*" + str(die_pool) + "d6*")
    
    # Perform the roll
    roll = d6(die_pool)
    
    # Send results to Slack
    output = check(5, roll)
    
    try:
        slack.chat.post_message(
            '#scratch', 
            description + '\n' + str(roll) + "\n" + output, 
            username=character['Name'], 
            icon_url=character['imageURL']
            )
    except:
        print('failure sending to slack')

