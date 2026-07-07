from pydantic import BaseModel, ConfigDict, Field

class AddressBase(BaseModel):
    province_code: str    # Provinsi
    province_name: str    # Provinsi
    regency_code: str     # Kota/Kabupaten
    regency_name: str     # Kota/Kabupaten
    subdistrict_code: str # Kecamatan
    subdistrict_name: str # Kecamatan
    village_code: str     # Kelurahan
    village_name: str     # Kelurahan
    full_address: str     # Full Address
    postal_code: str = Field(
        min_length=5,
        max_length=5,
        pattern=r"^\d{5}$",    
    )      # Kode POS


class AddressCreate(AddressBase):
    pass


class AddressUpdate(BaseModel):
    province_code: str | None
    province_name: str | None
    regency_code: str | None
    regency_name: str | None
    subdistrict_code: str | None
    subdistrict_name: str | None
    village_code: str | None
    village_name: str | None
    full_address: str | None
    postal_code: str | None


class AddressResponse(AddressBase):
    id: int

    model_config = ConfigDict(from_attributes=True)