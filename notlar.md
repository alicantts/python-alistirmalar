# Python Alıştırmaları Quiz Cevapları

Python ile yazılmış, terminalde çalışan basit bir hesap makinesi.


## Venv nedir, neden gerekir?

- Her projenin kendi kütüphanelerini ayrı tuttuğu bir klasördür.
- Her proje kendi kütüphane sürümlerini kullanır.
- Bir projede kurulan şey ötekini bozmaz ve bilgisayarın genel Python'u temiz kalır.


## requirements.txt nedir ve nasıl oluşturulur?

- Projenin ihtiyaç duyduğu kütüphanelerin ve sürümlerin yazıldığı txt dosyasıdır. 
- örn: colorama == 0.4.6/pluggy == 1.6.0\ pytest == 8.4.1 (sürüm numaraları güncellenebilir.)
- Venv klasörü Github'a gitmez ama  requirements.txt gider. Böylece projenin çalıştırılacağı bilgisayarda aynı kütüphaneler tek kodla kurulabilir. 
- Önce proje klasörüne proje dosyalarıyla aynı hizada requirements.txt dosyası oluşturulup içine igili kütüphaneler eklenir.
- Ardından Git'e commitlenip push edilir. 




## Bir fonksiyonda print ile return farkı nedir?

- Return fonksiyonun o return komutundaki istenen şeyi yapar.
- Fonksiyon çağrıldığna return ifadesindeki işlem yapılır.
- Örneğin bir değişkene değer atama, bir ifade print etme.
- Print ise sadece yazma işlem yapar.
- Değer atama vs. yapamaz.
- Fonksiyon çağrıldığında print işlemi yapar.

