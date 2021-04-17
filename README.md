# Shodan_Search
Based on the Shodan API, it displays the open ports and security vulnerabilities of the server related to the entered ip or hostname.

"Shodan_Search" programı "Shodan Api"sine dayanan bir zafiyet arama programıdır. Ip'si ya da hostname'i bilinen sunucunun açık portlarını ve varsa güvenlik açıklarını "Shodan"a ait veritabanından python aracılığıyla çekerek kullanıcıya gösterir. Ayrıca istenirse, verilen network aralığındaki IP ve açık  port bilgilerini de getirir. Aşırı veri alışverişini önlemek için network taramalarında gösterilen IP sayısı 100 ile sınırlandırılmıştır. Sadece Python scripti olarak değil, tam anlamıyla derlenecek bir program olarak tasarlanmıştır.

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



Önemli Not
--------------
Programın çalışabilmesi için "Shodan Api Key"e sahip olunması gerekir.
Bunun için "shodan.io" web sitesine gidilerek üye olunması gerekir. 
Bu üyelikten sonra kullancı hesabına ("My Account") gidilerek "Shodan Api Key" öğrenilir.


Shodan api key örneğine ait ekran görüntüsü aşağıdadır.
![Shodan_Api_Key](https://user-images.githubusercontent.com/71177413/115117003-2d198700-9fa5-11eb-8811-de91c21ded2e.JPG)

Bu "api key"i kaynak kodda görülen "Shodan_Api_Key.txt" adlı dosyanın içerisine kaydedilmelidir. 



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
