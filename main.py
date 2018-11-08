from sys import exit
import random

key = False

print "Hello Adventuer!"
print "Your journey begins!"

def dead(why):
	print why, "Game Over"
	
	print "Continue? Y/N"
	next = raw_input(">")
	
	if next == "Y":
		begin()
	else:
		print "Thanks for playing!"
		exit(0)
		
def begin():
	print "You find yourself in a fork in the road. Which way do you take?"
	
	print "left or right?"
	next = raw_input(">")
	
	while True:
		if next == "left":
			house()
		elif next == "right":
			wall()
		else:
			print "Try Again:"
			next = raw_input(">")
		
def house():
	print "You approach an old house."
	print "It seems to be abondoned."
	print "You hear thunder crack nearby. A storm is approching."
	
	print "What do you do?"
	next = raw_input(">")
	
	while True:
		if next == "observe":
			print "It is an old house that has not been well kept."
			print "The storm is getting closer."
			print "What do you do?"
			next = raw_input(">")
		elif next == "approach":
			house_door()
		elif next == "stay":
			dead("You get struck by lightning.")
		elif next == "go back":
			begin()
		else:
			print "Options: observe, approach, stay, go back"
			print "Try Again:"
			next = raw_input(">")

def house_door():
	print "You approach the door."
	print "It is old and made of dark wood, like the rest of the house."
	print "You look for a nob, but find none."
	print "You then notice three buttons arranged horizontally in the middle of the door."
	
	lock = True
	
	while True:
		print "What do you do?"
		next = raw_input(">")
		
		if next == "press left" and lock == False:
			print "The door opens!"
			print "You walk inside."
			house_inside()
		elif next == "press left" and lock == True:
			print "Nothing happens."
		elif next == "press middle" and lock == True:
			print "You hear a metallic clicking sound."
			lock = False
		elif next == "press middle" and lock == False:
			print "Nothing happens."
		elif next == "press right" and lock == True:
			print "Nothing happens."
		elif next == "press right" and lock == False:
			print "You hear a metallic clicking sound."
			lock = True
		elif next == "leave":
			house()
		else:
			print "Options: press left, press middle, press right, leave"
			print "Try Again:"
			next = raw_input(">")

def house_inside():
	print "You find yourself mysteriously walking into a luxurious casino."
	print "Two games are available: blackjack and roullette"
	print "Which do you choose?"
	next = raw_input(">")
	
	while True:
		if next == "blackjack":
			blackjack()
		elif next == "roullette":
			roullette()
		elif next == "observe":
			print "Two games are available: blackjack and roullette"
		elif next == "leave":
			print "The door is locked. Not turning back"
		else:
			print "Options: blackjack, roullette, slots, observe, leave."
			print "Try Again:"
			next = raw_input(">")
			
def blackjack():
	print "You approach the blackjack table."
	print "An older gentleman greets you with a smile, but says nothing."
	print "He deals you in."
	
	cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
	
	dealer_card_hidden = random.choice(cards)
	dealer_card_show = random.choice(cards)
	dealer_total = dealer_card_hidden + dealer_card_show
	
	print "The dealer is showing " + str(dealer_card_show)
	
	player_card_hidden = random.choice(cards)
	player_card_show = random.choice(cards)
	player_total = player_card_hidden + player_card_show
	
	print "You are showing " + str(player_card_show) + " and " + str(player_card_hidden) + " face down."
	print "Your current total is " + str(player_total)
	
	player_turn = True
	
	while player_turn == True:
		if player_total == 21:
			print "Blackjack! You win!"
			give_key()
		print "What will you do?"
		next = raw_input(">")
		
		if next == "hit":
			player_total += random.choice(cards)
			if player_total > 21:
				dead("Bust! The dealer draws a gun and shoots!")
			else:
				print "Your total is now " + str(player_total)
		elif next == "check":
			print "Your current total is " + str(player_total)
		elif next == "stay":
			player_turn = False
		else:
			print "Options: hit, stay, check"
	
	print "The dealer flips his face down card."
	print "His total is " + str(dealer_total)
	print "The dealer will now play."
	
	while dealer_total < 17:
		dealer_total += random.choice(cards)
		
	print "Dealer's new total is " + str(dealer_total)
	
	if dealer_total > 21:
		print "Dealer busts! You win!"
		give_key()
	elif dealer_total < player_total:
		print "You win!"
		give_key()
	else:
		dead("You lose! The dealer draws a gun and shoots!")

def roullette():
	print "You approach the roullette table."
	print "The dealer just stares at you, unmoving."
	
	print "Place your bet! (Pick a number between 0-38)"
	
	roll = random.randint(0, 38)
	
	next = raw_input(">")
	bet = int(next)
	
	try_count = 3
	while True:
		if try_count == 0:
			dead("The dealer draws a gun and shoots!")
		
		print "You have " + str(try_count) + " tries left."
		
		print "Try again."
		next = raw_input(">")
		bet = int(next)
		
		if bet == roll:
			print "You win!"
			give_key()
		elif bet < roll or bet > roll:
			print "You lose!"
			try_count -= 1
		else:
			"Please pick a number between 0-38"
			next = raw_input(">")
			bet = int(next)
			
def give_key():
	print "The dealer smiles a sinister grin."
	print "They extend their arm towards you, holding a wooden box."
	print "You take the box and open it."
	print "Inside is a brass key."
	
	global key
	key = True
	
	print "You then feel dizzy. The room starts spinning."
	print "You black out."
	begin()
	
def wall():
	print key
	exit(0)
			
begin()