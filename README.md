# SUMO

Some simple operations about Sumo traffic simulator.
---
[Reference](https://zhuanlan.zhihu.com/p/35707739)    
https://zhuanlan.zhihu.com/p/35707739


</br> 

Installing
---
[Install](https://sumo.dlr.de/docs/Installing.html)
https://sumo.dlr.de/docs/Installing.html
* My system is windows, so I use < 64 bit zip: sumo-win64-1.3.1.zip >
* Download and extra it , a package of file will be in Desktop.

</br> 

Simple Example
---
* https://sumo.dlr.de/docs/Tutorials/quick_start.html
* Follow the file, and obtain the traffic flow running in Sumo:
<div align=center> <img src="https://github.com/AvisChiu/SUMO/blob/master/figure/simple_example.PNG" width="600"/></div>
</br> 
* Note: the bin in package cover some files, for routing or network structure. 
* In netedit.exe, you can design the network like the above.save it and will get .net.xml
* In addition, from [listing 1.5](https://sumo.dlr.de/docs/Tutorials/quick_start.html), you can get the routing code. Save it and get .rou.xml
* In listing 1.7, you need to creat a .sumocfg, just copy the code 
* Turn on sumo-gui.exe, open a simulation, import a file which end with sumocfg. you need to add input files, .net.xml and rou.xml
<div align=center> <img src="https://github.com/AvisChiu/SUMO/blob/master/figure/figure1.PNG" width="600"/></div>

</br> 

Open Street Map
---
* To use the real world map in Sumo. 
* Link: https://www.openstreetmap.org/export#map=16/25.0198/121.5518
* Export the map and get a .osm file , now need to transform it into .net.xml
* Open your terminal, cd in the .osm 's document (all files included .osm / .net.xml / .rou.xml / .sumocfg are better in a document)
```
netconvert --osm-files map.osm -o map.net.xml
```
* Check the network in netedit.exe
<div align=center> <img src="https://github.com/AvisChiu/SUMO/blob/master/figure/figure2.PNG" width="600"/></div>
</br> 
* Next step is set the routing. It need to the randomTrips.py (in tools)
* Open your terminal, cd in the document(contains the files above, copy the .py into the document), then and get a .rou.xml
```
python randomTrips.py -n map.net.xml -r map.rou.xml -e 100 -l
```
* change the input in .sumocfg first, 
<div align=center> <img src="https://github.com/AvisChiu/SUMO/blob/master/figure/figure5.PNG" width="600"/></div>
</br> 
* Open sumo-gui.exe, import a .sumocfg, (change the simulation time) ,then begin
<div align=center> <img src="https://github.com/AvisChiu/SUMO/blob/master/figure/figure4.PNG" width="600"/></div>
</br>
<div align=center> <img src="https://github.com/AvisChiu/SUMO/blob/master/figure/figure6.PNG" width="600"/></div>

