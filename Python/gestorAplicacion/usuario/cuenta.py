import random

from Python.gestorAplicacion.usuario.cliente import Cliente


class Cuenta:
    id = 1000

    def __int__(self, titular, saldo, tipoCuenta):
        self.titular = titular
        self.tipoCuenta = tipoCuenta
        self.saldoTotal = saldo
        self.saldoDisponible = saldo
        self.misBolsillos = []
        self.estado = True
        self.numero = random.randint(1000,10000)
        Cuenta.id = Cuenta.getId() + 1

        if len(self.misBolsillos) == 0:
            self.saldoDisponible = self.saldoTotal
        else:
            self.saldoDisponible = self.saldoTotal - self.saldoEnBolsillos()


        #Función para disminuir el saldo total de la cuenta
        def aumentarSaldo(self, cantidad):
            if self.estado:
                setSaldoTotal(getSaldoTotal() + cantidad)

        #Función para disminuir el saldo total de la cuenta
        def disminuirSaldo(self, cantidad):
            if self.estado and (getSaldoDisponibles() >= cantidad):
                setSaldoTotal(getSaldoTotal() - cantidad)

        #Función que retorna el saldo de los bolsillos
        def saldoEnBolsillos(self):
            valorEnBolsilos = 0;
            for bolsillo in self.misBolsillos:
                valorEnBolsilos += bolsillo.getValorCargaBolsillo()
            return valorEnBolsilos

        @classmethod
        def getId(cls):
            return (Cliente.listaCuentas).index(cls)
        def getTitular(self):
            return self.titular

        def setTitular(self, titular):
            self.titular = titular

        def getTipoCuenta(self):
            return self.tipoCuenta

        def setTipoCuenta(self, tipoCuenta):
            self.tipoCuenta = tipoCuenta

        def getSaldoTotal(self):
            return self.saldoTotal

        def setSaldoTotal(self, saldoTotal):
            self.saldoTotal = saldoTotal

        def getSaldoDisponibles(self):
            return self.saldoDisponible

        def setSaldoDisponible(self, saldoDisponible):
            self.saldoDisponible= saldoDisponible

        def getMisBolsillos(self):
            return self.misBolsillos

        def setMisBolsillos(self, misBolsillos):
            self.misBolsillos = misBolsillos

        def getEstado(self):
            return self.estado

        def setEstado(self, estado):
            self.estado = estado

        def getNumero(self):
            return self.numero

        def setNumero(self, numero):
            self.numero = numero















