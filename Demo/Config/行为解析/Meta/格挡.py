# coding=utf-8

import Meta.Tools as Tools

def 格挡(master, output):
    sort = [ "时长" ]

    defs = {
        "时长": 30
    }

    fmt = "Behavior.MetaRoleBlock(self, {0});"
    Tools.BuildArgs(master, sort, defs, fmt, output)
