# stock_ratio_MACD_comparison
Wskaźnik giełdowy MACD
Inwestorzy giełdowi dokonując wyboru instrumentów finansowych, w które chcieliby zainwestować w krótkim okresie wykorzystują analizę techniczną. Jest ona oparta na analizie kształtowania się cen instrumentów finansowych (np. kursów akcji), wartości obrotów dokonywanych nimi na giełdzie, wielkości zleceń czy wskaźników technicznych. Pozwala określić jak będą kształtowały się kursy akcji w przyszłości na podstawie oceny czynników, które mogą determinować podaż oraz popyt na te akcje. 
W analizie technicznej wykorzystywanych jest wiele wskaźników, do których zaliczyć można: oscylatory, wskaźnik sił względnej (RSI), wskaźnik zmian (ROC), wskaźniki rynku akcji jak również wskaźnik MACD. 
Metoda obliczenia MACD
Najbardziej popularnym ze względu na łatwość interpretacji oraz możliwość wykorzystania jest wskaźnik (oscylator) MACD (Moving Average Convergence Divergence). Ten oscylator zaliczany do wskaźników trendu sygnalizuje zbieżność bądź rozbieżność pomiędzy średnimi ruchomymi. Wykorzystując go do oceny opłacalności inwestycji, należy porównać kształtowanie linii MACD z linią sygnalną. 
Linię MACD stanowi różnica pomiędzy średnią długookresową i średnią krótkookresową. Należy zwrócić jednak uwagę na to, że sama metoda liczenia średnich może być różna, jednak najczęściej wykorzystuje się średnią kroczącą wykładniczą (tzw. EMA - exponential moving average). Jest to tzw. średnia ruchoma. Można przedstawić ją wzorem:
〖EMA〗_x=(∑_(i=0)^x▒〖(1-a)^i c_i 〗)/(∑_(i=0)^x▒(1-a)^i )					{ 1.1 }
a=2/(i+1)						{1.2}
gdzie: 
x – liczba wszystkich notowań danego instrumentu finansowego poddanych analizie,
c – cena z i-tego notowania,
a – współczynnik nadający wagę dla kolejnych notowań, przyjmuje wartość od 0 do 1.
Zatem przywiązuje ona większe znaczenie ostatnim kursom akcji (nadaje im większą wagę) niż cenom z początku wybranego przez inwestora okresu. 
Jeżeli chodzi o okres, który uznać należy za długi lub krótki dla obliczenia średniej – początkowo w obliczeniach tego wskaźnika przyjęto, że są to średnie 26-okresowe oraz 12-okresowe. Aktualnie jednak uważa się, że można dowolnie wybierać pomiędzy okresami średnich, jak również rodzajami cen, branymi pod uwagę w analizie (początkowo była to cena zamknięcia). 
Drugi rodzaj linii stosowany w analizie to linia sygnalna będącą średnią ruchoma z linii MACD (najczęściej 9-dniowa). 
Interpretacja MACD
Wskaźnik ten generuje dwa podstawowe rodzaje sygnałów:
- przecięcie linii MACD z linią sygnalną,
- dywergencje.
Analiza kształtowania się opisanych powyżej linii pozwala na określenie, kiedy inwestor powinien zakupić bądź sprzedać instrument finansowy. Inwestor może spodziewać się wzrostu np. cen akcji (sygnał kupna), kiedy linia sygnalna przecina linię MACD od góry w dół. Natomiast momentem, gdy należy pozbywać się akcji (sygnał sprzedaży) jest przecięcie linii MACD przez linię sygnalną od dołu w górę. 
Dywergencje to różnice pomiędzy tym, co pokazuje wskaźnik, a tym co prezentuje wykres cenowy. Gdy kolejne dołki cenowe na wykresie tworzą się na coraz niższych poziomach, a punkty linii MACD kształtują się coraz wyżej, jest to sygnałem do kupna. Natomiast sytuacja odwrotna – gdy kolejne wierzchołki cenowe są coraz wyżej, a punkty wskaźnika MACD opadają, daje nam sygnał do sprzedaży. 

