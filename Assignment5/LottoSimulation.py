

#1b. Build a simulation program for Paf Låttå using the "generate_row" and "check_row" functions from LottoFunctions.py
#This code simulates a lottery system over 104 weeks with 2000 players per week. It tracks weekly payouts, counts how many numbers players got correct, handles jackpot growth, and prints a final summary of wins and losses.
# treat this file as main to import functions from LottoFunctions


from LottoFunctions import generate_row, check_row
def run_simulation():       #main simulation function
    weeks = 104                #total number of weeks to imulate (=2 years)
    players_per_week = 2000   #number of lottery tickets played each week
    row_length = 8             #number of numbers on each ticket
    max_number = 52
    jackpot_start = 20000     #initial jackpot amount
    jackpot_increase = 1000   #amount the jackpot grows each week IF no one wins it

    #payout table and statistics
    payout = [0, 0, 0, 0, 20, 50, 1000, 10000, 50000]       #list of winnings for 0–8 correct numbers. The index of the list represents how many numbers were correct. The value at that index is the amount of money the player wins. You need to have at least 4 correct to get min amout which is 20€
    played_rows = [0]*(row_length+1)                        #[0] * (ROW_LENGTH + 1) creates a list of zeros. The length of the list is (ROW_LENGTH + 1)
    total_payout = 0                                        #Keeps track of total money paid out to players.
    JACKPOT = jackpot_start                                 # begins from 20 000 at the beginning of the simulation. Later in the simulation, the jackpot variable changes week by week depending on whether someone wins or not.

    for week in range (1, weeks +1):       #Loops over each week in the simulation (from 1 to 104)
        print (f"Week {week}: The jackpot is now {JACKPOT}")
        winning_row = generate_row(max_number, row_length)
        print ("Correct row this week:", winning_row)
        jackpot_won = False                 #Flag as Bool type FALSE until proven right, to check if the jackpot is won this week

        for player in range (players_per_week):  #Loops over all the players for this week (2000 times)
            played_row = generate_row(max_number,row_length )   #Generates a unique ticket for this player using the function generate_row
            num_correct = check_row(winning_row,played_row)     #check if they match usinf function check_row
            played_rows[num_correct]+=1                         #Updates the count for tickets with num_correct (eg. 0-8) matches
            if num_correct>=4:                                  #can only get payout from the payout list if correct tickets are four or more
                total_payout +=payout[num_correct]              #If the player got at least 4 numbers correct, they win money and it is added to total_payout.
            if num_correct == row_length:                       #If the player got all numbers correct, the jackpot is won
                jackpot_won = True

        if jackpot_won:                    #things to do If the jackpot was won this week:
            print(f"JACKPOT! YOU GOT {JACKPOT}€!")
            total_payout += JACKPOT
            JACKPOT = jackpot_start
        else:
            print("No Jackpot this week, the pot grows...")     #If no one won the jackpot...
            JACKPOT+=jackpot_increase

    #print summary
    total_rows = sum(played_rows)
    for i, count in enumerate(played_rows):     #Loops over all match counts (0–8) and prints how many tickets had each number of correct guesses and the percentage.
        percentage = count / total_rows * 100
        print(f"{i} correct: {count} rows ({percentage:.3f}%) ")
    total_income = players_per_week * weeks * 5 #Calculates total money collected. Assumes each ticket costs 5€ for example.
    print (f"Total income: {total_income}€ ")
    print (f"Total payouts: {total_payout}€")

if __name__ == "__main__":
    run_simulation()