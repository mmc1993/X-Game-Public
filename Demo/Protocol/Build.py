# -- coding: utf-8 --
import os
import sys

# EnumPath = "..\\Client\\Assets\\Src\\Game\\Enum.cs"
# CSOutput = "..\\Client\\Assets\\Src\\Game\\Protocol"
EnumPath = "..\\Server\\Src\\Enum.cs"
CSOutput = "..\\Server\\Src\\Protocol"
PBCmd = "{0} --proto_path=In --csharp_out=Out "
PBGen = "..\\Tools\\ProtoBuf\\protogen.exe"
PBCmd = str.format(PBCmd, PBGen)

def GenPID(prefix, path, out):
    with open(path, encoding = "UTF-8") as f:
    # with open(path) as f:
        for line in f.readlines():
            if line.startswith(prefix):
                pbeg = len(prefix)
                pend = len(prefix) + 4
                pid = line[pbeg: pend]

                pbeg = pend + 2
                pend = line.find(",", pbeg)
                key = line[pbeg: pend]

                pbeg = pend + 2
                pend = len(line)
                tip = line[pbeg: pend-1]

                out.append((pid, key, tip))
    return out

def GenPIDs():
    status, after, befor, content = 0, [], [], []
    with open(EnumPath, encoding = "UTF-8") as f:
    # with open(EnumPath) as f:
        for line in f.readlines():
            if   line.startswith("//--- Beg Proto"):
                status = 1
                after.append(line)
            elif line.startswith("//--- End Proto"):
                status = 2

            if   status == 0:
                after.append(line)
            elif status == 2:
                befor.append(line)

    req = GenPID("//  req pid: ", "In\\req.proto", [])
    rsp = GenPID("//  rsp pid: ", "In\\rsp.proto", [])
    for ret in req:
        content.append(str.format("        k{0} = {1}, // {2}", ret[1], ret[0], ret[2]))
    for ret in rsp:
        content.append(str.format("        k{0} = {1}, // {2}", ret[1], ret[0], ret[2]))

    data = str.format("{0}{1}{2}", "".join(after), "\n".join(content) + "\n", "".join(befor))

    with open(EnumPath, "w", encoding = "UTF-8") as f:
    # with open(EnumPath, "w") as f:
        f.write(data)

def Build():
    cmd = PBCmd + "share.proto"
    os.system(cmd)
    cmd = PBCmd + "rsp.proto"
    os.system(cmd)
    cmd = PBCmd + "req.proto"
    os.system(cmd)

    cmd = str.format("xcopy /Y Out\* {0}", CSOutput)
    os.system(cmd)

    GenPIDs()

if __name__ == "__main__":
    # global EnumPath
    # global CSOutput
    EnumPath = "..\\Client\\Assets\\Src\\Const.cs"
    CSOutput = "..\\Client\\Assets\\Src\\Protocol"
    Build()
    EnumPath = "..\\ServerRoom\\Src\\Const.cs"
    CSOutput = "..\\ServerRoom\\Src\\Protocol"
    Build()
    EnumPath = "..\\ServerGame\\Src\\Const.cs"
    CSOutput = "..\\ServerGame\\Src\\Protocol"
    Build()
    input("end...")

