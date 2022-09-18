# coding=utf-8

import Meta.Tools as Tools

def 奇点(master, output):
    sort = [ "时长" ]
    defs = { }

    fmt = "yield return Behavior.MetaBlackHole(attack, {0});"
    Tools.BuildArgs(master, sort, defs, fmt, output)
