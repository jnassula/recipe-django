from django.test import TestCase
from django.urls import resolve, reverse
from recipes.views import home, category, recipe
from recipes.models import Recipe, Category, User


class RecipeViewsTest(TestCase):
    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, home)

    def test_recipe_category_view_function_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIs(view.func, category)


    def test_recipe_detail_view_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(view.func, recipe)
        
    def test_recipe_home_returns_status_code_200_OK(self):
        response = self.client.get(reverse('recipes:home'))
        print(response)
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_loads_correct_template(self): 
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            '<h2>Recipes Not Found Here!</h2>',
            response.content.decode('utf-8')
        )

    def test_recipe_category_returns_404_if_recipes_not_found(self):
        response = self.client.get(
                reverse('recipes:category', kwargs={'category_id': 1000})
                )
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_returns_404_if_recipe_not_found(self):
        response = self.client.get(
                reverse('recipes:recipe', kwargs={'id': 1000})
                )
        self.assertEqual(response.status_code, 404)

    def test_recipe_home_template_loads_recipes(self):
        category = Category.objects.create(name='Category')
        author = User.objects.create_user(
                first_name='user',
                last_name='name',
                username='username',
                password='12345',
                email='user@email.com'
                )
        recipe = Recipe.objects.create(
                category=category,
                author=author,
                title='Recipe Title',
                description='Recipe Description',
                slug='recipe-slug',
                preparation_time=10,
                preparation_time_unit='Minutos',
                servings=5,
                servings_unit='Porções',
                preparation_steps='Recipe Preparation Steps',
                preparation_steps_is_html=False,
                is_published=True,
                )
        # self.assert
        ...
