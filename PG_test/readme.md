# Documentación Django Rest API
## Rutas expuestas:
1.  professor/
2.  student/
3.  score/

# CRUD.
La estructura de request y response de los siguientes servicios respetan los mismos formatos:
 - professor/
 - student/
 - 
### Creación (POST):
Request body:
```json
			{
				"name":"professorOne"
			}
```
Response body:
```json
			{  
				"response":  "ok",  
				"message":  "result set"  			
			}
``` 
### Consulta (GET):
Enviar petición GET a la url ***"http://localhost:8000/professor/"***, retornara la lista de todas las marcas creadas.
Response body
```json
	[  
		{  
			"id":  3,  
			"name":  "Oscar"  
		},  
		{  
			"id":  4,  
			"name":  "Miguel"  
		},  
		{  
			"id":  5,  
			"name":  "professorOne"  
		}  
	]
``` 
#### Nota: 
Agregando a la URL los parametros ***name= ?*** o ***id= ?***, el servicio retornara el conjunto de resultados que coincidan con el valor del parámetro correspondiente.
Si ademas se agrega el parámetro ***ordering=name*** o ***ordering=id***, el servicio retornara el conjunto de resultados ordenados por atributo seleccionado

***"http://localhost:8000/professor/?name=professorOne&ordering=id"***
***"http://localhost:8000/professor/?id=5"***

   
### Actualización(PUT):
Request body
```json
		{
            "id": 5,
            "name": "ProfessorOne_Updated"
		 }
```
Response body
```json
		{  
			"response":  "ok",  
			"message":  "professor updated id: 5, name: ProfessorOne Updated"  
		}
```
### Borrado(Delete):
Request a la url donde se envíe como parámetro el id del registro que se desea eliminar.
***http://localhost:8000/professor/?id=5***  
Response body
```json
		{  
			"response":  "ok",  
			"message":  "erased 5"  
		}

```

## CRUD Score

### POST
Request body
```json
	{
	    "name": "ScoreOne",
	    "value": 4.5,
	    "student":9,
	    "professor":4
	}
```
Response body
```json
	{  
		"response":  "ok",  
		"message":  "score created"  
	}
```

### GET
Request body
```json
http://localhost:8000/score/
```
#### Nota
De igual manera se puede aplicar los filtros y orden por cualquiera de los campos de un registro score.

Response body
```json
	[  
		{  "id":  6,  
			"name":  "score_two",  
			"value":  6.8,  
			"professor":  {  
							"id":  3,  
							"name":  "Oscar"  
							},  
			"student":  {  
							"id":  4,  
							"name":  "Mafe"  
						}  
		},  
		{  
			"id":  9,  
			"name":  "ScoreOne",  
			"value":  4.5,  
			"professor":  {  
							"id":  4,  
							"name":  "Miguel"  
							},  
			"student":  {  
							"id":  9,  
							"name":  "Felipe"  
						}  
		}  
	]
```

### PUT
Request body
```json
	{
	    "id":9,
	    "name": "ScoreOne updated",
	    "value": 0.0,
	    "professor":3,
	    "student":4
	}
```
Response body
```json
	{  
		"response":  "ok",  
		"message":  "score updated"  
	}
```

### DELETE
Request body
```json
	http://localhost:8000/score/?id=9
```
Response body
```json
	{  
		"response":  "ok",  
		"message":  "erased"  
	}
```
