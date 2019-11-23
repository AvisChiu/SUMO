Python connect Sumo (Using own files)
---
* Target: Create documents, run .py, obtained the simulation.


Create files
---
* Create .net.xml : follow the example in https://sumo.dlr.de/docs/Tutorials/quick_start.html.
* Save as .net.xml
</br>
<div align=center> <img src="https://github.com/AvisChiu/SUMO/blob/master/simple%20project(connect%20python)/figure/figure2.PNG" width="600"/></div>
</br>    

* Create rou.xml : follow the example in https://sumo.dlr.de/docs/Tutorials/quick_start.html.
* Save as .net.xml
* Create .sumocfg : follow the example in https://sumo.dlr.de/docs/Tutorials/quick_start.html.
</br>
<div align=center> <img src="https://github.com/AvisChiu/SUMO/blob/master/simple%20project(connect%20python)/figure/figure3.PNG" width="600"/></div>
</br>    

Can run through sumo-gui first
---
* Will find the .rou.xml changed...

Change the code in runner.py
---
* Just copy the code in .rou.xml.
* Pay attention in vehicle ID, the code in foe loop need to be change.
* Because this environment doesm't have traffic light, so command it.
* We can know def run() is the control module, and def generate_routefile() set the traffic demand.
* Remenber to get the correct files.
</br>
<div align=center> <img src="https://github.com/AvisChiu/SUMO/blob/master/simple%20project(connect%20python)/figure/figure4.PNG" width="600"/></div>
</br>    
</br>
<div align=center> <img src="https://github.com/AvisChiu/SUMO/blob/master/simple%20project(connect%20python)/figure/figure5.PNG" width="600"/></div>
</br>    
<div align=center> <img src="https://github.com/AvisChiu/SUMO/blob/master/simple%20project(connect%20python)/figure/figure6.PNG" width="600"/></div>
</br>    


Run the runner.py
---
* Run the runner.py in terminal
* Check the simulation time in .sumocfg   
<div align=center> <img src="https://github.com/AvisChiu/SUMO/blob/master/simple%20project(connect%20python)/figure/figure7.PNG" width="600"/></div>
</br>    
<div align=center> <img src="https://github.com/AvisChiu/SUMO/blob/master/simple%20project(connect%20python)/figure/figure1.PNG" width="600"/></div>
</br>    
