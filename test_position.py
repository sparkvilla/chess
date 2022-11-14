import pytest
from piece import *

import pdb


def test_get_diag_p_up_pos():
    p = Position("e2")
    assert p.get_diag_p_up_pos() == ["f3", "g4", "h5"]


def test_get_diag_p_up_pos_1step():
    p = Position("e2")
    assert p.get_diag_p_up_pos(steps=1) == ["f3"]
