from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Enum
from db import Base
import enum


class FuelType(str, enum.Enum):
    petrol = "Petrol"
    diesel = "Diesel"


class CarInfo(Base):
    __tablename__ = "car"

    id = Column(Integer, primary_key=True, index=True)
    manafaturer = Column(String)
    ModelName = Column(String)
    cc = Column(Integer)
    onRoadPrice = Column(Integer)
    seatingCapacity = Column(Integer)
    gearBox = Column(Integer)
    fuelType = Column(Enum(FuelType))
