import slacker
import private

slack = slacker.Slacker(private.i3)

class ShadowSlacker:
    def __init__(self, name, channel, pic):
        self.name = name
        self.channel = channel
        self.pic = pic


def msgpost(thecharacter, output):
    slack.chat.post_message(thecharacter.channel, output, username=thecharacter.name, icon_url=thecharacter.pic)
