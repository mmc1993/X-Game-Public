# coding=utf-8

import Meta.Tools as Tools

def 转向目标(master, output):
    sort = [ "时长" ]
    defs = { }

    fmt = "yield return Behavior.MetaLookAtTarget(self, {0});"
    Tools.BuildArgs(master, sort, defs, fmt, output)
