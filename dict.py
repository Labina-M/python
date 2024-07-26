# Distionaries in python


mydict={}
dict={
2:"hello",
"a":"world",
56:1,
"this":"welcome",
9:"to world",
}

print(dict)
#printing values from dict
print("printing first value")     
print(dict[2])                             #printints the 2nd element from doc
print("printing second value")     
print(dict["this"])                        #another way of printing the element
print("before deleting")
print(dict)
del dict[2]                                #deleting the element
print("after deleting")
print(dict)
print("length")
len(dict)                                   #finding the length
print(str(dict))
print("before clearing")
print(dict)
print("after clearing")
dict.clear()                                #remove the dict
print("cleared")
