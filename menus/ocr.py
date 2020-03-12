import pytesseract
from PIL import Image


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def createIngredientDict(image):
    """
    Outputs a dictionary in the form of {'product_name':['quantity','unit'], ...}
    Input: a screenshot of ingredients
    """
    ingredientList = createIngredientList(image)
    ingredientDict = {}

    for elem in ingredientList:
        quantity = isolateQuantity(elem)
        unit = isolateUnit(elem)
        productName = isolateProductName(ingredient=elem, quantity=isolateQuantity(elem, original=True), unit=unit)
        productName = cleanUpProductName(productName)
        ingredientDict[productName] = [quantity, unit]

    return ingredientDict

def createIngredientList(imagePath):
    """
    Creates a list of ingredients from a screenshot
    """
    image = Image.open(imagePath)
    text = cleanUp(pytesseract.image_to_string(image)).lower()
    ingredients = text.splitlines()
    # Remove empty entries
    if '' in ingredients:
        ingredients.remove('')
    return ingredients

def cleanUp(text):
    """
    Function to counter common Tesseract mistakes
    """
    # Replacing '%' wit ',5' (e.g. in 1,5 Liter); fits most of the time
    text = text.replace('%',',5 ')
    if (text[0]==','):
        text = text.replace(',',"0,")
    text = text.replace("1, 5", "1,5" )
    text = text.replace("ii",'ü')
    text = text.replace('9', 'g')
    text = text.replace("grin", "grün")
    text = text.replace("dél", "öl")
    text = text.replace('¥', '')
    return text


def cleanUpProductName(text):
    """
    Function to clean up further residues of falsely left in details
    """
    text = text.replace(",5", '')
    # Removes all digits that might be left over
    text = ''.join(i for i in text if not i.isdigit())

    return text.strip()


def isolateQuantity(ingredient, original=False):
    """
    Isolates the digits from the input String. Original=True is used for eliminating the quantity from the productname.
    With original=False, "1, 5" will become "1,5"
    With original=True, "1, 5" will stay "1, 5"
    """
    set = '0123456789,'
    text = ''.join([c for c in ingredient if c in set])

    if (original):
        if "n.B." in ingredient:
            return "nach Belieben"
        if text.strip() == ",5":
            return "0,5"
    text = text.replace(',', '.')
    return text


def isolateUnit(ingredient):
    """
    Isolates the unit from the input String
    """
    ingredient = ingredient.lower()
    measurementUnitInt = ['gramm', ' g ', 'dekagramm', 'dag', 'kilogramm', ' kg ', 'pfd', 'pfund', 'deciliter', 'dl ',
                          'centiliter', 'cl ', 'ml ', 'liter',
                          'esslöffel', 'el ', 'tl ', 'ssp.' 'tr', 'tropfen', 'sp', 'spritzer', 'schuss', 'messerspitze',
                          'msp', 'tasse', 'scheiben', 'scheibe(n)', 'scheibe', 'zehen', 'zehe',
                          'kleines', 'kleine' 'großes', 'große'
                                                        'etwas', 'prisen', 'prise(n)', 'prise',
                          'bund', 'bd ', 'dosen', 'dose(n)', 'dose', 'glas', 'gläser', 'packungen', 'packung', 'pck.',
                          'rollen', 'rolle(n)', 'rolle', 'würfel']

    measurementUnitUS = ['teaspoons', 'tablespoons', 'cups', 'containers', 'packets', 'bags', 'quarts', 'pounds',
                         'cans', 'bottles',
                         'pints', 'packages', 'ounces', 'jars', 'heads', 'gallons', 'drops', 'envelopes', 'bars',
                         'boxes', 'pinches',
                         'dashes', 'bunches', 'recipes', 'layers', 'slices', 'links', 'bulbs', 'stalks', 'squares',
                         'sprigs',
                         'fillets', 'pieces', 'legs', 'thighs', 'cubes', 'granules', 'strips', 'trays', 'leaves',
                         'loaves', 'halves']

    for elem in measurementUnitInt:
        if elem in ingredient:
            return elem.strip()

    for elem in measurementUnitUS:
        if elem in ingredient:
            return elem

    return ''

def isolateProductName(ingredient, quantity, unit):
    """
    Stripping the quantity and unit from the ingredient, leaving the product name
    """
    return ingredient.replace(str(quantity), '').replace(unit, '').strip()


