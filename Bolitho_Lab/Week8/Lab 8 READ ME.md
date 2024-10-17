# E-Portfolio Leah Bolitho 

---

## The Problem

One of the largest problems facing city planning, management, construction, and disaster remediation is the flooding of water features such as streams, rivers, lakes, and water features. Flooding can occur quickly and without warning, meaning corporations and developers have to be aware of potential flooding risks within their developments. This also means they should take flooding risk into consideration when analyzing the feasibility of new builds and projects.

### Project Goal/ Solution

The Goal is to build a database of all streams, rivers, lakes, and water features, as well as analyze their flood potential. By intersecting multiple databases and images, we will be able to understand the flood potential of waterways, as well as how it intersects with buildings, roads, and other structures. This will help to minimize risks both in the public sphere and within private corporations. 

This tool is also useful in analyzing the viability, cost effectiveness, and risks of potential building locations. It can also indicate the damage potential to building expansions, etc. 

---

### Software Used 

The software that will used is ArcGIS, ArcPy, and Visual Studio Code. 

*ArcGIS*

ArcGIS is a online system used for mapping analysis. Through the software you can make maps, analyze data, and share projects to other develops. 

*ArcPy*

ArcPy is a Python library that allows developers to use python functionally in ArcGIS and ArcGIS associated tools. ArcPy allows developers to automate many functions used throughout the ArcGIS system. 

Python incorporates a readable and general use language that can be transferred between multiple interfaces. 

*Visual Studio Code*

Visual studio code is a source code editor useful in writing and building code. Visual studio code has an easy and understandable layout, as well features that allow developers to customize their experience and use. 

Visual studio code is viable on Windows, macOS, and Linux. It can understand and edit a large degree of languages, including python, which as indicated earlier will be used in this project. Visual Studio code also allows software to be saved online and accessed on other devices, making this system and its associated code available outside of the ArcGIS interface. 

### Project Outline

1. Identify Study Area: This is dependent on the area of potential builds, current risk areas, etc. that are within corporate interest as determined by the risk mediation and environmental safety teams. 
2. List: First, lists of coordinates, buildings, etc. must be complied and inputted into ArcPy. An example of how to compile lists and perform basic functions can be found in the link below: 
    [Lab 2](https://github.com/tamu-edu-students/Bolitho_GEOG676/blob/main/Bolitho_Lab/Week2/Lab%202%20python%20script.py)
3. Import: Import coordinates of buildings, roads, and structures into the map. Example of reading data from a file can be found in the link below: 
    [Lab 3](https://github.com/tamu-edu-students/Bolitho_GEOG676/blob/main/Bolitho_Lab/Week3/Lab%203%20Python%20Script.py)
4. Creating a Geodatabase and Buffering: After pertinent information has been inputted, a geodatabase can be created through those layers and saved for future projects and use. Using the buffer operation, create a buffer polygon around waterways layer (input) to a distance representing a feasible area of flooding. An example of the script used to create a geodatabase and buffer points can be found below:
    [Lab 4](https://github.com/tamu-edu-students/Bolitho_GEOG676/blob/main/Bolitho_Lab/Week4/Lab%204%20Python%20Script.pyt)
5. Creating a toolbox: A toolbox can be created in ArcGIS to buffer distances, intersect layers, and output the resulting information into a CSV file to be utilized by the mitigation team. This also allows for these functions and commands to be utilized quickly on other projects, including other study areas and locations. An example of the script used to create the toolbox can be found in the link below: 
    [Lab 5](https://github.com/tamu-edu-students/Bolitho_GEOG676/blob/main/Bolitho_Lab/Week5/Lab%205%20Python%20Script.pyt)
6. Graduated Color Scheme: Using graduated colors, you can analyze different degrees of storm surge/ flooding probability. Use color gradients to show various degrees of distances of flooding from waterways. An example of a color map and the associated code can be found in the link below 
    [Lab 6](https://github.com/tamu-edu-students/Bolitho_GEOG676/blob/main/Bolitho_Lab/Week6/Lab%206%20Script%20final.pyt)
7. Ariel Overlays: The database will be supported by ariel images of water features, which is helpful in analyzing change over time. This is also useful in analyzing variability of water features throughout different locations. An example of using ariel images can be found in the link below 
    [Lab 7](https://github.com/tamu-edu-students/Bolitho_GEOG676/blob/main/Bolitho_Lab/Week7/Lab%207%20Python%20Script.pyt)

---

### Other 

# Return on Investment # 
- Return on Investment will be seen through risk mitigation. Through strategic building locations, as well as the detection of catastrophic flooding, money will be saved on emergency cleanup and rebuilding. Reduction of risk will eventually correlate to a return on investment. 

- The Code and database will be developed through developers and software team working in house. This will be maintained on ArcGis software by the same team over the course of its use. 