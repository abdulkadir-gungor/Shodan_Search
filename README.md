# Shodan_Search
Based on the Shodan API, it displays the open ports and security vulnerabilities of the server related to the entered ip or hostname.

"Shodan_Search" programı "Shodan Api"sine dayanan bir zafiyet arama programıdır. Ip'si ya da hostname'i bilinen sunucunun açık portlarını ve varsa güvenlik açıklarını "Shodan" ait veritabanından python aracılığıyla çekerek kullanıcıya gösterir. Ayrıca verilen network aralığındaki IP ve açık  port bilgilerini de getirir. Aşırı veri alışverişini önlemek için network taramamlarında gösterilen IP sayısı 100 ile sınırlandırılmıştır. Sadece Python scripti olarak değil, tam anlamıyla derlenecek bir program olarak tasarlanmıştır.

Programın derlenmiş çalışır haline ait video  "https://www.youtube.com/watch?v=BEOQeEUjMDo" adresine konmuştur.

Kaynak kodun derlenmiş ('exe' uzantılı) dosya hali https://drive.google.com/file/d/1w4j-7bkhSFA462YMX1Zx3fRqTT2q1peR/view adresine konulmuştur.
Rar şifresi "Gngr-V1.1".



Gereksinimler
------------------
Gerekli kütüphaneler: shodan, pyinstaller

pip install shodan

pip install pyinstaller

"pyinstaller" kodu tek parça çalıştırılabilir dosya haline getirmek için kullanılacak.



Kaynak Kodu Derlemek İçin
-----------------------------

>> pyinstaller --onefile  --icon=main.ico ShodanSearch.py


Kaynak Kodun Derlemiş Hali
---------------------------
Programın derlenmiş ve çalışır haline ait ekran görüntüleri verilmiştir.


[1 -Programın Ana Menüsü]

![n1](https://user-images.githubusercontent.com/71177413/115116407-0279ff00-9fa2-11eb-84c4-fbe4bd3fa249.JPG)


[2- IP scan]

![n3](https://user-images.githubusercontent.com/71177413/115116418-145ba200-9fa2-11eb-8486-7b0b56b0b0b9.JPG)


[3- Hostname scan]

![n4](https://user-images.githubusercontent.com/71177413/115116447-2e958000-9fa2-11eb-9cb6-77124dab5526.JPG)


[4- Hostname scan]

![n5](https://user-images.githubusercontent.com/71177413/115116453-3523f780-9fa2-11eb-936b-aacd4e52ba32.JPG)


[5- Network scan]

![n6](https://user-images.githubusercontent.com/71177413/115116472-48cf5e00-9fa2-11eb-81ac-8ac265cfd839.JPG)


[6- Network scan]

![n7](https://user-images.githubusercontent.com/71177413/115116484-5dabf180-9fa2-11eb-943d-3d7de956d1f5.JPG)


[7- Network scan]

![n8](https://user-images.githubusercontent.com/71177413/115116488-61d80f00-9fa2-11eb-8082-07a22e2c11be.JPG)






Yasal Uyarı
--------------------
Eğitim amacıyla hazırlanmıştır.

Kullanıcıların bazı kullanım şekilleri suça sebep olabilir.

Olumsuz durumlarla karşılaşmamak için "Yasal_Uyarı.txt" dosyasını okuyunuz.
