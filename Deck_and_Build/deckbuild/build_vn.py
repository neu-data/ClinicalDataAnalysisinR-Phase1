# -*- coding: utf-8 -*-
"""Build the VIETNAMESE deck (_VN.pptx) with a Vietnamese-diacritic-safe title
font. Must set the env var BEFORE importing engine/assemble so the font default
binds correctly. Does NOT touch the English deck."""
import os

# Century Gothic lacks Vietnamese diacritics -> use Segoe UI (full VN support,
# already the template's subtitle font). Verdana/Segoe/Consolas support VN too.
os.environ["DECK_TITLE_FONT"] = "Segoe UI"
os.environ["DECK_LANG"] = "vi"          # localise engine-generated labels

import assemble as A          # imports engine, which now reads the env var

A.OUT = os.path.join(A.DECKROOT, "Slides",
                     "Clinical_Data_Analysis_in_R_Phase1_VN.pptx")

import content_VN
n = A.build(content_VN.SLIDES)
print("Built", n, "VN slides")
A.pack()
print("Wrote", A.OUT)
