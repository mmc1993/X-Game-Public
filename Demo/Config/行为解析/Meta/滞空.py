# coding=utf-8

import Meta.Tools as Tools

def 滞空(master, output):
    sort = [ "时长" ]

    defs = {
        "时长": 0,
    }

    fmt = "Behavior.MetaRoleSupend(self, {0});"
    Tools.BuildArgs(master, sort, defs, fmt, output)
