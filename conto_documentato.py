## @file conto_documentato.py
#  @brief Conto bancario con op. di prelievo e deposito

## @brief Rappresenta un conto bancario con intestatario e utile
#  @details Consente deposito e prelievo. Se il saldo risulta inferiore
#           della quantità di prelievo desiderata, esso non è permesso.
class ContoBancario():

    ## @brief Nuovo conto bancario
    #  @param intestatario nuovo conto
    def __init__ (self, intestatario):
        self.intestatario = intestatario
        self.saldo = 0

    ## @brief Deposito denaro
    #  @param importo somma deposito
    def deposita(self, importo):
        self.saldo += importo

    ## @brief Preleva denaro
    #  @param importo somma prelievo
    #  @exception ValueError Sollevata se saldo insufficiente
    def preleva(self, importo):
        if self.saldo < importo:
            raise ValueError('Saldo insufficiente')
        else:
            self.saldo -= importo

    ## @brief Restituisce dati sul conto
    #  @return Stringa con intestatario e saldo
    def __str__ (self):
        return f'Conto di {self.intestatario} saldo: {self.saldo}'


def main():
    conto = ContoBancario("Mario Rossi")
    print (conto)
    conto.deposita(200)
    conto.preleva(50)
    conto.preleva(25)
    print(conto)
    try:
        conto.preleva(700)
    except ValueError as e:
        print('Operazione rifiutata: ', e)

if __name__ == "__main__":
    main()
