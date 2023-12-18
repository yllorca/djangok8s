## Docker Hub

Para realizar un "build" y "push" de una imagen de contenedor a Docker Hub, debes seguir varios pasos básicos. Aquí te guío a través del proceso:

1. **Crear una Cuenta en Docker Hub**:
   - Si aún no tienes una, crea una cuenta en [Docker Hub](https://hub.docker.com/).
   - Una vez creada la cuenta, puedes iniciar sesión en Docker Hub desde tu terminal usando `docker login`.

2. **Construir (Build) la Imagen de Docker Localmente**:
   - Asegúrate de tener un archivo `Dockerfile` en tu proyecto. Este archivo define cómo se construye tu imagen de Docker.
   - Construye la imagen con el comando `docker build`. Por ejemplo:
     ```bash
     docker build -t tu-usuario-dockerhub/nombre-imagen:tag .
     ```
     Aquí, `tu-usuario-dockerhub` es tu nombre de usuario en Docker Hub, `nombre-imagen` es el nombre que deseas dar a tu imagen, `tag` es una etiqueta para la versión de la imagen (como `latest` o `v1.0`), y el punto al final indica que el `Dockerfile` está en el directorio actual.

3. **Subir (Push) la Imagen a Docker Hub**:
   - Una vez que la imagen se ha construido con éxito, puedes subirla (push) a Docker Hub usando:
     ```bash
     docker push tu-usuario-dockerhub/nombre-imagen:tag
     ```
   - Este comando subirá la imagen construida a tu repositorio en Docker Hub.

4. **Verificar en Docker Hub**:
   - Después de subir la imagen, puedes ir a tu cuenta de Docker Hub en un navegador web y verificar que la imagen se muestra en tus repositorios.

5. **Consideraciones Adicionales**:
   - Asegúrate de que estás subiendo a un repositorio que has creado en Docker Hub o a uno al que tienes acceso.
   - Si estás trabajando con imágenes privadas, recuerda configurar la privacidad del repositorio en Docker Hub.
   - Para versiones de imagen, es una buena práctica usar etiquetas significativas en lugar de siempre usar `latest`.

Recuerda que cada vez que realices cambios significativos en tu imagen y quieras actualizarla en Docker Hub, deberás repetir estos pasos (reconstruir la imagen con `docker build` y luego subirla con `docker push`).


1. **Construir la Imagen**:
   ```bash
   docker build -t yllorca/django-k8s:latest -f Dockerfile.djangok8s .
   ```
   Este comando construirá la imagen usando el `Dockerfile` en tu directorio actual (el punto al final indica el contexto de construcción actual) y etiquetará la imagen con tu nombre de usuario en Docker Hub (`yllorca`), el nombre del repositorio (`django-k8s`) y la etiqueta (`latest`).

2. **Subir la Imagen a Docker Hub**:
   ```bash
   docker push yllorca/django-k8s:latest
   ```
   Este comando subirá la imagen que has etiquetado como `yllorca/django-k8s:latest` a Docker Hub. No necesitas usar `--all-tags` a menos que tengas varias etiquetas para la misma imagen que deseas subir todas a la vez.

Así que en resumen, primero construyes la imagen con `docker build`, etiquetándola apropiadamente, y luego la subes con `docker push` usando la misma etiqueta.

## Conectar tu repositorio de Docker Hub con tu repositorio de GitHub, 

Esto permite que los cambios en tu código fuente en GitHub automaticen la construcción (build) y actualización de tus imágenes de Docker en Docker Hub. Este proceso se conoce como integración continua (CI) y despliegue continuo (CD).

Aquí te explico cómo puedes configurarlo:

1. **Vincula tu Cuenta de GitHub con Docker Hub**:
   - En Docker Hub, ve a tu perfil y busca la opción para vincular tu cuenta de GitHub. Esto suele estar en la configuración o en la sección "Linked Accounts" (Cuentas Vinculadas).
   - Sigue las instrucciones para autorizar a Docker Hub a acceder a tus repositorios de GitHub.

2. **Configura un Repositorio Automatizado en Docker Hub**:
   - En Docker Hub, crea un nuevo repositorio y selecciona la opción para hacerlo un repositorio "Automated Build" (Construcción Automatizada).
   - Elige el repositorio de GitHub que quieres vincular.
   - Configura las reglas de construcción, especificando detalles como la rama de GitHub que desencadenará la construcción, la ubicación del `Dockerfile` y las etiquetas para la imagen construida.

3. **Actualiza tu Repositorio de GitHub**:
   - Cada vez que haces push a tu repositorio de GitHub (en la rama que configuraste para desencadenar la construcción), Docker Hub automáticamente construirá una nueva imagen basada en el último código fuente.
   - Puedes configurar diferentes reglas para diferentes ramas o etiquetas si es necesario.

4. **Verifica y Prueba las Construcciones Automáticas**:
   - Después de vincular y configurar todo, haz un cambio en tu repositorio de GitHub y haz push.
   - Ve a Docker Hub y verifica si se inicia una nueva construcción automáticamente.
   - Una vez que la construcción esté completa, puedes ver la nueva imagen en tu repositorio de Docker Hub.

5. **Consideraciones de Seguridad**:
   - Asegúrate de que solo las ramas relevantes estén configuradas para desencadenar construcciones automáticas.
   - Si estás trabajando con información sensible o variables de entorno, asegúrate de que no se expongan en el proceso de construcción.


Esta integración es muy útil para mantener tus imágenes de Docker actualizadas automáticamente con los últimos cambios en tu código fuente, simplificando así el proceso de despliegue y mantenimiento de tus aplicaciones.


5. **Generación de Contraseñas Seguras**:
   - Se utiliza el módulo `secrets` de Python para generar una contraseña segura para el superusuario de Django.
   - Se genera una nueva clave secreta de Django utilizando herramientas proporcionadas por Django o Python.

6. **Preparación para la Implementación en Kubernetes**:
   - Antes de desplegar la aplicación Django en Kubernetes, es crucial que el proyecto Django tenga acceso a estas variables de entorno.
   - Se enfatiza la importancia de no incluir estas variables directamente en la imagen del contenedor de Docker por razones de seguridad.
   - El próximo paso será utilizar "secrets" de Kubernetes para inyectar estas variables en el despliegue de Django.

```
python -c "import secrets;print(secrets.token_urlsafe(32))"
```

