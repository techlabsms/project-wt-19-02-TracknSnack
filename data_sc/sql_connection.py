"""
This Module manages the Connection to the mySQL-Server
"""

import mysql.connector
from mysql.connector import errorcode
from mysql.connector import (connection)
import pandas as pd


def connect_to_sql_database():
    cnx = connection.MySQLConnection(user='track_n_snack',
                                     password='jhjxd5pdCDx7u6sb',
                                     host='34.90.88.18',
                                     database='nutritional_data')
    return cnx


class NutritionalValues:
    def __init__(self):
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

