# Python list

- list is mutable


Example : 


```python
nums = [25,12,35,64,43,54]

#fetching elements
nums[1]

# printing from til end
nums[2:]

# printing from start
nums[:4]

# we can have negative numbers
nums[-5]

#String list
lst = ['sadsa','dsadas','dsdas']

#different type list
lst1 = [3.4,5,6,7,'hello',32]

#get list merged
mrg = [lst,lst1]

#append list to add at last
nums.append(434)

#insert element at index
nums.insert(2,44)

#remove the numers
nums.remove(12)

#pop an index element
nums.pop(1)

#pop a last element
nums.pop() #without index number

#everything after 2nd index will be deleted
del nums[2:]

#add multiple valuse
nums.extend{[12,23,45,67]}

#min
min(nums)

#max
max(nums)

#sorting
sort(nums)

#add elements
sum(nums)

```