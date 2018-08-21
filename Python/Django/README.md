# Django

### Django Shell

```
python manage.py shell
```

#### Using Django Shell

```python
>>> from profiles.models import Profile
>>> p = Profile(name="Ada", email="ada@lovelace.com", phone="10121815")
>>>
>>> # save
>>> p.save()
>>> p_found = Profile.objects.get(id=2)
>>> p_found.name
u'Ada'
>>> p.id
2
>>> p_found.name = "Ada Lovelace"
>>>
>>> # apply changes
>>> p_found.save()
>>> p_found_again = Profile.objects.get(id=2)
>>> p_found_again.name
u'Ada Lovelace'
>>>
>>> # searching by name
>>> p_search = Profile.objects.get(name="Alan Turing")
>>> p_search.name
u'Alan Turing'
>>> p_search.id
1
>>> # searching by name and phone
>>> p = Profile.objects.get(name="Ada Lovelace", phone="10121815")
>>> p.name
u'Ada Lovelace'
>>>
>>> # delete
>>> p.delete()
>>>
>>> # filtering
>>> profiles = Profile.objects.filter(name__contains="a")
>>> for p in profiles:
...     print(p.name)
...
Alan Turing
Ada Lovelace
>>> # Other filtering options:
>>> # icontains (Case-insensitive)
>>> # startswith
>>> profiles = Profile.objects.filter(name__startswith="Alan")
>>> for p in profiles:
...     print(p.name)
...
Alan Turing
>>>
```

### Run Server

```
python manage.py runserver
```

### Creates a new App

```
python manage.py startapp XXXX
```

### Creating Database

```
python manage.py migrate
```

*O comando python migrate é o responsável em efetivar as alterações geradas pelo makemigrations.*

### Propagates changes of models into the database

```
python manage.py makemigrations
```
*O comando makemigrations é a forma utilizada pelo Django para propagar as mudanças em nosso modelo no esquema do banco de dados.*

#### Existem 3 comandos para lidar com as Migrations no mundo Django:

1. migrate -> Executar as Migrations que ainda não foram executadas;

2. makemigration -> Usada para gerar uma Migration a partir das modificações no modelos;

3. sqlmigrate -> Exibir o SQL que será gerado por uma Migration;