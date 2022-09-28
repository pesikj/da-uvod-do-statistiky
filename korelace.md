# Korelace

Modul `pandas` samozřejmě umí vypočítat základní statistické ukazatele, které jsme si ukazovali.
Pro základní přehled o datech může být zajímavá metoda `describe()`, která nám zobrazí hodnoty všech
základních ukazatelů najednou.

Abychom získali data pro tuto kapitolu, načteme si informace o ceně akcií společnosti Microsoft s pomocí
modulu `yfinance`, který stahuje data ze služby Yahoo Finance. Protože je jeho název poměrně dlouhý, budeme používat
zkratku `yf`. Pro získání dat musíme znát kód každé akcie (akcie Microsoftu používají na new yorské burze MSFT).

```py
import pandas


msft = yf.Ticker("MSFT")
msft_df = msft.history(period="1y")
msft_df.describe()
```

Modul `yfinance` vrací informace o otevírací, nejvyšší, nejnižší a uzavírací ceně pro každý den, objemu provedených obchodů, vyplacených dividendách a tzv. splitech, tedy rozdělení akcie.

V řádku `50 %` vidíme medián. Toto podivné označení vychází z toho, že 50 % hodnot v souboru je menších a 50 % větších než medián. Obecně ale můžeme chtít zjistit podobnou informaci pro jakékoli jiné procento. Takovým hodnotám se říká kvantily a řádek `25 %` označuje hodnotu, pro kterou platí, že 25 % hodnot v souboru je menších a 75 % větších. Vezmeme-li dohromady `25 %` a `75 %`, máme meze, ve kterých se hodnota akcie nacházela 50 % času. Podobnou informaci zobrazuji graficky nám již známý krabicový graf.

Pojďme si načíst ještě informace o akciích společnosti Apple (APPL).

```py
aapl = yf.Ticker("AAPL")
aapl_df = aapl.history(period="1y")
```

U cen akcií bývá důležité, jak moc jsou provázané, tj. jestli ceny akcií mají tendenci růst a klesat společně, jestli se pohybují obráceně či jsou nezávislé. Propojíme nejprve ceny obou akcií do jedné tabulky. Dáleoužijeme metodu `pct_change()`, která vypočítá procentuální změny hodnoty akcie. Poté zkusíme zobrazit data v grafu, kde na jedné ose budeme procentuální změnu ceny akcie Microsoftu a na druhé procentuální cenu akcie Apple.

Vztah těchto dvou akcií již rozhodně není tak silný. Rozhodování na základě grafu by ale pro větší množství akcií bylo nereálné, proto můžeme využít číselný ukazatel, který označujeme jako korelace. Korelace je měřítko *lineární závislosti* mezi dvěma veličinami. Nabývá hodnot v intervalu -1 až 1. Hodnoty blízké 1 znamenají silnou přímou lineární závislost, hodnoty blízké -1 silnou nepřímou lineární závislost a hodnoty blízké 0 lineární nezávislost.

Korelaci mezi všemi sloupci v tabulce získáme pomocí metody `corr()`.
