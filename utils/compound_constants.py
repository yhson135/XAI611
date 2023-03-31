#   Copyright (c) 2021 PaddlePaddle Authors. All Rights Reserved.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
| Compound constants.
"""

# functional groups from https://www.daylight.com/dayhtml_tutorials/languages/smarts/smarts_examples.html
DAY_LIGHT_FG_SMARTS_LIST = [
    # C
    "[CX4]",
    "[$([CX2](=C)=C)]",
    "[$([CX3]=[CX3])]",
    "[$([CX2]#C)]",
    # C & O
    "[CX3]=[OX1]",
    "[$([CX3]=[OX1]),$([CX3+]-[OX1-])]",
    "[CX3](=[OX1])C",
    "[OX1]=CN",
    "[CX3](=[OX1])O",
    "[CX3](=[OX1])[F,Cl,Br,I]",
    "[CX3H1](=O)[#6]",
    "[CX3](=[OX1])[OX2][CX3](=[OX1])",
    "[NX3][CX3](=[OX1])[#6]",
    "[NX3][CX3]=[NX3+]",
    "[NX3,NX4+][CX3](=[OX1])[OX2,OX1-]",
    "[NX3][CX3](=[OX1])[OX2H0]",
    "[NX3,NX4+][CX3](=[OX1])[OX2H,OX1-]",
    "[CX3](=O)[O-]",
    "[CX3](=[OX1])(O)O",
    "[CX3](=[OX1])([OX2])[OX2H,OX1H0-1]",
    "C[OX2][CX3](=[OX1])[OX2]C",
    "[CX3](=O)[OX2H1]",
    "[CX3](=O)[OX1H0-,OX2H1]",
    "[NX3][CX2]#[NX1]",
    "[#6][CX3](=O)[OX2H0][#6]",
    "[#6][CX3](=O)[#6]",
    "[OD2]([#6])[#6]",
    # H
    "[H]",
    "[!#1]",
    "[H+]",
    "[+H]",
    "[!H]",
    # N
    "[NX3;H2,H1;!$(NC=O)]",
    "[NX3][CX3]=[CX3]",
    "[NX3;H2;!$(NC=[!#6]);!$(NC#[!#6])][#6]",
    "[NX3;H2,H1;!$(NC=O)].[NX3;H2,H1;!$(NC=O)]",
    "[NX3][$(C=C),$(cc)]",
    "[NX3,NX4+][CX4H]([*])[CX3](=[OX1])[O,N]",
    "[NX3H2,NH3X4+][CX4H]([*])[CX3](=[OX1])[NX3,NX4+][CX4H]([*])[CX3](=[OX1])[OX2H,OX1-]",
    "[$([NX3H2,NX4H3+]),$([NX3H](C)(C))][CX4H]([*])[CX3](=[OX1])[OX2H,OX1-,N]",
    "[CH3X4]",
    "[CH2X4][CH2X4][CH2X4][NHX3][CH0X3](=[NH2X3+,NHX2+0])[NH2X3]",
    "[CH2X4][CX3](=[OX1])[NX3H2]",
    "[CH2X4][CX3](=[OX1])[OH0-,OH]",
    "[CH2X4][SX2H,SX1H0-]",
    "[CH2X4][CH2X4][CX3](=[OX1])[OH0-,OH]",
    "[$([$([NX3H2,NX4H3+]),$([NX3H](C)(C))][CX4H2][CX3](=[OX1])[OX2H,OX1-,N])]",
    "[CH2X4][#6X3]1:[$([#7X3H+,#7X2H0+0]:[#6X3H]:[#7X3H]),$([#7X3H])]:[#6X3H]:\
[$([#7X3H+,#7X2H0+0]:[#6X3H]:[#7X3H]),$([#7X3H])]:[#6X3H]1",
    "[CHX4]([CH3X4])[CH2X4][CH3X4]",
    "[CH2X4][CHX4]([CH3X4])[CH3X4]",
    "[CH2X4][CH2X4][CH2X4][CH2X4][NX4+,NX3+0]",
    "[CH2X4][CH2X4][SX2][CH3X4]",
    "[CH2X4][cX3]1[cX3H][cX3H][cX3H][cX3H][cX3H]1",
    "[$([NX3H,NX4H2+]),$([NX3](C)(C)(C))]1[CX4H]([CH2][CH2][CH2]1)[CX3](=[OX1])[OX2H,OX1-,N]",
    "[CH2X4][OX2H]",
    "[NX3][CX3]=[SX1]",
    "[CHX4]([CH3X4])[OX2H]",
    "[CH2X4][cX3]1[cX3H][nX3H][cX3]2[cX3H][cX3H][cX3H][cX3H][cX3]12",
    "[CH2X4][cX3]1[cX3H][cX3H][cX3]([OHX2,OH0X1-])[cX3H][cX3H]1",
    "[CHX4]([CH3X4])[CH3X4]",
    "N[CX4H2][CX3](=[OX1])[O,N]",
    "N1[CX4H]([CH2][CH2][CH2]1)[CX3](=[OX1])[O,N]",
    "[$(*-[NX2-]-[NX2+]#[NX1]),$(*-[NX2]=[NX2+]=[NX1-])]",
    "[$([NX1-]=[NX2+]=[NX1-]),$([NX1]#[NX2+]-[NX1-2])]",
    "[#7]",
    "[NX2]=N",
    "[NX2]=[NX2]",
    "[$([NX2]=[NX3+]([O-])[#6]),$([NX2]=[NX3+0](=[O])[#6])]",
    "[$([#6]=[N+]=[N-]),$([#6-]-[N+]#[N])]",
    "[$([nr5]:[nr5,or5,sr5]),$([nr5]:[cr5]:[nr5,or5,sr5])]",
    "[NX3][NX3]",
    "[NX3][NX2]=[*]",
    "[CX3;$([C]([#6])[#6]),$([CH][#6])]=[NX2][#6]",
    "[$([CX3]([#6])[#6]),$([CX3H][#6])]=[$([NX2][#6]),$([NX2H])]",
    "[NX3+]=[CX3]",
    "[CX3](=[OX1])[NX3H][CX3](=[OX1])",
    "[CX3](=[OX1])[NX3H0]([#6])[CX3](=[OX1])",
    "[CX3](=[OX1])[NX3H0]([NX3H0]([CX3](=[OX1]))[CX3](=[OX1]))[CX3](=[OX1])",
    "[$([NX3](=[OX1])(=[OX1])O),$([NX3+]([OX1-])(=[OX1])O)]",
    "[$([OX1]=[NX3](=[OX1])[OX1-]),$([OX1]=[NX3+]([OX1-])[OX1-])]",
    "[NX1]#[CX2]",
    "[CX1-]#[NX2+]",
    "[$([NX3](=O)=O),$([NX3+](=O)[O-])][!#8]",
    "[$([NX3](=O)=O),$([NX3+](=O)[O-])][!#8].[$([NX3](=O)=O),$([NX3+](=O)[O-])][!#8]",
    "[NX2]=[OX1]",
    "[$([#7+][OX1-]),$([#7v5]=[OX1]);!$([#7](~[O])~[O]);!$([#7]=[#7])]",
    # O
    "[OX2H]",
    "[#6][OX2H]",
    "[OX2H][CX3]=[OX1]",
    "[OX2H]P",
    "[OX2H][#6X3]=[#6]",
    "[OX2H][cX3]:[c]",
    "[OX2H][$(C=C),$(cc)]",
    "[$([OH]-*=[!#6])]",
    "[OX2,OX1-][OX2,OX1-]",
    # P
    "[$(P(=[OX1])([$([OX2H]),$([OX1-]),$([OX2]P)])([$([OX2H]),$([OX1-]),\
$([OX2]P)])[$([OX2H]),$([OX1-]),$([OX2]P)]),$([P+]([OX1-])([$([OX2H]),$([OX1-])\
,$([OX2]P)])([$([OX2H]),$([OX1-]),$([OX2]P)])[$([OX2H]),$([OX1-]),$([OX2]P)])]",
    "[$(P(=[OX1])([OX2][#6])([$([OX2H]),$([OX1-]),$([OX2][#6])])[$([OX2H]),\
$([OX1-]),$([OX2][#6]),$([OX2]P)]),$([P+]([OX1-])([OX2][#6])([$([OX2H]),$([OX1-]),\
$([OX2][#6])])[$([OX2H]),$([OX1-]),$([OX2][#6]),$([OX2]P)])]",
    # S
    "[S-][CX3](=S)[#6]",
    "[#6X3](=[SX1])([!N])[!N]",
    "[SX2]",
    "[#16X2H]",
    "[#16!H0]",
    "[#16X2H0]",
    "[#16X2H0][!#16]",
    "[#16X2H0][#16X2H0]",
    "[#16X2H0][!#16].[#16X2H0][!#16]",
    "[$([#16X3](=[OX1])[OX2H0]),$([#16X3+]([OX1-])[OX2H0])]",
    "[$([#16X3](=[OX1])[OX2H,OX1H0-]),$([#16X3+]([OX1-])[OX2H,OX1H0-])]",
    "[$([#16X4](=[OX1])=[OX1]),$([#16X4+2]([OX1-])[OX1-])]",
    "[$([#16X4](=[OX1])(=[OX1])([#6])[#6]),$([#16X4+2]([OX1-])([OX1-])([#6])[#6])]",
    "[$([#16X4](=[OX1])(=[OX1])([#6])[OX2H,OX1H0-]),$([#16X4+2]([OX1-])([OX1-])([#6])[OX2H,OX1H0-])]",
    "[$([#16X4](=[OX1])(=[OX1])([#6])[OX2H0]),$([#16X4+2]([OX1-])([OX1-])([#6])[OX2H0])]",
    "[$([#16X4]([NX3])(=[OX1])(=[OX1])[#6]),$([#16X4+2]([NX3])([OX1-])([OX1-])[#6])]",
    "[SX4](C)(C)(=O)=N",
    "[$([SX4](=[OX1])(=[OX1])([!O])[NX3]),$([SX4+2]([OX1-])([OX1-])([!O])[NX3])]",
    "[$([#16X3]=[OX1]),$([#16X3+][OX1-])]",
    "[$([#16X3](=[OX1])([#6])[#6]),$([#16X3+]([OX1-])([#6])[#6])]",
    "[$([#16X4](=[OX1])(=[OX1])([OX2H,OX1H0-])[OX2][#6]),$([#16X4+2]([OX1-])([OX1-])([OX2H,OX1H0-])[OX2][#6])]",
    "[$([SX4](=O)(=O)(O)O),$([SX4+2]([O-])([O-])(O)O)]",
    "[$([#16X4](=[OX1])(=[OX1])([OX2][#6])[OX2][#6]),$([#16X4](=[OX1])(=[OX1])([OX2][#6])[OX2][#6])]",
    "[$([#16X4]([NX3])(=[OX1])(=[OX1])[OX2][#6]),$([#16X4+2]([NX3])([OX1-])([OX1-])[OX2][#6])]",
    "[$([#16X4]([NX3])(=[OX1])(=[OX1])[OX2H,OX1H0-]),$([#16X4+2]([NX3])([OX1-])([OX1-])[OX2H,OX1H0-])]",
    "[#16X2][OX2H,OX1H0-]",
    "[#16X2][OX2H0]",
    # X
    "[#6][F,Cl,Br,I]",
    "[F,Cl,Br,I]",
    "[F,Cl,Br,I].[F,Cl,Br,I].[F,Cl,Br,I]",
]


_i2a = {
    0: "NaN",
    1: "H",
    2: "He",
    3: "Li",
    4: "Be",
    5: "B",
    6: "C",
    7: "N",
    8: "O",
    9: "F",
    10: " Ne",
    11: "Na",
    12: "Mg",
    13: "Al",
    14: "Si",
    15: "P",
    16: "S",
    17: "Cl",
    18: "Ar",
    19: "K",
    20: "Ca",
    22: "Ti",
    24: "Cr",
    26: "Fe",
    28: "Ni",
    29: "Cu",
    31: "Ga",
    32: "Ge",
    34: "Se",
    35: "Br",
    40: "Zr",
    44: "Ru",
    45: "Rh",
    46: "Pd",
    47: "Ag",
    50: "Sn",
    51: "Sb",
    52: "Te",
    53: "I",
    65: "Tb",
    75: "Re",
    77: "Ir",
    78: "Pt",
    79: "Au",
    80: "Hg",
    81: "Tl",
    82: "Pb",
    83: "Bi",
    119: ">",
    120: "<",
    121: "=",
    122: "[",
    123: "]",
    124: "(",
    125: ")",
    126: "#",
    127: "-",
    128: "+",
    129: "@",
    130: "/",
    131: "\\",
    132: "c",
    133: "n",
    134: "o",
    135: "s",
    136: "1",
    137: "2",
    138: "3",
    139: "4",
    140: "5",
    141: "6",
    142: "7",
    143: "8",
    144: "9",
    145: ".",
}


_a2i = {
    "NaN": 0,
    "H": 1,
    "He": 2,
    "Li": 3,
    "Be": 4,
    "B": 5,
    "C": 6,
    "N": 7,
    "O": 8,
    "F": 9,
    " Ne": 10,
    "Na": 11,
    "Mg": 12,
    "Al": 13,
    "Si": 14,
    "P": 15,
    "S": 16,
    "Cl": 17,
    "Ar": 18,
    "K": 19,
    "Ca": 20,
    "Ti": 22,
    "Cr": 24,
    "Fe": 26,
    "Ni": 28,
    "Cu": 29,
    "Ga": 31,
    "Ge": 32,
    "Se": 34,
    "Br": 35,
    "Zr": 40,
    "Ru": 44,
    "Rh": 45,
    "Pd": 46,
    "Ag": 47,
    "Sn": 50,
    "Sb": 51,
    "Te": 52,
    "I": 53,
    "Tb": 65,
    "Re": 75,
    "Ir": 77,
    "Pt": 78,
    "Au": 79,
    "Hg": 80,
    "Tl": 81,
    "Pb": 82,
    "Bi": 83,
    ">": 119,
    "<": 120,
    "=": 121,
    "[": 122,
    "]": 123,
    "(": 124,
    ")": 125,
    "#": 126,
    "-": 127,
    "+": 128,
    "@": 129,
    "/": 130,
    "\\": 131,
    "c": 132,
    "n": 133,
    "o": 134,
    "s": 135,
    "1": 136,
    "2": 137,
    "3": 138,
    "4": 139,
    "5": 140,
    "6": 141,
    "7": 142,
    "8": 143,
    "9": 144,
    ".": 145,
}

_pair_list = [
    "He",
    "Li",
    "Be",
    "Ne",
    "Na",
    "Mg",
    "Al",
    "Si",
    "Cl",
    "Ar",
    "Ca",
    "Ti",
    "Cr",
    "Fe",
    "Ni",
    "Cu",
    "Zn",
    "Ga",
    "Ge",
    "As",
    "Se",
    "Br",
    "Kr",
    "Rb",
    "Sr",
    "Zr",
    "Nb",
    "Mo",
    "Tc",
    "Ru",
    "Pd",
    "Ag",
    "Cd",
    "Sb",
    "Te",
    "Xe",
    "Ba",
    "La",
    "Ce",
    "Pr",
    "Nd",
    "Pm",
    "Sm",
    "Eu",
    "Gd",
    "Tb",
    "Dy",
    "Er",
    "Tm",
    "Yb",
    "Lu",
    "Hf",
    "Ta",
    "Re",
    "Ir",
    "Pt",
    "Au",
    "Hg",
    "Tl",
    "Pb",
    "Bi",
    "At",
    "Fr",
    "Ra",
    "Ac",
    "Th",
    "Pa",
    "Pu",
    "Am",
    "Cm",
    "Bk",
    "Cf",
    "Es",
    "Fm",
    "Md",
    "Lr",
    "Rf",
    "Db",
    "Sg",
    "Mt",
    "Ds",
    "Rg",
    "Fl",
    "Mc",
    "Lv",
    "Ts",
    "Og",
    "Rh",
]