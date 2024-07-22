korean = [{'menu' : "김치찌개", "price" : 8000}, {'menu' : "감자탕", "price" : 32000}, {'menu' : "제육볶음", "price" : 12000}]

for dict in korean:
    print(dict.get('menu'), dict.get('price'))

def tot_price(korean):
    total_price = 0
    for dict in korean:
        total_price += dict.get('price')
    return total_price

print(f"총가격 : {tot_price(korean)}")