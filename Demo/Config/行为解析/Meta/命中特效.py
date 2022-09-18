# coding=utf-8

import Meta.Tools as Tools

def 命中特效(master, output):
    if len(master.Ins) == 0:
        sort = [ ]
        defs = { }
        fmt = "Behavior.MetaEffectHit(attack);"
        Tools.BuildArgs(master, sort, defs, fmt, output)
    else:
        sort = [ "ID" ]
        defs = { }
        fmt = "Behavior.MetaEffectHit(attack, config.ID * 10 + {0});"
        Tools.BuildArgs(master, sort, defs, fmt, output)