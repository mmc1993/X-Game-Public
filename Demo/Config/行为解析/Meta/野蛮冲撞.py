# coding=utf-8

import Meta.Tools as Tools

def 野蛮冲撞(master, output):
    sort = [ "范围", "段数", "频率", "特效", "距离", "时长" ]
    defs = {
        "特效": -1,
    }

    fmt = "yield return Behavior.MetaAttackForwardMove(config, {0}, {1}, {2}, {3}, {4}, {5}, {6});"
    Tools.BuildArgs(master, sort, defs, fmt, output)