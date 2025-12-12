#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  6 18:53:26 2025

The main use for this script is to test and demonstrate the use of user defined
units.

@author: Reiner Jung
"""

from cfunits import Units

def info(unit, name:str):
    print(f"Unit {name}")
    print(f"  Status {unit.isvalid}")
    print(f"  Reason {unit.reason_notvalid}")
    print(f"  Unit {unit}")
    try:
        result=unit.formatted()
        print(f"  Formatted {result}")
    except ValueError as e:
        print(f"  Formatting failed: {e}")

# make a new custom unit
Units.new_unit("pebbles")

# berry is not previously defined
u_unknown = Units("berry")

# ppm and dB are an addition to udunits, but defined in cf_units
u_ppm = Units("ppm")
u_db = Units("dB")

# use custom unit
u_pebbles = Units("pebbles")

# use composed unit of predefined units from udunits
u_m_kg = Units("m/kg")

# use composed unit of a cf_units unit and an udunits unit
u_db_m = Units("dB/m")

# use composed unit of a custom unit and an udunits unit 
u_pebbles_m = Units("pebbles/m")

# print info on these units
info(u_ppm, "PPM")
info(u_db, "decibel")

info(u_unknown, "berry")
info(u_pebbles, "pebbles")

info(u_m_kg, "m/kg")
info(u_db_m, "decibel/m")
info(u_pebbles_m, "pebbles/m")

# end

