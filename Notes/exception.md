# Exception Handling in python



```python

a = 5
k = int(input("Enter a nuber"))

try:
	print("resource open")
	print(a/k)
except Exception as e:
	print("Hey, you cannot divide number by 0",e)
finally:
	print("Executed")

```