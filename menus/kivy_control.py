
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from data_base_mgmt import *
from ocr import *
from  kivy.clock import Clock
Builder.load_file('menus/input_processing_menu.kv')
Builder.load_file('menus/intro.kv')
Builder.load_file('menus/input_menu.kv')
Builder.load_file('menus/loading.kv')

sql = None
image_file = None
ingredient_frame = None


def load_database():
    global sql
    sql = NutritionalValues()


class InputProcessingMenu(Screen):
    def __init__(self):
        super().__init__()
        self.ingredients = []
        self.filled = False

    def load_database(self):
        if sql is None:
            load_database()
        if ingredient_frame is not None:
            self.fill_table()

    def fill_table(self):
        if self.filled:
            return
        print('RUNNING FILL')
        input_frame = ingredient_frame

        for key, val in input_frame.items():
            #print(key, val)
            ingredient_in = key
            quantity_in = val[0]
            # Process Quantity
            total = 0
            if '/' in quantity_in:
                # is a fraction
                total = 0.0
                components = quantity_in.split(' ')
                for component in components:
                    if '/' in component:
                        # this is a fraction
                        fraction = component.split('/')
                        #print(fraction)
                        total += float(int(fraction[0])/int(fraction[1]))
                    else:
                        # Whole Number
                        total += int(component)
                quantity_in = float(total)
            else:
                try:
                    quantity_in = float(quantity_in)
                except:
                    quantity_in = 0

            unit_in = val[1]
            self.ingredients.append(IngredientField( ingredient_in, quantity_in, unit_in))

        for widget in self.ingredients:
            self.ids.layout.add_widget(widget)


        # Change Button
        self.ids.but.text = 'Calculate'
        #self.ids.but.unbind(on_release=self.fill_table)
        self.ids.but.bind(on_release=self.calculate_sugar)
        self.filled = True

    def calculate_sugar(self,_):
        total_all = 0
        for widget in self.ingredients:
            sugar = 0
            quantity = float(widget.ids.q_out.text)
            content_of_sugar = float(widget.ids.sugar_per_unit.text)
            #print('{} grams/ml with a {} g of sugar /100g'.format(quantity,content_of_sugar))
            total= (quantity/100)*content_of_sugar
            widget.ids.total.text = str(total)
            total_all += total
        self.ids.total_all.text = 'For a total of {} g Sugar'.format(round(total_all, 2))

class IngredientField(BoxLayout):
    def __init__(self, ingredient_in, quantity_in, unit_in):
        super().__init__()
        self.ingredient_in = ingredient_in
        self.quantity_in = quantity_in
        self.unit_in = unit_in
        # Set the View
        self.ids.ingredient_in.text = self.ingredient_in
        # Search for the name in the database
        ingredient_out = sql.search_fuzzy(self.ingredient_in)[0]
        self.ids.ingredient_out.text = ingredient_out
        # Search for the equivalent unit
        q_out, u_out = sql.unit_convert(self.quantity_in, self.unit_in)
        self.ids.q_out.text = str(q_out)
        self.ids.unit_out.text = u_out
        # Fill the sugar/unit
        subset = sql.database.loc[sql.database['ingredient_de'] == ingredient_out]
        if subset.size == 0:
            subset = sql.database.loc[sql.database['ingredient_en'] == ingredient_out]
        #print(subset)
        if subset.size > 0:
            #print(subset.iloc[0]['sugar'])
            self.ids.sugar_per_unit.text = str(subset.iloc[0]['sugar'])
        else:
            self.ids.sugar_per_unit.text = '0'


class InputMenu(Screen):
    def read(self):
        global image_file
        image_file = self.ids.fc.selection
        self.manager.current = 'loading'


class Intro(Screen):
    pass


class Loading(Screen):
    def loading(self):
        Clock.schedule_once(self.process_ai, 3)

    def process_ai(self, dt):
        global ingredient_frame
        print(image_file[0])
        if str(image_file[0]) is not None:
            ingredient_frame = createIngredientDict(image=image_file[0])
            print(ingredient_frame)
            self.manager.current = 'processing'