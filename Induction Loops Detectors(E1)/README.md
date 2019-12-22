目標：在各路段安裝監測器來檢測交通狀況
---
需要的檔案
---
```
generateTLSE1Detectors.py ： 位於 tools/output 目錄底下
net.xml
```
* 先把 net.xml 拉到 tools/output 目錄底下，打開 cmd
* 執行完之後會 output 一個 e1.add.xml
```
python generateTLSE2Detectors.py --help
```
</br>
<div align=center> <img src="https://github.com/AvisChiu/SUMO/blob/master/Induction%20Loops%20Detectors(E1)/figure/figure1.PNG" width="600"/></div>
</br> 

編輯 sumocfg
---
* 在 input 中加上 e1.add.xml
* 使用 sumo-gui 開始模擬， 模擬完之後會生成一個 e1output.xml
* 可以看到地圖已安裝了監測裝置，是放在每一個路口，且每一條車道都有一個


結果
---
* 查看 e1output.xml， 有各種信息，各欄位資料還需要確認。
*  e1output.xml 比  e2output.xm了小很多
* 可以對比每一次跑完模擬後生成的檔案，都是一樣的，因此不用擔心隨機性。

</br>
<div align=center> <img src="https://github.com/AvisChiu/SUMO/blob/master/Induction%20Loops%20Detectors(E1)/figure/figure2.PNG" width="600"/></div>
</br> 

NOTE
---
* 跑模擬的時候需要有 net.xml, rou.xml, .sumocfg
* 需要生成的檔案自己定義

| Name | Type | Description |
| --- | --- | --- |
|begin|(simulation) seconds|	The first time step the values were collected in|
|end	|(simulation) seconds	|The last time step + DELTA_T the values were collected in|
|id	|id|	The id of the detector|
|nVehContrib	|#vehicles|	The number of vehicles that have completely passed the detector within the interval|
|flow	|#vehicles/hour|	The number of contributing vehicles extrapolated to an hour|
|occupancy|	%	|The percentage (0-100%) of the time a vehicle was at the detector.|
|speed	|m/s|	The arithmetic mean of the velocities of all completely collected vehicles (-1 indicates that no vehicles were collected). This gives the time mean speed.|
|harmonicMeanSpeed	|m/s	|The harmonic mean of the velocities of all completely collected vehicles (-1 indicates that no vehicles were collected). This gives the space mean speed.|
|length	|m|	The mean length of all completely collected vehicles (-1 indicates that no vehicles were collected).|
|nVehEntered	|#vehicles	|All vehicles that have touched the detector. Includes vehicles which have not passed the detector completely (and which do not contribute to collected values).|
