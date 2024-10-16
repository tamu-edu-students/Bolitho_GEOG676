import arcpy 
print(arcpy)

arcpy.env.workspace = r'C:\Users\emily\Documents\GitHub\Bolitho_GEOG676'
folder_path = r'C:\Users\emily\Documents\GitHub\Bolitho_GEOG676'
gdb_name = 'test.gdb'
gdb_path = folder_path + '\\' + gdb_name 
arcpy.CreateFileGDB_management(folder_path, gdb_name)

csv_path = r'C:\Users\emily\Documents\GitHub\2024-TAMU-GEOG-676-GIS-Programming-MGsc-main\2024-TAMU-GEOG-676-GIS-Programming-MGsc-main\data\homework\04\garages.csv'
garage_layer_name = 'Garage_Points'
garages = arcpy.MakeXYEventLayer_management(csv_path, 'X', 'Y', garage_layer_name)

input_layer = garages
arcpy.FeatureClassToGeodatabase_conversion(input_layer, gdb_path)
garage_points = gdb_path + '\\' + garage_layer_name 

# open campus gdb, copy building feature to our gdb 
campus = r'C:\Users\emily\Documents\GitHub\2024-TAMU-GEOG-676-GIS-Programming-MGsc-main\2024-TAMU-GEOG-676-GIS-Programming-MGsc-main\data\homework\04\Campus.gdb'
buildings_campus = campus + '\Structures'
buildings = gdb_path + '\\' + 'Buildings'

arcpy.Copy_management(buildings_campus, buildings)

# re-projection 
spatial_ref = arcpy.Describe(buildings).spatialReference
arcpy.Project_management(garage_points, gdb_path + '\Garage_Points_reprojected', spatial_ref)


# buffer the garages 
garageBuffered = arcpy.Buffer_analysis(gdb_path + '\Garage_Points_reprojected', gdb_path + '\Garage_Points_buffered', 150)

# Intersect our buffer with the buildings 
arcpy.Intersect_analysis([garageBuffered, buildings], gdb_path + '\Garage_Building_Intersection', 'ALL')

arcpy.TableToTable_conversion(gdb_path + '\Garage_Building_Intersection.dbf', r'C:\Users\emily\Documents\GitHub\Bolitho_GEOG676', 'nearbyBuildings.csv')
