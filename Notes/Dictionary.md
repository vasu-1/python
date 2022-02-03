# Dictionary in Python



```python

data = {1:'navin', 2:'kiran', 3:'vasu',5:'manish'}

#fetch the values
data[1]

#get an error which is not the key like data[4]

#get a value
data.get(1)

#it will not give error
data.get(4)

#if we have't the key then we can show the message
data.get(4,'Not Found')

#list
keys = ['vasu','jay','manish']
values = ['jt','daa','csa']

#two list into dictionary
data = dict(zip(keys,values))

#add item in dict
data['monika'] = 'CS'

#delete value with key
del data['vasu']


#Nested dict and lists

prog = {'js':'atom','cs':'code','python':['sublime','pycharm'],'java':{'JSE':'netbeans','JEE':'eclipse'}}

#prog['python'] will give both values
#prog['python']['1'] will give pycharm
#prog['java']['JEE'] will give eclipse


```