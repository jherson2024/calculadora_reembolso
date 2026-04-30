Característica: Calculadora de reembolsos de hotel

  Como sistema de reservas
  Quiero calcular reembolsos correctamente
  Para garantizar reglas de negocio y beneficios VIP


  Escenario: Cliente VIP cancela con 2 horas de anticipación
    Dado que el monto de la reserva es 200
    Y el cliente es VIP
    Cuando cancela con 2 horas de anticipación
    Entonces recibe un reembolso de 100


  Escenario: Cliente normal cancela con mucha anticipación
    Dado que el monto de la reserva es 200
    Y el cliente no es VIP
    Cuando cancela con 80 horas de anticipación
    Entonces recibe un reembolso de 200


  Escenario: Cliente normal cancela en rango medio
    Dado que el monto de la reserva es 200
    Cuando cancela con 48 horas de anticipación
    Entonces recibe un reembolso de 100


  Escenario: Cliente normal cancela en última hora
    Dado que el monto de la reserva es 200
    Cuando cancela con 10 horas de anticipación
    Entonces recibe un reembolso de 0


  Escenario: Validación de valor límite en 24 horas
    Dado que el monto es 200
    Cuando cancela con 24 horas
    Entonces recibe 100


  Escenario: Validación de valor límite en 72 horas
    Dado que el monto es 200
    Cuando cancela con 72 horas
    Entonces recibe 100