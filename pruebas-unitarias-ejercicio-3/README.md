Una aplicación posee un sistema de autenticación de usuarios. La clase `ServicioAutenticacion` es la encargada de verificar si un usuario puede iniciar sesión.

Para ello, utiliza un objeto `RepositorioUsuarios`, que permite buscar un usuario por su nombre de usuario.

El proceso de autenticación es el siguiente:

* Se solicita al repositorio el usuario correspondiente al nombre ingresado.
* Si el usuario no existe, la autenticación debe fallar.
* Si el usuario existe, la autenticación será exitosa únicamente si la contraseña ingresada coincide con la contraseña almacenada.
* En cualquier otro caso, la autenticación debe fallar.

En este ejercicio no se desea utilizar una base de datos real, por lo que debe reemplazarse el repositorio mediante una clase stub o mock.

Se pide:

* Analizar las clases `TestAutenticarMock` y `TestAutenticarStub`.
* Completar la implementación de `RepositorioUsuariosStub` que se encuentra en el directorio `tests\stubs\`.
* Completar la implementación de los métodos `test_usuario_password_correcto` y `test_usuario_password_incorrecto` de las clases `TestAutenticarMock` y `TestAutenticarStub` y verificar que las pruebas se ejecutan correctamente.

---

En la misma aplicación existe además una clase `RegistroUsuarios`, cuya responsabilidad es registrar nuevos usuarios. Para ello, utiliza un `RepositorioUsuarios` para almacenar el usuario y un `ServicioEmail` para enviar un correo electrónico de bienvenida al usuario una vez completado el registro.

Se pide analizar la clase `TestRegistrar` y responder:

* ¿Qué comportamiento de la clase `RegistroUsuarios` verifica el caso de prueba?
* ¿Qué rol cumplen los objetos Mock utilizados en la prueba?
* ¿Qué ventaja ofrece el uso de mocks frente a utilizar implementaciones reales del repositorio y del servicio de correo electrónico?