Implementacja
Użyte biblioteki
Do zaimplementowania kodu pozwalającego obliczyć wskaźnik MACD użyto języka Python. W celu wczytania danych wykorzystano bibliotekę „pandas” a „matplotlib.pyplot” w celu wizualizacji danych. 
Działanie programu
Z uwagi na fakt, iż coraz częściej do analizy bierze się pod uwagę różne rodzaje cen (nie tylko zamknięcia), w niniejszej analizie wyświetlono wykresy i obliczono stany portfela dla otwarcia i zamknięcia. W celu porównania danych wykres dzielony jest na dwa wiersze – w pierwszym wyświetlane są dane dotyczące ceny, a w drugim wykres z liniami MACD i SIGNAL. Pozwala to na szybką analizę czy wskaźnik ten wskazuje na poprawne zachowania dla wszystkich okresów.
Obliczanie MACD i SIGNAL
Wczytywane dane przetwarzane są poprzez funkcję „liczMACD_SIGNAL”, która przyjmuje próbki danych, maksymalną długość przetwarzanych danych (gdyż dane wejściowe to wektor o długości większej, niż analizowany okres), oraz wartość, ile okresów ma być branych pod uwagę przy liczeniu średnich kroczących EMA przy obliczaniu MACD oraz linii sygnału SIGNAL. Dane skracane są odpowiednio, aby nie obliczać wartości, które nie będą brane pod uwagę przy obliczaniu wartości wyświetlanych na wykresie, a następnie wywoływane są odpowiednie funkcje liczące odpowiednio MACD a następnie SIGNAL. Wspomniane funkcje obliczają kolejne wartości dla wektorów MACD i SIGNAL na podstawie wyników zwracanych przez funkcję „liczEMA”, która jest implementacją średniej kroczącej zapisanej wzorem 1.
Algorytm automatycznego kupna i sprzedaży
Zaimplementowano funkcję o nazwie „autoAkcjonariusz”, która przechodząc po wartościach wektora o nazwie „przecinajaca” (MACD) i „przecinana” (SIGNAL) sprawdza, czy wartości funkcji się nie przecinają, a następnie na podstawie tego czy przecinająca przecina przecinaną z góry czy z dołu – podejmuje decyzję o sprzedaży bądź zakupie akcji. Zmienna „portfel” przechowuje stan rachunku w biurze maklerskim (po sprzedaży akcji), a zmienna „akcje” liczbę zakupionych akcji, dla których jest przeprowadzana symulacja. Funkcja zakłada dwa możliwe stany:
	Stan portfela = 0 => kupiono akcje
	Liczba akcji = 0 => sprzedano akcje
Symulacja nie przewiduje zakupu np. 10 akcji i późniejszego ewentualnego ich dokupienia, gdyż największy zysk można osiągnąć przy maksymalizacji zainwestowanych środków, jednak biorąc pod uwagę, że wiąże się to z dużym ryzykiem. Należy także zwrócić uwagę na to, iż przy zmianie wartości zmiennych takich jak cena czy portfel wartość za każdym razem jest zaokrąglana – dzieje się tak, gdyż np.  złoty polski (w których są podane dane wartości akcji spółki), jak większość innych walut, mają najmniejszy nominał w wartości 1/100 podstawowej jednostki monetarnej.
Ponadto z uwagi na zastosowanie uniwersalnego schematu działania i nazw – „przecinająca” i „przecinana”, algorytm ten jest uniwersalny dla wszystkich wskaźników, które można przedstawić w formie linii. Wykorzystano to do porównania wyników zwracanych przez funkcję „autoAkcjonariusz” dla wskaźnika MACD i dla ROC.

Wskaźnik zmiany ROC
Wskaźnik ten (ang. Rate of change) jest jak MACD jednym z popularniejszych wskaźników giełdowej analizy technicznej, który wskazuje trendy, ku jakim zmierza cena. Obrazuje procentową zmianę ceny z obecnej sesji do ceny sprzed k sesji, gdzie wartość parametru k dla inwestycji średnioterminowych jest najczęściej podawana jako 10, zaś dla krótkoterminowych jako 5.
Metoda obliczenia ROC
Wartość wskaźnika ROC określa się za pomocą wzoru:
〖ROC〗_(n,k)=(P_n-P_(n-k))/P_(n-k)   					{2.1 }
gdzie: 
〖ROC〗_(n,k) – wartość wskaźnika zmian ROC dla n-tego notowania przy okresie k
P_n – cena z n-tego notowania,
P_(n-k) – cena z (n-k) -tego notowania tj. cena sprzed k okresów od n-tego notowania.

