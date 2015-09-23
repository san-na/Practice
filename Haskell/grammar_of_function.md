### 函数的语法
***

#### 1.模式匹配

*如果一个函数的定义中调用了自身，那么它就被称为递归函数。*

```
Prelude> :l grammar_of_function.hs 
[1 of 1] Compiling Main             ( grammar_of_function.hs, interpreted )
*Main> factorial 0
1
*Main> factorial 10
3628800
```

#### 2.哨卫 && where?!

```
Prelude> :l grammar_of_function.hs
[1 of 1] Compiling Main             ( grammar_of_function.hs, interpreted )
Ok, modules loaded: Main.
*Main> bmiCalc 65 170
"underweight"
```

#### 3.let 和where

```
where允许我们再函数底部绑定变量，对包括所有哨卫在内的整个函数可见，
let则是个表达式，允许再任何位置定义局部变量；且不能对其他哨卫可见
```