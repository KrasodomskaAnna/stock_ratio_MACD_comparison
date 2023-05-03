import math
import matplotlib.pyplot as plt
import pandas as pd


def liczEMA(dane, n, licz_od):
    alfa = 2 / (n + 1)
    palfa = 1
    licznik = 0
    mianownik = 0
    for i in range(0, n + 1):
        licznik += palfa * dane[licz_od - i]
        mianownik += palfa

        palfa *= 1 - alfa
    return licznik / mianownik


def liczMACD(dane, max_x_dlugosc, krotszy_okres, dluzszy_okres):
    dlugosc = max_x_dlugosc if max_x_dlugosc <= len(dane) - dluzszy_okres else len(dane) - dluzszy_okres
    od_idx = len(dane) - dlugosc
    EMA12 = [0] * dlugosc
    EMA26 = [0] * dlugosc
    MACD = [0] * dlugosc
    for i in range(0, dlugosc):
        EMA12[i] = liczEMA(dane, krotszy_okres, i + od_idx)
        EMA26[i] = liczEMA(dane, dluzszy_okres, i + od_idx)
        MACD[i] = EMA12[i] - EMA26[i]
    return MACD


def liczSIGNAL(macd, max_x_dlugosc, signal_okres):
    dlugosc = max_x_dlugosc if max_x_dlugosc <= len(macd) - signal_okres else len(macd) - signal_okres
    od_idx = len(macd) - dlugosc
    SIGNAL = [0] * dlugosc
    for i in range(0, dlugosc):
        SIGNAL[i] = liczEMA(macd, signal_okres, i + od_idx)
    return SIGNAL


def liczMACD_SIGNAL(dane, max_x_dlugosc, krotszy_okres, dluzszy_okres, signal_okres):
    macd_wydluzone = liczMACD(dane, max_x_dlugosc + signal_okres, krotszy_okres, dluzszy_okres)
    signal = liczSIGNAL(macd_wydluzone, max_x_dlugosc, signal_okres)
    return macd_wydluzone[signal_okres:], signal

# przecinająca - macd, roc
# przecinana - signal, linia 0
# jeśli z dołu - zakup
def autoAkcjonariusz(dane, przecinajaca, przecinana):
    wczesniejsza_wart_portfela = 0
    portfel = 1000
    akcje = 0
    pzecinana_przesuniecie = len(przecinajaca) - len(przecinana)  # macd może być krótszy od signal
    dane_przesuniecie = len(dane) - len(przecinajaca)  # dane mogą być krótsze od macd
    for i in range(0, len(przecinana) - 1):
        if akcje == 0:  # jeżeli możemy coś kupić
            if przecinajaca[i + pzecinana_przesuniecie] < przecinana[i] and przecinajaca[i + pzecinana_przesuniecie + 1] >= przecinana[i + 1]:
                # przecina od dołu -> zakup akcji
                cena = round(dane[i + dane_przesuniecie + 1], 2)
                akcje = math.floor(portfel / cena)
                wczesniejsza_wart_portfela = portfel
                portfel -= round(akcje * cena, 2)

        if akcje > 0:  # jeżeli możemy sprzedać akcje
            if przecinajaca[i + pzecinana_przesuniecie] >= przecinana[i] and przecinajaca[i + pzecinana_przesuniecie + 1] < przecinana[i + 1]:
                # przecina od góry -> sprzedaż akcji
                cena = round(dane[i + dane_przesuniecie + 1], 2)
                portfel += round(akcje * cena, 2)
                #print("ZYSK, gdy ox = " + str(i)) if wczesniejsza_wart_portfela < portfel else print(
                #    "strata, gdy ox = " + str(i))
                akcje = 0

    # jeżeli skończyliśmy z jakimiś akcjami w naszym portfelu inwestycyjnym,
    # to należy je "sprzedać" aby zobaczyć ile w sumie w zł mamy w naszym portfelu
    portfel += round(akcje * round(dane[len(dane) - 1], 2), 2)
    return round(portfel, 2)


def liczROC(dane, k, max_x_dlugosc):
    dlugosc = max_x_dlugosc if max_x_dlugosc <= len(dane) - k else len(dane) - k
    od_idx = len(dane) - dlugosc
    ROC = [0] * dlugosc
    for i in range(0, dlugosc):
        ROC[i] = (dane[i + od_idx] - dane[i + od_idx-k]) / dane[i + od_idx - k]
    return ROC


dane_calosciowe = pd.read_csv('snx_d.csv')

max_x_dlugosc = 1000
linia_x = [i for i in range(0, max_x_dlugosc)]

dane = [dane_calosciowe["Otwarcie"], dane_calosciowe["Zamkniecie"]]
dane_opis_tytyul = ["otwarcia", "zamkniecia"]
dane_opis_label = ["otwarcie", "zamkniecie"]
dlugosc_danych = len(dane[0]) - max_x_dlugosc

# obliczanie roc
roc = liczROC(dane[1], 10, max_x_dlugosc)
portfel_roc = autoAkcjonariusz(dane[1], roc, [0]*len(roc))

# obliczanie wskaźników dla otwarcia, najwyższego, najniższego i zamknięcia
plt.rcParams['figure.figsize'] = [16, 8]
for i in range(2):
    plt.subplots_adjust(left=0.1,
                        bottom=0.1,
                        right=0.9,
                        top=0.95,
                        wspace=0.4,
                        hspace=0.5)
    # wykres danych
    plt.subplot(3, 1, 1)
    plt.plot(linia_x, dane[i][dlugosc_danych:], label=dane_opis_label[i])
    plt.legend()
    plt.title("Wartość akcji")
    plt.xlabel("Próbka")
    plt.ylabel("Wartość")
    plt.locator_params('x', nbins=20)
    plt.grid(True)

    # wykres MACD / SIGNAL
    toople = liczMACD_SIGNAL(dane[i], max_x_dlugosc, 12, 26, 9)
    macd = toople[0]
    signal = toople[1]

    plt.subplot(3, 1, 2)
    plt.plot(linia_x, macd, label="MACD")
    plt.plot(linia_x, signal, label="SIGNAL")
    plt.legend()
    plt.title("Wykres wskaźników MACD i SIGNAL dla pola " + dane_opis_tytyul[i])
    plt.xlabel("Próbka")
    plt.ylabel("Wartość")
    plt.locator_params('x', nbins=20)
    plt.grid(True)

    # wynik stanu portfela
    portfel = autoAkcjonariusz(dane[i], macd, signal)
    print("Stan portfela wynosi:", portfel, "dla pola", dane_opis_tytyul[i])

    plt.subplot(3, 1, 3)
    plt.plot(linia_x, roc, label=dane_opis_label[i])
    plt.legend()
    plt.title("ROC dla zamkniecia")
    plt.xlabel("Próbka")
    plt.ylabel("Wartość")
    plt.locator_params('x', nbins=20)
    plt.grid(True)

    # wyświetlanie ROC
    print("ROC Stan portfela wynosi:", portfel_roc, "dla pola zamkniecie")

    #plt.show()
    plt.savefig("analiza"+dane_opis_tytyul[i]+".png")
    plt.clf()