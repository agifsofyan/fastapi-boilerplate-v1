from dataclasses import dataclass

@dataclass
class AddressEntity:
    id: int | None
    user_id: int
    province_code: str
    province_name: str
    regency_code: str
    regency_name: str
    subdistrict_code: str
    subdistrict_name: str
    village_code: str
    village_name: str
    full_address: str
    postal_code: str