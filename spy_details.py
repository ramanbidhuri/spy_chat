from datetime import datetime


class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


class ChatMessage:

    def __init__(self, message, sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy('bidhuri', 'Mr.', 22, 4.7)

friend_one = Spy('Raman', 'Mr.', 22, 4.8)
friend_two = Spy('sakshi', 'Ms.', 21, 5)
friend_three = Spy('nitin', 'Dr.', 37, 5.2)


friends = [friend_one, friend_two, friend_three]

