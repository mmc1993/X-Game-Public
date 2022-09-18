# coding=utf-8

import Meta.Tools as Tools

def 设置筛选参数(master, output):
    sort = ["范围", "标识"]

    defs = {
    }

    brance0 = master.Ins["范围"]
    brance0.Data = "Mathm.Quad.New({0})".format(brance0.Data.replace(" ", ", "))

    brance1 = master.Ins["标识"]
    brance1.Data = Tools.MapName(brance1.Data)

    fmt = "select.Area = {0};\n" \
        + "select.Flags = {1};"
    Tools.BuildArgs(master, sort, defs, fmt, output)

