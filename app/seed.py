#!/usr/bin/env python3

from models.models import *
from database.database import session
from faker import Faker
import random

if __name__=='__main__':
    session.query(Recipe).delete()
    session.query(Ingredient).delete()
    session.query(Meal_plan).delete()
    session.commit()
    print('seeding......')

    fake=Faker()

    recipe_names=["Amish Casserole","Creamy White Chili",
                 "Banana Bread","Cheeseburger Soup","Chicken Potpie",
                 "Chicken Fajitas","Apple Pie","Basic Homemade Bread",
                 "Zucchini Cupcakes","Cheddar Meat Loaves","Meat Loaf",
                 "Moist Chocolate Cake","Stuffed Pepper Soup","Fluffy Key Lime Pie",
                 "Pineapple Orange Cake","Baked Spaghetti","Buttery Cornbread",
                 "Chicken Curry","Rice","Chocolate Cake","Mushroom Chicken",
                 "Hot Milk Cake","Rustic Italian Tortellini Soup","Coffee","Pizza",
                 "Roasted Meat","Burger","Cake","Cookies","Potato Pie","Salad"
                 "Fried Meat","Bone Soup"]
    categorys=["breakfast","lunch","dinner","dessert"]




    recipes=[]
    for i in range (20):
        recipe=Recipe(
            name=random.choice(recipe_names),
            category=random.choice(categorys),
            instructions=fake.sentence(),
            time_in_minutes=fake.random_int(5,30)
        )
        session.add(recipe)
        session.commit()
        recipes.append(recipe)
   
    meal_plan_names=["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]
    meal_plans=[] 
    for i in range(10):
        meal_plan=Meal_plan(
            name=random.choice(meal_plan_names),
            start_date=fake.date_of_birth(),
            end=fake.date_of_birth()
        )
        session.add(meal_plan)
        session.commit()
        meal_plans.append(meal_plan)
    
    
    ingredient_names=["Gruyere CheeseIt","Gouda CheeseIt","Feta CheeseFeta","Milk"
                     " Coriander","Chives","Galangal","Tulsi","Sage","Rosemary",
                     "Yellow Chillies","Oregano","Nasturtium","Salt","Mustard ",
                     "Paprika","Mint Leaves","Marjoram","Lemongrass","Red Chilli",
                     "Saffron","Dried Fenugreek"]
    ingredients=[]
    for recipe in recipes:
        for i in range(random.randint(1,20)):
            meal_plan=random.choice(meal_plans)
            ingredient=Ingredient(
                name=random.choice(ingredient_names),
                recipe_id=recipe.id,
                meal_plan_id=meal_plan.id
            )   
            session.add(ingredient)
            session.commit()
            ingredients.append(ingredient)  
    session.bulk_save_objects(ingredients) 
    session.commit()
    session.close()       

  
