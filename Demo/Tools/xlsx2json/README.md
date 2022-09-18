# Excel表格转Json数据结构

辗转了好几个项目，每个项目的导表工具都巨难用，速度慢，潜规则多，扩展性差，不易于调试。Sqlite，Json，Lua，Xml各种格式都用过。

举个例子：

> 大多数导表工具不支持文本数组的解析，因为它们对数组的解析算法异常粗暴，无非就是一个Split(value, ",")，当你的文本数组没有逗号时，一切都OK，一旦出现逗号，解析结果错误，但程序依旧正常运行，直到游戏中读取错误时，你才能意识到出问题了。
>
> 不能类型组合，通常这些导表工具都不支持类型之间的组合，例如整数数组，哈希数组等等。有的支持整数数组，但它并不是把整数和数组两个类型结合，而是单独定义了一个**整数数组**的类型，当需要稍微复杂一点的结构时，则不支持甚至完全不能实现，比如数组嵌套数组。
>
> 错误无法定位，输出的错误信息几乎没有看不懂，策划更是束手无策。
> 
> 没有类型安全，当配置表的某个字段名被修改时，程序可能完全不知道，直到游戏中读取配置错误。

### 数据结构

在数据结构上我个人最理想的数据格式是Json。

*Sqlite* 对客户端不友善，大多数客户端对SQL语句并不熟悉。作为配置数据而言，关系数据库的优势并不明显，如果数据查询需要复杂的SQL语句，这个数据结构设计本身就是错误的，如果仅使用简单的SQL语句查询，那为什么不直接用Key-Value数据结构？此外，Sqlite需要用专门的数据库软件浏览，而不能直接在IDE或者文本编辑器中查看。

*Lua* 结构跟Json类似，但它有两个问题，1. 不容易区分数组和哈希，2. 作为数据结构而言，应用范围比较狭窄，Json比Lua出名太多，Json第三方解析库比Lua多太多，以至于大家更容易接受Json而非Lua。

*Xml* 太多额外数据，阅读相对于Json不直观。

*Json* 结构简洁，大多数文本编辑器可高亮内容，第三方解析库众多，流行范围广，前后端都容易接受。

### 易用性

我见过一次导表开销花掉1小时的，以至于没有人敢轻易尝试导出Excel，这个情况持续了1年，终结这个情况的并不是项目凉了，而是我重新实现了一个工具且完全它的解析格式，新的解析程序导出全部Excel只需10秒。

我见过Excel配置非常繁琐，众多潜规则，当你新建一份配置表时，你必须参考一份旧表，要不然你根本不知道该怎么填。

### 一个好用的导表工具

由于最近重返手游行业，于是想实现一个效率，扩展性，易用性，安全性都比较OK的导表工具。

**格式** *(详情请看Demo)*
```C++
//  已支持的格式
bool        布尔值
number      数值
string      字符串
list        数组
dict        哈希
type        自定义结构

//  格式定义
bool b;
number n;
string s;
[number] n_list;                            //  数值数组    list<number> n_list;
{number} n_dict;                            //  数组哈希    dict<number> d_dict;
<number n, string s> type;                  //  自定义结构  struct {
                                            //                  number n;
                                            //                  string s;
                                            //              } type;

//  类型组合
[[number]]  n_n_list;                       //  数组嵌套数组
{[number]}  n_n_dict;                       //  哈希嵌套数组
<[number] n_list, {number} n_dict> type;    //  数据格式如下:
                                            //  struct {
                                            //      list<number> n_list;
                                            //      dict<number> n_dict;
                                            //  } type;
```

**错误定位** *(详情请看Demo)*
```C++
//  打印错误文件，行，列，出错原因
C:\Github\xlsx2json>export.py
> 异常: C:\Github\xlsx2json/in/cfg_2.xlsx | 5:2 | [bool]值错误 "
> ---Export End---
```

**安全性** *(详情请看Demo)*
```C#
//  输出指定语言的数据结构(当前只支持C++和C#)
//  可通过Json库解析到对应的数据结构
var test = Json.From<config.Test>("test.json");
var n = test.n;
var s = test.s;
```

### 结束

执行文件：export.py

运行环境：Python3.0

运行依赖：openpyxl

导表配置 (export.py文件)：
```python
#   Json输入目录
JSON_I = os.getcwd() + "/in/"
#   Json输出目录
JSON_O = os.getcwd() + "/out/"
#   结构化输出目录
STRUCT_O = os.getcwd() + "/out/config.cs"
#   命名空间
NAMESPACE = "config"
```