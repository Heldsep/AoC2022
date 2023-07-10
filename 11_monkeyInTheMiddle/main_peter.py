
primefactor = 2*3*5*7*11*13*17*19
# primefactor = 13*17*19*23


class Monkey:
    def __init__(self, id, it, op, te, ac1, ac2):
        self.id = int(id)
        self.items = list(map(lambda x: int(x), it))
        self.newcalc = ' '.join(op)
        self.divider = int(te)
        self.throwiftrue = int(ac1)
        self.throwiffalse = int(ac2)
        self.inspected = 0

    def __str__(self):
        return f'Monkey({self.id, self.items,self.inspected})'

    def __repr__(self):
        return f"Monkey(id='{self.id}', items={self.items}, inspected={self.inspected} newcalc={self.newcalc}, divider={self.divider}, throwiftrue={self.throwiftrue}, throwiffalse={self.throwiffalse})"


def evaluate(m):
    #print('Monkey', m.id)
    for item in m.items:
        #print(' Monkey inspects an item with a worry level of', item)
        m.inspected += 1
        old = item
        item = int(eval(m.newcalc, {}, {"old": old}))  # calculates from old
        #print('  Worry level ',old,'is calculated by ', str(m.newcalc), 'so', item )
        #print(item % m.divider)
        if (item % m.divider == 0):
            #print('  Current worry level ', item ,'is divisible by', m.divider)
            #print('  *Item with level', item, 'thrown to', m.throwiftrue)
            # Zoiets, maar den werkend
            if (item > primefactor):
                # print(item, '-reduced to-', primefactor)
                item = item % primefactor
            Monkeys[m.throwiftrue].items.append(item)
        else:
            #print('  Current worry level ', item ,'is not divisible by', m.divider)
            #print('  *Item with level', item, 'thrown to', m.throwiffalse)
            Monkeys[m.throwiffalse].items.append(item)
    # en dan zijn die hier dus weg
    m.items = []


Monkeys = []

with open("11_monkeyInTheMiddle\large_input_peter.txt", "r") as file:
    while True:
        line1 = file.readline()  # Monkey #:
        if not line1:
            break
        line2 = file.readline().replace(',', '')  # Starting items
        line3 = file.readline()  # Operation
        line4 = file.readline()  # Test
        line5 = file.readline()  # if true
        line6 = file.readline()  # if false
        line7 = file.readline()  # lege

        Monkeys.append(Monkey(line1.split()[1][:-1],
                              line2.split()[2:],
                              line3.split()[3:],
                              line4.split()[3],
                              line5.split()[5],
                              line6.split()[5]
                              ))
    print(Monkeys)
    print(primefactor)

    for round in range(10000):
        # print('======================= ROUND', round+1)
        for monkey in Monkeys:
            evaluate(monkey)
        if round+1 % 1000 == 0:
            # print('======================= ROUND', round+1)
            for m in Monkeys:
                print(m)

sorted = []
for m in Monkeys:
    print(m.id, m.inspected)
    sorted.append(m.inspected)

sorted.sort()
a, b = sorted[-2:]
print(a, b)
print(a*b)
#print (Monkeys)
# 119978 * 120005 is too low
