import unittest
from figures import Figure, Circle, Triangle


class TestShapeCalculator(unittest.TestCase):
    def test_circle_area(self):
        self.assertAlmostEqual(Circle(5).calculate_area(), 78.54, places=2)

    def test_triangle_area(self):
        self.assertAlmostEqual(
            Triangle(5, 4, 3).calculate_area(), 6.0, places=2
        )

    def test_is_right_triangle(self):
        self.assertTrue(Triangle(3, 4, 5).is_right())
        self.assertFalse(Triangle(3, 4, 6).is_right())

    def test_figure_type_circle_area(self):
        self.assertAlmostEqual(
            Figure(Circle(5)).calculate_area(),
            78.54,
            places=2,
        )

    def test_figure_type_triangle_area(self):
        self.assertAlmostEqual(
            Figure(Triangle(5, 4, 3)).calculate_area(), 6.0, places=2
        )


if __name__ == "__main__":
    unittest.main()
