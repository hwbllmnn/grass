import os
from grass.script.temporal import *
import grass.script as grass

###############################################################################

def test_dict_sql_serializer():
    t = dict_sql_serializer()
    t.test()

def test_dataset_identifer():
	for i in range(2):
	    base = raster_base(ident="soil" + str(i) + "@PERMANENT", name="soil" + str(i), mapset="PERMANENT", creator="soeren", temporal_type="absolute", revision=1)
	    base.insert()
	    base.select()
	    base.print_self()
	    base.clear()
	    base.set_creator("rene")
	    base.update()
	    base.select()
	    base.print_self()

	for i in range(2):
	    base = raster3d_base(ident="soil" + str(i) + "@PERMANENT", name="soil" + str(i), mapset="PERMANENT", temporal_type="absolute", creator="soeren")
	    base.insert()
	    base.select()
	    base.print_self()
	    base.clear()
	    base.set_creator("rene")
	    base.update()
	    base.select()
	    base.print_self()

	for i in range(2):
	    base = vector_base(ident="soil" + str(i) + "@PERMANENT", name="soil" + str(i), mapset="PERMANENT", temporal_type="absolute", creator="soeren")
	    base.insert()
	    base.select()
	    base.print_self()
	    base.clear()
	    base.set_creator("rene")
	    base.update()
	    base.select()
	    base.print_self()

	for i in range(2):
	    base = strds_base(ident="soil" + str(i) + "@PERMANENT", name="soil" + str(i), mapset="PERMANENT", creator="soeren", semantic_type="event", temporal_type="absolute", revision=1)
	    base.insert()
	    base.select()
	    base.print_self()
	    base.clear()
	    base.set_creator("rene")
	    base.update()
	    base.select()
	    base.print_self()

	for i in range(2):
	    base = str3ds_base(ident="soil" + str(i) + "@PERMANENT", name="soil" + str(i), mapset="PERMANENT", temporal_type="absolute", semantic_type="event", creator="soeren")
	    base.insert()
	    base.select()
	    base.print_self()
	    base.clear()
	    base.set_creator("rene")
	    base.update()
	    base.select()
	    base.print_self()

	for i in range(2):
	    base = stvds_base(ident="soil" + str(i) + "@PERMANENT", name="soil" + str(i), mapset="PERMANENT", temporal_type="absolute", semantic_type="event", creator="soeren")
	    base.insert()
	    base.select()
	    base.print_self()
	    base.clear()
	    base.set_creator("rene")
	    base.update()
	    base.select()
	    base.print_self()
            
def test_absolute_timestamp():
	for i in range(2):
	    base = raster_absolute_time(ident="soil" + str(i) + "@PERMANENT", start_time=datetime(2011,01,01), end_time=datetime(2011,07,01), timezone=1)
	    base.insert()
	    base.select()
	    base.print_self()
	    base.clear()
	    base.set_start_time(datetime(2010,01,01))
	    base.update()
	    base.select()
	    base.print_self()

	for i in range(2):
	    base = raster3d_absolute_time(ident="soil" + str(i) + "@PERMANENT", start_time=datetime(2011,01,01), end_time=datetime(2011,07,01), timezone=1)
	    base.insert()
	    base.select()
	    base.print_self()
	    base.clear()
	    base.set_start_time(datetime(2010,01,01))
	    base.update()
	    base.select()
	    base.print_self()

	for i in range(2):
	    base = vector_absolute_time(ident="soil" + str(i) + "@PERMANENT", start_time=datetime(2011,01,01), end_time=datetime(2011,07,01), timezone=1)
	    base.insert()
	    base.select()
	    base.print_self()
	    base.clear()
	    base.set_start_time(datetime(2010,01,01))
	    base.update()
	    base.select()
	    base.print_self()
            
	for i in range(2):
	    base = strds_absolute_time(ident="soil" + str(i) + "@PERMANENT", start_time=datetime(2011,01,01), end_time=datetime(2011,07,01), granularity="1 day", timezone=1)
	    base.insert()
	    base.select()
	    base.print_self()
	    base.clear()
	    base.set_start_time(datetime(2010,01,01))
	    base.update()
	    base.select()
	    base.print_self()

	for i in range(2):
	    base = str3ds_absolute_time(ident="soil" + str(i) + "@PERMANENT", start_time=datetime(2011,01,01), end_time=datetime(2011,07,01), granularity="1 day", timezone=1)
	    base.insert()
	    base.select()
	    base.print_self()
	    base.clear()
	    base.set_start_time(datetime(2010,01,01))
	    base.update()
	    base.select()
	    base.print_self()

	for i in range(2):
	    base = stvds_absolute_time(ident="soil" + str(i) + "@PERMANENT", start_time=datetime(2011,01,01), end_time=datetime(2011,07,01), granularity="1 day", timezone=1)
	    base.insert()
	    base.select()
	    base.print_self()
	    base.clear()
	    base.set_start_time(datetime(2010,01,01))
	    base.update()
	    base.select()
	    base.print_self()
            
