food=[("apple", "fruit"),("banana", "fruit"),("carrot", "vegetable"),("tomato", "vegetable"),("milk", "dairy")]
itemsorted={}
for i in food:
	itemsorted.setdefault(i[1], []).append(i[0])
print(itemsorted)
