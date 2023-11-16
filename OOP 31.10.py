# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.15.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import random
import matplotlib.pyplot as plt

# %%
SIGMA = 0.02

class Probability():
    
    def __set_name__(self, owner, name): #name to pdeath albo preproduction
        self.public_name = name
        self.private = "_" + name
        pass
        
    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)
    
    def __set__(self, obj, value):
        setattr(obj, self.private_name, min(1.0, max(0.0,value)))
    
class Creature:
    alive = True
    p_death = Probability()
    p_reproduction = Probability()
    
    def __init__(self, p_death=0.2, p_reproduction=0.2) :
        self.p_death = p_death
        self.p_reproduction = p_reproduction
        
    def natural_selection(self):
        if random.random() <= self.p_death:
            self.alive = False
            
    def reproduce(self):
        if random.random() <= self.p_reproduction:
            return Creature(self.p_death + random.normalvariate(sigma=SIGMA ), self.p_reproduction + random.normalvariate(sigma= SIGMA))
    
#     @property
#     def p_death(self):
#         return self._p_death
    
#     @p_death.setter
#     def p_death(self,value):
#         if value < 0:
#             self._p_death = 0.0
#         else:
#             self._p_death = value
            
#     @property
#     def p_reproduction(self):
#         return self._p_reproduction
    
#     @p_reproduction.setter
#     def p_reproduction(self,value):
#         if value < 0:
#             self._p_reproduction = 0.0
#         else:
#             self._p_reproduction = value
    
    
class Population:
      
    def __init__(self, size=100):
        self.specimen = {Creature() for _ in range(size)}
        self.history=[]
    
    def count_alive(self):
        return len({creature for creature in self.specimen if creature.alive})
    
    def natural_selection(self):
        for creature in self.specimen:
            creature.natural_selection()
            
    def reproduce(self):
        new_creatures = {creature.reproduce() for creature in self.specimen}
        new_creatures -= {None}
        self.specimen|= new_creatures
       
    def simulate(self, generations):
        for _ in range(generations):
            self.history.append(self.count_alive())
            self.natural_selection()
            self.reproduce()
        
    def plot_history(self):
        plt.plot(self.history)
        
    def plot_attribute(self,attribute='p_death'):
        values = [getattr(creature,attribute) for creature in self.specimen if creature.alive]
        plt.hist(values, density = True)
        plt.title("p_death")
        


# %%
population= Population(3000)

# %%
population.plot_attribute()

# %%
population.simulate(50)

# %%
population.plot_attribute()

# %%
population.plot_attribute(attribute='p_reproduction')

# %%
population.count_alive()

# %%
stwór = Creature()
stwór.p_death = -1
stwór.p_death

# %%
stwór = Creature()
stwór._p_death = -1
stwór.p_death


# %%
class A: 
    def __init__ (self,x=3):
        self.x = x
        
    @property
    def x(self):
        print('inside getter')
        return self._x
    
    @x.setter
    
    def x(self, value):
        print("inside setter")
        self._x = value
    
    

# %%
obj= A(20)

# %%
obj2 = A()
obj2.x

# %%
obj.x
