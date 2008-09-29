#!/usr/bin/env python

############################################################################
#
# MODULE:       v.db.dropcolumn
# AUTHOR(S):    Markus Neteler
#               Converted to Python by Glynn Clements
# PURPOSE:      interface to db.execute to drop a column from the 
#               attribute table connected to a given vector map
#               - Based on v.db.addcol
#               - with special trick for SQLite
# COPYRIGHT:    (C) 2007 by the GRASS Development Team
#
#               This program is free software under the GNU General Public
#               License (>=v2). Read the file COPYING that comes with GRASS
#               for details.
#
#############################################################################


#%Module
#%  description: Drops a column from the attribute table connected to a given vector map.
#%  keywords: vector, database, attribute table
#%End

#%option
#% key: map
#% type: string
#% gisprompt: old,vector,vector
#% key_desc : name
#% description: Vector map for which to drop attribute column
#% required : yes
#%end

#%option
#% key: layer
#% type: integer
#% description: Layer where to drop column
#% answer: 1
#% required : no
#%end

#%option
#% key: column
#% type: string
#% description: Name of the column
#% required : yes
#%end

import sys
import os
import string
import grass

def main():
    map = options['map']
    layer = options['layer']
    column = options['column']

    mapset = grass.gisenv()['MAPSET']

    # does map exist in CURRENT mapset?
    if not grass.find_file(map, element = 'vector', mapset = mapset):
	grass.fatal("Vector map <%s> not found in current mapset" % map)

    s = grass.read_command('v.db.connect', flags = 'g', map = map, layer = layer);
    if not s:
	grass.fatal("An error occured while running v.db.connect")
    f = s.split()
    table = f[1]
    keycol = f[2]
    database = f[3]
    driver = f[4]

    if not table:
	grass.fatal("There is no table connected to the input vector map Cannot delete any column")

    if column == keycol:
	grass.fatal("Cannot delete <$col> column as it is needed to keep table <%s> connected to the input vector map <%s>" % (table, map))

    s = grass.read_command('v.info', flags = 'c', map = map, layer = layer, quiet = True)
    if column not in [l.split('|')[1].lstrip() for l in s.splitlines()]:
	grass.fatal("Column <%s> not found in table <%s>" % (column, table))

    if driver == "sqlite":
	#echo "Using special trick for SQLite"
	# http://www.sqlite.org/faq.html#q13
	colnames = []
	coltypes = []
	s = grass.read_command('db.describe', flags = 'c', table = table)
	for l in s.splitlines():
	    if not l.startswith('Column '):
		continue
	    f = l.split(':')
	    f[1] = f[1].lstrip()
	    if f[1] == column:
		continue
	    colnames.append(f[1])
	    coltypes.append("%s %s" % (f[1], f[2]))

	colnames = ", ".join(colnames)
	coltypes = ", ".join(coltypes)

	cmds = [
	    "BEGIN TRANSACTION",
	    "CREATE TEMPORARY TABLE ${table}_backup(${coldef})",
	    "INSERT INTO ${table}_backup SELECT ${colnames} FROM ${table}",
	    "DROP TABLE ${table}",
	    "CREATE TABLE ${table}(${coldef})",
	    "INSERT INTO ${table} SELECT ${colnames} FROM ${table}_backup",
	    "DROP TABLE ${table}_backup",
	    "COMMIT"
	    ]
	tmpl = string.Template(';\n'.join(cmds))
	sql = tmpl.substitute(table = table, coldef = coltypes, colnames = colnames)
    else:
	sql = "ALTER TABLE %s DROP COLUMN %s" % (table, column)

    if grass.write_command('db.execute', database = database, driver = driver,
			   stdin = sql) != 0:
	grass.fatal("Cannot continue (problem deleting column).")

    # write cmd history:
    grass.run_command('v.support', map = map, cmdhist = os.environ['CMDLINE'])

if __name__ == "__main__":
    options, flags = grass.parser()
    main()
