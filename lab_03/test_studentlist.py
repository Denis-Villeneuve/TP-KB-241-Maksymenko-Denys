import os
import tempfile
import unittest

from student import Student
from student_list import StudentList


class TestStudentList(unittest.TestCase):
    def setUp(self):
        self.sl = StudentList()
        self.s1 = Student("Alice", "111", "a@example.com", "Addr1")
        self.s2 = Student("Bob", "222", "b@example.com", "Addr2")
        self.s3 = Student("Carol", "333", "c@example.com", "Addr3")

    def test_add_sorted(self):
        self.sl.add_student(self.s2)
        self.sl.add_student(self.s1)
        self.sl.add_student(self.s3)
        names = [s.name for s in self.sl.list_all()]
        self.assertEqual(names, ["Alice", "Bob", "Carol"])

    def test_remove_by_name(self):
        self.sl.add_student(self.s1)
        self.sl.add_student(self.s2)
        ok = self.sl.remove_student_by_name("Alice")
        self.assertTrue(ok)
        names = [s.name for s in self.sl.list_all()]
        self.assertEqual(names, ["Bob"])

    def test_remove_not_found(self):
        ok = self.sl.remove_student_by_name("Noname")
        self.assertFalse(ok)

    def test_update_student(self):
        self.sl.add_student(self.s1)
        ok = self.sl.update_student(
            "Alice", new_phone="999", new_email="new@example.com"
        )
        self.assertTrue(ok)
        s = self.sl.find_by_name("Alice")
        self.assertEqual(s.phone, "999")
        self.assertEqual(s.email, "new@example.com")

    def test_save_and_load_json(self):
        self.sl.add_student(self.s1)
        self.sl.add_student(self.s2)

        import utils
        from utils import FileManager  # щоб було використання

        with tempfile.TemporaryDirectory() as tmpdir:
            path = os.path.join(tmpdir, "students.json")
            self.sl.save_to_file(path)

            sl2 = StudentList()
            sl2.load_from_file(path)
            names = [s.name for s in sl2.list_all()]
            self.assertEqual(names, ["Alice", "Bob"])


if __name__ == "__main__":
    unittest.main()