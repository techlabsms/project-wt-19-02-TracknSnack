"""
This Module manages the Connection to the mySQL-Server
"""

from mysql.connector import (connection)
import pandas as pd
from fuzzywuzzy import process


def connect_to_sql_database():
    cnx = connection.MySQLConnection(user='track_n_snack',
                                     password='jhjxd5pdCDx7u6sb',
                                     host='34.90.88.18',
                                     database='nutritional_data')
    return cnx


class NutritionalValues:
    def __init__(self):
        # Database Connection
        print('Conecting to Database...\r')
        try:
            cnx = connect_to_sql_database()
            self.database = pd.read_sql('SELECT * FROM nutritional_data.ingredients', cnx)
            cnx.close()
            del self.database['id']
        except:
            print('!!ERR!!\nCould not Connect to Databse...')
            self.database = None
            return
        print('\rDatabase imported!\n First 5 Items:')
        print(self.database.head())
        # List of Ingredients
        self.known_ingredients = self.database['ingredient_en'].tolist() + self.database['ingredient_de'].tolist()
        self.unit_scala = [
            {
                'id': 'kilogram',
                'possible': ['kg', 'kilogram', 'kilogramm'],
                'scala': 1000,
                'out': 'g'
            },
            {
                'id': 'gram',
                'possible': ['g', 'gram', 'gramm'],
                'scala': 1,
                'out': 'g'
            },
            {
                'id': 'mg',
                'possible': ['mg', 'milligramm', 'milligram'],
                'scala': 0.001,
                'out': 'g'
            },
            {
                'id': 'l',
                'possible': ['liter', 'l', 'litre'],
                'scala': 1000,
                'out': 'ml'
            },
            {
                'id': 'ml',
                'possible': ['ml', 'milliliter', 'millilitre'],
                'scala': 1,
                'out': 'ml'
            },
            {
                'id:': 'el',
                'possible': ['el', 'esslöffel', 'tablespoon', 'tbsp'],
                'scala': 15,
                'out': 'ml'
            },
            {
                'id': 'tl',
                'possible': ['tl', 'teelöffel', 'teaspoon', 'tsp'],
                'scala': 5,
                'out': 'ml'
            },
            {
                'id': 'messerspitze',
                'possible': ['messerspitze', 'msp', 'pinch', 'knife point'],
                'scala': 0.5,
                'out': 'g'
            },
            {
                'id': 'pound',
                'possible': ['pound', 'pd', 'pounds'],
                'scala': 454,
                'out': 'g'
            },
            {
                'id': 'ounce',
                'possible': ['ounce', 'ounces', 'oz', 'oz.'],
                'scala': 28.35,
                'out': 'g'
            },
            {
                'id': 'pfund',
                'possible': ['pfund', 'pfd'],
                'scala': 500,
                'out': 'g'
            },
            {
                'id': 'prise',
                'possible': ['prise', 'pr'],
                'scala': 0.04,
                'out': 'g'
            },
            {
                'id': 'zentiliter',
                'possible': ['zentiliter', 'centiliter', 'cl'],
                'scala': 10,
                'out': 'ml'
            },
            {
                'id': 'deziliter',
                'possible': ['deziliter', 'dl', 'deciliter'],
                'scala': 100,
                'out': 'ml'
            },
            {
                'id': '1 packung backpulver',
                'possible': ['1 pck. backpulver'],
                'scala': 16,
                'out': 'g'
            },
            {
                'id': '1 packung vanillezucker',
                'possible': ['1 Pck. Vanillezucker', '1 Packung Vanillinzucker', '1 Pck. Vanillinzucker'],
                'scala': 8,
                'out': 'g'
            }
        ]

    def search_fuzzy(self, to_search):
        # Get a best match
        fuzzywuzzy_one = process.extractOne(to_search, self.known_ingredients)
        best_match = fuzzywuzzy_one[0]
        rating = fuzzywuzzy_one[1]
        #print('Result for {}: {} with a rating of {}'.format(to_search, best_match, rating))
        return best_match, rating

    def unit_convert(self, quantity_in, unit_in ):
        for unit in self.unit_scala:
            for possibility in unit['possible']:
                if unit_in is possibility:
                    quantity_in = float(quantity_in) * unit['scala']
                    unit_in = unit['out']
        return quantity_in, unit_in
