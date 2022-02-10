# Decoratores In Python

### we can change the behavior of the function at the comiple time itself

```python

def div(a,b):
	print(a/b)


def smart_div(func): # accept parameter of an function
	def inner(a,b): # accept parameter of a div function
		if(a<b): # check the condition for a,b
			a,b=b,a
		return func(a,b) # return to smart function

	return inner # it will return to div function

div = smart_div(div) 
# we can use different name of function 
# like div1 = smart_div(div)

div(2,4) # it still give 2.0 because of smart div
div(4,2) # it will give 2.0

```