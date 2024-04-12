def get_input():
    shelf_dict = {}
    shopping_list = []

    num_shelves = int(input("Zadejte počet regálů: "))
    for i in range(num_shelves):
        print(f"Zadejte zboží pro regál {i}:")
        while True:
            item = input()
            if item == "":
                break
            shelf_dict[item.lower()] = i

    print("Zadejte zboží, které chcete koupit:")
    while True:
        item = input()
        if item == "":
            break
        shopping_list.append(item.lower())

    return shelf_dict, shopping_list

def find_item(shelf_dict, item):
    for key in shelf_dict.keys():
        if item in key:
            return shelf_dict[key]
    return float('inf')

def optimize_shopping_list(shelf_dict, shopping_list):
    optimized_shopping_list = []

    for item in sorted(shopping_list, key=lambda x: find_item(shelf_dict, x)):
        optimized_shopping_list.append((find_item(shelf_dict, item), item))

    return optimized_shopping_list

def main():
    shelf_dict, shopping_list = get_input()
    optimized_shopping_list = optimize_shopping_list(shelf_dict, shopping_list)

    print("Optimalizovaný nákupní seznam:")
    for i, (shelf, item) in enumerate(optimized_shopping_list):
        print(f"{i}. {item.upper()} -> #{shelf} {item}")

if __name__ == "__main__":
    main()
