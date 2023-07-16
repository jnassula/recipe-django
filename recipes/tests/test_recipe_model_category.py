#!/usr/bin/env python3
from .test_recipe_base import RecipeBaseTest
from django.core.exceptions import ValidationError
from parameterized import parameterized


class RecipeModelTest(RecipeBaseTest):
    def setUp(self):
        self.category = self.make_category(
            name='Category Testing'
        )
        return super().setUp()

    def test_recipe_category_model_string_represetation_is_name_field(self):
        self.assertEqual(
            str(self.category),
            self.category.name
        )

    def test_recipe_category_model_name_has_65_chars(self):
        self.category.name = 'A' * 66
        with self.assertRaises(ValidationError):
            self.category.full_clean()
