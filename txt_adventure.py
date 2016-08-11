RorL = input("Do you want to hike left or right?")
# comments through hashtag key

if RorL == "left" or RorL == "Left":
	print("A cliff! Where did that come from?")
	brave = input("Are you brave?")
	if brave == "yes" or brave =="Yes":
		print("Use the vines behind you and 'tarzan' over it.")
	elif brave == "no" or brave =="No":
		print("Find a bridge.")
		over = input("Do you want to go over it?")
		if over == "yes" or over =="Yes":
			print("Go ahead and try.")
		elif over == "no" or over =="No":
			print("Attempt to find a way around the cliff. I doubt your possibilities of doing so...")
		

elif RorL == "right" or RorL == "Right":
	print("A cave! It's so dark!")
	scared = input("Are you scared?")
	if scared == "yes" or scared =="Yes":
		print("Of course! It's pitvh black!")
		print ("Attempt to walk around the cave.")
	else:
		print("No way! I'm no chicken")
		print("Go inside and discover its secrets. Ooh!")
		
		
print("You walked so far! Take a breather")
wanttoend = input("Are you done for the day?") 
if wanttoend == "yes" or wanttoend == "Yes":
	print("Camp for the night.")
else:
	print("Keep on hiking!")