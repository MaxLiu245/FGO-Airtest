# FGO-Airtest
《懒得肝无限池而想整个脚本打游戏这件事》

## 若脚本启动出现设备连接问题
```python
AttributeError: 'NoneType' object has no attribute 'snapshot'
```
可以在 `.py` 脚本开头加入下面代码（只连接 mumu 模拟器时）
```python
from airtest.core.api import *
from airtest.cli.parser import cli_setup
if not cli_setup():
    auto_setup(__file__, devices=["Android:///"])
```
> 参考
> * https://airtest.doc.io.netease.com/IDEdocs/airtest_framework/2_connect_device/#2_1
> * https://airtest.doc.io.netease.com/IDEdocs/3.2device_connection/2_emulator_connection/#3py


