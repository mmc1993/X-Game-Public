# coding=utf-8

#   描述: xlsx输出json
#   作者: mmc
#   日期: 2020-03-21

import os
import sys
import tojson
import gen_struct_cpp
import gen_struct_cshap

#   Json输入目录
# JSON_I = os.getcwd() + "/in/"
JSON_I = os.getcwd() + "/"
#   Json输出目录
# JSON_O = os.getcwd() + "/out/"
JSON_O = os.getcwd() + "/../Client/Assets/Res/Config/"
#   结构化输出目录
# STRUCT_O = os.getcwd() + "/out/config.cs"
STRUCT_O = os.getcwd() + "/../Client/Assets/Src/Config.cs"
#   命名空间
NAMESPACE = "Config"

def Write(url, data):
    with open(url, "w", encoding = "utf-8") as f:
        f.write(data)

def Export():
    json_collect = []
    unit_collect = []
    for name in os.listdir(JSON_I):
        split = os.path.splitext(name)
        if split[1] == ".xlsx" and split[0][0] != "~":
            output_json, parse_funcs = tojson.ToJson(JSON_I + name)
            json_collect.append((split[0], output_json))
            unit_collect.append((split[0], parse_funcs))

    #   写入Json
    try: os.rmdir(JSON_O)
    except: pass
    try: os.mkdir(JSON_O)
    except: pass
    for info in json_collect:
        Write(JSON_O + info[0] + ".json", info[1])

    #   写入C#
    out_struct = gen_struct_cshap.Gen(NAMESPACE, unit_collect)
    # out_struct = gen_struct_cpp.Gen(NAMESPACE, unit_collect)
    Write(STRUCT_O, out_struct)

if __name__ == "__main__":
    try:
        Export()
    except AssertionError as e:
        print("> 异常: %s" % e)
    print("> ---Export End---")

