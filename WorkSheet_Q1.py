import sys

sys.stdout.write('Hello' + '\n')

print ("Hello")

sys.stdout.write('1' + '\n')
sys.stdout.write('1.5' + '\n')
print (1)
print (1.5)

n = 2

sys.stdout.write(str(n) + '\n')

print (n)

sys.stdout.write('Hello' + str(n))
sys.stdout.write('Hello' + str(n) + '\n')

print ("Hello" + str(n))
print ("Hello" + str(n))

# sys.stdout.write can only do strings while print can do intergers, strings and
# floats as long as they are not togther i.e. printing a string and an intager.
# Also having two print statements, one under the other, signafies a new line
# but having two sys.stdout.write, one under the other, does not signafy a
# new line unless explicitly told so.
