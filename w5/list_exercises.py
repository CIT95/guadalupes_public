lst=[11, 100, 99, 1000, 999]
answer_1=lst[0]

print(answer_1)


lst=[11, 100, 101, 999, 1001]

print(lst[1])


lst=[11, 100, 101, 999, 1001]
#Type your answer here.

answer_1=lst[4]

print(answer_1)


gift_list=['socks', '4K drone', 'wine', 'jam']
# Type your code here.
gift_list.append('pajamas')


print(gift_list)


gift_list=['socks', '4K drone', 'wine', 'jam']
# Type your code here.
gift_list.append(["socks", "tshirt", "pajamas"])


print(gift_list)
# got this wrong the first few times because I didn't realize I mispelled tshirt. I typed tshirts.

# original code that I got wrong
gift_list=['socks', '4K drone', 'wine', 'jam']
# Type your code here.
gift_list.append(['socks', 'tshirts', 'pajamas'])


print(gift_list)


# had to use hint 1 for this one and did a google search for .insert()
gift_list=['socks', '4K drone', 'wine', 'jam']
# Type your code here.
gift_list.insert(2, 'slippers')


print(gift_list)


# had to google this one as well

lst=[55, 777, 54, 6, 76, 101, 1, 2, 8679, 123, 99]
#  Type your code here.

answer_1= lst.index(8679)

print(answer_1)


lst=["CRV", "Outback", "XC90", "GL", "Cherokee", "Escalade"]
#  Type your code here.
lst.append(['Navigator', 'Suburban'])


print(lst)


lst=[55, 777, 54, 6, 76, 101, 1, 2, 8679, 123, 99]
#  Type your code here.
lst.remove(99)


print(lst)


lst=[55, 777, 54, 6, 76, 101, 1, 2, 8679, 123, 99]
#  Type your code here.
lst.reverse()


print(lst)


# didn't understand what this meant and actually tried to write print(lst.count(6)) which resulted in an error
lst=[55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]
#  Type your code inside print() function.

answer_1=lst.count(6)

print(answer_1)


lst=[55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]

#  Type your code on line 4:
answer_1=min(lst)

print(answer_1)


# after googling min() for the previous example I made a guess and used max() which worked.
lst=[55, 6, 777, 54, 6, 76, 101, 1, 6, 2, 6]

#  Type your code on line 4:
answer_1= max(lst)

print(answer_1)

