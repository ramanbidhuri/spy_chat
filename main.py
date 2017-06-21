from spy_details import spy, Spy, friends, ChatMessage
from steganography.steganography import Steganography
from datetime import datetime


STATUS_MESSAGES = ['My name is Raman, Raman Bidhuri']

print'namaste ^_^'
print 'Let\'s get started'

question = 'continue as' + ' ' + spy.salutation + ' ' + spy.name + '(y/n)?'
existing = raw_input(question)


def add_status():

    updated_status_message = None

    if spy.current_status_message != None:
        print 'Your current status message is ' + (spy.current_status_message) + '\n'
    else:
        print 'You don\'t have any status message.\n'

    default = raw_input("Do you want to select from the older status (y/n)? ")

    if default.upper() == 'N':
        new_status_message = raw_input("What status message do you want to set?")

        if len(new_status_message) > 0:
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message

    elif default.upper() == 'Y':
        item_position = 1

        for message in STATUS_MESSAGES:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1

        message_selection = int(raw_input("\nChoose from the above messages "))

        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]

    else:
        print 'the option is not valid.'

    if updated_status_message:
        print 'Your updated status message is: %s' % (updated_status_message)

    else:
        print 'You did not update your status message'

    return updated_status_message


def add_friend():
    new_friend = Spy(' ', ' ', 0, 0.0)

    new_friend.name = raw_input("Please add your friend's name:")
    new_friend.salutation = raw_input("Are they Mr. or Ms.?: ")

    new_friend.name = new_friend.name + " " + new_friend.salutation
    new_friend.age = raw_input("Age?")
    new_friend.rating = raw_input("Spy rating?")

    new_friend.age = int(new_friend.age)
    new_friend.rating = float(new_friend.rating)

    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating:
            friends.append(new_friend)

            print 'Friend Added!'
    else:
            print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'

    return len(friends)


def select_friend():
    item_number = 1
    for friend in friends:
        print '%d. %s' % (item_number, friend.name)
        item_number = item_number + 1
    friend_choice = raw_input("Choose from your friends")
    friend_choice_position = int(friend_choice) - 1
    return friend_choice_position


def send_message():
    friend_choice = select_friend()

    original_image = raw_input("What is the name of the image?")
    output_path = 'output.jpg'
    text = raw_input("What do you want to say?")
    Steganography.encode(original_image, output_path, text)

    new_chat = ChatMessage(text, True)

    friends[friend_choice].chats.append(new_chat)
    print "Your secret message is ready!"


def read_message():
    sender = select_friend()

    output_path = raw_input("What is the name of the file?")
    secret_text = Steganography.decode(output_path)

    new_chat = ChatMessage(secret_text,False)

    friends[sender].chats.append(new_chat)
    print "Your secret message has been saved!"


def read_chat_history():

    read_for = select_friend()

    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            print '[%s] %s: %s' % (chat.time.strftime("%d %B %Y"), 'You said:', chat.message)
        else:
            print '[%s] %s said: %s' % (chat.time.strftime("%d %B %Y"), friends[read_for].name, chat.message)


def start_chat(spy):

    print spy.name

    if spy.age > 10 and spy.age < 30:
        print'Authentication complete ' + spy.name + " age: " + str(spy.age) + " and rating of: " + str(spy.rating)

        show_menu = True
        while show_menu:
            menu_choices = 'what do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Select a Friend \n 4. Send secret message \n 5. Read secret message \n 6. Read chat history \n'
            menu_choice = raw_input(menu_choices)
            if len(menu_choice)>0:
                menu_choice = int(menu_choice)

                if menu_choice == 1:
                    spy.current_status_message = add_status()
                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    print 'You have %d friends' % (number_of_friends)
                elif menu_choice == 3:
                    index = select_friend()
                    print index
                elif menu_choice == 4:
                    send_message()
                elif menu_choice == 5:
                    read_message()
                elif menu_choice == 6:
                    read_chat_history()
                else:
                    show_menu = False
    else:
        print 'Sorry you are not of the correct age to be a spy'

if existing == 'y':
    start_chat(spy)
else:

    spy = Spy(' ', ' ', 0, 0.0)

    spy.name = raw_input('What is your name?')
    if len(spy.name) > 0:
        spy.salutation = raw_input('Mr. or Ms.')
        spy.age = raw_input('what is your age?')
        spy.age = int(spy.age)
        spy.rating = raw_input('what is your spy rating')
        spy.rating = float(spy.rating)
        spy_online = True

        start_chat(spy)
    else:
        print 'invalid name'