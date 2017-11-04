class Person:
    population = 0
    def __init__(self, name):
        self.name = name
        print("(Initializing {})".format(self.name))
        Person.population += 1

    def die(self):
        print("{} is being destroyed!".format(self.name))

        Person.population -= 1

        if Person.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} persons working.",format(Person.population))


    def say_hello(self):
        print('hello, my name is', self.name)

    @classmethod
    def how_many(cls):
        print("We have {:d} persons".format(cls.population))
    pass



p = Person('xpf')
p.say_hello()
Person.how_many()

p1 = Person("yjj")
p1.say_hello()
Person.how_many()

print('\nPerson can do some work here.\n')

print("Person have finished their work. So let's destroy them.")
p.die()
Person.how_many()
p1.die()
Person.how_many()

