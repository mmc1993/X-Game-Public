# coding=utf-8

import Meta.Tools as Tools

def 等待(master, output):
    sort = ["时长"]

    defs = {
        "时长" : 1
    }

    fmt = "yield return Tools.Time2Frame({0});"
    Tools.BuildArgs(master, sort, defs, fmt, output)
