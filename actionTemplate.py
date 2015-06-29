# this is the actionTemplate, copy and fill in data
# please use a unique file name without spaces

from sys import argv
import runnerAction


def main():

    ##
    # required
    ##

    character_name = 'Mr T.'
    action_name = 'pities the fool'

    attribute = 'INT'
    skill = ''
    skill_group = ''

    modifiers = {
        'gold chains': 3
    }

    ##
    # optional flavor text
    ##

    glitch_text = '... but who is the real fool?'
    fail_text = ''
    success_text = ''
    great_success_text = '... and it is highly effective'

    ##
    # Do Not Edit Below This !!!
    ##

    threshold = argv[1]

    character_action = (character_name,
                        action_name,
                        attribute,
                        skill,
                        skill_group,
                        modifiers,
                        threshold,
                        glitch_text,
                        fail_text,
                        success_text,
                        great_success_text)

    return character_action


if __name__ == '__main__':

    try:
        runnerAction(main())
    except:
        print('ERROR - runnerAction failed')

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
