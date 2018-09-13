'''
    ნიკა ოთიაშვილი, დავალება 1.1.
    პოულობს c-ს ჯერადებს a-სა და b-ს შორის.
'''

# პირველი გზა (ცუდი გზა)
def first(a, b, c):
    '''
    დაუვლის ყველა მთელ რიცხვს a-დან b-მდე, შეამოწმებს არის თუ არა c-ს ჯერადი და
    დაითვლის მათ. დააბრუნებს რაოდენობას.
    '''
    count = 0 # ჯერადების რაოდენობა
    i = a
    while i <= b:
        if i % c == 0:
            count += 1
        i += 1
    return count

# მეორე გზა (უკეთესი, უფრო სწრაფი, გზა)
def second(a, b, c):
    '''
    გაიგებს b-მდე c-ს ჯერადების რაოდენობას, შემდომ (a - 1)-მდე c-ს ჯერადების 
    რაოდენობას და შემდგომ მათ სხვაობას. a-1 საჭიროა, ვინაიდან b-მდე ჯერადებში 
    a-ც შეიძლება შევიდეს.
    '''
    count = (b // c) - ((a - 1) // c)
    return count

print("rules: 0 < c < a < b")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

print("count: {}".format(second(a, b, c)))