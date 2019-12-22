使用 trips 檔案來生成流量
---
需要的檔案
---
```
bigmac.net.xml
bigmac.rou.xml
route2trips.py
```

* 爲了可以 output 出 trips 檔案，先要修改一下 code
</br>
<div align=center> <img src="https://github.com/AvisChiu/SUMO/blob/master/route2trip/figure1.PNG" width="600"/></div>
</br> 

* 使用 sumo-gui 跑模擬的時候，在 sumocfg 裏面就變成 input trips 檔案， 而不是 xml

NOTE
---
* 還是需要用 random 來生成 rou.xml
