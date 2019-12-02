Map Pruning
---
* Target: delete uncessary part of a map.
```
netconvert --osm-files map.osm --keep-edges.by-vclass passenger -o hangzhou.net.xml --output.street-names --remove-edges.isolated --no-turnarounds --geometry.remove --roundabouts.guess
```
```
hangzhou.net.xml <----- XXX.net.xml (name by youself)
```

Example: before pruning
---
</br>
<div align=center> <img src="https://github.com/AvisChiu/SUMO/blob/master/map%20pruning/figure/figure2.PNG" width="600"/></div>
</br>   

Example: after pruning
---
</br>
<div align=center> <img src="https://github.com/AvisChiu/SUMO/blob/master/map%20pruning/figure/figure1.PNG" width="600"/></div>
</br>   
