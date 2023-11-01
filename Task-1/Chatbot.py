import re


recipes = {
    
    'pancakes': 'To make pancakes, whisk together flour, sugar, baking powder, and salt in a bowl. In another bowl, whisk '
                'together milk, egg, and melted butter. Combine wet and dry ingredients, mixing until just combined. '
                'Heat a griddle or frying pan over medium-high heat and grease it. Pour 1/4 cup of batter for each pancake. '
                'Cook until bubbles form on the surface, then flip and cook until golden brown.',
    
    'chocolate chip cookies': 'To make chocolate chip cookies, preheat the oven to 350°F (175°C). In a bowl, cream together '
                              'butter, sugar, and brown sugar. Beat in eggs, one at a time, then stir in vanilla. In another bowl, '
                              'combine flour, baking soda, and salt. Gradually add the dry ingredients to the wet mixture, '
                              'then fold in chocolate chips. Drop spoonfuls of dough onto a baking sheet and bake for 10-12 minutes.',

    'biryani': 'To make biryani, marinate chicken or meat in yogurt and spices. In a large pot, sauté onions until golden brown. '
               'Add marinated meat and cook until it changes color. Add rice, water, and seasonings. Cook until rice is tender '
               'and meat is cooked through. Garnish with fried onions, mint, and coriander leaves. Serve hot with raita.'
}

greetings = ['hi', 'hello', 'hey', 'howdy', 'good day']


recipe_patterns = {re.compile(r'\b{}\b'.format(recipe), re.IGNORECASE): procedure for recipe, procedure in recipes.items()}
recipe_list = ", ".join(recipes.keys())
def chatbot_response(user_input):
    user_input = user_input.lower()
    for pattern, procedure in recipe_patterns.items():
        if pattern.search(user_input):
            return procedure
    
    for greeting in greetings:
        if greeting in user_input:
            return f"Hello! How can I assist you today? Here are some recipes you can make: {recipe_list}"
    
    return f"I don't have the procedure for that recipe. Try asking about {recipe_list}"


while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)
