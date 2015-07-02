# this is the actionTemplate, rename and fill in data
# please use a unique file name without spaces

from sys import argv
import Action


def main():

    action_info = {
        
        ##
        # required
        ##
        
        'character_name'        : 'Mr T',
        'action_name'           : 'pities the fool :godmode:',

        'attribute'             : 'INT',
        'skill'                 : 'pitty',
        'skill_group'           : 'social skills',

        'modifiers'             : {
                                    'gold chains' : 3,
                                    'getting old' : -1,
                                },

        ##
        # optional flavor text
        ##

        'glitch_text'           : '... but who is the real fool?',
        'fail_text'             : '',
        'success_text'          : '',
        'great_success_text'    : '... and it is highly effective',
    
    }
    
    # Do not edit below this line
    
    
    # Set the threshold for the number of successes required (set with first argument)
    
    if len(argv) > 1:
        action_info['threshold'] = str(argv[1])
    else:
        action_info['threshold'] = 0

    
    return action_info



if __name__ == '__main__':

    try:
        Action.runner(main())
    except:
        print('ERROR - Action.runner() failed')

## 
# BELOW IS FOR REFERENCE ONLY
#
# LIST OF ATTRIBUTES
#   BOD AGI REA STR CHA INT LOG WIL INI EDG MAG RES ESS
#
# LIST OF SKILLS
#
#
#
# LIST OF SKILL GROUPS
#
##

