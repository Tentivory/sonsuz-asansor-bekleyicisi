import time
import random

def sonsuz_asansor():
    """Dünyanın en yavaş asansörü. Hiçbir yere varmaz, sadece bekletir."""
    print("Asansör çağırıldı... (Bürokrasi modu aktif)")
    katlar = ["Zemin", "1. Kat", "2. Kat", "Çatı", "Gizli Kat (Sadece Özel Kişiler)"]
    
    while True:  # Sonsuza kadar, çünkü bu asansör öyle
        mevcut_kat = random.choice(katlar)
        print(f"Asansör {mevcut_kat} katında. Kapı açılıyor... (veya açılmıyor)")
        time.sleep(random.uniform(2, 5))  # Gerçekçi bekleme
        print("Kapı kapanıyor. Bir sonraki durağa gidiliyor... belki.")
        time.sleep(1)
        if random.random() < 0.1:
            print("UYARI: Asansör kısıldı! Teknik ekip yolda. (Tahmini varış: 3 iş günü)")
            # Gizli siyasi not: Bürokrasi her yerde, asansör bile.
            time.sleep(3)

if __name__ == "__main__":
    print("=== SONSUZ ASANSÖR SİMÜLATÖRÜ v1.0 ===")
    print("Çıkmak için Ctrl+C. Ama çıkamazsın, çünkü sonsuz.")
    try:
        sonsuz_asansor()
    except KeyboardInterrupt:
        print("\nAsansörden indin. Tebrikler, hayatta kaldın.")
