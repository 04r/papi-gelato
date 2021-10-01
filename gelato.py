import time



def stap3a():
	inp1 = input("Hier is uw hoorntje met {} bolletje(s). Wilt u nog meer bestellen? (Y/N)".format(hoeveel).lower())
	if inp1 == "Y":
		mainnn()
	else:
		print("Bedankt en tot ziens!")

def stap3b():
	inp = input("Hier is uw bakje met {} bolletje(s). Wilt u nog meer bestellen? (Y/N)".format(hoeveel).lower())
	if inp == "Y":
		mainnn()
	else:
		print("Bedankt en tot ziens!")
		quit()


def stap2():
	met = input("Wilt u deze {} bolletje(s) in A) een hoorntje of B) een bakje?".format(hoeveel).lower())
	if met == "a":
		stap3a()
	elif met == "b":
		stap3b()
	else:
		print("Sorry, dat snap ik niet...")
		stap2()


def stap1():

	print('Welkom bij Papi Gelato je mag alle smaken kiezen zolang het maar vanille ijs is.\n')

	time.sleep(1)

	stap2()

hoeveel = int(input('Hoeveel bolletjes wilt u?\n'))

def mainnn():
	stap1()
	if hoeveel < 4:
		stap2()
	elif hoeveel >5:
		if hoeveel <9:
			print("Dan krijgt u van mij een bakje met {} bolletjes".format(hoeveel))
	elif hoeveel >9:
		print("Sorry, zulke grote bakken hebben we niet")
	else:
		print("Sorry, dat snap ik niet...")

mainnn()