# -*- coding: utf-8 -*-
"""Build the VIETNAMESE deck (_VN.pptx). Arial has full Vietnamese support, so the
VN deck uses the same font as the English deck; only the engine labels differ.
Does NOT touch the English deck."""
import os

os.environ["DECK_TITLE_FONT"] = "Arial"
os.environ["DECK_LANG"] = "vi"          # localise engine-generated labels

import assemble as A          # imports engine, which now reads the env var

A.OUT = os.path.join(A.DECKROOT, "Slides",
                     "Clinical_Data_Analysis_in_R_Phase1_VN.pptx")

import content_VN
n = A.build(content_VN.SLIDES)
print("Built", n, "VN slides")
A.pack()
print("Wrote", A.OUT)
