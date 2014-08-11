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
#from constants import *
#        gr.sync_block.__init__(self,
#class carrier_sense(gr.sync_block):
#in_sig=[gr.io_signature(1, 1, gr.sizeof_gr_complex)],
class carrier_sense(gr.sync_block):
    """
    docstring for block carrier_sense
    """
    def __init__(self, window, shift, threshold, verbose):
		gr.sync_block.__init__(self,
			name="carrier_sense",
            in_sig=[numpy.complex64],
			out_sig=None)
            
		self.window = int(window)
		self.shift = shift
		self.threshold = threshold
		self.verbose = verbose
		self.buf = []


    def work(self, input_items, output_items):
    	mean = 0.0
        in0 = input_items[0]
        for m in xrange(len(in0)-self.window):
        	for n in xrange(self.window):
        		mean += abs(in0[n+m])
        mean = mean/self.window
        if mean > self.threshold:
        	constants.cs = 1
        else:
        	constants.cs = 0
        if self.verbose:
            print "CS value"
            print constants.cs
	    print "Mean"
            print mean
            print "---------"
        	
        
        
        return len(input_items[0])

