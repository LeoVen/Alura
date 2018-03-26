# Estatística em Python

```python
>>> import pandas
>>> df = pandas.DataFrame([1, 1, 50, 50, 50, 50, 50, 50, 50, 60, 60, 65, 70, 200, 250, 300, 700])
>>> df.mean()
121.0
>>> df.median()
50.0
>>> df.quantile() #moda
50.0
```