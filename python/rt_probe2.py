#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2014 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy
from gnuradio import gr

class rt_probe2(gr.sync_block):
    """
    docstring for block rt_probe2
    """
    def __init__(self, probe_value):
        gr.sync_block.__init__(self,
            name="rt_probe2",
            in_sig=None,
            out_sig=[numpy.float32])
            
        self.d_probe_value = 0.0
            
    def set_probe_value(self, probe_value):
        self.d_probe_value = probe_value
            


    def work(self, input_items, output_items):
        out = output_items[0]
        self.d_probe_value
        # <+signal processing here+>
        out[:] = self.d_probe_value
        return len(output_items[0])

