# MUNDO AL DIA con Django y Faker

![Imagen django](https://img.channelpartner.es/wp-content/uploads/2022/05/14082803/27888_28.jpg.webp)

El **Proyecto de Noticias Interactivo** es una plataforma web desarrollada con Django que permite a los usuarios leer, publicar y comentar noticias y artículos de manera interactiva y eficiente.

## Características Destacadas

- **Gestión de Noticias**: Los usuarios pueden ver noticias y artículos existentes, así como también publicar nuevas noticias.
- **Interfaz de Usuario Intuitiva**: Diseñada con atención al detalle para proporcionar una experiencia de usuario intuitiva y agradable.
- **Comentarios en Noticias**: Los usuarios pueden comentar en las noticias y participar en la discusión.
- **Base de Datos Robusta**: Utiliza MySQL como base de datos para garantizar una gestión eficiente y segura de los datos.

## Tecnologías Utilizadas

- **Django**: Framework web de Python que proporciona una base sólida para el desarrollo de aplicaciones web.
- **HTML y CSS**: Utilizados para diseñar y estilizar la interfaz de usuario, proporcionando una experiencia de usuario atractiva.
- **MySQL**: Base de datos relacional utilizada para almacenar noticias, artículos y comentarios, garantizando la integridad de los datos y un rendimiento óptimo.

## Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/Bemontx/WebNotice.git


cd proyecto-noticias-interactivo

pip install -r requirements.txt

```

## Configuración del Proyecto

Configura la base de datos en el archivo settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nombre_basedatos',
        'USER': 'usuario',
        'PASSWORD': 'contraseña',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

Ejecuta las migraciones:

```bash
python manage.py migrate
```

Inicia el servidor de desarrollo:
```bash
python manage.py runserver
```

### Contribución

¡Se anima a cualquier contribución al proyecto! Si deseas mejorar la funcionalidad, corregir errores o agregar nuevas características, por favor no dudes en enviar una solicitud de extracción. Todas las contribuciones serán revisadas y consideradas.
