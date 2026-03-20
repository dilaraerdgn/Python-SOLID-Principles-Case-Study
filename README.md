# Python-SOLID-Principles-Case-Study
Mevcut bir sistemdeki tasarım kusurlarını tespit etmek ve bu kusurları temiz kod (Clean Code) standartlarına uygun hale getirmektir. Proje içerisinde hem uygulama kodları hem de teknik analiz raporu yer almaktadır.

# Python ile SOLID Prensipleri Uygulaması

Bu proje, bir raporlama sisteminin **SOLID** (Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion) prensiplerine uygun olarak nasıl yeniden yapılandırılacağını gösteren bir vaka çalışmasıdır (case study).


## Uygulanan Prensipler
- **Interface Segregation:** `IDatabaseConnector`, `IDataSaver`, `INotifier` gibi küçük ve özelleşmiş arayüzler kullanılarak gereksiz bağımlılıklar önlenmiştir.
- **Dependency Inversion:** `ReportManager` sınıfı doğrudan somut sınıflara değil, soyut arayüzlere (Abstractions) bağımlıdır.
- **Single Responsibility:** Her sınıfın (MySQLConnector, EmailSender vb.) yalnızca tek bir görev tanımı vardır.
  Kalanını dilerseniz **Solid_Inceleme_Raporu**'ndan okumaya devam edebilirsiniz.

## Analiz Raporu
Kodun ilk halindeki eksiklikler ve yapılan iyileştirmelerin detaylı anlatımı için raporu inceleyebilirsiniz:

📄 **[SOLID Inceleme Raporu.pdf](./reports/SOLID_Inceleme_Raporu.pdf)**

---
*Bu çalışma, sürdürülebilir yazılım mimarileri geliştirme yetkinliğimi sergilemek amacıyla hazırlanmıştır.*
