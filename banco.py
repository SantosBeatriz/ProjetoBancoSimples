class Banco():
    def __init__(self, nome, numero_c, saldo_c, tipo_c, atividade_c, status_c=False, limite_c=False):
        self.limite_disponivel = 0
        self.diferenca_limite = 0
        self.limite = 0
        self.saldo_total = 0
        self.nome = nome
        self.numero_c = numero_c
        self.saldo_c = saldo_c
        self.tipo_c = tipo_c
        self.atividade_c = atividade_c
        self.status_c = status_c
        self.limite_c = limite_c

    def ativar(self):
        if self.status_c == False:
            self.status_c = True
            print(f'Olá {self.nome}, sua conta {self.tipo_c} está ativa.')

            with open ("extrato.txt", "a", encoding="utf-8") as arquivo:
                arquivo.write(f'{self.nome} - - {self.numero_c} - - {self.tipo_c}')
    def depositar(self, deposito):
        if not self.limite_c or self.limite_disponivel == self.limite:
            self.saldo_c += deposito
            self.saldo_total += self.saldo_c
            print(
                f'{self.nome}, seu deposito no valor de {deposito} foi efetuado com sucesso. Obrigada por usar nosso serviço!')
            self.atividade_c += 1

        if self.limite_c is True or self.limite_disponivel < self.limite:
            self.diferenca_limite = self.limite - self.limite_disponivel

            if deposito > self.diferenca_limite:
                self.limite_disponivel += self.diferenca_limite
                self.acrescimo_depo = deposito - self.diferenca_limite
                self.saldo_c += self.acrescimo_depo
                self.saldo_total += self.saldo_c
                print(
                    f'{self.nome}, seu deposito no valor de {deposito} foi efetuado com sucesso. Obrigada por usar nosso serviço!')
                self.atividade_c += 1

            else:
                self.limite_disponivel += deposito
                print(
                    f'{self.nome}, seu deposito no valor de {deposito} foi efetuado com sucesso. Obrigada por usar nosso serviço!')
                self.atividade_c += 1

            with open("extrato.txt", "a", encoding="utf-8") as arquivo:
                import datetime
                self.data_atual = datetime.datetime.now()
                self.data_hora_formatada = self.data_atual.strftime("%d/%m/%Y %H:%M:%S")
                arquivo.write(f"\nDepósito de R${deposito} - - {self.data_hora_formatada}")

    def sacar(self, saque):
        if self.status_c is True:
            if saque != 0 and saque <= self.saldo_c:
                self.saldo_c -= saque
                print(
                    f'{self.nome}, seu saque no valor de {saque} foi efetuado com sucesso. Obrigada por usar nosso serviço!')
                self.atividade_c += 1

            elif saque != 0 and self.limite_c is True and saque > self.saldo_c:
                self.resto_saque = saque - self.saldo_c
                self.saldo_c -= self.saldo_c
                self.limite_disponivel -= self.resto_saque
                print(
                    f'{self.nome}, seu saque no valor de {saque} foi efetuado com sucesso. Obrigada por usar nosso serviço!')
                self.atividade_c += 1

            with open("extrato.txt", "a", encoding="utf-8") as arquivo:
                import datetime
                self.data_atual = datetime.datetime.now()
                self.data_hora_formatada = self.data_atual.strftime("%d/%m/%Y %H:%M:%S")
                arquivo.write(f"\nSaque de R${saque} - - {self.data_hora_formatada}")

        else:
            print(f'{self.nome}, sua conta não está ativada, para efetuar saque, ative ela.')

    def verificar(self):
        print(f'{self.nome}, seu saldo é: {self.saldo_c}')

        if self.limite_c is True:
            print(f'{self.nome}, seu saldo emergêncial é: {self.limite_disponivel}')

            with open("extrato.txt", "a", encoding="utf-8") as arquivo:
                import datetime
                self.data_atual = datetime.datetime.now()
                self.data_hora_formatada = self.data_atual.strftime("%d/%m/%Y %H:%M:%S")
                arquivo.write(
                    f'\nVerificação de saldo de R${self.saldo_c} - - Verificação de saldo emergêncial de R${self.limite_disponivel} - - {self.data_hora_formatada}')

        with open("extrato.txt", "a", encoding="utf-8") as arquivo:
            import datetime
            self.data_atual = datetime.datetime.now()
            self.data_hora_formatada = self.data_atual.strftime("%d/%m/%Y %H:%M:%S")
            arquivo.write(f"\nVerificação de saldo de R${self.saldo_c} - - {self.data_hora_formatada}")

    def limite_emergencial(self):
        if self.atividade_c <= 5:
            self.limite_c = True
            self.limite = 200
            self.limite_disponivel = self.limite
            print(
                f'{self.nome}, seu limite no valor {self.limite_disponivel} foi ativado com sucesso, para aumentar seu limite ultilize mais os serviços do banco. Obrigado por usar nosso serviço!')

        elif self.atividade_c <= 10:
            self.limite_c = True
            self.limite = 600
            self.limite_disponivel = self.limite
            print(
                f'{self.nome}, seu limite no valor {self.limite_disponivel} foi ativado com sucesso, para aumentar seu limite ultilize mais os serviços do banco. Obrigado por usar nosso serviço!')

        elif self.atividade_c > 10:
            self.limite_c = True
            self.limite = 2000
            self.limite_disponivel = self.limite
            print(
                f'{self.nome}, seu limite no valor {self.limite_disponivel} foi ativado com sucesso, para aumentar seu limite ultilize mais os serviços do banco. Obrigado por usar nosso serviço!')

        else:
            self.limite_c = True
            self.limite = 50
            self.limite_disponivel = self.limite
            print(
                f'{self.nome}, seu limite no valor {self.limite_disponivel} foi ativado com sucesso, para aumentar seu limite ultilize mais os serviços do banco. Obrigado por usar nosso serviço!')

    def aumentar_limite(self):
        if self.limite_c is True and self.saldo_total > 5000:
            self.limite_c = self.limite_c + ((self.saldo_total/15) * 100)
            self.limite_c = round(self.limite_c + 0.5)
            print(f'{self.nome}, seu limite foi aumentado e se encontra no valor de {self.limite_c}.')

        elif self.limite_c is True and self.saldo_total > 3500:
            self.limite_c = self.limite_c + ((self.saldo_total / 10) * 100)
            self.limite_c = round(self.limite_c + 0.5)
            print(f'{self.nome}, seu limite foi aumentado e se encontra no valor de {self.limite_c}.')

        elif self.limite_c is True and self.saldo_total > 1500:
            self.limite_c = self.limite_c + ((self.saldo_total / 5) * 100)
            self.limite_c = round(self.limite_c + 0.5)
            print(f'{self.nome}, seu limite foi aumentado e se encontra no valor de {self.limite_c}.')

        else:
            print(f'{self.nome}, seu aumento de limite foi recusado, aumente o uso de sua conta e tente novamente.')


    def extrato(self):
        with open("extrato.txt", "r") as arquivo:
            self.exibir = arquivo.read()
        return self.exibir

    def desativar(self):
        if self.saldo_c == 0:
            if self.limite_disponivel == self.limite:
                if self.status_c is True:
                    print(
                        f'Olá {self.nome}, sua conta {self.tipo_c} foi desativada com sucesso. Obrigada por usar nosso serviço!')

            elif self.limite_disponivel < self.limite:
                print(
                    f'{self.nome}, você possui uma pendência com o seu limite emergêncial, para desativar sua conta você precisa quitar sua pedência.')

        elif self.saldo_c > 0:
            print(
                f'{self.nome}, você possui um saldo de {self.saldo_c} em uma conta, para desativar sua conta você precisa retira o saldo total da conta.')


cliente1 = Banco("Hana", 301, 0, "Corrente", 0)
cliente1.sacar(50)
cliente1.ativar()
cliente1.depositar(100)
cliente1.sacar(50)
cliente1.limite_emergencial()
cliente1.verificar()
cliente1.sacar(250)
cliente1.verificar()
cliente1.depositar(200)
cliente1.verificar()
cliente1.sacar(50)
cliente1.desativar()
cliente1.depositar(5000)
cliente1.aumentar_limite()
cliente1.verificar()
cliente1.sacar(4950)
cliente1.desativar()
print()