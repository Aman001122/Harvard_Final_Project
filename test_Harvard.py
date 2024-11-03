import unittest
from io import StringIO
import sys
from Harvard_Final_Project import add_habit, log_completion, display_statistics

class HabitTrackerTests(unittest.TestCase):
    """Unit tests for the habit tracker functionality."""

    def setUp(self):
        """Initialize a habit tracker for each test."""
        self.habits = {}

    def test_add_habit(self):
        """Verify that a new habit is added successfully."""
        add_habit(self.habits, habit_name="exercise")
        self.assertIn("exercise", self.habits)
        self.assertEqual(self.habits["exercise"]["target_days"], 30)
        self.assertEqual(self.habits["exercise"]["logged_days"], 0)

    def test_log_habit_completion(self):
        """Check that a habit completion is logged properly."""
        self.habits["reading"] = {'target_days': 10, 'logged_days': 0}
        log_completion(self.habits, habit_name="reading")
        self.assertEqual(self.habits["reading"]["logged_days"], 1)

    def test_display_statistics_no_habits(self):
        """Test the output when no habits have been added."""
        captured_output = StringIO()
        sys.stdout = captured_output
        display_statistics(self.habits)
        sys.stdout = sys.__stdout__
        self.assertIn("You haven't added any habits yet.", captured_output.getvalue())

    def test_display_statistics_with_habits(self):
        """Ensure statistics display correctly when habits are present."""
        self.habits["meditation"] = {'target_days': 20, 'logged_days': 5}
        captured_output = StringIO()
        sys.stdout = captured_output
        display_statistics(self.habits)
        sys.stdout = sys.__stdout__
        self.assertIn("meditation: 5 out of 20 days completed (25.00%)", captured_output.getvalue())

if __name__ == "__main__":
    unittest.main()
