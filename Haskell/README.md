### Haskell 学习笔记
***
#### 一： 安装

```
apt-get install ghc
```

#### 二： 基本操作

##### 1.进入交互模式

```
➜  ~  ghci
GHCi, version 7.6.3: http://www.haskell.org/ghc/  :? for help
Loading package ghc-prim ... linking ... done.
Loading package integer-gmp ... linking ... done.
Loading package base ... linking ... done.
Prelude> 
显示帮助信息":?"
```

##### 2.基本算术和逻辑运算

```
Prelude> 1024 + 233
1257
Prelude> False || True
True
Prelude> False && True
False

# Haskell 中的不等于是"/="而不是"！="
Prelude> 3 == 3
True
Prelude> 3 /= 3
False
```

##### 3.调用函数

```
在Haskell中函数又分为中缀函数(如乘法运算*)和前缀函数(占大部分)。
```

```
# 取 1024的后续(1025) 减去 100和125中的最大数 在加 233
Prelude> (succ 1024) - (max 100 125) + 233
1133

```

##### 4.函数操作

```
可使用:l filename.hs将文件filename中的函数装载进GHCi(需同级目录)
```

```
➜  Haskell git:(master) ✗ cat haskell.hs 
doubleMe x = x + x

doubleUs x y = x * 2 + y * 2

doubleSmallNumber x = if x > 100
                        then x
                        else x * 2

doubleSmallNumber' x = (if x > 100 then x else x*2) + 1

conanO'Brien = "This is String test ', Haskell"

```

```
➜  Haskell git:(master) ✗ ghci
GHCi, version 7.6.3: http://www.haskell.org/ghc/  :? for help
Loading package ghc-prim ... linking ... done.
Loading package integer-gmp ... linking ... done.
Loading package base ... linking ... done.
Prelude> :l haskell.hs 
[1 of 1] Compiling Main             ( haskell.hs, interpreted )
Ok, modules loaded: Main.
*Main> conanO'Brien
"This is String test ', Haskell"

```

##### 5.列表操作

```
# 定义列表
*Main> let list_ = [1,3,4,5,6]
*Main> list_
[1,3,4,5,6]

# 列表拼接
*Main> [1,2,3] ++ [33,44,66]
[1,2,3,33,44,66]
*Main> 'I' : " LOVE Haskell."
"I LOVE Haskell."

# 访问列表中的元素
*Main> "Hello World." !! 4
'o'

# 判断一个元素是否在列表中
Prelude> "hello" `elem` ["hello", "world"]
True
Prelude> "Haskell" `elem` ["hello", "world"]
False

# 比较列表(若第一位相同，则比较下一位)
*Main> [3, 4, 5] > [3, 1, 6]
True

# 返回第一个元素(取反则是tail)
Prelude> head [1, 3, 5, 7]
1

# 返回最后一个元素(取反则是init)
Prelude> last [1, 3, 5, 7]
7

# 返回列表长度
Prelude> length  [1, 3, 5, 7]
4

# 判断列表是否为空
Prelude> null [1, 3, 5, 7]
False
Prelude> null []
True

# 反转列表
Prelude> reverse  [1, 3, 5, 7]
[7,5,3,1]

# 返回指定长度的列表元素
Prelude> take 2 [7,5,3,1]
[7,5]

# 删除指定长度的列表元素
Prelude> drop 2 [7,5,3,1]
[3,1]

# 返回列表中最大元素(最小则是minimum)
Prelude> maximum  [7,5,3,1]
7
Prelude> maximum ['h', 'u', 'a']
'u'

# 返回列表中所有元素之和(求所有元素之积则是product)--只适用于元素均为实数的列表
Prelude> sum  [7,5,3,1]
16
Prelude> product [7,5,3,1]
105

```