def test_spatial_extent():
	for i in range(2):
	    base = raster_spatial_extent(ident="soil" + str(i) + "@PERMANENT", north=100 + i, south=10+i, east=50+i, west=20+i, top=i, bottom=0)
	    base.insert()
	    base.select()
	    base.print_self()
	    base.clear()
	    base.set_north(120+i)
	    base.update()
	    base.select()
	    base.print_self()

	for i in range(2):
	    base = raster3d_spatial_extent(ident="soil" + str(i) + "@PERMANENT", north=100 + i, south=10+i, east=50+i, west=20+i, top=i, bottom=0)
	    base.insert()
	    base.select()
	    base.print_self()
	    base.clear()
	    base.set_north(120+i)
	    base.update()
	    base.select()
	    base.print_self()

	for i in range(2):
	    base = vector_spatial_extent(ident="soil" + str(i) + "@PERMANENT", north=100 + i, south=10+i, east=50+i, west=20+i, top=i, bottom=0)
	    base.insert()
	    base.select()
	    base.print_self()
	    base.clear()
	    base.set_north(120+i)
	    base.update()
	    base.select()
	    base.print_self()
            
	for i in range(2):
	    base = strds_spatial_extent(ident="soil" + str(i) + "@PERMANENT", north=100 + i, south=10+i, east=50+i, west=20+i, top=i, bottom=0)
	    base.insert()
	    base.select()
	    base.print_self()
	    base.clear()
	    base.set_north(120+i)
	    base.update()
	    base.select()
	    base.print_self()

	for i in range(2):
	    base = str3ds_spatial_extent(ident="soil" + str(i) + "@PERMANENT", north=100 + i, south=10+i, east=50+i, west=20+i, top=i, bottom=0)
	    base.insert()
	    base.select()
	    base.print_self()
	    base.clear()
	    base.set_north(120+i)
	    base.update()
	    base.select()
	    base.print_self()

	for i in range(2):
	    base = stvds_spatial_extent(ident="soil" + str(i) + "@PERMANENT", north=100 + i, south=10+i, east=50+i, west=20+i, top=i, bottom=0)
	    base.insert()
	    base.select()
	    base.print_self()
	    base.clear()
	    base.set_north(120+i)
	    base.update()
	    base.select()
	    base.print_self()

def test_relative_timestamp():
	for i in range(2):
	    base = raster_relative_time(ident="soil" + str(i) + "@PERMANENT", interval=i)
	    base.insert()
	    base.select()
	    base.print_self()
	    base.clear()
	    base.set_interval(i+1)
	    base.update()
	    base.select()
	    base.print_self()

	for i in range(2):
	    base = raster3d_relative_time(ident="soil" + str(i) + "@PERMANENT", interval=i)
	    base.insert()
	    base.select()
	    base.print_self()
	    base.clear()
	    base.set_interval(i+1)
	    base.update()
	    base.select()
	    base.print_self()

	for i in range(2):
	    base = vector_relative_time(ident="soil" + str(i) + "@PERMANENT", interval=i)
	    base.insert()
	    base.select()
	    base.print_self()
	    base.clear()
	    base.set_interval(i+1)
	    base.update()
	    base.select()
	    base.print_self()
            
	for i in range(2):
	    base = strds_relative_time(ident="soil" + str(i) + "@PERMANENT", interval=i, granularity=5.5)
	    base.insert()
	    base.select()
	    base.print_self()
	    base.clear()
	    base.set_interval(i+1)
	    base.update()
	    base.select()
	    base.print_self()

	for i in range(2):
	    base = str3ds_relative_time(ident="soil" + str(i) + "@PERMANENT", interval=i, granularity=5.5)
	    base.insert()
	    base.select()
	    base.print_self()
	    base.clear()
	    base.set_interval(i+1)
	    base.update()
	    base.select()
	    base.print_self()

	for i in range(2):
	    base = stvds_relative_time(ident="soil" + str(i) + "@PERMANENT", interval=i, granularity=5.5)
	    base.insert()
	    base.select()
	    base.print_self()
	    base.clear()
	    base.set_interval(i+1)
	    base.update()
	    base.select()
	    base.print_self()
            
