from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

# Pydantic model to define the phone structure
class Phone(BaseModel):
    id: int
    brand: str
    model: str
    year: int
    price: float
    picture_url: str  # Added picture_url to the model

phones_db = [
    {
        "id": 1,
        "brand": "Apple",
        "model": "iPhone 14",
        "year": 2023,
        "price": 999.99,
        "picture_url": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-14-3.jpg"
    },
    {
        "id": 2,
        "brand": "Samsung",
        "model": "Galaxy S23 5G",
        "year": 2023,
        "price": 799.99,
        "picture_url": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-s23-5g-1.jpg"
    },
    {
        "id": 3,
        "brand": "Google",
        "model": "Pixel 8 Pro",
        "year": 2023,
        "price": 899.99,
        "picture_url": "https://fdn2.gsmarena.com/vv/pics/google/google-pixel-8-1.jpg"
    },
    {
        "id": 4,
        "brand": "OnePlus",
        "model": "10 Pro",
        "year": 2023,
        "price": 245,
        "picture_url": "https://fdn2.gsmarena.com/vv/pics/oneplus/oneplus-10-pro-1.jpg"
    },
    {
        "id": 5,
        "brand": "Xiaomi",
        "model": "12 Ultra",
        "year": 2022,
        "price": 399.99,
        "picture_url": "https://fdn2.gsmarena.com/vv/pics/xiaomi/xiaomi-12s-ultra-black-1.jpg"
    },
    {
        "id": 6,
        "brand": "Sony",
        "model": "Xperia 5 IV",
        "year": 2022,
        "price": 812,
        "picture_url": "https://fdn2.gsmarena.com/vv/pics/sony/sony-xperia-5-iv-ecru-white.jpg"
    },
    {
        "id": 7,
        "brand": "Samsung",
        "model": "Galaxy Z Fold6",
        "year": 2024,
        "price": 1719.99,
        "picture_url": "https://fdn2.gsmarena.com/vv/pics/samsung/samsung-galaxy-z-fold6-2.jpg"
    },
    {
        "id": 8,
        "brand": "Apple",
        "model": "iPhone 16 Pro Max",
        "year": 2024,
        "price": 1499.99,
        "picture_url": "https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-16-pro-max-1.jpg"
    },
    {
        "id": 9,
        "brand": "Honor",
        "model": "X8b",
        "year": 2023,
        "price": 319,
        "picture_url": "https://fdn2.gsmarena.com/vv/pics/honor/honor-x8b-1.jpg"
    },
    {
        "id": 10,
        "brand": "LG",
        "model": "K92 5G",
        "year": 2020,
        "price": 119,
        "picture_url": "https://fdn2.gsmarena.com/vv/pics/lg/lg-k92-5g-1.jpg"
    },
    {
        "id": 11,
        "brand": "HTC",
        "model": "Wildfire E5 Plus",
        "year": 2025,
        "price": 67,
        "picture_url": "https://fdn2.gsmarena.com/vv/pics/htc/htc-wildfire-e5-plus-1.jpg"
    },
    {
        "id": 12,
        "brand": "Motorola",
        "model": "Moto G Power",
        "year": 2025,
        "price": 179.99,
        "picture_url": "https://fdn2.gsmarena.com/vv/pics/motorola/motorola-moto-g-power-2025-1.jpg"
    }
]

# Create the FastAPI router
router = APIRouter()


@router.get("/phones/", response_model=List[Phone])
async def get_phones():
    return phones_db


@router.get("/phones/{phone_id}", response_model=Phone)
async def get_phone(phone_id: int):
    phone = next((phone for phone in phones_db if phone["id"] == phone_id), None)
    if phone is None:
        raise HTTPException(status_code=404, detail="Phone not found")
    return phone
