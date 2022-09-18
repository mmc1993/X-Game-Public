# coding=utf-8

import Meta.Tools as Tools

def 设置攻击参数(master, output):
    sort = ["血量", "硬直", "推力时长", "推力距离", "停顿时长"]

    defs = {
        "血量": "0",
        "硬直": "0",
        "推力时长": "0",
        "推力距离": "0",
        "停顿时长": "0.3f",
    }

    fmt = "attack.Attack = {0};\n"          \
        + "attack.Stable = {1};\n"          \
        + "attack.ForceDuration = {2};\n"   \
        + "attack.ForceDistance = {3};\n"   \
        + "attack.StopMotionTime = {4};\n"
    Tools.BuildArgs(master, sort, defs, fmt, output)

