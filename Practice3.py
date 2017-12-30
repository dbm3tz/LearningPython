# 3 An Informal Introduction to Python
# https://docs.python.org/3/tutorial/introduction.html

a = 2 + 2
print(a)

b = 5 / 6
c = 5 // 6 # Floor division
d = 5 % 6 # Modulo
e = 5 ** 6 # 5 to the power of 6
print(b)
print(c)
print(d)

# Strings can use double or single quotes

word = 'python'
length = len(word)
word[2]
word[-1]
word[2:5]
word[:]
word[:4]
word[4:]
word[-2:]
word[42:]

squares = [1,4,9,16,25]
squares = squares + [36,49]
squares.append(64)
squares[0] = -3

print(squares)