from Engine import Engine
from Vehicle import Vehicle

engine = Engine("V6")
vehicle = Vehicle("Car", True, engine)
vehicle.engine.startEngine()