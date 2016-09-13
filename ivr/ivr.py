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

import ConfigParser

class IVR:
    """A simple example class"""
    def __init__(self):
       	settings = ConfigParser.RawConfigParser()
        settings.read('test/settings.conf')
        description-file = settings.get('metadata', 'description-file')
		
    def f(self):
        """ Nothing to see here"""
        settings = ConfigParser.RawConfigParser()
        settings.read('test/settings.conf')
        return description-file
        #return os.path.abspath(__file__)