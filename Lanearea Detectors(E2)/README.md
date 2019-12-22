目標：在各路段安裝監測器來檢測交通狀況
---
需要的檔案
---
```
generateTLSE2Detectors.py ： 位於 tools/output 目錄底下
net.xml
```

* 先把 net.xml 拉到 tools/output 目錄底下，打開 cmd
* 執行完之後會 output 一個 e2.add.xml
```
python generateTLSE2Detectors.py --help
```
</br>
<div align=center> <img src="https://github.com/AvisChiu/SUMO/blob/master/Lanearea%20Detectors(E2)/figure/figure2.PNG" width="600"/></div>
</br> 

編輯 sumocfg
---
* 在 input 中加上 e2.add.xml
* 使用 sumo-gui 開始模擬， 模擬完之後會生成一個 e2output.xml
* 可以看到地圖已安裝了監測裝置。
</br>
<div align=center> <img src="https://github.com/AvisChiu/SUMO/blob/master/Lanearea%20Detectors(E2)/figure/figure1.PNG" width="600"/></div>
</br> 
</br>
<div align=center> <img src="https://github.com/AvisChiu/SUMO/blob/master/Lanearea%20Detectors(E2)/figure/figure4.PNG" width="600"/></div>
</br> 

結果
---
* 查看 e2output.xml， 有各種信息，各欄位資料還需要確認。
*  e2output.xml 檔案較大
</br>
<div align=center> <img src="https://github.com/AvisChiu/SUMO/blob/master/Lanearea%20Detectors(E2)/figure/figure3.PNG" width="600"/></div>
</br> 

NOTE
---
* 跑模擬的時候需要有 net.xml, rou.xml, .sumocfg
* 需要生成的檔案自己定義

補充
---
| Name | Type | Description |
| --- | --- | --- |
| begin	 | (simulation) seconds	 | The first time step the values were collected in |
|  end	 | (simulation) seconds	 | The last time step + DELTA_T the values were collected in (may be equal to begin) |

