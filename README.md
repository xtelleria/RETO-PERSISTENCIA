# RETO-PERSISTENCIA
## EXPLICACIÓN DE LOS PASOS SEGUIDOS
Para llevar a cabo este proyecto, pasé por varios pasos. Inicialmente, tuve dudas sobre qué aplicación utilizar, pero luego el profesor nos presentó la plataforma InfluxDB, que me pareció perfecta para este proyecto. Comencé siguiendo un tutorial para familiarizarme con la plataforma.

Al principio, intenté pasar un solo dato utilizando un nombre de usuario y contraseña, pero no logré que funcionara como esperaba. En cambio, opté por seguir el tutorial y utilizar un token para la autenticación, lo cual resultó mucho más sencillo y efectivo.

Después de establecer la conexión correctamente, procedí a cargar todos los datos del dataset en la base de datos de InfluxDB. Esto implicó asegurarme de que los datos estuvieran formateados correctamente y que se insertaran con las marcas de tiempo adecuadas.

Una vez que todos los datos estuvieron en la base de datos, decidí calcular la media de cada columna como una demostración de las capacidades analíticas de InfluxDB. Esto me permitió realizar consultas sobre los datos almacenados y obtener estadísticas útiles.
## INSTRUCCIONES DE USO
docker-compose up -d

python3 turbina_viento.py

Añadir la media: SCRIPT EDITOR -> |>mean()
## POSIBLES VIAS DE MEJORA

Para mejorar aún más mi proyecto, consideraría las siguientes sugerencias:

1. Automatización de la media: En lugar de calcular manualmente la media, podría automatizar este proceso mediante scripts o consultas programadas en InfluxDB. Por ejemplo, podría escribir un script que ejecute consultas de InfluxDB para calcular y almacenar automáticamente las medias de las columnas relevantes en intervalos regulares.
2. Control de las funcionalidades de InfluxDB: Es importante tener un mejor control y comprensión de las funcionalidades que ofrece InfluxDB para aprovechar al máximo su potencial. Esto podría implicar estudiar la documentación oficial de InfluxDB.

## RETOS ENCONTRADOS
Al avanzar en mi proyecto, me encontré con algunos desafíos:

1. Error 401 - Problemas de autenticación: Me enfrenté a este error al intentar pasar datos con usuario y contraseña en InfluxDB. Afortunadamente, pude resolver este problema al cambiar a la autenticación mediante token, lo que resultó ser más efectivo y me permitió avanzar con el proyecto.
2. Añadir la media: Una vez que logré cargar los datos en la base de datos, me propuse calcular la media de cada columna. Sin embargo, esta tarea resultó más compleja de lo que esperaba. Tuve dificultades para automatizar este proceso y terminé calculando manualmente las medias. Para mejorar, necesitaré encontrar una manera de automatizar este cálculo, posiblemente explorando funciones y scripts avanzados en InfluxDB.

## ALTERNATIVAS POSIBLES
Explorar alternativas como MongoDB y MySQL para gestionar los datos de una turbina de viento puede ser una excelente idea según las necesidades específicas del proyecto. Aquí hay algunas consideraciones sobre cómo estas opciones podrían adaptarse al caso:

1. MongoDB: Si la estructura de los datos es flexible y no está completamente definida de antemano, MongoDB podría ser una opción sólida. MongoDB es una base de datos NoSQL que utiliza un formato de documento flexible similar a JSON, lo que permite almacenar datos con diferentes estructuras sin necesidad de un esquema fijo. Esto puede ser beneficioso si los datos de la turbina de viento tienen diferentes campos o características que pueden variar con el tiempo. Además, MongoDB es escalable y puede manejar grandes volúmenes de datos, lo que lo hace adecuado para aplicaciones que requieren almacenamiento y procesamiento de datos a gran escala.
2. MySQL: Si los datos tienen una estructura más definida y se ajustan bien a un esquema relacional, MySQL podría ser una opción más adecuada. MySQL es una base de datos relacional que utiliza tablas con filas y columnas, lo que puede ser más apropiado si los datos de la turbina de viento tienen una estructura tabular clara y relaciones entre diferentes conjuntos de datos. MySQL es conocido por su estabilidad, robustez y rendimiento, lo que lo hace una opción popular para una amplia gama de aplicaciones.

### Autor: Xabier Telleria
