## Expose your Deployment with a Load Balancer

El video explica cómo exponer un despliegue (deployment) de Kubernetes al mundo exterior, utilizando Nginx como ejemplo. A continuación se presenta un resumen detallado:

1. **Verificación del Despliegue**:
   - Antes de exponer el despliegue, el presentador verifica que el despliegue de Nginx esté activo usando el comando `kubectl apply -f k8s/nginx/deployment.yaml` y luego `kubectl get pods`.

2. **Creación del Archivo de Servicio**:
   - Se crea un nuevo archivo denominado `service.yaml`.
   - Dentro de este archivo, se declara la versión de la API (`v1`), se especifica que el tipo (`kind`) es un `Service`, y se proporciona metadatos con el nombre `nginx-service`.

3. **Configuración del Servicio**:
   - Se especifica que el tipo de servicio es un `LoadBalancer`.
   - Se configuran los puertos, usando el puerto 80 como el puerto estándar para la exposición al mundo exterior. 
   - El puerto de destino (`targetPort`) se establece en 8000.
   - Se utiliza un selector para conectar el servicio con el despliegue de Nginx.

4. **Despliegue del Servicio**:
   - Para desplegar el servicio, se usa `kubectl apply -f k8s/nginx/service.yaml`.
   - El comando `kubectl get services` muestra los servicios activos, incluyendo la IP externa y los puertos asignados.

5. **Creación del Load Balancer**:
   - Kubernetes provisiona automáticamente un Load Balancer en proveedor, que se muestra en la consola de administración de Linode.
   - El Load Balancer distribuye el tráfico entre las réplicas del despliegue de Nginx.

6. **Acceso al Servicio**:
   - Una vez creado el Load Balancer, el servicio Nginx se vuelve accesible desde el exterior a través de la dirección IP externa proporcionada.

7. **Recuperación de Configuraciones**:
   - El presentador explica cómo recuperar configuraciones eliminadas accidentalmente utilizando `kubectl get service -o yaml`.
   - Muestra cómo exportar y modificar la configuración del servicio en un nuevo archivo YAML.

8. **Combinación de Despliegue y Servicio**:
   - Se discute la práctica común de combinar la configuración del despliegue y el servicio en un único archivo YAML (`combo.yaml`), separados por tres guiones (`---`).
   - Se aplica la configuración combinada con `kubectl apply`.

9. **Desafío Final**:
   - El video termina desafiando al espectador a eliminar tanto el despliegue como el servicio, lo que debería ser un proceso sencillo a este punto.

El video se centra en enseñar cómo exponer un despliegue de Kubernetes al mundo exterior, configurando un servicio y un Load Balancer, y cómo manejar y recuperar configuraciones en Kubernetes.
