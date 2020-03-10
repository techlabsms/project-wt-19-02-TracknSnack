
unit_scala = [
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
        'possible': ['liter', 'l','litre'],
        'scala': 1000,
        'out': 'ml'
    },
    {
        'id': 'ml',
        'possible': ['ml', 'milliliter','millilitre'],
        'scala': 1,
        'out': 'ml'
    },
    {
        'id:': 'el',
        'possible': ['el','esslöffel', 'tablespoon', 'tbsp'],
        'scala': 15,
        'out': 'ml'
    },
    {
        'id': 'tl',
        'possible': ['tl','teelöffel', 'teaspoon', 'tsp'],
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
        'possible': ['ounce','ounces', 'oz', 'oz.'],
        'scala': 28.35,
        'out': 'g'
    },
    {
        'id': 'pfund',
        'possible': ['pfund','pfd'],
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
        'possible': ['zentiliter','centiliter', 'cl'],
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

def unit_convert(input_frame):
    quantity_in = input_frame[0]
    unit_in = input_frame[1]
    for unit in unit_scala:
        for possibility in unit['possible']:
            if unit_in is possibility:
                quantity_in = quantity_in * unit['scala']
                unit_in = unit['out']
    return quantity_in, unit_in





    input_frame_bs[0] = input_frame_bs[0] * unit_scala['scala']
    input_frame_bs[1] = unit_scala['out']
    return input_frame_bs



input_frame_bs = [10, 'kg']

out= unit_convert(input_frame_bs)
print(out)
