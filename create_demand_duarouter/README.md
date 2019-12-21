目標：使用 duarouter 來生成交通流量， 並對比未使用 duarouter 的交通流量狀況
---
需要的檔案
---
```
randomTrips.py
bigmac.net.xml
```
説明： duarouter （動態均衡算法）
---
* For a given set of vehicles with of origin-destination relations (trips), the simulation must determine routes through the network (list of edges) that are used to reach the destination from the origin edge. The simplest method to find these routes is by computing shortest or fastest routes through the network using a routing algorithm such as Djikstra or A*. These algorithms require assumptions regarding the travel time for each network edge which is commonly not known before running the simulation due to the fact that travel times depend on the number of vehicles in the network.


步驟一：
---
* 把 net.xml 利用 randomTrips.py 生成 bigmac.rou.xml。
* 做完這一步會生成 trips.trips.xml， 此時的 trip 是非常隨機的。
* 模擬時間 7200 秒， 每隔 0.4 秒生成一輛車子
```
python randomTrips.py -n bigmac.net.xml -r taipei.rou.xml -e 7200 -p 0.4
```

步驟二：
---
* duaIterate.py 放在 tools/assign 目錄地下
```
python duaIterate.py -n bigmac.net.xml -t trips.trips.xml 
```
* 會生成一系列檔案，可以留意到還生成了 sumocfg
</br>
<div align=center> <img src="https://github.com/AvisChiu/SUMO/blob/master/create_demand_duarouter/figure/figure1.PNG" width="600"/></div>
</br> 

步驟三
---
* 用 randomTrips.py 生成的檔案還需要自己編輯 sumocfg

結果比較
---
* random 的結果會比較擁擠，沒有考慮動態均衡
</br>
<div align=center> <img src="https://github.com/AvisChiu/SUMO/blob/master/create_demand_duarouter/figure/figure2.PNG" width="600"/></div>
</br> 

* duarouter 的結果相對不會發生擁塞

</br>
<div align=center> <img src="https://github.com/AvisChiu/SUMO/blob/master/create_demand_duarouter/figure/figure3.PNG" width="600"/></div>
</br> 

注意事項
---
* random 不需要 trip， 之後要自己編輯sumocfg
* duarouter 要準備 trip， 之後自動生成 sumocfg
