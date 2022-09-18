# coding=utf-8

import Meta.Tools as Tools

def 播放特效(master, output):
    sort = [ "ID" ]
    defs = { }

    fmt = "Behavior.MetaEffect(config.ID * 10 + {0}, attack);"
    Tools.BuildArgs(master, sort, defs, fmt, output)