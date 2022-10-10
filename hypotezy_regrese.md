# Testování hypotéz

Hypotézou obecně myslíme nějaké tvrzení. Testování hypotéz se zabývá ověřením, zda je nějaká hypotéza platná. Při testování hypotéz předpokládáme, že máme k dispozici nějaký vzorek dat, nikoli kompletní data. To vnáší prvek určité nejistoty.

Vraťme se k prvnímu příkladu - srovnávní voleb a předvolebního průzkumu. Uvažujme tvrzení, že má různou podporu voličů v Praze než v Brně. Pokud se díváme na skutečný výsledek voleb, jasně vidíme, kolik strana ve volbách získala v obou městech. Pokud provádíme předvolební průzkum, pracujeme s nějakým vzorkem (výběrem) z populace, který má např. 500 lidí v obou městech. To přináší do našeho zkoumání nejistotu. Může se například stát, že jsme (čistě náhodou) do našeho průzkumu v jednom městě vybrali lidi, kteří mají danou stranu více rádi, než zbytek města.

Uvažujme například následující výsledky:

- V Praze podporuje danou stranu 40 % lidí a v Brně pouze 5 %. V takovém případě bychom se asi intuitivně shodli, že podpora v Praze je vyšší.
- V Praze podporuje danou stranu 10 % lidí a v Brně 50 %. V takovém případě bychom se asi intuitivně shodli, že podpora v Brně je vyšší.
- V Praze podporuje danou stranu 26 % lidí a v Brně 25 %. Zde už výsledek není jednoznačně, protože rozdíl je opravdu malý. Znamená 1 procentní bod rozdílu v našem průzkumu opravdu, že se podpora voličů liší? Co když se nám pouze náhodou do našeho vzorku v Praze dostalo více podporovatelů dané strany.

Právě na posledním příkladě se ukazuje, proč je testování hypotéz užitečné. Nedokáže sice jednoznačně říct, zda je hypotéza pravdivá, může nám ale říct, s jakou pravděpodobností je pravdivá nebo s jako pravděpodobností se mýlíme.

Vrátíme-li se k našemu souboru o cenách domů. Náš datový soubor určitě neobsahuje informace o všech domech v USA, ale pouze o některých, tj. o nějakém výběru domů. Pokud bychom tedy chtěli ověřit nějaká tvrzení o všech domech, opět se dostaneme do roviny testování hypotéz.

- Domy s bazénem jsou v průměru dražší než domy bez bazénu.
- Cena domu je ovlivněna jeho obytnou plochou.
- Ceny domu ve středně hustě zalidněných oblastech jsou méně různorodé než ceny domů ve velmi hustě zalidněných oblastech.
- Průměrná cena pozemků je různá pro různé typy umístění pozemku v zástavbě.

Testování hypotéz má pevný postup, který se skládá z následujících kroků:

* Formulace statistických hypotéz.
* Výběr vhodného testu.
* Výpočet hodnoty testového kritéria.
* Rozhodnutí o platnosti nulové hypotézy.

## Formulace statistických hypotéz

Při testování hypotéz vždy nejprve definujeme dvě hypotézy - **nulovou** a **alternativní**. Tyto dvě hypotézy musí být vždy ve sporu, tj. nemůže nastat situace, že by byly obě pravdivé. Nulová hypotéza v sobě má často znaménko *rovná se*, alternativní pak mívá znaménko *nerovná se*, *větší než* nebo *menší než*. Dále můžeme v nulové hypotéze tvrdit, že mezi dvěma sloupci v tabulce není závislost, a alternativní hypotéza bude říkat, že závislost existuje.

Navažme na předchozí lekci, kde jsme měřili sílu statistické závislosti mezi cenou domu a obytnou plochou. Hodnotu korelačního koeficientu sice známe, ale ta nám toho sama o sobě tolik neřekne. Nyní budeme chtít ověřit, že je vliv velikosti obytné plochy na cenu domu **statisticky významný**, tj. rozhodneme, zda tento vliv není čistě náhodný. 

Uvažujme následující dvojici hypotéz:

- Nulová hypotéza: Obytná plocha domu a jeho cena jsou lineárně nezávislé.
- Alternativní hypotéza: Obytná plocha domu a jeho cena jsou lineárně závislé.

Je zřejmé, že obě hypotézy nemohou být pravidivé.

Poněkud nepříjemnou zprávou pro vás může být informace, že výsledek našeho testu může být chybný, a to i v případě, že jsme postuovali správně. Může se totiž stát, že prostě máme smůlu na náš vzorek, který nereprezentuje data úplně správně.

Při testování se můžeme dopustit 2 chyb, které jsou popsány v tabulce níže.

|   | Nulová hypotéze platí | Nulová hypotéza neplatí |
|---|---|---|
| **Nezamítáme nulovou hypotézu** | Správný výsledek | Chyba II. druhu |
| **Zamítáme nulovou hypotézu**  | Chyba I. druhu | Správný výsledek |

Při testování hypotéz si zpravidla vybíráme pravděpodobnost, s jakou se chceme dopustit chyby I. druhu. Pravděpodobnost chyby I. druhu označujeme jako **hladinu významnosti**.

## Výběr vhodného testu

Dále zvolíme vhodný test pro ověření naší hypotézy. Výběr vhodného testu obvykle závisí na typu hypotézy, který testujeme. Dále musíme respektovat, že každý test má nějaké **předpoklady**. Vraťme se k výběru korelačního koeficientu. Pandas ve výchozím nastavení používá tzv. Pearsonův korelační koeficient. Pokud bychom s jeho pomocí chtěli ověřit, zda je vliv jedné veličiny na druhou statisticky významný, je potřeba pamatovat na to, že test hypotézy o závislosti za pomocí Pearsonova korelačního koeficientu **předpokládá, že data mají normální rozdělení** (normalitu dat).

Pokud si nejsme jisti, zda je tento předpoklad splněn, můžeme opět použít testování hypotéz.

### Test normality dat

Testujeme-li normalitu dat, formulujeme hypotézy následujícím způsobem:

- Nulová hypotéza: Data mají normální rozdělení.
- Alternativní hypotéza: Data nemají normální rozdělení.

Pro ověření normality dat existuje řada testů. Oblíbený je například Shapiro-Wilk test, který je součástí modulu `scipy`.
