print('This program adds up all the numbers from 0 to the number you specify')
print('What number would you like to continue to?')
total = 0
endNum = input()
for i in range(int(endNum) + 1) :
    total = total + i
print('After adding up all the numbers from 0 - ' + endNum + ' we get:')
print(total)