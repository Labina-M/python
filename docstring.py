
def function_name():
    """this will print the statement"""        #this is a docstring (documentation strings)
    print("hello world")

function_name() 
print(function_name.__doc__)                   # accessing the docstring


def swap_num(x,y):
    print(x,y)
    temp=0
    temp=x
    x=y
    y=temp
    print(x,y)

swap_num(10,20)