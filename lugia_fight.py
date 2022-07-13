# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 21:44:48 2022

@author: Nevermore
"""

lugia = {"Aeroblast":5,
         "Extrasensory":30,
         "Hydro Pump":5,
         "Rain Dance":5}

def lugia_move(move):
    lugia[f"{move}"] = lugia.get(f"{move}") - 1
    return lugia

def main():
    print("Modest nature is best")
    
if __name__ == '__main__':
    main()