from art import logo

print(logo)
bids = {}


def highest_bidder(bid):
    highest = 0
    winner = ''
    for i in bid:
        if bid[i] > highest:
            highest = bid[i]
            winner = i
    print(f'The winner is {winner} with bid amount {highest} ')


while True:
    name = input('Enter your name : ')
    price = int(input('Enter the bid amount : '))
    bids[name] = price
    check = input('Is there another bidder ? yes or no : ')
    if check == 'no':
        highest_bidder(bids)
        break
