names = {"vasu","jay","aditi"}
company = {"Google","TCS","Microsoft"}

zipped = dict(zip(names,company))
print(zipped)

zipped1 = set(zip(names,company))
print(zipped1)

zipped2 = zip(names,company)
for (a,b) in zipped2:
	print(a,b)
