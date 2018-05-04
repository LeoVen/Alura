# MongoDB

## Install

* Baixar o instalador para Windows (Windows Server 2008 em diante);
* Instalar MongoDB e criar a pasta ```C:\data\db```;
* No prompt rodar ```mongod --bind_ip 127.0.0.1```.

Opcional:

* Colocar a basta ```bin``` em ```C:\Program Files\MongoDB\Server\{version}\bin``` no PATH do windows.

### Insert to a Collection

	db.{collectionName}.insert(
		"param1" : "value1",
		"param2" : "value2",
		"param3" : [
				{
					"param3-1-1" : "value3-1-1",
					"param3-1-2" : "value3-1-2"
				},
				{
					"param3-2-1" : "value3-2-1",
					"param3-2-2" : "value3-2-2"
				}
			]
		)

### Remove from a Collection

	db.{collectionName}.remove({"_id": ObjectId("578b87a7239a421f908ed46b")})

Example

	db.StudentList.remove({"_id": ObjectId("578b87a7239a421f908ed46b")})

### Search in a Collection

	db.{collectionName}.find()

Or better

	db.{collectionName}.find().pretty()

Example

	db.StudentList.find().pretty()

Finding by an object example

	db.{collectionName}.find(
		"param1" : "value1"
		)

Or when we have nested values

	db.{collectionName}.find(
		"param1.param1-2" : "value1-2"
		)

Multiple search parameters

	db.{collectionName}.find(
		"param1.param1-2" : "value1-2",
		"param2" : "value2"
		)

If a Key is declared twice only the last is considered. In this case, ```param1``` would be ```value2```.

	db.{collectionName}.find(
		"param1" : "value1",
		"param1" : "value2"
		)

### OR, AND, IN

[See documentation](https://docs.mongodb.com/manual/reference/operator/query-logical/)

### Update

		db.{collectionName}.update(
			{"conditional_param1" : "value1"},
			{
				{"param1" : "value1"}
			}
		)

This way the document is updated completely having only ```param1``` with ```value1``` as its content. To update only a single value use ```$set```

		db.{collectionName}.update(
			{"conditional_param1" : "value1"},
			{
				$set {
					"param1" : "value1"
				}
			}
		)

To update multiple lines use ```multi : true```

		db.{collectionName}.update(
			{"conditional_param1" : "value1"},
			{
				$set {
					"param1" : "value1"
				}
			}, {
				multi : true
			}
		)

To add more values to an array one by one (not the array itself)

	db.{collectionName}.update(
		{ "nome" : "Guilherme" },
		{
			$push : {
				"notas" : {
					$each:[8.5, 10]
				}
			}
		}
	)

[See documentation for more](https://docs.mongodb.com/manual/reference/operator/update/)

### More complex searches

Search for documents where either the enemy team or the home team has made 6 goals or more

```
db.WorldCupNorm.find(
	{ $and : [
			{ $or : [
				{"Home Team Goals" : { $gt : "6" }},
				{"Away Team Goals" : { $gt : "6" }}
				]
			},
			{"Year" : { $gt : "2000"}}
		]
	}
)
```

Sort by a parameter (1 is ascending and -1 is descending)

```
db.{collectionName}.find().sort({"keyName" : 1})
```

To limit the search (n documents)

```
db.{collectionName}.find().limit(n)
```

Ou também
```
db.{collectionName}.find().sort({"keyName" : 1}).limit(n)
```

### Agregar por Proximidade

Para importar no banco os dados

	mongoimport -d {databaseName} -c {collectionName} --jsonArray < file.json

Criar um index de busca

	db.{collectionName}.createIndex({
		localizacao : "2dsphere"
	})

Calcula os 4 pontos mais próximos (o primeiro é pulado ```$skip : 1```) de um ponto com coordenadas ```coordinates``` onde a distância é dada como uma esfera e a distância é escrita no campo ```distanceField : "distancia.calculada"```.

```
db.{collectionName}.aggregate([
{
	$geoNear : {
		near : {
			coordinates : [-23.5640265, -46.6527128],
			type : "Point"
		},
		distanceField : "distancia.calculada",
		spherical : true,
		num : 4
	}
},
{$skip : 1}
])
```

mongoimport -c DataScience --jsonArray < alunos.json