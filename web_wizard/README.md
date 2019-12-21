Using Web Wizard to generate traffic demand
---
* 在 sumo/tools 的目錄底下，有一個 osmWebWizard.py 檔案
* 執行以下， 會進入到一個網頁
```
python osmWebWizard.py
```
</br>
<div align=center> <img src="https://github.com/AvisChiu/SUMO/blob/master/web_wizard/figure1.PNG" width="600"/></div>
</br> 

選擇地圖區域，手動增加需要的交通流量
---
* 民權東路附近區域
* 最後按右上角的 generate scenario 會在 /tools 地下生成一個日期的文檔
* 自動打開 sumo-gui， 開始跑模擬

</br>
<div align=center> <img src="https://github.com/AvisChiu/SUMO/blob/master/web_wizard/figure2.PNG" width="600"/></div>
</br> 


結論
---
* 雖然簡單方便，但沒有辦法生成一個完整的一天的交通流量
