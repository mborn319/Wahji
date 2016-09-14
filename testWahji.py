import os

os.system("python wahji.py")

ans = raw_input("Do you want to run removeWahji.py?\n")

if ans.lower() == "yes":
	os.system("python removeWahji.py")
else:
	print "Goodbye."
