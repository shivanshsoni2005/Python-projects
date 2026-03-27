#1- import the rendom module
import random

#2- create subjects
subjects = [
    "Shahrukh khan",
    "Virat Kohli",
    "Nirmala Sitharaman",
    "A Mumbai Cat",
    "A Group of Monkeys",
    "Prime Ministed Modi",
    "Auto Rickshaw Driver from Delhi"
]

actions = [
    "launches",
    "cancels",
    "dances with",
    "eats",
    "declares waron",
    "orders",
    "celebrates"
]

places_or_things = [
    "at Red Fort",
    "in Mumbai Local Train",
    "a plote of samosa",
    "inside parliament",
    "at Ganga Ghat",
    "during IPL Match",
    "at India Gate"
]

# 3- Start the headline generation loop
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    places_or_thing = random.choice(places_or_things)

    headline = f"BREAKING NEWS: {subject} {action} {places_or_thing}"
    print("\n"+ headline)

    user_input = input("\n Do you want another headline? (yes/no)").strip().lower()
    if user_input == "no":
        break

#print goodby message
print("\n Thanks for using Fake News Headline Generator. Have a fun day")


