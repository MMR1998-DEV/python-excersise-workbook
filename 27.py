"""Create a function that calculates acceleration given initial velocity v1, final velocity v2, start time t1, and end time t2.
To test your solution, call the function by inputting values 0, 10, 0, 20 for v1, v2, t1, and t2, respectively, and you should get the expected output.
Expected output: 0.5
"""
def acelaration(v1,v2,t1,t2):
    result = (v2-v1) / (t2-t1)
    return result

print(acelaration(0,10,0,20))

#call the function and print result