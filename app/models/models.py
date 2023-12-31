from database.database import Base
from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import relationship

class Recipe(Base):
    __tablename__='recipes'

    id=Column(Integer(),primary_key=True)
    name=Column(String())
    category=Column(String())
    time_in_minutes=Column(Integer())
    instructions=Column(String())
    ingredients=relationship('Ingredient',back_populates='recipe')
    meal_plans=association_proxy('ingredients','meal_plan',creator=lambda gm: Ingredient(meal_plan=gm))

    def __repr__(self):
        return f"Recipe: {self.name} ,Category: {self.category} ,Time: {self.time_in_minutes},Instructions: {self.instructions}"
    

class Meal_plan(Base):
    __tablename__='meal_plans'

    id=Column(Integer(),primary_key=True)
    name=Column(String())
    start_date=Column(String())
    end=Column(Integer())
    ingredients=relationship('Ingredient',back_populates='meal_plan')
    recipes=association_proxy('ingredients','recipe',creator=lambda us : Ingredient(recipe=us))

    def __repr__(self):
        return f"Name : {self.name}"
    

class Ingredient(Base):
    __tablename__='ingredients'

    id=Column(Integer(),primary_key=True)
    name=Column(String())
    recipe_id=Column(Integer(),ForeignKey('recipes.id'))
    meal_plan_id=Column(Integer(),ForeignKey('meal_plans.id'))
    recipe=relationship('Recipe',back_populates='ingredients')
    meal_plan=relationship('Meal_plan',back_populates='ingredients')

    def __repr__(self):
        return   f"Ingredient: {self.name} " 