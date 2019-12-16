目標：隨機增加交通流量
---
需要的檔案
---
```
randomTrips.py
taipei.net.xml
```

步驟
---
* 把 net.xml 利用 randomTrips.py 生成 taipei.rou.xml, 這是最重要的一步。
* 做完這一步會生成 rou.xml, rou.alt.xml, trips.trips.xml
```
$ python /usr/local/src/sumo-0.15.0/tools/trip/randomTrips.py -n taipei.net.xml -e 50 -l
$ python /usr/local/src/sumo-0.15.0/tools/trip/randomTrips.py -n taipei.net.xml -r taipei.rou.xml -e 50 –l
```

* 編輯 sumocfg， 不需要什麽特別的操作（僅僅是 input 檔案和設定模擬時間 ）


發現到的問題
---
* 據説是版本問題， 目前用的是 sumo1.3.1
```
Warning: Vehicle '15' performs emergency braking with decel=-9.00 wished=4.50 severity=1.00, time=57.00.
Warning: Vehicle '15' performs emergency stop at the end of lane '222682222#3_2' because there is no connection to the next edge (decel=-10.17, offset=0.99), time=57.00.
```
</br>
<div align=center> <img src="https://github.com/AvisChiu/SUMO/blob/master/create_demand_random/figure/figure1.PNG" width="600"/></div>
</br> 

總結
---
* 會卡死其實與整張地圖的汽車總容量有關
