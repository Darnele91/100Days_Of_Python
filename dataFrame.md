

```python
data = {"name": ["Linda", "Julie", "Ethan", "Luna", "Felix"],
       "gender": ["F", "NB","M", "F", "M"],
       "country": ["USA", "France", "UK", "Spain", "Dominican Republic"],
       "age": [22, 34, 50, 17, 25]}
```


```python
data
```




    {'name': ['Linda', 'Julie', 'Ethan', 'Luna', 'Felix'],
     'gender': ['F', 'NB', 'M', 'F', 'M'],
     'country': ['USA', 'France', 'UK', 'Spain', 'Dominican Republic'],
     'age': [22, 34, 50, 17, 25]}




```python
import pandas as pd
```


```python
df = pd.DataFrame(data)
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>gender</th>
      <th>country</th>
      <th>age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Linda</td>
      <td>F</td>
      <td>USA</td>
      <td>22</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Julie</td>
      <td>NB</td>
      <td>France</td>
      <td>34</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Ethan</td>
      <td>M</td>
      <td>UK</td>
      <td>50</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Luna</td>
      <td>F</td>
      <td>Spain</td>
      <td>17</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Felix</td>
      <td>M</td>
      <td>Dominican Republic</td>
      <td>25</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.columns
```




    Index(['name', 'gender', 'country', 'age'], dtype='object')




```python
df.index
```




    RangeIndex(start=0, stop=5, step=1)




```python
df.set_index('name', drop=True, inplace=True)
```


```python
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>gender</th>
      <th>country</th>
      <th>age</th>
    </tr>
    <tr>
      <th>name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Linda</th>
      <td>F</td>
      <td>USA</td>
      <td>22</td>
    </tr>
    <tr>
      <th>Julie</th>
      <td>NB</td>
      <td>France</td>
      <td>34</td>
    </tr>
    <tr>
      <th>Ethan</th>
      <td>M</td>
      <td>UK</td>
      <td>50</td>
    </tr>
    <tr>
      <th>Luna</th>
      <td>F</td>
      <td>Spain</td>
      <td>17</td>
    </tr>
    <tr>
      <th>Felix</th>
      <td>M</td>
      <td>Dominican Republic</td>
      <td>25</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.reset_index(drop=False, inplace=False)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>gender</th>
      <th>country</th>
      <th>age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Linda</td>
      <td>F</td>
      <td>USA</td>
      <td>22</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Julie</td>
      <td>NB</td>
      <td>France</td>
      <td>34</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Ethan</td>
      <td>M</td>
      <td>UK</td>
      <td>50</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Luna</td>
      <td>F</td>
      <td>Spain</td>
      <td>17</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Felix</td>
      <td>M</td>
      <td>Dominican Republic</td>
      <td>25</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
