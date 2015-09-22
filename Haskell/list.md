### 列表操作
***

#### 1.定义列表

```
*Main> let list_ = [1,3,4,5,6]
*Main> list_
[1,3,4,5,6]
```

#### 2.列表拼接

```
*Main> [1,2,3] ++ [33,44,66]
[1,2,3,33,44,66]
*Main> 'I' : " LOVE Haskell."
"I LOVE Haskell."
```

#### 3.访问列表中的元素

```
*Main> "Hello World." !! 4
'o'
```

#### 4.判断一个元素是否在列表中

```
Prelude> "hello" `elem` ["hello", "world"]
True
Prelude> "Haskell" `elem` ["hello", "world"]
False
```

#### 5.比较列表(若第一位相同，则比较下一位)

```
*Main> [3, 4, 5] > [3, 1, 6]
True
```

#### 6.返回第一个元素(取反则是tail)

```
Prelude> head [1, 3, 5, 7]
1
```

#### 7.返回最后一个元素(取反则是init)

```
Prelude> last [1, 3, 5, 7]
7
```

#### 8.返回列表长度

```
Prelude> length  [1, 3, 5, 7]
4
```

#### 9.判断列表是否为空

```
Prelude> null [1, 3, 5, 7]
False
Prelude> null []
True
```

#### 10.反转列表

```
Prelude> reverse  [1, 3, 5, 7]
[7,5,3,1]
```

#### 11.返回指定长度的列表元素

```
Prelude> take 2 [7,5,3,1]
[7,5]
```

#### 12.删除指定长度的列表元素

```
Prelude> drop 2 [7,5,3,1]
[3,1]
```

#### 13.返回列表中最大元素(最小则是minimum)

```
Prelude> maximum  [7,5,3,1]
7
Prelude> maximum ['h', 'u', 'a']
'u'
```

#### 14.返回列表中元素之和(积则是product)

*仅用于元素均为实数的列表*

```
Prelude> sum  [7,5,3,1]
16
Prelude> product [7,5,3,1]
105
```

#### 15.德州区间

*区间是构造列表的方法之一，但其值必须是可枚举(可排序)的*

```
Prelude> [1..5]
[1,2,3,4,5]
Prelude> ['a'..'z']
"abcdefghijklmnopqrstuvwxyz"
Prelude> ['a', 'c'..'z']
"acegikmoqsuwy"

Prelude> [3, 6..10*3]
[3,6,9,12,15,18,21,24,27,30]
Prelude> take 10 [3, 6..]
[3,6,9,12,15,18,21,24,27,30]
```

##### cycle函数接受一个列表作为参数并返回一个无限列表

```
Prelude> take 7 (cycle [1,2])
[1,2,1,2,1,2,1]
```

##### repeat函数接受一个值作为参数，返回一个仅包含该值的无限列表

```
Prelude> take 7 (repeat 7)
[7,7,7,7,7,7,7]

# 另外一种replicate
Prelude> replicate 6 7
[7,7,7,7,7,7]
```

#### 16.列表推导

*一种过滤/转换或者组合列表的方法*

```
Prelude> [x + 2 | x <- [1..10]]
[3,4,5,6,7,8,9,10,11,12]
Prelude> [x + 2 | x <- [1..10], x >= 5]
[7,8,9,10,11,12]
```