Interpretacja ROC
Analiza kształtowania się wskaźnika zmiany ROC pozwala na określenie, kiedy inwestor powinien zakupić bądź sprzedać instrument finansowy. Inwestor może spodziewać się wzrostu np. cen akcji (sygnał kupna), kiedy linia ROC przecina linię 0 od doły w górę. Natomiast momentem, gdy należy pozbywać się akcji (sygnał sprzedaży) jest przecięcie linii MACD przez linię sygnalną od góry w dół. 
 

Dane
Do przeprowadzonej symulacji użyto dane notowań spółki z Sunex SA., czołowego producenta m.in. pomp ciepła, z okresu od 25.03.2019 do 27.03.2023. Jak wcześniej zostało wspomniane, analizowane były dane dla otwarcia i zamknięcia.
Dla analizowanych danych pola na osi ox odpowiadają kolejnym dniom:
Pole	Dzień	      Uwagi
0	    2019-03-25	
100	  2019-08-27	
200	  2020-01-24	24.01.2020 pierwszy przypadek zakażenia covid w Europie
                  10.03.2020 pierwsze obostrzenia w Polsce
300	  2020-06-18	
400	  2020-11-05	
500	  2021-04-06	
600	  2021-08-26	
700	  2022-01-20  24.02.2022 zbrojna inwazja Rosji na Ukrainę
800	  2022-06-14	
900	  2022-11-04	
1000	2023-03-27	

Program zwrócił poniższe wykresy dla danych wejściowych:

