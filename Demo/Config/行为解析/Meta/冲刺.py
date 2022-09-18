# coding=utf-8

import Meta.Tools as Tools

def 冲刺(master, output):
    sort = [ "距离", "时长" ]

    defs = {
        "距离": 0,
        "时长": 0,
    }

    fmt = "Behavior.MetaRoleNextF(self, {0}, {1});"
    Tools.BuildArgs(master, sort, defs, fmt, output)
