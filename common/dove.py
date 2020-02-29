

class Dove:
    def __init__(self):
        self.__messageCenter = {}

    def remove_sender(self, sender):
        if sender in self.__messageCenter:
            del self.__messageCenter[sender]

    def add_message(self, sender, message):
        self.__set_messages(sender, self.__get_messages(sender).append(message))

    def get_next_message(self, sender):
        messages = self.__get_messages(sender)
        message = None if not messages else messages.pop(0)
        self.__set_messages(sender, messages)
        return message

    def __get_messages(self, sender):
        if sender in self.__messageCenter:
            return self.__messageCenter[sender]
        return []

    def __set_messages(self, sender, messages):
        self.__messageCenter.update({sender: messages})
