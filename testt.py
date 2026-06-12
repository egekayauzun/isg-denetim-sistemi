from ultralytics import YOLO

# Yeni ofis modelini çağırıyoruz
model = YOLO('yofficebest.pt')

# İçindeki gerçek sınıf isimlerini ve sıralamasını ekrana basıyoruz
print(model.names)