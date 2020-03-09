Python中列表和字典操作的大O性能

## 一、列表

1. 索引操作和分配索引位置操作，与列表长度无关，算法复杂度是：O(1)
2. 增加列表：append O(1)，拼接O(k)，k表示要拼接的列表的大小
3. 比较四种列表生成方式的算法复杂度

## 二、字典

  

| list内置操作的时间复杂度 |                                           |
| ------------------------ | ----------------------------------------- |
|                          |                                           |
|                          | Operation                Big-O Efficiency |
|                          | indexx[]		 O(1)                     |
|                          | index assignment 	 O(1)                |
|                          | append			 O(1)                   |
|                          | pop()			 O(1)                    |
|                          | pop(i)			 O(n)                   |
|                          | insert(i,item)		 O(n)               |
|                          | del operator		 O(n)                 |
|                          | iteration		 O(n)                    |
|                          | contains (in)		 O(n)                |
|                          | get slice [x:y]	 	 O(k)             |
|                          | del slice 		 O(n)                   |
|                          | set slice		 O(n+ k)                 |
|                          | reverse			 O(n)                  |
|                          | concatenate 		 O(k)                 |
|                          | sort                     O(n log n)       |
|                          | multiply                 O(nk)            |
|                          |                                           |
|                          |                                           |
| dict内置操作的时间复杂度 |                                           |
|                          |                                           |
|                          | Operation		 Big-O Efficiency        |
|                          | copy			 O(n)                     |
|                          | get item		 O(1)                     |
|                          | set item		 O(1)                     |
|                          | delete item		 O(1)                  |
|                          | contains (in)		 O(1)                |
|                          | iteration		 O(n)                    |