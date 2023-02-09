import random

user_hand = []
dealer_hand = []

is_hit = False
is_hold = False


def setup_hands():
    global user_hand, dealer_hand
    for i in range(2):
        user_hand.append(random.randint(1,10))
        dealer_hand.append(random.randint(1, 10))

    print(f'Your hand: {user_hand}')
    print(f'Dealer card: {dealer_hand[0]}')


def get_input():
    global is_hit, is_hold
    hit_or_hold = input('Enter hit or hold: ')
    hit_or_hold = hit_or_hold.lower()

    while (not is_hold) and (not is_hit):
        if hit_or_hold == 'hit':
             is_hit = True

        elif hit_or_hold == 'hold':
            is_hold = True           

        else:
            hit_or_hold = input('Enter hit or hold: ')
            hit_or_hold = hit_or_hold.lower()


def check_input():
    global is_hit, is_hold, user_hand, dealer_hand
    if is_hit :
        user_hand.append(random.randint(1,10))
        print(user_hand)

    if is_hold:
        print(dealer_hand)

setup_hands()
get_input()
check_input()
