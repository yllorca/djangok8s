## limpiar la configuración global de kubernetes

Para limpiar la configuración antigua de Kubernetes utilizando `kubectl config unset`, primero identificaremos las secciones clave en tu configuración actual y luego las eliminaremos. Basándonos en tu configuración, parece que necesitas eliminar un clúster (`lke146790`), un usuario (`lke146790-admin`), y un contexto (`lke146790-ctx`).

Sigue estos pasos:

### 1. Eliminar el Clúster

```sh
kubectl config unset clusters.lke146790
```

Este comando eliminará la configuración del clúster `lke146790`.

### 2. Eliminar el Usuario

```sh
kubectl config unset users.lke146790-admin
```

Con este comando, eliminarás la configuración del usuario `lke146790-admin`.

### 3. Eliminar el Contexto

```sh
kubectl config unset contexts.lke146790-ctx
```

Este comando eliminará el contexto `lke146790-ctx`.

### 4. Verificar los Cambios

Después de ejecutar estos comandos, puedes verificar que se hayan realizado los cambios con:

```sh
kubectl config view
```

Este comando mostrará tu configuración de `kubectl` actualizada. Deberías ver que las entradas para el clúster, el usuario y el contexto que eliminaste ya no están presentes.

### Nota Adicional

- Si tienes múltiples entradas de clústeres, usuarios o contextos que deseas eliminar, repite los comandos `unset` para cada uno de ellos.
- Asegúrate de tener la configuración correcta para cualquier otro clúster que todavía necesites utilizar.

Estos pasos te permitirán limpiar tu archivo de configuración de Kubernetes de entradas antiguas o no deseadas, manteniéndolo actualizado y organizado.


## creamos dentro del proyecto nuestro carpeta oculta:

```
mkdir -p .kube 
```

### Paso 1: Editar el Archivo `.zshrc`

1. **Abrir tu Archivo `.zshrc`**:
   - Abre una terminal.
   - Escribe el siguiente comando para editar tu archivo `.zshrc`:
     ```sh
     nano ~/.zshrc
     ```
   - Esto abrirá el archivo `.zshrc` en el editor `nano`. Si prefieres otro editor, siéntete libre de usarlo.

### Paso 2: Añadir los Alias en `.zshrc`

2. **Añadir Alias para Cambiar el KUBECONFIG**:
   - En el archivo `.zshrc`, desplázate hasta el final (o el lugar donde prefieras añadir tus alias).
   - Añade líneas para tus alias. Por ejemplo:
     ```sh
     alias kubeconfig-djangok8s="export KUBECONFIG=/Users/yllorca/Desktop/Development/django-k8s/.kube/config"
     ```
   - Reemplaza las rutas con las rutas correctas a tus archivos de configuración de Kubernetes para cada proyecto.

### Paso 3: Guardar y Cargar la Nueva Configuración

3. **Guardar y Salir del Editor**:
   - Para guardar los cambios en `nano`, pulsa `Ctrl + O`, luego `Enter`, y para salir, `Ctrl + X`.
   - Si usaste otro editor, guarda el archivo según corresponda.

4. **Aplicar los Cambios**:
   - Para que los cambios surtan efecto, debes cargar la nueva configuración de tu `.zshrc`.
   - Puedes hacerlo cerrando y abriendo tu terminal o ejecutando:
     ```sh
     source ~/.zshrc
     ```

### Paso 4: Usar los Alias

Ahora, cada vez que quieras cambiar la configuración de Kubernetes a uno de tus proyectos, simplemente usa los alias correspondientes en tu terminal. Por ejemplo, escribe `kubeconfig-djangok8s` para cambiar al djangok8s.

### Verificar el Contexto de Kubernetes

Después de cambiar la configuración con un alias, puedes verificar el contexto actual de Kubernetes con:

```sh
kubectl config current-context
```

Este paso te asegurará que estás trabajando con el clúster correcto para el proyecto seleccionado.


