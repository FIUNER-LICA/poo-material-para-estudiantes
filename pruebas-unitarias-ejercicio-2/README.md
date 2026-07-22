La clase `CuentaBancaria` representa una cuenta bancaria y tiene las siguientes especificaciones:

* El saldo inicial no puede ser negativo.
* Se pueden realizar depósitos únicamente de montos estrictamente positivos.
* Se pueden realizar extracciones únicamente de montos estrictamente positivos.
* No se puede retirar más dinero del disponible.
* Una transferencia consiste en retirar dinero de la cuenta origen y depositarlo en la cuenta destino.
* El saldo nunca puede ser negativo.

Complete los casos de prueba del módulo `test_cuenta_bancaria` basándose en las especificaciones y en los nombres de los tests. Utilice donde sea necesario los objetos ya definidos en `setUp`. La clase `CuentaBancaria` podría tener errores respecto de las especificaciones, en tal caso los tests adecuadamente diseñados deberían dejarlos en evidencia.