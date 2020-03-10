
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
    for keys, vals in input_frame.items():
        found= False
        for unit in unit_scala:
            for possiblitiy in unit['possible']:
                if vals[1] is possiblitiy:
                    input_frame[keys][0]= input_frame[keys][0] * unit['scala']
                    input_frame[keys][1]= unit['out']
                    found = True
                    break
        if not found:
            print('Ups! ' + vals[1] + " for " + keys + " is not found, is it a volume or mass?")
            types= input()
            r_unit = 'g'
            if 'volume' in types:
                r_unit = 'ml'
            elif 'mass' in types:
                r_unit = 'g'
            print ("Ups! " + vals[1] + " for " + keys + " is not a known unit! Please give the conversion to " + r_unit)
            conv= input()
            input_frame[keys][0] = input_frame[keys] [0]*int(conv)
            input_frame[keys][1] = r_unit
            return input_frame

input_frame_bs = {'apples': [10, 'kg'],
                     'chocolate': [140, 'g']}

out= unit_convert(input_frame_bs)
print(out)
