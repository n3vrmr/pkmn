# * coding: utf8 *
"""
Created on Tue Jul 12 18:58:44 2022

@author: Nevermore
"""

import pandas as pd

nature_chart = pd.DataFrame({"Nature":["Hardy", "Lonely", "Adamant", "Naughty",
                                "Brave", "Bold", "Docile", "Impish", "Lax",
                                "Relaxed", "Modest", "Mild", "Bashful", "Rash",
                                "Quiet", "Calm", "Gentle", "Careful", "Quirky",
                                "Sassy", "Timid", "Hasty", "Jolly", "Naive",
                                "Serious"],
                        "Boost":["Attack", "Attack", "Attack", "Attack", "Attack",
                                 "Defense", "Defense", "Defense", "Defense", "Defense",
                                 "Sp. Atk", "Sp. Atk", "Sp. Atk", "Sp. Atk", "Sp. Atk",
                                 "Sp. Def","Sp. Def", "Sp. Def", "Sp. Def", "Sp. Def",
                                 "Speed", "Speed", "Speed", "Speed", "Speed"],
                        "Drop":["Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed",
                                "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed",
                                "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed",
                                "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed",
                                "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed"]})

def stats(nature):
    """
    Gives a description of a given nature.

    Parameters
    ----------
    nature : Pokémon nature.

    Returns
    -------
    None.

    """
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    split = list(nature)
    curiosity = nature_chart[nature_chart["Nature"] == f"{nature}"]
    if split[0] in vowels:
        print(f"An {nature} nature gives Pokémon a boost to the {curiosity['Boost'].values[0]} stat, and a drop to the {curiosity['Drop'].values[0]} stat.")
    else:
        print(f"A {nature} nature gives Pokémon a boost to the {curiosity['Boost'].values[0]} stat, and a drop to the {curiosity['Drop'].values[0]} stat.")
    if curiosity["Boost"].values[0] == curiosity["Drop"].values[0]:
        print("This is a neutral nature.")
    return curiosity

def main():
    print("Gotta catch'em all")
    
if __name__ == '__main__':
    main()
