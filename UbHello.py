
print("Goodnight, World")

# basic arithmetic operations
print(2+3)  # addition
print(2-3)  # subtraction
print(2*3)  # multiplication
print(8/2)  # division
print(7//3)  # integer division truncation basically the quotient without the remainder
# useful in : resource allocation, pagination since you cant render half a page
# lets the programer know the number of full pages to render
# , mapping and time calculations
print(50%250)  # modulus the remainder after division left side by right side
# useful in alternating row colours, like  we see in distinguishing odd & Even
#cyclic operations eg, with the interger division we got 2hours from 130%60
#the modulus operator tells us theres 10mins left it is also used in
#  hashing, cryptography, and random number generation
print(2**3)  # exponential

#data types, ype function simply finds out what data type.
print(type(2))  # int
print(type(2.0))  # float   
print(type("hello"))  # string
print(type(True))  # boolean
print(type(2+3j))  # complex
print(type({'name': "mike"}))  # dictionary
print(type([1, 2, 3, "mike"]))  # list
print(type((1, 2.4, 3, "mike")))  # tuple
print(type({"mike", 2, 2.4, "name"}))  # set