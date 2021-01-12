from kitchen import Rosemary
from kitchen.utensils import Plate, Bowl, Oven, BakingTray
from kitchen.ingredients import Butter, Sugar, Egg, Salt, Flour, ChocolateChips, BakingPowder

# Ingredients: one part butter, 200 grams sugar, two eggs, pinch of salt, 300 grams flour, 200 grams chocochips, bakingpowder
#preheat the oven
oven = Oven.use()
oven.preheat(degrees=170)
#grab the bowl
bowl = Bowl.use(name='batter')

def cookies(number): #number of portions of cookies
    #mix the butter
    bowl.add(Butter.take(grams = int((200/8)*number)))
    bowl.mix()
    #slowly mix in sugar in 6 parts
    sugar = Sugar.take(grams = int((200/8)*number))
    for i in range(6):
        bowl.add(sugar.take('1/6'))
        bowl.mix()
    #adding the eggs
    eggs = Egg.take(int((2/8)*number))
    for egg in eggs:
        egg.crack()
        bowl.add(egg)
    bowl.mix()
    #adding a pinch of salt
    bowl.add(Salt.take('pinch'))
    #adding the flour and choco chips in 6 parts
    flour = Flour.take(grams = int((300/8)*number))
    chocolatechips = ChocolateChips.take(grams = int((200/8)*number))
    for i in range(6):
        bowl.add(flour.take('1/6'))
        bowl.mix()
        bowl.add(chocolatechips.take('1/6'))
        bowl.mix()

    #add the bakingpowder
    bakingpowder = BakingPowder.take('some')
    bowl.add(bakingpowder)
    bowl.mix()

    #scooping 8 cookies on the trey
    bakingtray = BakingTray.use(name='cookie')
    for i in range(8):
        bakingtray.add(bowl.take('1/8'))

    #baking the cookies
    oven.add(bakingtray)
    oven.bake(minutes=10)
    bakingtray = oven.take()

    #plating the 8 cookies
    plate = Plate.use()
    for i in range(8):
        plate.add(bakingtray.take())
    return plate 
#change portions of cookies here
plate = cookies(8) 
Rosemary.serve(plate)


