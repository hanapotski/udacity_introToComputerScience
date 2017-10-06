# Write Python code to print out how far light travels 
# in centimeters in one nanosecond.  Use the values
# defined below.    
# speed_of_light = 299792458   meters per second
# centimeters = 100            one meter is 100 centimeters
# nanosecond = 1.0/1000000000  one billionth of a second

print 299792458 * 100 * 1.0/1000000000

# If you find you are getting 0 when you run your code, try changing the values to decimals.
# 
# When you divide an integer (number without a decimal) by another integer, Python does something called integer division which means it ignores the decimal part of the answer. For example, 5/2 gives 2 instead of 2.5, and 1/10 gives 0 instead of 0.1.
# 
# To force Python to give you an answer including a decimal, you need to make one of the numbers into a decimal by putting a decimal point after it. For example, 5/2.0 gives 2.5, and so does 5.0/2. Try experimenting in the interpreter so that you get a feel of how it works. For example, type
# 
# print 5/2
# 
# and then press the "Test Run" button to see what happens. Then try
# 
# print 5.0/2
# 
# and see what you get then.