from zoo_exercise.project.animal import Animal
from zoo_exercise.project.mammal import Mammal
from zoo_exercise.project.reptile import Reptile
from zoo_exercise.project.bear import Bear
from zoo_exercise.project.gorilla import Gorilla
from zoo_exercise.project.lizard import Lizard
from zoo_exercise.project.snake import Snake

mammal = Mammal("Stella")
print(mammal.__class__.__bases__[0].__name__)
print(mammal.name)
print(mammal._Animal__name)
lizard = Lizard("John")
print(lizard.__class__.__bases__[0].__name__)
print(lizard.name)
print(lizard._Animal__name)
