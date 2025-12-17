from typing import List, Optional
from student import Student
from utils import FileManager


class StudentList:
    def __init__(self) -> None:
        self._students: List[Student] = []

    def list_all(self) -> List[Student]:
        return list(self._students)

    def add_student(self, student: Student) -> None:
        # вставка з сортуванням за ім'ям (ПІБ)
        pos = 0
        for s in self._students:
            if student.name > s.name:
                pos += 1
            else:
                break
        self._students.insert(pos, student)

    def find_by_name(self, name: str) -> Optional[Student]:
        for s in self._students:
            if s.name == name:
                return s
        return None

    def remove_student_by_name(self, name: str) -> bool:
        s = self.find_by_name(name)
        if s is None:
            return False
        self._students.remove(s)
        return True

    def update_student(
        self,
        name: str,
        new_phone: Optional[str] = None,
        new_email: Optional[str] = None,
        new_address: Optional[str] = None,
    ) -> bool:
        s = self.find_by_name(name)
        if s is None:
            return False
        if new_phone is not None and new_phone.strip():
            s.phone = new_phone
        if new_email is not None and new_email.strip():
            s.email = new_email
        if new_address is not None and new_address.strip():
            s.address = new_address
        return True

    # робота з файлом через FileManager, але формат — список dict з простими полями
    def load_from_file(self, path: str) -> None:
        raw = FileManager.read_json(path)
        self._students = [Student.from_dict(d) for d in raw]

    def save_to_file(self, path: str) -> None:
        raw = [s.to_dict() for s in self._students]
        FileManager.write_json(path, raw)