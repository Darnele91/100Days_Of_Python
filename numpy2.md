

```python
import numpy as np
```


```python
x = [list(range(0,6)),list(range(10,16)),list(range(20,26))]
```


```python
x
```




    [[0, 1, 2, 3, 4, 5], [10, 11, 12, 13, 14, 15], [20, 21, 22, 23, 24, 25]]




```python
xnp = np.array(x)
xnp
```




    array([[ 0,  1,  2,  3,  4,  5],
           [10, 11, 12, 13, 14, 15],
           [20, 21, 22, 23, 24, 25]])



# Indexing


```python
x[0]
```




    [0, 1, 2, 3, 4, 5]




```python
x[0][1]
```




    1




```python
x[0][-1]
```




    5




```python
xnp[0][1]
```




    1




```python
xnp[0, -1]
```




    5



# Slicing


```python
x[0:2]
```




    [[0, 1, 2, 3, 4, 5], [10, 11, 12, 13, 14, 15]]




```python
xnp
```




    array([[ 0,  1,  2,  3,  4,  5],
           [10, 11, 12, 13, 14, 15],
           [20, 21, 22, 23, 24, 25]])




```python
xnp[0:2, 1:4]
```




    array([[ 1,  2,  3],
           [11, 12, 13]])




```python
xnp[1, 3:5]
```




    array([13, 14])



# Logical Indexing


```python
xnp
```




    array([[ 0,  1,  2,  3,  4,  5],
           [10, 11, 12, 13, 14, 15],
           [20, 21, 22, 23, 24, 25]])




```python
xnp > 10
```




    array([[False, False, False, False, False, False],
           [False,  True,  True,  True,  True,  True],
           [ True,  True,  True,  True,  True,  True]])




```python
xnp[xnp>10]
```




    array([11, 12, 13, 14, 15, 20, 21, 22, 23, 24, 25])




```python
xnp[:, 2]
```




    array([ 2, 12, 22])




```python
xnp[:, 2] > 10
```




    array([False,  True,  True])




```python
xnp[2]
```




    array([20, 21, 22, 23, 24, 25])




```python

```
