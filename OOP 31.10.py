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
import matplotlib.pyplot


# %%
class Creature:
    p_death = 0.2
    p_reproduction = 0.2
    alive = True
    
    def natural_selection(self):
        if random.random() <= self.p_death:
            self.alive = False
            
    def reproduce(self):
        if random.random() <= self.p_reproduction:
            return Creature()
    
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
        new_creatures -= None
        self.specimen|= new_creatures
       
    def simulate(self, generations):
        for _ in range(generations):
            self.history.append(self.count_alive())
            self.natural_selection()
            self.reproduce()
    


# %%
population= Population(3000)

# %%
population.natural_selection()
population.count_alive()

# %%
creature = Creature ()

# %%
