# coding=utf-8

import Meta.Tools as Tools

def 播放动画(master, output):
    sort = ["名字", "过渡", "是否百分比"]

    defs = {
        "过渡" : "0.1f",
        "是否百分比" : "false"
    }

    fmt = "Behavior.MetaRoleAnim(self, \"{0}\", {1}, {2});"
    Tools.BuildArgs(master, sort, defs, fmt, output)
