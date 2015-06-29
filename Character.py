import untangle


class Character(object):
    def __init__(self, data):
            assert isinstance(data, dict)
            self.__dict__ = data


def get_data(character):
    '''
    :param character: String, character name
    :return: Dictionary, character data
    '''
    
    path = 'test_data/'
    filepath = path + character + '.chum5'

    try:
        c = untangle.parse(filepath)
    except IOError:
        print("Error: can't find file or read data")

    data = {
        'Name': c.character.name.cdata,
        'imageURL': str(c.character.notes.cdata),

        'Charisma': int(c.character.attributes.attribute[4].value.cdata),
        'Intelligence': int(c.character.attributes.attribute[5].value.cdata),

        'Hacking': int(c.character.skills.skill[37].rating.cdata),
        'Seduction': int(c.character.skills.skill[37].rating.cdata)
    }

    return data

