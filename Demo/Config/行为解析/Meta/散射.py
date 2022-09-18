# coding=utf-8

import Meta.Tools as Tools

def 散射(master, output):
    sort = [ "fov", "特效", "次数", "间隔" ]

    defs = {
        "次数": "1",
        "间隔": "1"
    }

    fmt = "yield return Behavior.MetaFireFan(attack, {0}, config.ID * 10 + {1}, {2}, {3});"
    Tools.BuildArgs(master, sort, defs, fmt, output)
