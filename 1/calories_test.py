import unittest
from calories import Calories

class TestCalories(unittest.TestCase):

    def test_it_starts_empty(self):
        c = Calories()
        self.assertEqual(c.current_max, None)
        self.assertEqual(c.current_max_elf, None)
        self.assertEqual(c.running_sum, 0)
        self.assertEqual(c.running_elf, 1)

    def test_update_number(self):
        c = Calories()
        c.update(1000)
        self.assertEqual(c.current_max, None)
        self.assertEqual(c.current_max_elf, None)
        self.assertEqual(c.running_sum, 1000)
        self.assertEqual(c.running_elf, 1)


    def test_update_empty(self):
        c = Calories()
        c.update(1000)
        c.next_elf()
        self.assertEqual(c.current_max, 1000)
        self.assertEqual(c.current_max_elf, 1)
        self.assertEqual(c.running_sum, 0)
        self.assertEqual(c.running_elf, 2)

    def test_running_sum(self):
        c = Calories()
        c.update(1000)
        c.update(2000)
        self.assertEqual(c.current_max, None)
        self.assertEqual(c.current_max_elf, None)
        self.assertEqual(c.running_sum, 3000)
        self.assertEqual(c.running_elf, 1)

    def test_update_max(self):
        c = Calories()
        c.update(1000)
        c.next_elf()
        c.update(1000)
        c.update(1000)
        c.next_elf()
        self.assertEqual(c.current_max, 2000)
        self.assertEqual(c.current_max_elf, 2)
        self.assertEqual(c.running_sum, 0)
        self.assertEqual(c.running_elf, 3)


    def test_dont_update_max(self):
        c = Calories()
        c.update(10000)
        c.next_elf()
        c.update(1000)
        c.update(1000)
        c.next_elf()
        self.assertEqual(c.current_max, 10000)
        self.assertEqual(c.current_max_elf, 1)
        self.assertEqual(c.running_sum, 0)
        self.assertEqual(c.running_elf, 3)

    def test_has_sorting(self):
        c = Calories()
        self.assertIsNotNone(c.sorted_elves)

    def test_ordered_elves(self):
        c = Calories()
        c.update(100)
        c.next_elf()
        c.update(200)
        c.next_elf()
        c.update(300)
        c.next_elf()
        self.assertEqual(c.sorted_elves, [(100, 1), (200, 2), (300, 3)])

    def test_ordered_elves_2(self):
        c = Calories()
        c.update(100)
        c.next_elf()
        c.update(300)
        c.next_elf()
        c.update(200)
        c.next_elf()
        self.assertEqual(c.sorted_elves, [(100, 1), (200, 3), (300, 2)])

    def test_ordered_elves_2(self):
        c = Calories()
        c.update(6000)
        c.next_elf()
        c.update(4000)
        c.next_elf()
        c.update(11000)
        c.next_elf()
        c.update(24000)
        c.next_elf()
        c.update(10000)
        c.next_elf()
        self.assertEqual(c.sorted_elves, [(4000, 2), (6000, 1), (10000, 5), (11000, 3), (24000, 4)])

if __name__ == '__main__':
    unittest.main()
