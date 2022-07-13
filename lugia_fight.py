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
    """
    Use this function when Lugia (level 47) uses a move in battle to count the
    PP for their moves.

    Parameters
    ----------
    move : name of the move Lugia just used.

    Returns
    -------
    lugia : updated dictionary with the PP of each move Lugia has left.

    """
    lugia[f"{move}"] = lugia.get(f"{move}") - 1
    return lugia

def main():
    print("Modest nature is best")
    
if __name__ == '__main__':
    main()