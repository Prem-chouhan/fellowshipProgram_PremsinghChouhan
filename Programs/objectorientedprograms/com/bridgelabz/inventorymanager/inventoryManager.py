import json

inventory = {'Rice': []}
inventory['Rice'].append({
    'name': 'Sharbati',
    'weight': '10kgs',
    'price': 1000
})
inventory['Rice'].append({
    'name': 'Basmati',
    'weight': '10kgs',
    'price': 1500
})
inventory['Rice'].append({
    'name': 'Ankur',
    'weight': '10kgs',
    'price': 500
})

inventory['Pulses'] = []
inventory['Pulses'].append({
    'name': 'Groundnuts',
    'weight': '10kgs',
    'price': 200
})
inventory['Pulses'].append({
    'name': 'Peanuts',
    'weight': '10kgs',
    'price': 100
})
inventory['Pulses'].append({
    'name': 'Green peas',
    'weight': '10kgs',
    'price': 150
})

inventory['Wheat'] = []
inventory['Wheat'].append({
    'name': 'rahet',
    'weight': '10kgs',
    'price': 100
})
inventory['Wheat'].append({
    'name': 'karet',
    'weight': '10kgs',
    'price': 200
})
inventory['Wheat'].append({
    'name': 'Shahet',
    'weight': '10kgs',
    'price': 300
})

with open("distros.json", "w") as outfile:
    inventory['Rice'].append({
        'name': 'pqr',
        'weight': '10kgs',
        'price': 1000
    })
    inventory["Pulses"].append({
        'name': 'pqr',
        'weight': '10kgs',
        'price': 1000
    })
    inventory["Wheat"].append({
        'name': 'pqr',
        'weight': '10kgs',
        'price': 1000
    })
    json.dump(inventory, outfile, indent=4, sort_keys=True)

with open('distros.json') as readfile:
    data = json.load(readfile)
    lst = ['Rice', 'Pulses', "Wheat"]
    total = 0
    for outer_loop in range(len(lst)):
        for inner_loop in data[lst[outer_loop]]:
            print("This are Values for each person :----->", total + inner_loop["price"])
            total = total + inner_loop['price']
print("Total Amount spent is :-", total)

with open("distros.json", 'w') as outfile:
    inventory["Wheat"].append({
        "Total Amount for Inventory": total,
    })
    json.dump(inventory, outfile, indent=4, sort_keys=True)


