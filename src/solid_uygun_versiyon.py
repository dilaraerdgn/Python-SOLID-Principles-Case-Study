from abc import ABC, abstractmethod


class IDatabaseConnector(ABC):
    @abstractmethod
    def connect(self):
        pass

class IDataSaver(ABC):
    @abstractmethod
    def save(self, data):
        pass

class INotifier(ABC):
    @abstractmethod
    def send(self, report):
        pass

class IExporter(ABC):
    @abstractmethod
    def export(self, content):
        pass




class MySQLConnector(IDatabaseConnector):
    def connect(self):
        print("MySQL veritabanına bağlanıldı.")

class MySQLSaver(IDataSaver):
    def save(self, data):
        print("Veri MySQL veritabanına kaydediliyor:", data)

class EmailSender(INotifier):
    def send(self, report):
        print("E-posta gönderiliyor:", report)

class PDFExporter(IExporter):
    def export(self, content):
        print("PDF dosyası oluşturuldu:", content)



class ReportGenerator:
    def generate(self, data):
        print("Rapor oluşturuluyor:", data)
        return f"Rapor: {data}"



class ReportManager:
    def __init__(
        self,
        connector: IDatabaseConnector,
        saver: IDataSaver,
        generator: ReportGenerator,
        notifier: INotifier,
        exporter: IExporter
    ):
        self.connector = connector
        self.saver = saver
        self.generator = generator
        self.notifier = notifier
        self.exporter = exporter

    def process_all(self, data):
        self.connector.connect()
        report = self.generator.generate(data)
        self.saver.save(data)
        self.notifier.send(report)
        self.exporter.export(report)



if __name__ == "__main__":
    connector = MySQLConnector()
    saver = MySQLSaver()
    generator = ReportGenerator()
    notifier = EmailSender()
    exporter = PDFExporter()

    manager = ReportManager(connector, saver, generator, notifier, exporter)
    manager.process_all("veri kümesi")
