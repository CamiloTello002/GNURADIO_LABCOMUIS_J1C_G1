#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2022 Pedreros ft Camilo.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#


import numpy
import math
from gnuradio import gr

class ParteEnteraD1A(gr.sync_block):
    """
    docstring for block ParteEnteraD1A
    """
    def __init__(self, PARAM1, PARAM2):
        self.PARAM1 = PARAM1
        self.PARAM2 = PARAM2
        gr.sync_block.__init__(self,
            name="ParteEnteraD1A",
            in_sig=[numpy.float32 ],
            out_sig=[numpy.float32 ])


    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        # <+signal processing here+>
        # out[:] = in0
        for i in range(len(in0)):
                if self.PARAM1:
                        out[i]=math.floor(in0[i])
                else:
                        out[i]=math.ceil(in0[i])
        return len(output_items[0])
