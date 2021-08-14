import json
import os
import requests
import pandas as pd
import re

def get_item_emoji_dict():
    d = {
        "ACUR": "🥒",
        "ANANAS": "🍌",
        "ARMUT DEVECI": "🍐",
        "ARMUT MUHT": "🍐",
        "ARMUT S.MARIA": "🍐",
        "ARMUT AKÇA": "🍐",
        "AVAKADO": "🥑",
        "BAMYA": "🟢",
        "BIBER DOLMA": "🟢",
        "BIBER KIL ACI": "🟢",
        "BIBER SIVRI": "🟢",
        "BIBER TATLI(ÇARLİSTON)": "🟢",
        "BIBER KIRMIZI": "🌶",
        "BORULCE": "🟢",
        "BROKOLI": "🥦",
        "CILEK": "🍓",
        "DARI(ADET)": "🌽",
        "DENIZ BÖRÜLCESİ": "🟢",
        "DOMATES BEEF": "🍅",
        "DOMATES SALKIM": "🍅",
        "DOMATES SERA": "🍅",
        "DOMATES TARLA": "🍅",
        "DOMATES CHERRY": "🍅",
        "DOMATES PEMBE": "🍅",
        "DOMATES SALÇALIK(RİO)": "🍅",
        "ELMA AMASYA": "🍎",
        "ELMA ARJANTİN": "🍏",
        "ELMA GOLDEN": "🍏",
        "ELMA STARKING": "🍏",
        "ELMA GSMIT(İTHAL)": "🍏",
        "ELMA MUHTELİF": "🍏",
        "ELMA STARKING(İTHAL)": "🍏",
        "ERIK ANJELIKA": "🟣",
        "ERIK MUHTELİF": "🟢",
        "FASULYE AYSE": "🟢",
        "FASULYE BARBUN": "🟣",
        "FASULYE CALI": "🟢",
        "HAVUC": "🥕",
        "HINDISTAN CEVIZI": "🥥",
        "INCIR BARDACIK": "🟢",
        "ISPANAK": "🟢",
        "KABAK TAZE": "🟢",
        "KARPUZ": "🍉",
        "KAVUN TARLA": "🍈",
        "KAYISI MUHT": "🟡",
        "KIRAZ SALIHLI": "🍒",
        "KIVI YERLI": "🥝",
        "LAHANA BEYAZ": "🟢",
        "LAHANA KIRMIZI": "🟢",
        "LIMON DOKME": "🟢",
        "LIMON LAMAS": "🟢",
        "MANTAR": "🟢",
        "MARUL": "🟢",
        "MARUL AYSBERG": "🟢",    
        "MARUL KIVIRCIK": "🟢",
        "MARUL LOLOROSSO": "🟢",
        "MUZ ITHAL": "🟢",
        "MUZ YERLI": "🟢",
        "NEKTARIN BEYAZ": "🟢",
        "NEKTARIN KIRMIZI": "🟢",
        "PANCAR": "🟢",
        "PATATES CALMA": "🟢",
        "PATATES TAZE(YIKANMIŞ)": "🟢",
        "PATLICAN UZUN": "🟢",
        "PATLICAN TOPAN": "🟢",
        "PAZI": "🟢",
        "PORTAKAL MUHT": "🟢",
        "SALATALIK KASA": "🟢",
        "SALATALIK SİLOR": "🟢",
        "SARIMSAK İTHAL": "🟢",
        "SARIMSAK KURU": "🟢",
        "SEMIZ OTU": "🟢",
        "SOGAN KIRMIZI": "🟢",
        "SOGAN KURU": "🟢",
        "SOGAN TAZE": "🟢",
        "ŞEFTALI": "🟢",
        "TURP KIRMIZI": "🟢",
        "ÜZÜM BEYAZ": "🟢",
        "ÜZÜM SİYAH": "🟢",
        "VISNE": "🟢",
        "Y.DEREOTU": "🟢",
        "Y.MAYDONOZ": "🟢",
        "Y.NANE": "🟢",
        "Y.ROKA": "🟢"
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