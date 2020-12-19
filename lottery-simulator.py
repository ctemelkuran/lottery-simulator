import random

# initialize global variables
weeklyRevenue = 0.0
dropBox = 0.0
broughtForward = 0.0
# initialize price rates for each type of winner
prizePercentage = [0, 0, 0.05, 0.1, 0.2, 0.25, 0.4]

def draw():
    # pick 6 unique random number between 1 and 50
    list_of_numbers = random.sample(range(1, 50), 6)
    return list_of_numbers
    # end function draw


def play_week():
    # initialize list of user tickets
    userTickets = []

    # loop for 7 days of week
    for i in range(0, 7):
        # random number of people between 50,000 and 100,000
        numberOfUsers = random.randint(50000,100000)
        # loop in numberOfUsers for every user
        for i in range(1, numberOfUsers):
            # add tickets to userTickets list
            userTickets.append(draw())
    # update global variable weeklyRevenue at the end of the week
    global weeklyRevenue
    weeklyRevenue = len(userTickets) * 3

    return userTickets


def decide_winners(played_tickets, lucky_numbers):
    # initialize right_guesses list
    right_guesses = [0, 0, 0, 0, 0, 0, 0]

    # create a set for lucky_numbers
    lucky_numbers_set = set(lucky_numbers)

    # loop for every index of played_tickets list
    for i in range(len(played_tickets)):

        # set for elements of played_tickets list
        played_tickets_set = set(played_tickets[i])

        # set for intersection of two sets
        intersection_set = lucky_numbers_set.intersection(played_tickets_set)

        # number of matches
        matches = len(intersection_set)

        # loop through number of matches
        for i in range(0,7):
            if matches == i:
                # increment i'th element of right_guesses list
                right_guesses[i] += 1

    # return the list of right guesses
    return right_guesses


def prize_payout(winners):

    # calculate total prize for each week
    totalPrize = 0.55 * weeklyRevenue

    # display total prize
    print(f"Total prize : {totalPrize:,.2f}")

    # update global variable dropBox as described above
    global dropBox
    dropBox += 0.45 * weeklyRevenue

    # loop through 2 to 6 to share the prize
    for i in range(2, len(prizePercentage)):
        # calculate prize for each number
        prizeForEach = prizePercentage[i] * totalPrize

        if winners[i] != 0: # if number of winners is not 0
            # calculate prizeForWinner
            prizeForWinners = prizeForEach / winners[i]

            # display number of winners and amount of prize
            print(f"{winners[i]} person who knew {i} out of 6 earned {prizeForWinners:,.2f} liras.")

        elif winners[i] == 0 and i !=6: # if no person can know 2,3,4,5
            print(f"Nobody knew {i} out of 6 and the prize that will be added to drop box is {prizeForEach:,.2f}")
            # prize is added to dropBox
            dropBox += prizeForEach

        elif winners[6] == 0: # If no person can know 6
            print(f"Nobody knew 6 out of 6 and the prize that will be forwarded to next week is {prizeForEach:,.2f}")
            # totalPrize is
            global broughtForward
            broughtForward += prizeForEach


def play_year():

    for i in range(1,13): # loop through 12 months
        print("MONTH : ", i)
        for j in range(1, 5): # loop through 4 weeks
            print("WEEK : ", j)

            played_tickets = play_week() # call play_week() to create tickets
            lucky_numbers = draw()       # call draw() to decide lucky numbers

            print(f"Weekly revenue : {weeklyRevenue:,.2f}")
            winners = decide_winners(played_tickets, lucky_numbers) # call decide_winners to choose winners
            prize_payout(winners)        # call prize_payout to share the prize
            print("")
    # brougthForward is added to dropBox at the end of the year
    global dropBox
    dropBox += broughtForward
    print(f"\nTotal revenue of the dropbox at the end of the year is : {dropBox:,.2f} liras")

# This the only function call that is needed to initiate(trigger) the simulation.
play_year()