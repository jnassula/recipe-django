from .test_recipe_base import RecipeBaseTest


class RecipeModelTest(RecipeBaseTest):
    def setUp(self):
        self.recipe = self.make_recipe()
        return super().setUp()

    def test_recipe_title_raises_error_if_title_has_more_than_65_chars(self):
        self.fail()
