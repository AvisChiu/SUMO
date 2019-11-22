Python connect Sumo
---
* Some note from the Sumo docunment.
* Target: run a .py and obtain the traffic simulation in sumo-gui


Environment Variable
---
* ADD in the path (C:\Users\AvisChiu\Desktop\sumo-1.3.1\bin), also create a new variable "SUMO_HOME" (add C:\Users\AvisChiu\Desktop\sumo-1.3.1) 
* The different between is "\bin"
* This is a necessary step before the using python
</br>   
<div align=center> <img src="https://github.com/AvisChiu/SUMO/blob/master/connect%20python/figure/figure1.PNG" width="400"/></div>
</br>   

Find the files
---
* You can find the files below
</br>   
<div align=center> <img src="https://github.com/AvisChiu/SUMO/blob/master/connect%20python/figure/figure2.PNG" width="600"/></div>
</br>   
   
* runner.py need the files in data, as you can see in the code.
<div align=center> <img src="https://github.com/AvisChiu/SUMO/blob/master/connect%20python/figure/figure3.PNG" width="600"/></div>
</br>       
   
* It mean the files in data is what you need, includes(net.xml, rou.xml...)
* In other word, no matter where your files are, they need to be saved with the same dictionary.

Dont change the code, just run...
---
```
python runner.py
```
<div align=center> <img src="https://github.com/AvisChiu/SUMO/blob/master/connect%20python/figure/figure4.PNG" width="600"/></div>
</br>  

In other word
---
* We can change to code, and achieve some controls in sumo.
* Like traffic flow monitor, traffic light control...
* At least we can use python now...
