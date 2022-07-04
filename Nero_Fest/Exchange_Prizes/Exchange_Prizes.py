# -*- encoding=utf8 -*-
__author__ = "Max"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
if not cli_setup():
    auto_setup(__file__, devices=["Android:///"])


if __name__ == "__main__":
    
    # 提前定好抽 flag 池，一次抽太多礼物盒会放不下QwQ
    # 适用于 10 池之后，从完整的池子开始抽
    # 一池是 30 次点击，平均一次有效点击需要点 8 次左右，干脆直接猛点 240 次 +，记得把损耗包进去
    # Airtest 连接卡的话容易对不齐轴，建议重连
    
    flag = 10
    while flag>0:
        while not exists(Template(r"tpl1656937659990.png", record_pos=(0.387, -0.09), resolution=(1024, 576))):
            for k in range(30*8+25):
                touch(v=(333,360))
        
        touch(wait(Template(r"tpl1656937659990.png", record_pos=(0.387, -0.09), resolution=(1024, 576)), timeout=60))
        sleep(2)
        touch(wait(Template(r"tpl1656937712022.png", record_pos=(0.149, 0.158), resolution=(1024, 576)), timeout=60))
        sleep(2)
        touch(wait(Template(r"tpl1656937750071.png", record_pos=(-0.005, 0.156), resolution=(1024, 576)),timeout=60))
        flag=flag-1
    
    
    ''' 无用的草稿...
    flag = 30 * 10
    while flag>0:
        while exists(Template(r"tpl1656937659990.png", record_pos=(0.387, -0.09), resolution=(1024, 576))):
            touch(wait(Template(r"tpl1656937659990.png", record_pos=(0.387, -0.09), resolution=(1024, 576)), timeout=60))
            sleep(1)
            touch(wait(Template(r"tpl1656937712022.png", record_pos=(0.149, 0.158), resolution=(1024, 576)), timeout=60))
            touch(wait(Template(r"tpl1656937750071.png", record_pos=(-0.005, 0.156), resolution=(1024, 576)),timeout=60))
        
        if exists(Template(r"tpl1656937777910.png", record_pos=(-0.173, 0.07), resolution=(1024, 576))):
            touch(Template(r"tpl1656937777910.png", record_pos=(-0.173, 0.07), resolution=(1024, 576)))
            sleep(1)
            touch(v=(240,290))
            sleep(1)
            flag = flag - 1
    '''
    
    
    '''  无用的草稿...
        if not exists(Template(r"tpl1656937659990.png", record_pos=(0.387, -0.09), resolution=(1024, 576))):
            for k in range(20):
                touch(v=(333,360))
            touch(Template(r"tpl1656937777910.png", record_pos=(-0.173, 0.07), resolution=(1024, 576)))
            for k in range(20):
                touch(v=(333,360))
    '''