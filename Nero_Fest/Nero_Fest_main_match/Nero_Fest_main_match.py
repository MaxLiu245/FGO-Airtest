# -*- encoding=utf8 -*-
__author__ = "Max"

from airtest.core.api import *
from airtest.cli.parser import cli_setup
if not cli_setup():
    auto_setup(__file__, devices=["Android:///"])

def attack_with_Noble_Phantasm(image): # 宝具+前2个指令卡
    touch(wait(Template(r"tpl1576850638587.png", record_pos=(0.242, 0.142), resolution=(2520, 1080)),timeout=60))
    touch(wait(image,timeout=60))
    sleep(1)
    touch(v=(150,400)) # 指令卡1
    sleep(1)
    touch(v=(350,400)) # 指令卡2
    sleep(15)
    
def attack_with_3_default_hits(): # 前3个指令卡
    touch(wait(Template(r"tpl1576850638587.png", record_pos=(0.242, 0.142), resolution=(2520, 1080)),timeout=60))
    touch(v=(150,400)) # 指令卡1
    sleep(1)
    touch(v=(350,400)) # 指令卡2
    sleep(1)
    touch(v=(550,400)) # 指令卡3
    sleep(5)
    
    
def Nero_Fest_main_match(): # 尼禄祭正赛
    
    if exists(Template(r"tpl1656602911910.png", record_pos=(-0.054, -0.025), resolution=(1024, 576))): # 吃苹果
        touch(wait(Template(r"tpl1656602911910.png", record_pos=(-0.054, -0.025), resolution=(1024, 576)),timeout=60))
        sleep(1)
        touch(wait(Template(r"tpl1576851988180.png", record_pos=(0.064, 0.12), resolution=(2520, 1080)),timeout=60)) # 吃苹果
        sleep(1)
    
    touch(wait(Template(r"tpl1656644974535.png", record_pos=(-0.167, -0.182), resolution=(1024, 576)),timeout=60)) # 有时候初始化会是别的职介，导致选不了c呆，多发生于第一次进副本
    
    while not exists(Template(r"tpl1656679013047.png", record_pos=(-0.401, -0.106), resolution=(1024, 576))): # 识别左边是因为若识别脸部，c呆几个阶段的脸都会被识别，后面换人会有点问题
        swipe((400,600),(400,100)) # 设置朝向，下滑找c呆
        sleep(1)
    touch(wait(Template(r"tpl1656679013047.png", record_pos=(-0.401, -0.106), resolution=(1024, 576)),timeout=60))
    sleep(2)
    

    
    if exists(Template(r"tpl1576848397065.png", record_pos=(0.278, 0.19), resolution=(2520, 1080))): # 准备打架
        touch(wait(Template(r"tpl1576848397065.png", record_pos=(0.278, 0.19), resolution=(2520, 1080)), timeout=60))
        sleep(5) # 等一下加载，否则后面可能跟不上导致不稳定
        
    wait(Template(r"tpl1576850638587.png", record_pos=(0.242, 0.142), resolution=(2520, 1080)), timeout=60) # 等待加载完成
    
    
    touch(wait(Template(r"tpl1656604030955.png", record_pos=(-0.379, 0.172), resolution=(1024, 576)), timeout=60))
    sleep(1)
    touch(wait(Template(r"tpl1656604004643.png", record_pos=(-0.001, 0.046), resolution=(1024, 576)), timeout=60))
    sleep(1)
    
    touch(wait(Template(r"tpl1656603493988.png", record_pos=(0.189, 0.17), resolution=(1024, 576)),timeout=60))
    touch(wait(Template(r"tpl1656604004643.png", record_pos=(-0.001, 0.046), resolution=(1024, 576)),timeout=60))
    sleep(3)# 容易漏下一步
    
    touch(wait(Template(r"tpl1656934683114.png", record_pos=(0.052, 0.171), resolution=(1024, 576)),timeout=60))  
    sleep(1)
    
    touch(wait(Template(r"tpl1656603572764.png", record_pos=(0.431, -0.031), resolution=(1024, 576)),timeout=60))
    touch(wait(Template(r"tpl1656603620051.png", record_pos=(0.347, -0.038), resolution=(1024, 576)),timeout=60))
    touch(wait(Template(r"tpl1656934836649.png", record_pos=(0.075, -0.011), resolution=(1024, 576)),timeout=60))

    touch(v=(400,300))# 讨厌~
    touch(wait(Template(r"tpl1656603782523.png", record_pos=(-0.005, 0.206), resolution=(1024, 576)),timeout=60))
    sleep(5)# 容易漏下一步
    
    touch(wait(Template(r"tpl1656934886761.png", record_pos=(-0.446, 0.17), resolution=(1024, 576)),timeout=60))
    sleep(2)# 容易漏下一步
    
    touch(wait(Template(r"tpl1656934955169.png", record_pos=(-0.198, 0.171), resolution=(1024, 576)),timeout=60))
    sleep(1)
    touch(wait(Template(r"tpl1656935000534.png", record_pos=(-0.376, 0.171), resolution=(1024, 576)),timeout=60))
    sleep(1)
    touch(wait(Template(r"tpl1656935048209.png", record_pos=(-0.238, 0.059), resolution=(1024, 576)),timeout=60))
    sleep(5)# 容易漏下一步
    
    touch(wait(Template(r"tpl1656604281819.png", record_pos=(-0.444, 0.171), resolution=(1024, 576)),timeout=60))
    sleep(1)
    
    
    attack_with_Noble_Phantasm(Template(r"tpl1656935186657.png", record_pos=(-0.167, -0.12), resolution=(1024, 576)))
    
    
    wait(Template(r"tpl1576850638587.png", record_pos=(0.242, 0.142), resolution=(2520, 1080)),timeout=60) # 2t开始
    
    
    
    touch(wait(Template(r"tpl1656604137003.png", record_pos=(-0.125, 0.17), resolution=(1024, 576)),timeout=60))
    sleep(1)
    touch(wait(Template(r"tpl1656604170772.png", record_pos=(0.0, 0.055), resolution=(1024, 576)),timeout=60))
    sleep(1)
    

    touch(wait(Template(r"tpl1656935327121.png", record_pos=(0.119, 0.172), resolution=(1024, 576)),timeout=60))
    sleep(1)
    touch(wait(Template(r"tpl1656604004643.png", record_pos=(-0.001, 0.046), resolution=(1024, 576)),timeout=60))
    sleep(1)
    
    touch(wait(Template(r"tpl1656603493988.png", record_pos=(0.189, 0.17), resolution=(1024, 576)),timeout=60))
    sleep(1)
    touch(wait(Template(r"tpl1656604004643.png", record_pos=(-0.001, 0.046), resolution=(1024, 576)),timeout=60))
    sleep(1)
    
    wait(Template(r"tpl1576850638587.png", record_pos=(0.242, 0.142), resolution=(2520, 1080)),timeout=60)
    
    
    
    attack_with_Noble_Phantasm(Template(r"tpl1656604202608.png", record_pos=(0.002, -0.099), resolution=(1024, 576)))
    
    
    wait(Template(r"tpl1576850638587.png", record_pos=(0.242, 0.142), resolution=(2520, 1080)),timeout=60) # 3t开始
    
    
    touch(wait(Template(r"tpl1656604296115.png", record_pos=(-0.057, 0.171), resolution=(1024, 576)),timeout=60))
    sleep(1)
    
    touch(wait(Template(r"tpl1656603572764.png", record_pos=(0.431, -0.031), resolution=(1024, 576)),timeout=60))
    sleep(1)
    touch(wait(Template(r"tpl1656604337279.png", record_pos=(0.206, -0.037), resolution=(1024, 576)),timeout=60))
    sleep(1)
    
    attack_with_Noble_Phantasm(Template(r"tpl1656604202608.png", record_pos=(0.002, -0.099), resolution=(1024, 576)))
    
       

    while not exists(Template(r"tpl1576850387830.png", record_pos=(0.225, 0.188), resolution=(2520, 1080))): # 应对可能的羁绊升级、御主经验升级、御主礼装经验升级，逻辑暴力所以有点慢
        click(v=(400,400)) # click刚好会点出从者信息
        
        if exists(Template(r"tpl1656666289162.png", record_pos=(-0.249, -0.1), resolution=(1024, 576))): # 练度不够时偶尔会出现最后一面伤害不够的情况，需要补一次伤害
            touch(Template(r"tpl1656666339141.png", record_pos=(0.349, -0.233), resolution=(1024, 576)))
            attack_with_3_default_hits()
            sleep(1)
        
        touch(wait(Template(r"tpl1576850295381.png", record_pos=(-0.053, 0.168), resolution=(2520, 1080)),timeout=60))
        sleep(1)
        touch(wait(Template(r"tpl1576850295381.png", record_pos=(-0.053, 0.168), resolution=(2520, 1080)),timeout=60))
        sleep(1)
        
    touch(wait(Template(r"tpl1576850387830.png", record_pos=(0.225, 0.188), resolution=(2520, 1080)),timeout=60)) # QP
    sleep(1)
    touch(wait(Template(r"tpl1656643360210.png", record_pos=(0.155, 0.158), resolution=(1024, 576)),timeout=60))
    sleep(1)
    
def Nero_Fest_finals(): # 尼禄祭决赛
    return 0


if __name__ == "__main__":
    
    for k in range(50):
        if exists(Template(r"tpl1656645278109.png", record_pos=(0.391, -0.088), resolution=(1024, 576))): # 进入副本
            touch(Template(r"tpl1656645278109.png", record_pos=(0.391, -0.088), resolution=(1024, 576))) 
            sleep(1)
        
        Nero_Fest_main_match()

    