## Deploy a Minimal FastAPI App

El video describe cómo desplegar una aplicación FastAPI mínima en Kubernetes, utilizando una imagen pública disponible en Docker Hub. A continuación, se presenta un resumen detallado del proceso:

1. **Preparación para el Despliegue**:
   - Se despliega una aplicación FastAPI que está disponible como un contenedor público en GitHub (IAC Python).
   - Es importante que el contenedor ya esté construido y sea público.

2. **Configuración del Despliegue**:
   - Se crea una nueva carpeta llamada `apps` en la estructura del proyecto.
   - Se crea un archivo YAML (`iac-python.yaml`) para la configuración del despliegue, similar a la configuración usada para Nginx en ejemplos anteriores.

3. **Detalles de la Configuración del Despliegue**:
   - Se sustituye la información específica de Nginx por la de la aplicación FastAPI.
   - Se utiliza la imagen de FastAPI disponible públicamente.
   - Se configura un puerto específico (8181) para la aplicación mediante una variable de entorno.

4. **Configuración del Servicio y Load Balancer**:
   - Se incluye la configuración del servicio y un Load Balancer en el mismo archivo YAML.
   - Se especifica que el tipo de servicio es un Load Balancer, destinado a distribuir el tráfico entre las réplicas del despliegue.

5. **Despliegue de la Aplicación**:
   - Se utiliza el comando `kubectl apply -f k8s/apps/iac-python.yaml` para desplegar la aplicación y el servicio en Kubernetes.
   - Se verifica el estado de los pods y despliegues con `kubectl get pods` y `kubectl get deployments`.

6. **Acceso y Verificación de la Aplicación**:
   - Se accede a uno de los pods para verificar la configuración interna, incluyendo las variables de entorno y la configuración del puerto.

7. **Similitudes con Proyectos Django**:
   - Se observan similitudes entre la configuración de FastAPI y los proyectos Django, especialmente en términos de la estructura del Dockerfile y el archivo de entrada (`entrypoint.sh`).

8. **Pasos Futuros para la Integración de Django**:
   - Se discuten los pasos necesarios para llevar un proyecto Django a producción en Kubernetes, incluyendo la creación de un repositorio de contenedores privado, la configuración de variables de entorno y la integración de bases de datos.

9. **Finalización del Despliegue y Verificación**:
   - Una vez que el Load Balancer se ha configurado completamente, se verifica que la aplicación FastAPI está funcionando correctamente accediendo a la dirección IP externa proporcionada por Digital Ocean.

El video se enfoca en mostrar cómo desplegar aplicaciones FastAPI en un entorno de producción en Kubernetes, destacando la importancia de tener imágenes de contenedores preconstruidas y la utilidad de configurar servicios y Load Balancers para exponer la aplicación al exterior. Además, se hace una comparación con la configuración necesaria para proyectos Django, preparando el camino para futuras implementaciones.



kubectl apply con la bandera --dry-run=client para validar tus cambios antes de aplicarlos realmente:
````
kubectl apply --dry-run=client -f k8s/apps/django-k8s-web.yaml
````