def test_map_metadata():
	for i in range(2):
	    base = raster_metadata(ident="soil" + str(i) + "@PERMANENT", strds_register="PERMANENT_soil_strds-register", datatype="CELL", \
			    cols=500, rows=400, number_of_cells=200000,nsres=1, ewres=1, min=0, max=33)
	    base.insert()
	    base.select()
	    base.print_self()
	    base.clear()
	    base.set_datatype("FCELL")
	    base.update()
	    base.select()
	    base.print_self()

	for i in range(2):
	    base = raster3d_metadata(ident="soil" + str(i) + "@PERMANENT", str3ds_register="PERMANENT_soil_str3ds-register", datatype="FCELL", \
			    cols=500, rows=400, depths=20, number_of_cells=200000,nsres=1, ewres=1, tbres=10, min=0, max=33)
	    base.insert()
	    base.select()
	    base.print_self()
	    base.clear()
	    base.set_datatype("DCELL")
	    base.update()
	    base.select()
	    base.print_self()

	for i in range(2):
	    base = vector_metadata(ident="soil" + str(i) + "@PERMANENT", stvds_register="PERMANENT_soil_stvds_register")
	    base.insert()
	    base.select()
	    base.print_self()
	    base.clear()
	    base.set_stvds_register("PERMANENT_soil_stvds_register")
	    base.update()
	    base.select()
	    base.print_self()

def test_base_absolute_time_extent_metadata():

	for i in range(10):
	    base = vector_base(ident="water" + str(i) + "@PERMANENT", name="water" + str(i), mapset="PERMANENT", creator="soeren")
	    base.insert()
	    base = raster_base(ident="water" + str(i) + "@PERMANENT", name="water" + str(i), mapset="PERMANENT", creator="soeren")
	    base.insert()
	    base = raster3d_base(ident="water" + str(i) + "@PERMANENT", name="water" + str(i), mapset="PERMANENT", creator="soeren")
	    base.insert()

	for i in range(10):
	    base = vector_base(ident="water" + str(i) + "@PERMANENT")
	    base.set_creator("rene")
	    base.update()
	    base = raster_base(ident="water" + str(i) + "@PERMANENT")
	    base.set_creator("rene")
	    base.update()
	    base = raster3d_base(ident="water" + str(i) + "@PERMANENT")
	    base.set_creator("rene")
	    base.update()

	for i in range(10):
	    base = vector_absolute_time(ident="water" + str(i) + "@PERMANENT", start_time=datetime.now(), end_time=datetime.now(), timezone=1)
	    base.insert()
	    base = raster_absolute_time(ident="water" + str(i) + "@PERMANENT", start_time=datetime.now(), end_time=datetime.now(), timezone=1)
	    base.insert()
	    base = raster3d_absolute_time(ident="water" + str(i) + "@PERMANENT", start_time=datetime.now(), end_time=datetime.now(), timezone=1)
	    base.insert()

	for i in range(10):
	    base = vector_absolute_time(ident="water" + str(i) + "@PERMANENT")
	    base.set_start_time(datetime(2010, 6, 1))
	    base.update()
	    base = raster_absolute_time(ident="water" + str(i) + "@PERMANENT")
	    base.set_start_time(datetime(2010, 6, 1))
	    base.update()
	    base = raster3d_absolute_time(ident="water" + str(i) + "@PERMANENT")
	    base.set_start_time(datetime(2010, 6, 1))
	    base.update()

	for i in range(10):
	    base = vector_spatial_extent(ident="water" + str(i) + "@PERMANENT", north=100 + i, south=10+i, east=50+i, west=20+i, top=i, bottom=0)
	    base.insert()
	    base = raster_spatial_extent(ident="water" + str(i) + "@PERMANENT", north=100 + i, south=10+i, east=50+i, west=20+i, top=0, bottom=0)
	    base.insert()
	    base = raster3d_spatial_extent(ident="water" + str(i) + "@PERMANENT", north=100 + i, south=10+i, east=50+i, west=20+i, top=i, bottom=0)
	    base.insert()

	for i in range(10):
	    base = vector_spatial_extent(ident="water" + str(i) + "@PERMANENT")
	    base.set_north(120 + i)
	    base.set_south(20 + i)
	    base.update()
	    base = raster_spatial_extent(ident="water" + str(i) + "@PERMANENT")
	    base.set_north(120 + i)
	    base.set_south(20 + i)
	    base.update()
	    base = raster3d_spatial_extent(ident="water" + str(i) + "@PERMANENT")
	    base.set_north(120 + i)
	    base.set_south(20 + i)
	    base.update()

	for i in range(10):
	    base = vector_metadata(ident="water" + str(i) + "@PERMANENT", stvds_register="PERMANENT_water_stvds_register")
	    base.insert()
	    base = raster_metadata(ident="water" + str(i) + "@PERMANENT", strds_register="PERMANENT_water_strds-register", datatype="CELL", \
			    cols=500, rows=400, number_of_cells=200000,nsres=1, ewres=1, min=0, max=33)
	    base.insert()
	    base = raster3d_metadata(ident="water" + str(i) + "@PERMANENT", str3ds_register="PERMANENT_water_str3ds-register", datatype="FCELL", \
			    cols=500, rows=400, depths=20, number_of_cells=200000,nsres=1, ewres=1, tbres=10, min=0, max=33)
	    base.insert()

	for i in range(10):
	    base = vector_metadata(ident="water" + str(i) + "@PERMANENT")
	    base.set_stvds_register("PERMANENT_water_stvds_register")
	    base.update()
	    base = raster_metadata(ident="water" + str(i) + "@PERMANENT")
	    base.set_datatype("DCELL")
	    base.update()
	    base = raster3d_metadata(ident="water" + str(i) + "@PERMANENT")
	    base.set_datatype("DCELL")
	    base.update()

	for i in range(10):
	    base = vector_base(ident="water" + str(i) + "@PERMANENT")
	    base.select()
	    base.print_self()
	    base = raster_base(ident="water" + str(i) + "@PERMANENT")
	    base.select()
	    base.print_self()
	    base = raster3d_base(ident="water" + str(i) + "@PERMANENT")
	    base.select()
	    base.print_self()

	print "Create a raster object"

	rds = raster_dataset("water0@PERMANENT")
	rds.select()
	rds.print_self()

	print rds.temporal_relation(rds)

