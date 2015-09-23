### 类型
***

#### 1.声明类型

```
Prelude> :t True
True :: Bool
Prelude> :t "Hello, Haskell."
"Hello, Haskell." :: [Char]
Prelude> :t ('A', 123, ["Github"])
('A', 123, ["Github"]) :: Num t => (Char, t, [[Char]])

Prelude> :l type_.hs 
[1 of 1] Compiling Main             ( type_.hs, interpreted )
Ok, modules loaded: Main.
*Main> addThree 1 2 3
6
```

#### 2.常见类型

```
# 整数
Int 	有界
Integer 无界

# 单精度浮点数 
Float

# 双精度浮点数
Double

# 布尔值
Bool

# 元组

# Char
```

#### 3.类型变量

*使用了类型变量的函数叫做多态函数*

```
Prelude> :t succ
succ :: Enum a => a -> a
```