def validity_of_number(num):
    if (num < 0 or num > 99):
        print('invalid')
    elif (num >= 50 and num <= 79):
        print('ineligible receiver')
    else:
        print('eligible receiver')


def divis_by_ten(integer):
    return integer % 10 != 0


validity_of_number(-1)
validity_of_number(100)
validity_of_number(50)
validity_of_number(60)
validity_of_number(79)
validity_of_number(44)

print('\n')

print(divis_by_ten(0))
print(divis_by_ten(10))
print(divis_by_ten(20))
print(divis_by_ten(5))
