class Student:
    def __init__(self, name: str, phone: str, email: str, address: str):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "address": self.address,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Student":
        return cls(
            name=data.get("name", ""),
            phone=data.get("phone", ""),
            email=data.get("email", ""),
            address=data.get("address", ""),
        )

    def __str__(self) -> str:
        return f"{self.name}: {self.phone}, {self.email}, {self.address}"