import os
import unittest
import lab2

class TestPhonebook(unittest.TestCase):

    def setUp(self):
        lab2.students = [
            {"name": "Bob", "phone": "1", "email": "b@e.com", "address": "Kyiv"},
            {"name": "Emma", "phone": "2", "email": "e@e.com", "address": "Lviv"},
        ]

    def test_add_student(self):
        lab2.students = []
        lab2.add_student("Carl", "3", "c@e.com", "Odesa")
        self.assertEqual(len(lab2.students), 1)
        self.assertEqual(lab2.students[0]["name"], "Carl")

    def test_delete_student(self):
        result = lab2.delete_student_by_name("Bob")
        self.assertTrue(result)
        self.assertEqual(len(lab2.students), 1)
        self.assertEqual(lab2.students[0]["name"], "Emma")

    def test_delete_student_not_found(self):
        result = lab2.delete_student_by_name("Noname")
        self.assertFalse(result)
        self.assertEqual(len(lab2.students), 2)

    def test_update_student(self):
        result = lab2.update_student(
            "Bob",
            new_phone="999",
            new_email="new@e.com",
            new_address="Dnipro"
        )
        self.assertTrue(result)
        self.assertEqual(lab2.students[0]["phone"], "999")
        self.assertEqual(lab2.students[0]["email"], "new@e.com")
        self.assertEqual(lab2.students[0]["address"], "Dnipro")

    def test_update_student_not_found(self):
        result = lab2.update_student("Noname", new_phone="555")
        self.assertFalse(result)

    def test_load_and_save_csv(self):
        tmp_file = "test_students.csv"

        lab2.save_students_to_csv(tmp_file)
        lab2.students = []
        lab2.load_students_from_csv(tmp_file)

        self.assertEqual(len(lab2.students), 2)
        self.assertEqual(lab2.students[0]["name"], "Bob")

        if os.path.exists(tmp_file):
            os.remove(tmp_file)


if __name__ == "__main__":
    unittest.main()
