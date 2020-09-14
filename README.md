# APIS-PROJECT
-----

# ![](https://www.agenciatelling.com/wp-content/uploads/2017/03/studio-ghibli-logo.jpg)


En este proyecto se unirá información de un csv con una api pública, para mejorar el contenido y obtener más información.

El dataset resultante muestra datos relativos a las diferentes peliculas del famoso estudio de animación japonesa *studio-ghibli*



![](https://i1.wp.com/www.sopitas.com/wp-content/uploads/2018/04/mi-vecino-totoro.jpg)

(El dataset se ha obtenido del siguiente enlace: [dataset](https://www.basedig.com/wikipedia/8010studio-ghibli-works-feature-works-170328/); y la api es la api publica de studio-ghibli: [API_ghibli](https://ghibliapi.herokuapp.com/#))

-----
## **Archivos**
Aqui, se encontrará el archivo [ghibli_clean](https://github.com/bmedm/apis-project/blob/master/studio_ghibli_clean.ipynb), donde se realiza la union y limpieza de los datos para conseguir un dataset final con la información deseada. 

![](https://img.ecartelera.com/noticias/fotos/34800/34809/1.jpg)

Ademas, en el archivo [main](https://github.com/bmedm/apis-project/blob/master/main.py), se podrá acceder a los datos deseados desde bash con los comandos indicados:

*   **-d** *(Nombre del director)*: Nos mostrará las diferentes peliculas del director elegido, con su puntuación y año de realización
    -  *'Hayao Miyazaki'*
    -  *'Isao Takahata'*
    -  *'Yoshifumi Kondō'*
    -  *'Hiroyuki Morita'*
    -  *'Gorō Miyazaki'*
    -  *'Hiromasa Yonebayashi'*
*  **-t** *(Título de la película)*: Devolverá los datos sobre la película indicada
    -  *'Castle in the Sky'*
    -  *'My Neighbor Totoro'*
    -  *'When Marnie Was There'*
    -  *'Pom Poko'*
    -  *'Howls Moving Castle'*
    -  *'The Tale of the Princess Kaguya'*
    -  *'Only Yesterday'*
    -  *'Porco Rosso'*
    -  *'Princess Mononoke'*
    -  *'Ponyo'*
    -  *'Grave of the Fireflies'*
    -  *'Arrietty','Whisper of the Heart'*
    -  *'The Wind Rises'*
    -  *'The Cat Returns'*
    -  *"Kiki's Delivery Service"*
    -  *'Tales from Earthsea'*
    -  *'From Up on Poppy Hill'*
    -  *'My Neighbors the Yamadas'*
    -  *'Spirited Away'*
*  **-s** *(Director)*: Devolverá la media de las puntuaciones de las películas realizadas por ese director.
    -  *'Hayao Miyazaki'*
    -  *'Isao Takahata'*
    -  *'Yoshifumi Kondō'*
    -  *'Hiroyuki Morita'*
    -  *'Gorō Miyazaki'*
    -  *'Hiromasa Yonebayashi'*

       ![](https://pa1.narvii.com/6282/db78e3549ae965c63e0673d67cf74c3a30f075ef_hq.gif)

 Por último, el archivo [ghibli-rate](https://github.com/bmedm/apis-project/blob/master/Ghibli-rate.ipynb) nos mostrará un pequeño resumen de los datos mediante gráficos para una sencilla visualización.
    
