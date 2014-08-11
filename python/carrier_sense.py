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

import cmath
import numpy
import constants
from gnuradio import gr

class carrier_sense(gr.sync_block):
    """
    docstring for block carrier_sense
    """
    def __init__(self, window, shift, threshold, alpha):
        gr.sync_block.__init__(self,
            name="carrier_sense",
            in_sig=[numpy.float32],
            out_sig=None)
            
        self.window = int(window)
        self.shift = shift
        self.threshold = threshold
        self.alpha = alpha
	self.summ = 0.0
	self.accum = 0


    def work(self, input_items, output_items):
        in0 = input_items[0]
	#print in0[0]
	#print "----------"
	mean = sum(in0)
	self.accum += len(in0)
	#for x in xrange(self.window):
	#    self.summ = self.alpha * abs(in0[x]) + (self.summ * (1 - self.alpha))
	
	#constants.cs = 1 if self.summ > self.threshold else 0
	if self.accum > self.window:
	    constants.cs = 1 if mean > self.threshold else 0
	    self.accum = 0
	    mean = 0
	

        return max(len(in0), self.window)

