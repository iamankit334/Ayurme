import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ayurveda_project.settings')
django.setup()

from nutrition.models import Recipe

# Additional Ayurvedic recipes to add
new_recipes = [
    # Breakfast recipes
    {
        'name': 'Quinoa Porridge with Almonds',
        'recipe_text': 'Cook quinoa in coconut milk, add chopped almonds, cinnamon, and a touch of maple syrup. Serve warm.',
        'meal_time': 'Breakfast',
        'food_type': 'Main Course',
        'pacifies': 'Vata, Pitta',
        'aggravates': 'Kapha',
        'specific_conditions': 'Digestive health, Energy boost'
    },
    {
        'name': 'Turmeric Golden Milk',
        'recipe_text': 'Heat almond milk with turmeric, ginger, cinnamon, and black pepper. Add honey to taste.',
        'meal_time': 'Breakfast',
        'food_type': 'Beverage',
        'pacifies': 'Vata, Kapha',
        'aggravates': 'Pitta',
        'specific_conditions': 'Anti-inflammatory, Immune support'
    },
    {
        'name': 'Chia Seed Pudding',
        'recipe_text': 'Mix chia seeds with almond milk, let sit overnight. Top with fresh berries and nuts.',
        'meal_time': 'Breakfast',
        'food_type': 'Main Course',
        'pacifies': 'Pitta, Kapha',
        'aggravates': 'Vata',
        'specific_conditions': 'Omega-3 rich, Digestive health'
    },

    # Lunch recipes
    {
        'name': 'Lentil Soup (Dal)',
        'recipe_text': 'Cook red lentils with tomatoes, onions, garlic, cumin, and coriander. Season with fresh cilantro.',
        'meal_time': 'Lunch',
        'food_type': 'Main Course',
        'pacifies': 'Vata, Pitta',
        'aggravates': 'Kapha',
        'specific_conditions': 'Protein rich, Heart healthy'
    },
    {
        'name': 'Steamed Vegetables with Rice',
        'recipe_text': 'Steam seasonal vegetables and serve with brown rice and a light sesame dressing.',
        'meal_time': 'Lunch',
        'food_type': 'Main Course',
        'pacifies': 'Pitta, Kapha',
        'aggravates': 'Vata',
        'specific_conditions': 'Light and nutritious, Easy digestion'
    },
    {
        'name': 'Cucumber Raita',
        'recipe_text': 'Mix yogurt with grated cucumber, cumin, mint, and a pinch of salt.',
        'meal_time': 'Lunch',
        'food_type': 'Side',
        'pacifies': 'Pitta, Kapha',
        'aggravates': 'Vata',
        'specific_conditions': 'Cooling effect, Digestive aid'
    },
    {
        'name': 'Mung Bean Soup',
        'recipe_text': 'Cook split mung beans with vegetables, turmeric, and mild spices. Serve hot.',
        'meal_time': 'Lunch',
        'food_type': 'Main Course',
        'pacifies': 'All Doshas',
        'aggravates': '',
        'specific_conditions': 'Detoxifying, Easy to digest'
    },

    # Dinner recipes
    {
        'name': 'Vegetable Curry',
        'recipe_text': 'Cook mixed vegetables in coconut milk with curry spices, served with quinoa.',
        'meal_time': 'Dinner',
        'food_type': 'Main Course',
        'pacifies': 'Vata, Pitta',
        'aggravates': 'Kapha',
        'specific_conditions': 'Anti-inflammatory, Nutrient dense'
    },
    {
        'name': 'Baked Sweet Potato',
        'recipe_text': 'Bake sweet potatoes and serve with steamed greens and a light tahini dressing.',
        'meal_time': 'Dinner',
        'food_type': 'Main Course',
        'pacifies': 'Vata, Kapha',
        'aggravates': 'Pitta',
        'specific_conditions': 'Blood sugar balancing, Vitamin rich'
    },
    {
        'name': 'Herbal Infusion',
        'recipe_text': 'Steep chamomile, peppermint, and ginger in hot water. Sweeten with honey if desired.',
        'meal_time': 'Dinner',
        'food_type': 'Beverage',
        'pacifies': 'Pitta, Kapha',
        'aggravates': 'Vata',
        'specific_conditions': 'Relaxing, Digestive support'
    },
    {
        'name': 'Stir-Fried Greens',
        'recipe_text': 'Quickly stir-fry seasonal greens with garlic, ginger, and a splash of tamari.',
        'meal_time': 'Dinner',
        'food_type': 'Side',
        'pacifies': 'All Doshas',
        'aggravates': '',
        'specific_conditions': 'Mineral rich, Detoxifying'
    },
    {
        'name': 'Coconut Rice',
        'recipe_text': 'Cook basmati rice in coconut milk with cardamom and serve as a side dish.',
        'meal_time': 'Dinner',
        'food_type': 'Side',
        'pacifies': 'Vata, Pitta',
        'aggravates': 'Kapha',
        'specific_conditions': 'Comforting, Energy sustaining'
    },
    {
        'name': 'Fruit Compote',
        'recipe_text': 'Simmer seasonal fruits with cinnamon and serve warm or chilled.',
        'meal_time': 'Dinner',
        'food_type': 'Side',
        'pacifies': 'Vata, Kapha',
        'aggravates': 'Pitta',
        'specific_conditions': 'Digestive aid, Natural sweetness'
    },

    # Additional variety
    {
        'name': 'Spiced Apple Tea',
        'recipe_text': 'Simmer apple slices with cinnamon, cloves, and ginger. Strain and serve warm.',
        'meal_time': 'Breakfast',
        'food_type': 'Beverage',
        'pacifies': 'Vata, Kapha',
        'aggravates': 'Pitta',
        'specific_conditions': 'Warming, Respiratory support'
    },
    {
        'name': 'Roasted Root Vegetables',
        'recipe_text': 'Roast carrots, beets, and parsnips with herbs and olive oil.',
        'meal_time': 'Lunch',
        'food_type': 'Side',
        'pacifies': 'Vata, Pitta',
        'aggravates': 'Kapha',
        'specific_conditions': 'Grounding, Blood building'
    },
    {
        'name': 'Almond Butter Toast',
        'recipe_text': 'Spread almond butter on whole grain toast, top with sliced banana.',
        'meal_time': 'Breakfast',
        'food_type': 'Main Course',
        'pacifies': 'Vata, Pitta',
        'aggravates': 'Kapha',
        'specific_conditions': 'Healthy fats, Sustained energy'
    },
    {
        'name': 'Cucumber Mint Cooler',
        'recipe_text': 'Blend cucumber, mint, lime, and water. Serve chilled.',
        'meal_time': 'Lunch',
        'food_type': 'Beverage',
        'pacifies': 'Pitta, Kapha',
        'aggravates': 'Vata',
        'specific_conditions': 'Hydrating, Cooling'
    },
    {
        'name': 'Steamed Fish with Herbs',
        'recipe_text': 'Steam white fish with dill, lemon, and serve with steamed vegetables.',
        'meal_time': 'Dinner',
        'food_type': 'Main Course',
        'pacifies': 'Vata, Pitta',
        'aggravates': 'Kapha',
        'specific_conditions': 'Omega-3 rich, Light protein'
    }
]

def add_recipes():
    added_count = 0
    for recipe_data in new_recipes:
        # Check if recipe already exists
        if not Recipe.objects.filter(name=recipe_data['name']).exists():
            Recipe.objects.create(**recipe_data)
            added_count += 1
            print(f"Added: {recipe_data['name']}")
        else:
            print(f"Skipped (already exists): {recipe_data['name']}")

    print(f"\nTotal recipes added: {added_count}")
    print(f"Total recipes in database: {Recipe.objects.count()}")

if __name__ == '__main__':
    add_recipes()
