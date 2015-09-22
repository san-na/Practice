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