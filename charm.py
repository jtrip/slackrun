__actionname__ = 'bats eyelashes :lips:'

from sys import argv

from character import Character, get_data
from dice import d6, check
import private
import slacker


def main(argv):

    slack = slacker.Slacker(private.i3)

    charactername = argv[0]
    difficulty = argv[1]
    channelname = argv[2]

    modifiers = \
        {
            'sexy sleepwear': 4,
            'pheromone augmentation': 2
        }
    last = len(modifiers) - 1

    mod_bonus = 0
    for key, value in modifiers.items():
        mod_bonus += value

    character = Character(get_data(charactername))

    die_pool = character.Charisma + character.Seduction + mod_bonus

    # create good looking description
    description = ''
    description += ('_' + character.Name + ' ' + __actionname__ + '_\n')

    description += (
        "Charisma(" + str(character.Charisma) + ")  + " +
        "Seduction(" + str(character.Seduction) + ") + ")

    for i, key in enumerate(modifiers):
        if i == last:
            operator = '= '
        else:
            operator = '+ '
        description += (
            str(key) + "(" + str(modifiers[key]) + ") " + operator)

    description += (
         "*" + str(die_pool) + "d6" + "*" + " @ difficulty(" + str(difficulty) + ')\n'
    )
    print(character.Name)

    # perform the roll
    roll = d6(die_pool)

    # send results to slack
    output = check(difficulty, roll)
    slack.chat.post_message(channelname, description + '\n' + str(roll) + "\n" + output, username=character.Name, icon_url=character.imageURL)


if __name__ == '__main__':
    main(['jtrip', 5, '#jtrip_home'])
