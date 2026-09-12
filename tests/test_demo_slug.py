import unittest

from demo_slug import slugify


class SlugifyTests(unittest.TestCase):
    def test_lowercases_and_joins_words(self):
        self.assertEqual(slugify("Hello Codex"), "hello-codex")

    def test_collapses_repeated_separators(self):
        self.assertEqual(slugify("  Review---fix___loop  "), "review-fix-loop")

    def test_rejects_blank_or_punctuation_only_input(self):
        for value in ("", "   ", "!!!"):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    slugify(value)

    def test_rejects_non_string_input(self):
        with self.assertRaises(TypeError):
            slugify(None)  # type: ignore[arg-type]


if __name__ == "__main__":
    unittest.main()