![alt text](https://github.com/KrasodomskaAnna/stock_ratio_MACD_comparison/blob/main/chart_1.png?raw=true)
Wykres 1. Kurs akcji, wskaźniki MACD, SIGNAL oraz ROC na zamknięciu sesji w okresie od 25.03.2019 do 27.03.2023 r.

![alt text](https://github.com/KrasodomskaAnna/stock_ratio_MACD_comparison/blob/main/chart_2.png?raw=true)
Wykres 2. Kurs akcji, wskaźniki MACD, SIGNAL oraz ROC na otwarciu sesji w okresie od 25.03.2019 do 27.03.2023 r.
Przeprowadzona analiza wykazała, że najwyższą stopę zwrotu uzyskano dla 1000 obserwacji z podanego okresu (1464 dni) w przypadku wykorzystania wskaźnika ROC, a następnie MACD dla cen na zamknięciu i MACD dla cen na otwarciu każdej sesji giełdowej.
W przypadku ROC portfel o wartości 1000 zł zwiększył swoją wartość do 8 737,93 zł, co w skali roku oznacza stopę wzrostu na poziomie ok. 193% rocznie. Natomiast w przypadku MACD na zamknięciu wartość portfela dnia 27.03.2023 r. wyniosła 5259 zł, co dało stopę zwrotu na poziomie ok. 106% rocznie. Należy jednak zauważyć, że tak wysoka stopa zwrotu możliwa była do osiągnięcia dzięki temu, że w badanym okresie kurs akcji badanej spółki wzrósł dwudziestokrotnie od ok. 0,968 zł na początku badanego okresu do ok. 20,2 zł na koniec badanego okresu.
W badanym okresie nastąpiło wiele sytuacji, w których linia MACD przecięła się z linią Signal. Na poniższym wykresie zaprezentowano przykładowe momenty, wskazujące na sygnał kupna bądź sprzedaży akcji w roku 2020.
 
![alt text](https://github.com/KrasodomskaAnna/stock_ratio_MACD_comparison/blob/main/chart_3.png?raw=true)
Wykres 3. Kurs akcji, wskaźniki MACD i SIGNAL na zamknięciu sesji w okresie od 1.01.2020 do 31.12.2020 r.
Pomimo tego, że w praktyce kursy akcji podaje się na wykresach osobnych – w tym przypadku zastosowano jeden wykres, jednak przy różnych osiach dla oscylatorów i kursu akcji. Czerwoną strzałką oznaczono moment, w którym inwestor powinien dokonać zakupu akcji, a zieloną – sprzedaż. 
Przedstawione na wykresie sytuacje są dowodem na to, że analiza kształtowania się MACD i linii Signal pozwala trafnie ocenić prognozę dotyczącą zmiany trendu. Jednak nie zawsze tak było. W okresie kryzysu wywołanego zarówno pandemią COVID-19 jak również wojną na Ukrainie inwestorzy giełdowi brali pod uwagę ryzyko, które wiązało się w powstałą sytuacją. Niestety przyczyniło się to także, do takich ich zachowań, które zakłóciły trafność prognoz. Na kolejnym wykresie dotyczącym okresu od 1.01.2022 do 27.03.2023 zaznaczono te momenty czarną strzałką.
 
![alt text](https://github.com/KrasodomskaAnna/stock_ratio_MACD_comparison/blob/main/chart_4.png?raw=true)
Wykres 4. Kurs akcji, wskaźniki MACD i SIGNAL na zamknięciu sesji w okresie od 1.01.2022 do 27.03.2023 r.

Kolorami czerwonym i zielonym, tak jak poprzednio zaznaczono punkty w czasie, w którym analiza MACD przyniosła poprawne przewidywanie trendu. 

Analiza
Analiza techniczna wykorzystywana jest w krótkim i średnim okresie. Inwestorzy długoterminowi charakteryzujący się mniejszą skłonnością do ponoszenia ryzyka, oprócz narzędzi analizy technicznej, wykorzystują także analizę fundamentalną, która pozwala im dokonać wyboru właściwych spółek. Dzięki narzędziom analizy portfelowej konstruują w kolejnym etapie portfel inwestycyjny, dzięki któremu mogą ograniczyć ryzyko inwestycyjne.
Dokonując oceny przydatności analizy MACD należy podkreślić, że wszystkie narzędzia analizy technicznej oparte są na analizie popytu, podaży oraz czynników je determinujących. Istotne znaczenie odgrywają tutaj także czynniki behawioralne, związane z psychologią zachowań ludzkich, które także wpływają na podejmowane przez nich decyzje inwestycyjne. Moim zdaniem inwestor powinien brać pod uwagę wiele narzędzi analizy, w tym także analizy technicznej. Przeprowadzona analiza wskazała na to, że w przypadku akcji spółki Sunex wyższą stopę zwrotu osiągnięto wykorzystując wskaźnik ROC. Nie oznacza to jednak, że jest to lepszy wskaźnik. 
Na koniec warto zauważyć, że wskaźnik MACD jest zapewne kompleksowym rozwiązaniem, jednak inwestorzy najczęściej łączą jego wykorzystanie z innymi wskaźnikami analizy technicznej, np. oscylatorem stochastycznym lub wskaźnikiem ruchu kierunkowego ADX. Ważne znaczenie ma w tym przypadku jednak przeprowadzenie licznych testów obliczeniowych, które pozwoli na odpowiednie ustawienie parametrów. 

Dodatkowe informacje
Jak wcześniej zostało wspomniane, początkowo w obliczeniach wskaźnika MACD przyjęto, że liczy się go na podstawie obliczeń dla średnich 26-okresowych i 12-okresowych, jednak aktualnie uważa się, że można je wybierać dowolnie. W związku z tym, przy założeniu, że zmiana wartości długości okresów będzie generować liniowy wzrost wartości portfela zaproponowano algorytm genetyczny, który wybiera najlepsze wartości współczynników. Dla jednej z iteracji uzyskano wynik:
Best individual: [2, 50, 19]		# krotszy_okres, dluzszy_okres, signal_okres
Best solution value: 26058,71 zł
co daje wynik o rząd wielkości lepszy niż dla standardowych wartości.

Źródła
https://www.edukacjagieldowa.pl/gieldowe-abc/analiza-techniczna/narzedzia-analizy-technicznej/krzywa-macd/
https://www.fxmag.pl/edukacja/forex/oscylator-macd-wska%C5%BAnik-interpretacja
https://bossa.pl/edukacja/slownik/rate-change
https://pl.wikipedia.org/wiki/Wskaźnik_zmiany_ROC
https://www.skarbiec.pl/slownik/roc-rate-of-change-return-of-capital/ 
https://stooq.pl/
