#creating list, set and dictionary

aList = []
aDict = {}
aSet = set()

for letter in "Hello world!":
    aList.append(letter)
    aSet.add(letter)
    aDict[letter] = len(aList)

print("List:", aList)
print("List:", aSet)
print("List:", aDict)

aList2 = []
for letter in "hello":
    for letter1 in "world":
        aList2.append((letter, letter1))

print(aList2)

#fizzBuzz

for x in range(50):
    if x % 3 == 0 and x % 5 == 0:
        print("fizzBuzz")
        continue
    elif x % 3 == 0:
        print("fizz")
        continue
    elif x % 5 == 0:
        print("buzz")
        continue
    print(x)
