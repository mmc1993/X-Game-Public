# coding=utf-8

import Meta.Tools as Tools

def 狂怒(master, output):
    sort = [ "时长" ]

    defs = {
        "时长": 0,
    }

    fmt = "Behavior.MetaRoleRage(self, {0});"
    Tools.BuildArgs(master, sort, defs, fmt, output)
