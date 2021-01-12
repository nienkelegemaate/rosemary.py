from kitchen import Rosemary
from kitchen.utensils import Pan, Plate, Bowl
from kitchen.ingredients import Flour, Egg, Milk, Butter, Salt

def pancakes(number): #number of portions of pancakes
    #grab the bowl
    bowl = Bowl.use(name='batter')

    #add the ingredients (250 grams of flour, salt, 2 eggs, and 500 mL milk) to a bowl and mix 
    eggs = Egg.take(int((2/8)*number))
    for egg in eggs:
        egg.crack()
        bowl.add(egg)
    bowl.mix()
    bowl.add(Salt.take('dash'))

    flour = Flour.take(grams = int((250/8)*number))
    for i in range(5):
        bowl.add(flour.take('1/5'))
        bowl.mix()

    milk = Milk.take(ml = int((500/8)*number))
    for i in range(2):
        bowl.add(milk.take('1/2'))
        bowl.mix()

    # bake four pancakes for 60 sec on each side and plate the pancakes
    pan = Pan.use(name='pancake')
    plate = Plate.use()
    for i in range(number):
        pan.add(Butter.take('slice'))
        pan.add(bowl.take(portion=f'1/{number}'))
        pan.cook(minutes=1)
        pan.flip()
        pan.cook(minutes=1)
        pancake = pan.take()
        plate.add(pancake)
    return plate
#change portions of pancakes here
plate = pancakes(8) 
Rosemary.serve(plate)

