嘗試模擬一天的交通車流量
---

監測路段： e1det_gneE128_0
```
0 ~ 25200 (00:00 ~ 07:00), -p 0.9
25201 ~ 32400 (07:00 ~ 09:00), -p 0.35
32401 ~ 61200 (09；00 ~ 17：00) -p 0.6
61201 ~ 68400 （17：00 ~ 19：00）-p 0.3
68400 ~ 86400 （19：00 ~ 24：00）-p 0.6
```

```
python randomTrips.py -n bigmac.net.xml -r bigmac.rou0.xml -b 0 -e 25200 -p 0.9
python randomTrips.py -n bigmac.net.xml -r bigmac.rou0.xml -b 25201 -e 32400 -p 0.35
python randomTrips.py -n bigmac.net.xml -r bigmac.rou0.xml -b 32401 -e 61200 -p 0.6
python randomTrips.py -n bigmac.net.xml -r bigmac.rou0.xml -b 61201 -e 68400 -p 0.3
python randomTrips.py -n bigmac.net.xml -r bigmac.rou0.xml -b 68401 -e 86400 -p 0.6
```
* 會建立好幾個 rou.xml

</br>
<div align=center> <img src="https://github.com/AvisChiu/SUMO/blob/master/oneday%20traffic%20simulation/figure/figure2.PNG" /></div>
</br> 

* 下一步就是分別做模擬，每一次都要更改 .sumocfg

</br>
<div align=center> <img src="https://github.com/AvisChiu/SUMO/blob/master/oneday%20traffic%20simulation/figure/figure3.png" /></div>
</br> 

* 會得到好幾個 e1ouput.xml， 這些都是資料，合並起來就是一天的資料。

</br>
<div align=center> <img src="https://github.com/AvisChiu/SUMO/blob/master/oneday%20traffic%20simulation/figure/figure4.PNG" /></div>
</br> 

* 最後對資料做處理，得到的結果如下

</br>
<div align=center> <img src="https://github.com/AvisChiu/SUMO/blob/master/oneday%20traffic%20simulation/data.PNG" /></div>
</br> 






