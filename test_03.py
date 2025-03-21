# leetcode 2115. Find All Possible Recipes from Given Supplies

# 1.) Testcases passed!
# 2.) Time Limit Exceeded. Gets wrong answers...
def findAllRecipes_00(recipes: list[str], ingredients: list[list[str]], supplies: list[str]) -> list[str]:
    failed = 0
    def all_ingredients_in_supplies(l: list[str]) -> bool:
        for val in l:
            if val not in supplies:
                if len(ingredients) == 1:
                    nonlocal failed
                    failed += 1
                return False
        return True
    
    res = []
    while len(ingredients) > 0 and failed < 2:
        for i, val in enumerate(ingredients):
            if all_ingredients_in_supplies(ingredients[i]):
                ingredients.remove(val)
                res.append(recipes[i])
                supplies.append(recipes[i])
                recipes.remove(recipes[i])

    return res


# unfinished thoughts...
def findAllRecipes_01(recipes: list[str], ingredients: list[list[str]], supplies: list[str]) -> list[str]:
    set_recipes = set()
    for val in recipes:
        set_recipes.add(val)
    for _val in ingredients:
        for __val in _val:
            set_recipes.add(__val)
    print(set_recipes)
    set_supplies = set(supplies)
    print(set_supplies)
    val_ = set_recipes.difference(set_supplies)
    print(val_)
    return [""]


# 1.) Testcases passed!
# 2.) Memory Limit Exceeded 9 / 113 testcases passed
def findAllRecipes(recipes: list[str], ingredients: list[list[str]], supplies: list[str]) -> list[str]:
    def all_ingredients_in_supplies(l: list[str]) -> bool:
        for val in l:
            if val not in supplies:
                return False
        return True
    
    local_dict = dict()
    for i, val in enumerate(recipes):
        local_dict[val] = ingredients[i]
    for i, _val in enumerate(recipes):
        for j, __val in enumerate(ingredients):
            if _val in ingredients[j]:
                ingredients[j] += local_dict[_val]
                ingredients[j].remove(_val)
    print(ingredients)
    res = []
    for i, ___val in enumerate(ingredients):
        if all_ingredients_in_supplies(___val):
            res.append(recipes[i])

    return res

# NOTE: Still have to finish this one.

def main() -> None:
    # print(findAllRecipes(recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"])) # ["bread"]
    # print(findAllRecipes(recipes = ["bread","sandwich"], ingredients = [["yeast","flour"], ["bread","meat"]], supplies = ["yeast","flour","meat"])) # ["bread","sandwich"]
    # print(findAllRecipes(recipes = ["sandwich","bread"], ingredients = [["bread","meat"], ["yeast","flour"]], supplies = ["yeast","flour","meat"])) # ["bread","sandwich"]
    print(findAllRecipes(recipes = ["bread","sandwich","burger"], ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], supplies = ["yeast","flour","meat"]))
    # print(findAllRecipes(recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast"])) # []


if __name__ == '__main__':
    main()
