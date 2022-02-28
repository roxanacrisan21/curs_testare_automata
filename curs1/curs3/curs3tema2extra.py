# 1. An online shop sells pet food and accessories. Customers can choose goods and conclude their orders on its website.
# The order is processed according to these rules:
#     · A customer enters his order and clicks SUBMIT. Depending in its total value the order is set to either of the following states:
#        - APPROVED, if the value is less than or equal to $100
#        - PENDING if the value is greater then $100 and the shop's personnel have to verify the validity of the online payment
#     · For PENDING orders, shop personnel can click one of the following:
#       - APPROVE if the payment is confirmed, thereby setting the order to the state of APPROVED
#       - CANCEL if the payment is invalid, thereby setting the order to the state of CANCELED
# For orders in an APPROVED state, the shop personnel choose the SHIP action after the goods are actually sent, thereby setting the order to a state of SHIPPED

order_value = int(input('Enter the order value : '))
process = input('Choose the next step, enter SUBMIT if you want to buy : ')
if process == 'SUBMIT' :
    if order_value <= 100 :
        print('The order is APPROVED')
    else :
        payment_confirmation = input('Choose payment confirmation YES of NO : ')
        print('The order is PENDING and payment confirmation is verified')
        if payment_confirmation == 'YES' :
            print('The payment is confirmed and the order is APPROVED')
        elif payment_confirmation == 'NO' :
            print('The payment is invalid and the order is CANCELED')
        else :
            print('Please choose yes or no for payment_confirmation')
else :
    print('Please enter the process to SUBMIT')


# 2. Company X sells merchandise to wholesale and retail outlets. Wholesale customers receive a two percent discount on all orders.
# The company also encourages both wholesale and retail customers to pay cash on delivery by offering a two percent discount for this method of payment.
# Another two percent discount is given on orders of 50 or more units. Each column represents a certain type of order.

buyer = input('Are you a wholesale or retail? ')
price = int(input('Enter the price : '))
pay = input('Enter the method pay (cash/card) :')
order = int(input('Enter the numbers of units to buy : '))
if buyer == 'wholesale':
    price = price * 0.98 # 2% discount
    print(f'Price for wholesale is {price}')
else:
    price = price
    print(f'Price for retail is {price}')
if pay == 'cash' :
    price = price * 0.98 # 2% discount
    print(f'Price if payed cash on delivery is {price}')
else :
    price = price
    print(f'Price if payed by card is {price}')
if order >= 50 :
    price = price * 0.98 # 2% discount
    print(f'The final price if more then 50 units to buy is {price}')
else :
    price = price
    print(f'The final price if less then 50 units to buy is {price}')

# 3. If a client has over 65 years, then it will be offered to him a discount of 15%.
# Otherwise if the customer does not have over 65 years, if the person travels with at least one account they will have a discount of 10%
# For both seniors and non seniors it will be applied an additional discount of 10% if they will travel during winter.
# Also, for both seniors and non seniors it will be applied a 3% luxury fee if they will travel in the first class (in any season) or 1% handling fee otherwise.

client_age = int(input('The client age is : '))
travel_account = int(input('Enter the numbers of accounts : '))
travel_season = input('Enter the season for travel (summer/autumn/winter/spring) : ')
travel_class = int(input('Enter the class for traveling (enter 1 or 2) : '))
ticket_price = int(input('Enter the ticket price : '))

if client_age > 65 :
    ticket_price = ticket_price * 0.90 # 10% discount for seniors
    print(f'Ticket price for senior is {ticket_price}')
else :
    ticket_price = ticket_price
    print(f'Ticket price for non-seniors is {ticket_price}')
    if travel_account >= 1 :
        ticket_price = ticket_price * 0.90 # 10% discount for non-seniors with at least one account
        print(f'Ticket price for non-seniors with at least one account is {ticket_price}')
    else :
        ticket_price = ticket_price
        print(f'Ticket price for non-seniors with no account is {ticket_price}')
if travel_season == 'winter' :
    ticket_price = ticket_price * 0.90 # 10% discount for travelling in winter
    print(f'Ticket price for traveling in winter is : {ticket_price}')
else :
    ticket_price = ticket_price
    print(f'Price for traveling in spring, summer or autumn is {ticket_price}')
if travel_class == 1 :
    ticket_price = ticket_price * 0.97 # 3% discount for 1st class
    print(f'Ticket price for traveling in 1st class is : {ticket_price}')
elif travel_class == 2 :
    ticket_price = ticket_price * 0.99 # 1% discount for 2nd class
    print(f'Ticket price for traveling in 2nd class is : {ticket_price}')
else :
    print('Please enter a valid traveling class (1 or 2)')

# BONUS EXERCISES (vor necesita cel mai probabil google si in functie de cat de complex vreti sa il faceti este posibil
# sa necesite si notiuni pe care le vom acoperi la cursul urmator)
#
# 1. Write the code for defining a riddle in which the person has to guess a number that is set as correct.
# The person has three tries to guess the animal, and if they haven't guessed the third time a message will be returned
# to them: you lost the game, please try again.
# Between tries they will receive the following message: The number is wrong, you have <number_left> of tries left
# If the person guesses the number they will receive a message: Congrats, you got it right!
# The program will also receive as input if the player wants to play (yes/no)
#
number = 3
play = input('Do you want to play? Please write yes or no : ')
number_left = int(3)

if play == 'yes' :
    print('You want to play')
    for i in range (0, 3) :
        guess_number = int(input('Please guess the correct number : '))
        if guess_number == number:
            print('Congrats, you got it right!')
            break
        else :
            number_left = number_left - 1
            print(f'The number is wrong, you have {number_left} of tries left')
            if number_left == 0 :
                print('You lost the game, please try again ')
            else :
                print('Try again!')
else :
    print("You don't want to play! Type yes if you want to play!")


# 2. We have a movie cinema that runs movies every day. We can have information about the movie name and movie date,
# movie hour, the room where it takes place, the price of the ticket and the available seats in each room.
#
# The room information will be stored in a dictionary, that will be made of a bunch of other dictionaries containing
# each room, and each room will have multiple key:value pairs containing information about chairs and wether they are
# active or not. The available seats will be generated with the range function and assigned with numbers from 1 to 50
# (assuming we have 50 seats in each room).
#
# The movies will be stored in a dictionary which will made of a bunch of other dictionaries representing each movie
# and containing multiple key:value pairs representing the date and the hour when the movie will run.
#
# We will also have a dictionary containing movies and rooms which will have inside multiple key:value pairs representing
# as keys the movies and as values the rooms in which they are running.
# We need to write a program that will take as input from the user the name of the movie they want to watch, the date
# and hour they prefer. The program will allocate for each reservation a seat in the room that the movie is running by
# marking that specific seat as occupied.
# The program will return a message on the screen: Your reservation was confirmed. We will be waiting you on <movie_date>
# at <movie_hour>. The movie will run in room <room_name> and your seat has the number <seat_number>

