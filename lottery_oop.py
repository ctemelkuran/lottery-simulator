import random


class Lottery:
    def __init__(self):
        self.weekly_revenue = 0
        self.dropbox  = 0
        self.brought_forward = 0
        self.prize_percentage = [0,0,0.05,0.1,0.2,0.4]

    def get_random_ticket(self):
        return random.sample(range(1,50),6)

    def weekly_draw(self):
        self.user_tickets = []
        
        for i in range(7):
            number_of_users = random.randint(500,50000)
            for user in range(number_of_users):
                self.user_tickets.append(self.get_random_ticket())

            self.weekly_revenue += number_of_users * 3

    def decide_winners(self):
        self.winner_ticket = self.get_random_ticket()
        self.winners = {0:0,1:0,2:0,3:0,4:0,5:0,6:0}
        for user_ticket in self.user_tickets:
            number_of_matches = 0
            for i in range(len(user_ticket)):
                if self.winner_ticket[i] == user_ticket[i]:
                    number_of_matches += 1
            self.winners[number_of_matches] += 1

    def prize_payout(self):
        self.total_prize = 0.55 * self.weekly_revenue

        print(f"Total prize : {self.total_prize:,.2f}")

        self.dropbox += 0.45 * self.weekly_revenue

        for i in range(2, len(self.prize_percentage)):
        # calculate prize for each number
            prize_for_each = self.prize_percentage[i] * self.total_prize

            if self.winners[i] != 0: # if number of winners is not 0
                # calculate prizeForWinner
                prizeForWinners = prize_for_each / self.winners[i]

                # display number of winners and amount of prize
                print(f"{self.winners[i]} person who knew {i} out of 6 earned {prizeForWinners:,.2f} liras.")

            elif self.winners[i] == 0 and i !=6: # if no person can know 2,3,4,5
                print(f"Nobody knew {i} out of 6 and the prize that will be added to drop box is {prize_for_each:,.2f}")
                # prize is added to dropbox
                self.dropbox += prize_for_each

            elif self.winners[6] == 0: # If no person can know 6
                print(f"Nobody knew 6 out of 6 and the prize that will be forwarded to next week is {prize_for_each:,.2f}")
                # self.total_prize is
                self.brought_forward += prize_for_each
    
    def play_year(self):

        for i in range(1,13): # loop through 12 months
            print("MONTH : ", i)
            for j in range(1, 5): # loop through 4 weeks
                print("WEEK : ", j)

                print(f"Weekly revenue : {self.weekly_revenue:,.2f}")
                self.weekly_draw()
                self.decide_winners() # call decide_winners to choose winners
                self.prize_payout()        # call prize_payout to share the prize
                print("")
        # brougthForward is added to dropbox at the end of the year
        self.dropbox += self.brought_forward
        print(f"\nTotal revenue of the dropbox at the end of the year is : {self.dropbox:,.2f} liras")

# This the only function call that is needed to initiate(trigger) the simulation.
lottery = Lottery()
lottery.play_year()
