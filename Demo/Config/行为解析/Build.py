# coding=utf-8
import enum
import os
import re
import sys

Meta = {}

def Check(cond, tips):
    if not cond: raise ValueError(tips)

def GetLineOrEnds(line, ends):
    pos = line.find(ends)
    return line[: pos]

#   提取元方法和名字
#   Name|Meta["Meta"]
def GetMetaOrName(buff):
    name = re.search("^[^\\[]+", buff)
    meta = re.search("\[(.+)\]", buff)
    if meta == None:
        return (name.group(0),)
    else:
        return (name.group(0), meta.group(1))

class BranceNode:
    def __init__(self, raw):
        split = self.Split(raw)
        self.Port = split[1]
        self.Link = split[2]

        ret = GetMetaOrName(split[0])
        if len(ret) == 2:
            self.Name = ret[0]
            self.Data = ret[1]
        else:
            self.Name = ret[0]
            self.Data = ret[0]

    def Split(self, raw):
        return re.search("(.+) --(.+)--> (.+)", raw).groups()

class MasterNode:
    def __init__(self, raw):
        ret = GetMetaOrName(raw)
        if len(ret) == 2:
            self.Name = ret[0]
            self.Meta = ret[1]
        else:
            self.Name = ret[0]
            self.Meta = ret[0]
        self.Ins = {}

class Contex:
    def __init__(self, meta, desc):
        self.Meta = meta
        self.Desc = desc
        self.Nodes = []

    def Find(self, name):
        for _, v in enumerate(self.Nodes):
            if v.Name == name: return v

    def Init(self, lines, cur):
        Check(lines[cur].startswith("```mermaid"), "没有mermaid"); cur += 1
        Check(lines[cur].startswith("graph TD"), "没有graph TD"); cur += 1

        #   开始解析主干
        while lines[cur] != "\n":
            raw = GetLineOrEnds(lines[cur], " ==>")
            self.Nodes.append(MasterNode(raw))
            cur = cur + 1
        cur = cur + 1

        while lines[cur] != "```\n":
            brance = BranceNode(lines[cur])
            master = self.Find(brance.Link)
            master.Ins[brance.Port] = brance
            cur = cur + 1
        cur = cur + 2

        return cur

    def ToCode(self, metas):
        buffer = []
        for i, v in enumerate(self.Nodes):
            buffer.append("// {0}: {1}".format(i, v.Name))
            metas[v.Meta](v, buffer)
        return "\n".join(buffer)

class Parser:
    def __init__(self, lines):
        self.Ctxs = []

        cur = 2
        self.Name = lines[0][2:-1]
        while cur <= len(lines):
            cur = self.Init(lines, cur)

    def Init(self, lines, cur):
        ctx = Contex(lines[cur + 1][len("* 方法: "):-1], \
                     lines[cur + 2][len("* 描述: "):-1])
        cur = ctx.Init(lines, cur + 3)
        self.Ctxs.append(ctx)
        return cur

    def ToCode(self, metas):
        buffer = []
        buffer.append("using System;")
        buffer.append("using System.Collections;")
        buffer.append("using System.Collections.Generic;")
        buffer.append("using UnityEngine;")
        buffer.append("\nnamespace mmc.Game.行为描述 {")
        buffer.append("public class {0}{{".format(self.Name))

        for _, ctx in enumerate(self.Ctxs):
            output = []
            output.append(("public static IEnumerator %s" % ctx.Meta)
                        + "(Actor actor, Config.Behavior config){")
            output.append(ctx.ToCode(metas))
            output.append("}")
            buffer.append("\n".join(output))

        buffer.append("}}")
        return "\n".join(buffer)

def LoadMetas():
    metas = {}
    for _, path in enumerate(os.listdir("Meta")):
        prefix, suffix = os.path.splitext(path)
        if suffix != ".py": continue

        a = __import__("Meta." + prefix)
        b = getattr(a, prefix)
        c = getattr(b, prefix)
        metas[prefix] = c
    return metas

def Main(ipath, opath):
    lines = None
    with open(ipath, encoding = "UTF-8") as f:
        lines = f.readlines()

    parser = Parser(lines)
    code = parser.ToCode(LoadMetas())

    with open(opath, "w", encoding = "UTF-8") as f:
        f.write(code)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        Main("In/骷髅兵.md", "Out/骷髅兵.cs")
    else:
        Main(sys.argv[1], sys.argv[2])