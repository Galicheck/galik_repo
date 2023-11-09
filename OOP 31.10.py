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
class Creature:
    alive = True
    
    def __init__(self, p_death=0.2, p_reproduction=0.2) :
        self.p_death = p_death
        self.p_reproduction = p_reproduction
        
    def natural_selection(self):
        if random.random() <= self.p_death:
            self.alive = False
            
    def reproduce(self):
        if random.random() <= self.p_reproduction:
            return Creature(self.p_death + random.normalvariate(sigma=SIGMA ), self.p_reproduction + random.normalvariate(sigma= SIGMA))
    
    @property
    def p_death(self):
        return self._p_death
    
    @p_death.setter
    def p_death(self,value):
        if value < 0:
            self._p_death = 0.0
        else:
            self._p_death = value
    
    
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
