# Copyright 2011 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# GNU Radio is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# GNU Radio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GNU Radio; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.

install(FILES
    mac_simple_mac.xml
    mac_virtual_channel_encoder.xml
	mac_virtual_channel_decoder.xml
    mac_packet_framer.xml
    mac_packet_deframer.xml
	mac_packet_to_pdu.xml
	mac_802_3_tracker.xml
	mac_burst_tagger.xml
    mac_carrier_sense.xml DESTINATION share/gnuradio/grc/blocks
)

