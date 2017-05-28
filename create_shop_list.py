import json

def read_all_recipes_from_file(file_name):
  recipes = {}
  with open(file_name) as json_data:
    data = json.load(json_data)
    for recipe in data:
      recipes[recipe['recipe_name'].lower()] = recipe
    return recipes


def get_shop_list_by_dishes(cook_book, dishes, person_count):
  shop_list = {}
  for dish in dishes:
    if dish not in cook_book:
      print('Блюдо {} не найдено'.format(dish))
      continue
    for ingridient in cook_book[dish]['ingridients']:
      new_shop_list_item = dict(ingridient)

      new_shop_list_item['quantity'] *= person_count
      if new_shop_list_item['ingridient_name'] not in shop_list:
        shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
      else:
        shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
  return shop_list

def print_shop_list(shop_list):
  for shop_list_item in shop_list.values():
    print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'], 
                            shop_list_item['measure']))

def create_shop_list():
  recipes = read_all_recipes_from_file('recipes.json')
  print(recipes)
  print('Доступные блюда:')
  for recipe_name in recipes.keys():
    print(recipe_name)
  person_count = int(input('Введите количество человек: '))
  dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
    .lower().split(', ')
  shop_list = get_shop_list_by_dishes(recipes, dishes, person_count)
  print_shop_list(shop_list)

create_shop_list()
