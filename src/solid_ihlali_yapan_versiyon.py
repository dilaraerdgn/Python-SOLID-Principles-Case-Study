# Herhangi bir arayüz (Interface) veya soyutlama (ABC) yok.
# Sınıflar birbirine göbekten bağlı.

class ReportManager:
    def __init__(self):
        # HATA: Bağımlılıklar sınıf içinde oluşturuluyor (Dependency Inversion İhlali)
        # Sadece MySQL ile çalışabilir, başka veritabanı eklemek için kodu bozmak gerekir.
        self.db_type = "MySQL"

    def process_all(self, data):
        # HATA: Veritabanı bağlantısı, raporlama, e-posta ve PDF işlemleri tek bir metodda.
        # (Single Responsibility İhlali)
        
        # 1. Veritabanına bağlan
        print(f"{self.db_type} veritabanına bağlanıldı.")

        # 2. Rapor oluştur (Mantık buraya gömülü)
        print("Rapor oluşturuluyor:", data)
        report = f"Rapor: {data}"

        # 3. Veriyi kaydet
        print(f"Veri {self.db_type} veritabanına kaydediliyor:", data)

        # 4. E-posta gönder (Başka bir bildirim yöntemi eklemek imkansız)
        print("E-posta gönderiliyor:", report)

        # 5. PDF oluştur
        print("PDF dosyası oluşturuldu:", report)

if __name__ == "__main__":
    # Kullanıcı nesneleri yönetemiyor, manager her şeye kendisi karar veriyor.
    manager = ReportManager()
    manager.process_all("veri kümesi")
