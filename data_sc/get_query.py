"""
this module manages the incoming information from the AI Script
"""
import pandas as pd
import string
from random import seed
from random import randint
from random import choice
from random import uniform


class SimulatedInput(dict):
    """
    Creates a dictionary that simulates a recipe (input from the AI script)
    """
    def __init__(self, database, number_of_ingredients=1, **kwargs):
        """
        The constructor of the class

        :param database: location of the database
        :param number_of_ingredients: how many ingredients are includes in the recipe?
        :param kwargs: see below

        :keyword rd_seed: set a seed to the random method
        :keyword damage: induce errors in the name of the ingredients
        """
        # Import the existing Database
        data = pd.read_csv(database, ';')
        # Get the Size
        size = data.shape[0]
        # get the random indexes
        indexes = []
        if 'rd_seed' in kwargs.keys():
            print('Using seed: ' + str(kwargs['rd_seed']))
            seed(kwargs['rd_seed'])
        for i in range(0, number_of_ingredients):
            indexes.append(randint(0, size))
        # Create the Dictionary
        dict.__init__(self)
        # set the possible units
        if kwargs.get('units', 0) == 0:
            units = ['teaspoon', 't', 'tsp', 'tablespoon', 'T', 'tbl', 'tbs', 'tbsp', 'ounce', 'fl', 'oz', 'gill',
                     'cup',
                     'c', 'pint', 'p', 'pt', 'quart', 'gallon', 'ml', 'l', 'litre', 'liter', 'mililiter', 'mililitre',
                     'cc', 'dl', 'decilitre', 'deciliter', 'pound', 'lb', '#', 'mg', 'milligram', 'milligrame', 'g',
                     'gram', 'miligram', 'kg', 'kilogram', 'kilogramme'
                     ]
        else:
            units = kwargs['units']
        # Ingredient selection
        for index in indexes:
            # Select Row
            row = data.iloc[index, :]
            # Get the ingredient (Random language)
            if index % 2:
                ingredient = row['ingredient_de']
            else:
                ingredient = row['ingredient_en']
            # Damage String (if wanted)
            if kwargs.get('damage', False):
                # Pick a character
                char = choice(string.ascii_lowercase)
                # pick a position
                pos = randint(0, len(ingredient)-1)
                # replace
                ingredient = ingredient.replace(ingredient[pos], char)
            # Select unit
            unit = choice(units)
            # Random quantity
            quantity = round(uniform(1, 100), randint(0, 2))
            self[ingredient] = [quantity, unit]
        # Report
        print("Simulated Recipe:", self)
