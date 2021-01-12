from kitchen.ingredients.Ingredient import LemonZest
from kitchen import Rosemary
from kitchen.utensils import Plate, Bowl, Oven, PieDish, Fridge
from kitchen.ingredients import Water, Flour, Salt, Butter, Apple, Lemon, Cornstarch, Cinnamon, Egg, Sugar

#preheat the oven
oven = Oven.use()
oven.preheat(degrees=180)

#put water in fridge
fridge = Fridge.use(degrees=5)
waterbowl = Bowl.use()
waterbowl.add(Water.take('some'))
fridge.add(waterbowl)

bowl = Bowl.use(name='dough')
#mix 300gr flour with teaspoon salt
bowl.add(Flour.take(grams=300))
bowl.add(Salt.take('teaspoon'))
bowl.mix()
#gradually add 250gr butter while kneading dough
butter = Butter.take(grams=250)
for i in range(6):
    bowl.add(butter.take('1/6'))
    bowl.mix()
#take water from fridge and gradually add water
waterbowl = fridge.take()
for i in range(6):
    bowl.add(waterbowl.take('1/6'))
    bowl.mix()
bowl.mix()
#put dough in fridge
fridge.add(bowl)
#grab another bowl
bowl2 = Bowl.use()
#peel and slice 6 apples
for i in range(6):
    apple = Apple.take()
    apple.peel()
    apple.slice()
    bowl2.add(apple)
#add 150gr sugar, spoon cornstarch, pinch salt, teaspoon cinnamon
bowl2.add(Sugar.take(grams=150))
bowl2.add(Cornstarch.take('spoon'))
bowl2.add(Salt.take('pinch'))
bowl2.add(Cinnamon.take('teaspoon'))
#zest and juice lemon and add half to filling
lemon = Lemon.take()
lemonzest = lemon.zest()
lemonjuice = lemon.squeeze()
bowl2.add(lemonzest.take('1/2'))
bowl2.add(lemonjuice.take('1/2'))
#cover pie dish with 3/4 dough and add filling
piedish = PieDish.use()
piedish.add(bowl.take('3/4'))
piedish.add(bowl2.take())
#add 1/4 dough on top
piedish.add(bowl.take('1/4'))
#in a new bowl, crack and mix egg
bowl3 = Bowl.use()
egg = Egg.take()
egg.crack()
bowl3.add(egg)   
bowl3.mix()
#add spoon of sugar and lemon zest to egg
bowl3.add(lemonzest.take('1/2'))
bowl3.add(Sugar.take('spoon'))
#spread out mixture on top of pie
piedish.add(bowl3.take())
#put in oven for 60 min
oven.add(piedish)
oven.bake(minutes=60)
#take the piedish out of the oven
piedish = oven.take()
#plate the pie
plate = Plate.use()
plate.add(piedish.take())
Rosemary.serve(plate)