import json
import os
import requests
import pandas as pd
import re

def get_item_emoji_dict():
    d = {
        "ACUR": "π₯",
        "ANANAS": "π",
        "ARMUT DEVECI": "π",
        "ARMUT MUHT": "π",
        "ARMUT S.MARIA": "π",
        "ARMUT AKΓA": "π",
        "AVAKADO": "π₯",
        "BAMYA": "π’",
        "BIBER DOLMA": "π’",
        "BIBER KIL ACI": "π’",
        "BIBER SIVRI": "π’",
        "BIBER TATLI(ΓARLΔ°STON)": "π’",
        "BIBER KIRMIZI": "πΆ",
        "BORULCE": "π’",
        "BROKOLI": "π₯¦",
        "CILEK": "π",
        "DARI(ADET)": "π½",
        "DENIZ BΓRΓLCESΔ°": "π’",
        "DOMATES BEEF": "π",
        "DOMATES SALKIM": "π",
        "DOMATES SERA": "π",
        "DOMATES TARLA": "π",
        "DOMATES CHERRY": "π",
        "DOMATES PEMBE": "π",
        "DOMATES SALΓALIK(RΔ°O)": "π",
        "ELMA AMASYA": "π",
        "ELMA ARJANTΔ°N": "π",
        "ELMA GOLDEN": "π",
        "ELMA STARKING": "π",
        "ELMA GSMIT(Δ°THAL)": "π",
        "ELMA MUHTELΔ°F": "π",
        "ELMA STARKING(Δ°THAL)": "π",
        "ERIK ANJELIKA": "π£",
        "ERIK MUHTELΔ°F": "π’",
        "FASULYE AYSE": "π’",
        "FASULYE BARBUN": "π£",
        "FASULYE CALI": "π’",
        "HAVUC": "π₯",
        "HINDISTAN CEVIZI": "π₯₯",
        "INCIR BARDACIK": "π’",
        "ISPANAK": "π’",
        "KABAK TAZE": "π’",
        "KARPUZ": "π",
        "KAVUN TARLA": "π",
        "KAYISI MUHT": "π‘",
        "KIRAZ SALIHLI": "π",
        "KIVI YERLI": "π₯",
        "LAHANA BEYAZ": "π’",
        "LAHANA KIRMIZI": "π’",
        "LIMON DOKME": "π’",
        "LIMON LAMAS": "π’",
        "MANTAR": "π’",
        "MARUL": "π’",
        "MARUL AYSBERG": "π’",    
        "MARUL KIVIRCIK": "π’",
        "MARUL LOLOROSSO": "π’",
        "MUZ ITHAL": "π’",
        "MUZ YERLI": "π’",
        "NEKTARIN BEYAZ": "π’",
        "NEKTARIN KIRMIZI": "π’",
        "PANCAR": "π’",
        "PATATES CALMA": "π’",
        "PATATES TAZE(YIKANMIΕ)": "π’",
        "PATLICAN UZUN": "π’",
        "PATLICAN TOPAN": "π’",
        "PAZI": "π’",
        "PORTAKAL MUHT": "π’",
        "SALATALIK KASA": "π’",
        "SALATALIK SΔ°LOR": "π’",
        "SARIMSAK Δ°THAL": "π’",
        "SARIMSAK KURU": "π’",
        "SEMIZ OTU": "π’",
        "SOGAN KIRMIZI": "π’",
        "SOGAN KURU": "π’",
        "SOGAN TAZE": "π’",
        "ΕEFTALI": "π’",
        "TURP KIRMIZI": "π’",
        "ΓZΓM BEYAZ": "π’",
        "ΓZΓM SΔ°YAH": "π’",
        "VISNE": "π’",
        "Y.DEREOTU": "π’",
        "Y.MAYDONOZ": "π’",
        "Y.NANE": "π’",
        "Y.ROKA": "π’"
    }

    return pd.DataFrame.from_dict(d,orient="index",columns=['symbol']).reset_index().rename(columns={'index':'MalAdi'})

def get_prices(date_str):
    the_url = os.path.join("https://openapi.izmir.bel.tr/api/ibb/halfiyatlari/sebzemeyve",date_str)
    d = requests.get(url=the_url,verify=False).json()

    emoji_df = get_item_emoji_dict()

    df = pd.DataFrame.from_dict(d['HalFiyatListesi'])
    df['MalAdi'] = df.apply(lambda row: re.sub("\s+"," ",row['MalAdi']),axis=1) 
    df = df.merge(emoji_df,on="MalAdi",how='left')[['symbol','MalAdi','Birim','OrtalamaUcret','AsgariUcret','AzamiUcret','MalTipAdi']]

    return df

if __name__ == "__main__":
    get_prices("2021-08-13")