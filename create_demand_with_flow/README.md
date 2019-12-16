Add traffic demand by using "flow"
---
* 官方定義：
* Using trip definitions
As described above, each trip consists at least of the starting and the ending edge and the departure time. This is useful for when you want to create demand by hand or when writing your own scripts to import custom data. You may either use DUAROUTER to turn your trips into routes. See Demand/Shortest_or_Optimal_Path_Routing and Demand/Dynamic_User_Assignment, or you may load the trips directly into SUMO (more details).
* Using flow definitions
This is mostly the same approach as using trip definitions, but one may join vehicles having the same departure and arrival edge using this method.


步驟
---
* 定義一個關於 flow 的 xml 檔案，關於起點和重點，這部分要給予 net.xml 來做。
</br>
<div align=center> <img src="https://github.com/AvisChiu/SUMO/blob/master/create_demand_with_flow/figure/figure1.png" width="600"/></div>
</br>    

* 生成 rou.xml 檔案, duarouter(有待瞭解，據説有幾種生成方式)
* 會得到 rou.xml 和 rou.alt.xml
```
duarouter -n MySUMONet.net.xml -f ex_FLOW.flow.xml -o ex_ROU.rou.xml
```
* 編寫 sumocfg 檔案（無非是設定 input 的地圖和路由， output 的一些檔案， 模擬的時間...）
</br>
<div align=center> <img src="https://github.com/AvisChiu/SUMO/blob/master/create_demand_with_flow/figure/figure2.png" width="600"/></div>
</br>   

* 用 sumo-GUI 開啓，看模擬的結果
</br>
<div align=center> <img src="https://github.com/AvisChiu/SUMO/blob/master/create_demand_with_flow/figure/figure3.PNG" width="600"/></div>
</br>   

總結
---
* 還是需要先設定起點和終點，才能生成 rou.xml。 但有時候需要生成一些比較隨機的 traffic demand， 因此要繼續研究。
* 對於生成的資料， output-tripinfos.xml 中，有一些的資料， 還需要研究這部分是不是想要的資訊。
```
<tripinfo id="flow3.0" 
depart="0.00" 
departLane="3i_0" 
departPos="5.10" 
departSpeed="0.00" 
departDelay="0.00" 
arrival="74.00" 
arrivalLane="4o_0" 
arrivalPos="495.25" 
arrivalSpeed="11.18" 
duration="74.00" 
routeLength="994.90" 
waitingTime="0.00" 
waitingCount="0" 
stopTime="0.00" 
timeLoss="8.40" 
rerouteNo="0" 
devices="vehroute_flow3.0 
tripinfo_flow3.0"
vType="DEFAULT_VEHTYPE" 
speedFactor="1.08" 
vaporized=""/>
```
