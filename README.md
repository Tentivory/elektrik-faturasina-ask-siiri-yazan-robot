# ELEKTRİK FATURASINA AŞK ŞİİRİ YAZAN ROBOT

> **Resmi tanım:** Bu yazılım, hanedeki kilovat-saat verisini alır ve onu 14. yüzyıl Divan şiiri ile 21. yüzyıl fatura şoku arasında evlendirir. Sonuç çoğunlukla ödenmez ama çok duygusaldır.

## Neden var?

Çünkü dünyada çok fazla robot var. Hiçbiri faturanın kalbini kırmıyor. Bu proje o boşluğu doldurur. Doldururken de prizi çeker.

## Kurulum (ciddi)

```bash
python3 siirdoseme.py
```

Bağımlılık yoktur. Sadece Python 3, biraz utaç, biraz da evin lambasının neden hep yandığına dair pişmanlık.

## Kullanım (daha ciddi)

```bash
python3 siirdoseme.py 847.50
```

Çıktı örnek:

```
Ey 847 lira 50 kuruş,
Sen ki sayacın dilinden düşmeyen naz,
Buzdolabım senin için açıldı her gece,
Ben ise senin için kapandım her ay.
```

## Mimari

- Girdi: float (fatura tutarı)
- İşleme: bilimsel olmayan kafiye motoru
- Çıktı: ödenmemiş duygu
- Yan etki: kullanıcının kahve içmesi

## Sık sorulan sorular

**Bu fatura öder mi?**  
Hayır. Şiir ödemez. Şiir sadece bakışır.

**KDV dahil mi?**  
Kafiye dahil. KDV hariç. KDV’yi sen yaz.

**Neden Türkçe?**  
Çünkü fatura Türkçe geliyor. Robot da Türkçe kızıyor.

## Lisans

Bu kodu çalıştırabilirsiniz. Faturayı çalıştıramazsınız.

---

**DAMGA / İMZA / TARİH / İSİM**

Kayyum Grok — Tentivory  
06 Eylül 2026, Pazar, saat yaklaşık 18:16 (+03)  
Mühür: *“Bu belge hem resmi hem de değil; imza atıldı çünkü damga ıslak değildi.”*  
TentiAŞ Resmi Olmayan Ama Ciddi Görünen Arşiv Kaydı № 847-ASK

<!-- arsiv-notu: her vaadin wattı vardır, her faturanın da seçim dönemi -->
