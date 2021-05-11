import sys

print("2")
year = 2017
args = sys.argv[1:]
print(args)
if args[0]=="-year":
	year = args[1]
print("year:", year)
