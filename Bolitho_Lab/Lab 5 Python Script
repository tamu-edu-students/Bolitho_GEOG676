import arcpy 
print (arcpy)

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the .pyt file)"""
        self.label = "Toolbox"
        self.alias = ""
        
        # List of tool classes associated with this toolbox
        self.tools = [GarageBuildingIntersection]
        
class GarageBuildingIntersection(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)"""
        self.label = "Lab 5 Python Toolbox"
        self.description = "Determines which buildings on TAMU's campus are near a targeted building"
        self.canRunInBackground = False # Only used in ArcMap 
        self.category = "Building Tools"
        
    def getParameterInfo(self):
        """Define parameter definitions"""
        param0 = arcpy.Parameter(
            displayName="GDB Folder", 
            name="GDBFolder",
            datatype="DEFolder",
            parameterType="Required",
            direction="Input"
        )
        param1 = arcpy.Parameter(
            displayName="GDB Name",
            name="GDBName",
            datatype="GPString",
            parameterType="Required",
            direction="Input"
        )
        param2 = arcpy.Parameter(
            displayName="Garage CSV File",
            name="GarageCSVFile",
            datatype="DEFile",
            parameterType="Required",
            direction="Input"
        )
        param3 = arcpy.Parameter(
            displayName="Campus Layer Name",
            name="GarageLayerName",
            datatype="GPString",
            parameterType="Required",
            direction="Input"
        )
        param4 = arcpy.Parameter(
            displayName="Campus GDB",
            name="CampusGDB",
            datatype="DEType",
            parameterType="Required",
            direction="Input"
        )
        param5 = arcpy.Parameter(
            displayName="Buffer Distance",
            name="BufferDistance",
            datatype="GPDouble",
            parameterType="Required",
            direction="Input"
        )
        params = [param0, param1, param2, param3, param4, param5]
        return params 
    
    def isLicensed(self):
        """Set whether tool is licensed to execute"""
        return True 
    
    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal validation is performed. This method is called whenever a parameter has been changed"""
        return 
    
    def execute(self, parameters, messages):
        """The source code of the tool"""
        folder_path = parameters[0].valueAsText
        gdb_name = parameters[1].valueAsText
        gdb_path = folder_path + '\\' + gdb_name
        arcpy.CreateFileGDB_management(folder_path, gdb_name)
        
        csv_path = parameters[2].valueAsText
        garage_layer_name = parameters[3].valueAsText
        garages = arcpy.MakeXYEEventLayer_management(csv_path, 'X', 'Y', garage_layer_name)
        
        input_layer = garages
        arcpy.FeatureClassToGeodatabase_conversion(input_layer, gdb_path)
        garage_points = gdb_path + '\\' + garage_layer_name
        
        #open campus gdb, copy building feature to our gdb
        campus = parameters[4].valueAsText
        buildings_campus = campus + '\Structures'
        buildings = gdb_path +'\\' + 'Buildings'
        
        arcpy.Copy_management(buildings_campus, buildings)
        
        # Re-Projection 
        spatial_ref = arcpy.Describe(buildings).spatialReference
        arcpy.Project_management(garage_points, gdb_path +'\Garage_Points_reprojected', spatial_ref)
        
        # buffer the garages 
        buffer_distance = int(parameters[5].value)
        
        # Intersect our buffer with the buildings 
        arcpy.Intersect_analysis([garageBuffered, Buildings], gdb_path + '\Garage_Building_Intersection', 'ALL')
        
        arcpy.TableToTable_converstion(gdb_path + '\Garage_Bulding_Intersection.dbf', r'C:\Users\emily\Documents\GitHub\Bolitho_GEOG676', 'nearbyBuildings.csv')
        
        return None
       
