# coding=utf-8

import Meta.Tools as Tools

def 子弹(master, output):
    sort = [ "范围", "命中特效", "抛物高度", "飞行伤害" ]
    defs = {
        "抛物高度": 1,
        "飞行伤害": "true"
    }

    fmt = "yield return Behavior.MetaBullet(self, Mathm.Quad.New({0}), config.ID + {1}, {2}, {3});"
    Tools.BuildArgs(master, sort, defs, fmt, output)
