from fastapi import APIRouter
from typing import List

from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    country: str

router = APIRouter()

fake_users_db = [
    {"id": 1, "name": "John Doe", "email": "john.doe@example.com", "phone": "+1-555-1234", "country": "USA"},
    {"id": 2, "name": "Jane Smith", "email": "jane.smith@example.com", "phone": "+1-555-2345", "country": "USA"},
    {"id": 3, "name": "Alice Johnson", "email": "alice.johnson@example.com", "phone": "+44-20-7123-4567", "country": "UK"},
    {"id": 4, "name": "Bob Brown", "email": "bob.brown@example.com", "phone": "+61-2-9876-5432", "country": "Australia"},
    {"id": 5, "name": "Charlie Davis", "email": "charlie.davis@example.com", "phone": "+49-170-1234567", "country": "Germany"},
    {"id": 6, "name": "David Wilson", "email": "david.wilson@example.com", "phone": "+33-1-45-67-89-01", "country": "France"},
    {"id": 7, "name": "Eva Martinez", "email": "eva.martinez@example.com", "phone": "+34-91-234-5678", "country": "Spain"},
    {"id": 8, "name": "Frank Moore", "email": "frank.moore@example.com", "phone": "+1-555-3456", "country": "USA"},
    {"id": 9, "name": "Grace Taylor", "email": "grace.taylor@example.com", "phone": "+44-20-8765-4321", "country": "UK"},
    {"id": 10, "name": "Hannah Lee", "email": "hannah.lee@example.com", "phone": "+1-555-4567", "country": "Canada"},
    {"id": 11, "name": "Isaac Harris", "email": "isaac.harris@example.com", "phone": "+61-2-2345-6789", "country": "Australia"},
    {"id": 12, "name": "Jack Clark", "email": "jack.clark@example.com", "phone": "+49-170-2345678", "country": "Germany"},
    {"id": 13, "name": "Kathy Lewis", "email": "kathy.lewis@example.com", "phone": "+33-1-67-89-10-11", "country": "France"},
    {"id": 14, "name": "Liam Walker", "email": "liam.walker@example.com", "phone": "+34-91-345-6789", "country": "Spain"},
    {"id": 15, "name": "Megan Allen", "email": "megan.allen@example.com", "phone": "+1-555-5678", "country": "USA"},
    {"id": 16, "name": "Nathan Young", "email": "nathan.young@example.com", "phone": "+44-20-9876-5432", "country": "UK"},
    {"id": 17, "name": "Olivia King", "email": "olivia.king@example.com", "phone": "+61-2-3456-7890", "country": "Australia"},
    {"id": 18, "name": "Paul Scott", "email": "paul.scott@example.com", "phone": "+49-170-3456789", "country": "Germany"},
    {"id": 19, "name": "Quincy Adams", "email": "quincy.adams@example.com", "phone": "+33-1-78-90-12-13", "country": "France"},
    {"id": 20, "name": "Rita Baker", "email": "rita.baker@example.com", "phone": "+34-91-456-7890", "country": "Spain"},
    {"id": 21, "name": "Sam Green", "email": "sam.green@example.com", "phone": "+1-555-6789", "country": "USA"},
    {"id": 22, "name": "Tina Carter", "email": "tina.carter@example.com", "phone": "+44-20-3456-7890", "country": "UK"},
    {"id": 23, "name": "Ursula Perez", "email": "ursula.perez@example.com", "phone": "+61-2-4567-8901", "country": "Australia"},
    {"id": 24, "name": "Victor Nelson", "email": "victor.nelson@example.com", "phone": "+49-170-4567890", "country": "Germany"},
    {"id": 25, "name": "Wendy Hill", "email": "wendy.hill@example.com", "phone": "+33-1-89-01-23-45", "country": "France"},
    {"id": 26, "name": "Xander Coleman", "email": "xander.coleman@example.com", "phone": "+34-91-567-8901", "country": "Spain"},
    {"id": 27, "name": "Yara Mitchell", "email": "yara.mitchell@example.com", "phone": "+1-555-7890", "country": "USA"},
    {"id": 28, "name": "Zane Rodriguez", "email": "zane.rodriguez@example.com", "phone": "+44-20-1234-5678", "country": "UK"},
    {"id": 29, "name": "Aiden Gonzalez", "email": "aiden.gonzalez@example.com", "phone": "+61-2-5678-9012", "country": "Australia"},
    {"id": 30, "name": "Becca Moore", "email": "becca.moore@example.com", "phone": "+49-170-5678901", "country": "Germany"},
    {"id": 31, "name": "Cameron Wright", "email": "cameron.wright@example.com", "phone": "+33-1-90-12-34-56", "country": "France"},
    {"id": 32, "name": "Diana Carter", "email": "diana.carter@example.com", "phone": "+34-91-678-9012", "country": "Spain"},
    {"id": 33, "name": "Elijah Bennett", "email": "elijah.bennett@example.com", "phone": "+1-555-8901", "country": "USA"},
    {"id": 34, "name": "Felix Gray", "email": "felix.gray@example.com", "phone": "+44-20-2345-6789", "country": "UK"},
    {"id": 35, "name": "Georgia Turner", "email": "georgia.turner@example.com", "phone": "+61-2-6789-0123", "country": "Australia"},
    {"id": 36, "name": "Henry Martinez", "email": "henry.martinez@example.com", "phone": "+49-170-6789012", "country": "Germany"},
    {"id": 37, "name": "Ivy Scott", "email": "ivy.scott@example.com", "phone": "+33-1-23-45-67-89", "country": "France"},
    {"id": 38, "name": "Jackie Taylor", "email": "jackie.taylor@example.com", "phone": "+34-91-789-0123", "country": "Spain"},
    {"id": 39, "name": "Ken Peters", "email": "ken.peters@example.com", "phone": "+1-555-9012", "country": "USA"},
    {"id": 40, "name": "Lena Cooper", "email": "lena.cooper@example.com", "phone": "+44-20-3456-7891", "country": "UK"},
    {"id": 41, "name": "Mason Roberts", "email": "mason.roberts@example.com", "phone": "+61-2-7890-1234", "country": "Australia"},
    {"id": 42, "name": "Nina Evans", "email": "nina.evans@example.com", "phone": "+49-170-7890123", "country": "Germany"},
    {"id": 43, "name": "Oscar Thompson", "email": "oscar.thompson@example.com", "phone": "+33-1-12-34-56-78", "country": "France"},
    {"id": 44, "name": "Piper Campbell", "email": "piper.campbell@example.com", "phone": "+34-91-890-1234", "country": "Spain"},
    {"id": 45, "name": "Quinn Moore", "email": "quinn.moore@example.com", "phone": "+1-555-0123", "country": "USA"},
    {"id": 46, "name": "Riley Diaz", "email": "riley.diaz@example.com", "phone": "+44-20-4567-8901", "country": "UK"},
    {"id": 47, "name": "Sophia James", "email": "sophia.james@example.com", "phone": "+61-2-8901-2345", "country": "Australia"},
    {"id": 48, "name": "Travis Lee", "email": "travis.lee@example.com", "phone": "+49-170-8901234", "country": "Germany"},
    {"id": 49, "name": "Uma Patel", "email": "uma.patel@example.com", "phone": "+33-1-23-45-67-89", "country": "France"},
    {"id": 50, "name": "Victor King", "email": "victor.king@example.com", "phone": "+34-91-901-2345", "country": "Spain"}
]


@router.get("/users", response_model=List[User])
async def get_users():
    return fake_users_db

@router.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int):
    user = next((user for user in fake_users_db if user["id"] == user_id), None)
    if user is None:
        return {"error": "User not found"}
    return user
