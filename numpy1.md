

```python
import numpy as np
```


```python
x = [100,200,300,400]
```


```python
x
```




    [100, 200, 300, 400]




```python
y = np.array(x)
y
```




    array([100, 200, 300, 400])




```python
type(x)
```




    list




```python
type(y)
```




    numpy.ndarray




```python
x + x
```




    [100, 200, 300, 400, 100, 200, 300, 400]




```python
x * 2
```




    [100, 200, 300, 400, 100, 200, 300, 400]




```python
x * 4
```




    [100,
     200,
     300,
     400,
     100,
     200,
     300,
     400,
     100,
     200,
     300,
     400,
     100,
     200,
     300,
     400]




```python
y + y
```




    array([200, 400, 600, 800])




```python
y * 3
```




    array([ 300,  600,  900, 1200])



# Subsetting and Slicing 


```python
y
```




    array([100, 200, 300, 400])




```python
y[3]
```




    400




```python
y[0:3]
```




    array([100, 200, 300])




```python
y[:3]
```




    array([100, 200, 300])



# Logical Indexing


```python
y
```




    array([100, 200, 300, 400])




```python
y > 200
```




    array([False, False,  True,  True])




```python
y == 300
```




    array([False, False,  True, False])




```python
y != 200 
```




    array([ True, False,  True,  True])




```python
y[y > 200]
```




    array([300, 400])




```python
y[y != 300]
```




    array([100, 200, 400])




```python

```
