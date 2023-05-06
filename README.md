# Consulta de UF

Este es un programa simple que consulta el valor de la UF (Unidad de Fomento) para una fecha dada, utilizando la página web del Servicio de Impuestos Internos de Chile para obtener el valor de la UF de una fecha específica.

## Requisitos

Para ejecutar este programa, es necesario tener instalado Python 3.11 y las siguientes bibliotecas:

- requests
- beautifulsoup4
- flask
- pytest (solo necesario para ejecutar las pruebas unitarias)

Puede instalar estas bibliotecas ejecutando el siguiente comando en su terminal:

```
pip install -r requirements.txt
```

También puede crear un entorno virtual antes de instalar las bibliotecas.

## Ejecución

Para ejecutar el programa, simplemente ejecute el archivo app.py. Luego, abra su navegador y vaya a http://localhost:5000/uf/YYYY-MM-DD, donde YYYY-MM-DD es la fecha para la que desea consultar el valor de la UF.

Si se encuentra el valor de la UF para la fecha especificada, se mostrará el valor de la UF y la fecha. Si no se encuentra el valor de la UF para la fecha especificada, se mostrará un mensaje de error.

## Pruebas

El archivo test_app.py contiene pruebas unitarias para el programa. Para ejecutar las pruebas, simplemente ejecute el siguiente comando en su terminal mientras el programa está en ejecución:

```
pytest
```

Si todas las pruebas pasan, debería ver una salida similar a la siguiente:

```
============================= test session starts =============================
platform win32 -- Python 3.11.2, pytest-7.3.1, pluggy-1.0.0
rootdir: C:\path/to/project/directory           
collected 6 items

test_app.py ......                                                                                                                                                                       [100%]

============================== 6 passed in 3.42s =============================

```

## Contribución

Las contribuciones son bienvenidas. Si desea contribuir a este proyecto, por favor, cree un Pull Request en este repositorio.

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo LICENSE para más detalles.
