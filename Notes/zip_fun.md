# Zip function in python

## we can zip list into multiple format like set or dictionary

```python

names = {"vasu","jay","aditi"}
company = {"Google","TCS","Microsoft"}

zipped = dict(zip(names,company))
print(zipped)

#output {'aditi': 'Google', 'jay': 'TCS', 'vasu': 'Microsoft'}

zipped1 = set(zip(names,company))
print(zipped1)

# output {('aditi', 'Microsoft'), ('jay', 'TCS'), ('vasu', 'Google')}

zipped2 = zip(names,company)
for (a,b) in zipped2:
	print(a,b)

#output # aditi Microsoft
		# jay TCS
		# vasu Google

```