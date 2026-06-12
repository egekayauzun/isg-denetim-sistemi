import cv2
from ultralytics import YOLO

# 1. Modeli yükle
model = YOLO('best.pt')

# 2. Test edeceğin fotoğraf
resim_yolu = 'ornek1.jpg' 
img = cv2.imread(resim_yolu)

# 3. Tahmin yap (Normal seviye olan 0.35'e geri çekelim ki gereksizleri yazmasın)
results = model.predict(source=resim_yolu, conf=0.50)

# 4. DATA.YAML SIRALAMASI
sinif_isimleri = {
    0: 'Person', 
    1: 'Shoe Covers', 
    2: 'Surgical Cap', 
    3: 'Surgical Gloves', 
    4: 'Surgical Gown', 
    5: 'Surgical Mask', 
    6: 'Surgical Scrubs', 
    7: 'face-shields', 
    8: 'no-facial-gear', 
    9: 'no-medical-attire', 
    10: 'no-surgical-cap', 
    11: 'no-surgical-gloves'
}

# --- TERMİNAL RAPORU BAŞLANGICI ---
print("\n" + "="*40)
print(" 🏥 SAĞLIK PERSONELİ DENETİM RAPORU 🏥")
print("="*40)

bulunan_nesneler = []

# 5. Çizim Aşaması
for box in results[0].boxes:
    x1, y1, x2, y2 = map(int, box.xyxy[0])
    cls = int(box.cls[0])
    conf = float(box.conf[0])
    
    label = sinif_isimleri.get(cls, f"ID:{cls}")
    
    # Bulunan nesneyi listeye ekle
    bulunan_nesneler.append(f"> {label} (Güven Oranı: %{conf*100:.0f})")
    
    # "no-" ise Kırmızı, değilse Yeşil çerçeve
    if "no-" in label:
        color = (0, 0, 255)
    else:
        color = (0, 255, 0)

    # Sadece kutuları çizdiriyoruz (Yazıları ekrandan silebilir veya çok ince tutabilirsin)
    cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
    
    # Yazıların üst üste binmesi sorununu çözmek için yazıyı çok küçülttük
    # İstersen alttaki 2 satırı tamamen silip ekrandaki yazıları yok edebilirsin!
    cv2.putText(img, f"{label}", (x1, y1 - 5), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0,0,0), 2, cv2.LINE_AA)
    cv2.putText(img, f"{label}", (x1, y1 - 5), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.35, color, 1, cv2.LINE_AA)

# Listeyi terminale tertemiz yazdır
if len(bulunan_nesneler) > 0:
    for oge in bulunan_nesneler:
        print(oge)
else:
    print("> Uyarı: Herhangi bir nesne tespit edilemedi!")

print("="*40 + "\n")
# --- TERMİNAL RAPORU BİTİŞİ ---

# 6. Sonucu Göster
cv2.imshow("Denetim Ekrani", img)
cv2.waitKey(0)
cv2.destroyAllWindows()