def test_absolut_time_temporal_relations():

    A = raster_absolute_time(ident="test1@PERMANENT", start_time=datetime(year=2000, month=1, day=1), \
		                                        end_time=datetime(year=2001, month=1, day=1), timezone=1)
    B = raster_absolute_time(ident="test2@PERMANENT", start_time=datetime(year=2001, month=1, day=1), \
		                                        end_time=datetime(year=2002, month=1, day=1), timezone=1)

    print "Precedes: ", A.temporal_relation(B)
    print "Follows:  ", B.temporal_relation(A)

    A = raster_absolute_time(ident="test1@PERMANENT", start_time=datetime(year=2000, month=1, day=1), \
		                                        end_time=datetime(year=2001, month=1, day=1), timezone=1)
    B = raster_absolute_time(ident="test2@PERMANENT", start_time=datetime(year=2001, month=1, day=2), \
		                                        end_time=datetime(year=2002, month=1, day=1), timezone=1)

    print "Before:   ", A.temporal_relation(B)
    print "After:    ", B.temporal_relation(A)

    A = raster_absolute_time(ident="test1@PERMANENT", start_time=datetime(year=2000, month=1, day=1), \
		                                        end_time=datetime(year=2001, month=1, day=1), timezone=1)
    B = raster_absolute_time(ident="test2@PERMANENT", start_time=datetime(year=2000, month=1, day=1), \
		                                        end_time=datetime(year=2002, month=1, day=1), timezone=1)

    print "Starts:   ", A.temporal_relation(B)
    print "Started:  ", B.temporal_relation(A)

    A = raster_absolute_time(ident="test1@PERMANENT", start_time=datetime(year=2000, month=1, day=1), \
		                                        end_time=datetime(year=2001, month=1, day=1), timezone=1)
    B = raster_absolute_time(ident="test2@PERMANENT", start_time=datetime(year=2000, month=1, day=2), \
		                                        end_time=datetime(year=2001, month=1, day=1), timezone=1)

    print "Finished: ", A.temporal_relation(B)
    print "Finishes: ", B.temporal_relation(A)

    A = raster_absolute_time(ident="test1@PERMANENT", start_time=datetime(year=2000, month=1, day=1), \
		                                        end_time=datetime(year=2001, month=1, day=1), timezone=1)
    B = raster_absolute_time(ident="test2@PERMANENT", start_time=datetime(year=2000, month=3, day=1), \
		                                        end_time=datetime(year=2000, month=9, day=1), timezone=1)

    print "Contains: ", A.temporal_relation(B)
    print "During:   ", B.temporal_relation(A)


    A = raster_absolute_time(ident="test1@PERMANENT", start_time=datetime(year=2000, month=1, day=1), \
		                                        end_time=datetime(year=2000, month=6, day=1), timezone=1)
    B = raster_absolute_time(ident="test2@PERMANENT", start_time=datetime(year=2000, month=3, day=1), \
		                                        end_time=datetime(year=2000, month=9, day=1), timezone=1)

    print "Overlap:   ", A.temporal_relation(B)
    print "Overlapped:", B.temporal_relation(A)

    A = raster_absolute_time(ident="test1@PERMANENT", start_time=datetime(year=2000, month=1, day=1), \
		                                        end_time=datetime(year=2000, month=1, day=1), timezone=1)
    B = raster_absolute_time(ident="test2@PERMANENT", start_time=datetime(year=2000, month=1, day=1), \
		                                        end_time=datetime(year=2000, month=1, day=1), timezone=1)

    print "Equivalent:", A.temporal_relation(B)
    print "Equivalent:", B.temporal_relation(A)


