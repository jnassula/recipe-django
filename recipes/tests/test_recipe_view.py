from django.urls import resolve, reverse
from recipes.views import home, category, recipe
from .test_recipe_base import RecipeBaseTest


class RecipeViewsTest(RecipeBaseTest):
    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse("recipes:home"))
        self.assertIs(view.func, home)

    def test_recipe_category_view_function_is_correct(self):
        view = resolve(reverse("recipes:category", kwargs={"category_id": 1}))
        self.assertIs(view.func, category)

    def test_recipe_detail_view_function_is_correct(self):
        view = resolve(reverse("recipes:recipe", kwargs={"id": 1}))
        self.assertIs(view.func, recipe)

    def test_recipe_home_returns_status_code_200_OK(self):
        response = self.client.get(reverse("recipes:home"))
        print(response)
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_loads_correct_template(self):
        response = self.client.get(reverse("recipes:home"))
        self.assertTemplateUsed(response, "recipes/pages/home.html")

    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
        response = self.client.get(reverse("recipes:home"))
        self.assertIn(
            "<h2>Recipes Not Found Here!</h2>", response.content.decode("utf-8")
        )

    def test_recipe_category_returns_404_if_recipes_not_found(self):
        response = self.client.get(
            reverse("recipes:category", kwargs={"category_id": 1000})
        )
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_returns_404_if_recipe_not_found(self):
        response = self.client.get(reverse("recipes:recipe", kwargs={"id": 1000}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_home_template_loads_recipes(self):
        self.make_recipe()
        response = self.client.get(reverse("recipes:home"))
        context = response.context["recipes"]
        content = response.content.decode("utf-8")
        self.assertEqual(context.first().title, "Recipe Title")
        self.assertIn("Recipe Title", content)
        self.assertEqual(len(context), 1)
