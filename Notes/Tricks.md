# Simple Tricks in Python


```python

#Swapping The Variable

a = 10
b = 9
temp = a
a = b
b  = temp


# Formuls to swapping
a = 10
b = 9
a = a + b
b = a - b
a = a - b

# one more way like xor
# it will not waste extra memory
a = 6
b = 5
a = a ^ b
b = a ^ b
a = a ^ b


# Simple Trick for swapping
a,b=b,a

```