def test_raster_dataset():
    
    grass.raster.mapcalc("test = sin(x()) + cos(y())", overwrite = True)
    
    name = "test"
    mapset =  grass.gisenv()["MAPSET"]
    
    print "Create a raster object"

    rds = raster_dataset(name + "@" + mapset)
    
    rds.load()
    
    print "Is in db: ", rds.is_in_db()
    
    rds.base.set_ttype("absolue")
    rds.absolute_time.set_start_time(datetime(year=2000, month=1, day=1))
    rds.absolute_time.set_end_time(datetime(year=2010, month=1, day=1))
    
    # Remove the entry if it is in the db
    rds.delete()
    
    rds.insert()
    rds.print_self()

    print rds.temporal_relation(rds)

def test_raster3d_dataset():
    
    grass.raster3d.mapcalc3d("test = sin(x()) + cos(y()) + sin(z())", overwrite = True)
    
    name = "test"
    mapset =  grass.gisenv()["MAPSET"]
    
    print "Create a raster3d object"

    r3ds = raster3d_dataset(name + "@" + mapset)
    
    r3ds.load()
    
    print "Is in db: ", r3ds.is_in_db()
    r3ds.print_self()
    
    r3ds.base.set_ttype("absolue")
    r3ds.absolute_time.set_start_time(datetime(year=2000, month=1, day=1))
    r3ds.absolute_time.set_end_time(datetime(year=2010, month=1, day=1))
    
    # Remove the entry if it is in the db
    r3ds.delete()
    
    r3ds.insert()
    r3ds.print_self()

    print r3ds.temporal_relation(r3ds)

def test_vector_dataset():
    
    grass.run_command("v.random", output="test", n=20, column="height", zmin=0, \
                      zmax=100, flags="z", overwrite = True)
    
    name = "test"
    mapset =  grass.gisenv()["MAPSET"]
    
    print "Create a vector object"

    vds = vector_dataset(name + "@" + mapset)
    
    vds.load()
    
    print "Is in db: ", vds.is_in_db()
    vds.print_self()
    
    vds.base.set_ttype("absolue")
    vds.absolute_time.set_start_time(datetime(year=2000, month=1, day=1))
    vds.absolute_time.set_end_time(datetime(year=2010, month=1, day=1))
    
    # Remove the entry if it is in the db
    vds.delete()
    
    vds.insert()
    vds.print_self()

    print vds.temporal_relation(vds)

#test_dict_sql_serializer()
create_temporal_database()
test_dataset_identifer()
test_absolute_timestamp()
test_relative_timestamp()
test_spatial_extent()
#test_map_metadata()
#test_base_absolute_time_extent_metadata()
#test_absolut_time_temporal_relations()
#test_raster_dataset()
#test_raster3d_dataset()
#test_vector_dataset()