#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set et sw=4 fenc=utf-8:
#
# Copyright 2016 INVITE Communications Co., Ltd. All Rights Reserved.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

"""
"""

from asterisk.agi import *

agi = AGI()
agi.answer()
agi.appexec('AMD')

amdstatus = agi.get_variable('AMDSTATUS')
amdcause = agi.get_variable('AMDCAUSE')

agi.verbose('Status: {0} Cause: {1}'.format(amdstatus, amdcause))

#agi.appexec('DumpChan')




agi.stream_file('tt-monty-knights')

agi.hangup()