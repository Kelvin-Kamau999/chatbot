import random


R_EATING= "I don't like eating anything because as you know am obviously a bot!"


def unknown():
    response = ['Could you please re-phrase that?',
                "...",
                "Sounds about right",
                "Quite interesting, elaborate further",
                "Sorry, I did not get that right",
                "What does that mean?"][random.randrange(4)]
    return response