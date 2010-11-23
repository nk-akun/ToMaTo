#!/usr/bin/python

# ToMaTo (Topology management software) 
# Copyright (C) 2010 Dennis Schwerdel, University of Kaiserslautern
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
# along with this program.  If not, see <http://www.gnu.org/licenses/>

import sys, tomato

try:
	from south.management.commands import schemamigration
	cmd = schemamigration.Command()
	if sys.argv[1] == "initial":
		cmd.handle(app="tomato", name=sys.argv[1], initial=True)
	else:
		cmd.handle(app="tomato", name=sys.argv[1], initial=False, auto=True)
except:
	from south.management.commands import startmigration
	cmd = startmigration.Command()
	initial = sys.argv[1] == "initial"
	cmd.handle(app="tomato", name=sys.argv[1], initial=initial, auto=True)
