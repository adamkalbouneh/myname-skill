from mycroft import MycroftSkill, intent_file_handler


class Myname(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('myname.intent')
    def handle_myname(self, message):
        self.speak_dialog('myname')


def create_skill():
    return Myname()

