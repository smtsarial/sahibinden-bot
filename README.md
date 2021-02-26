# sahibinden-bot
sahibinden için ilan bulucu karşılaştırıcı aradığınızı bulduracak discord botu.

Öncelikle merhabalar, bu kodları sadece işinizi kolaylaştırması ve hızlı bir şekilde yenilik var mı diye incelemenizi sağlayacak şekilde yaptım hiçbir ticari amaç yoktur ayrıca bunları görsel açıdan websitesi üzerinden rahatlıkla yapabilirsiniz.

# Kurulum ve Süreçler

Sahibinden.com yurt dışından gelen kullanıcılar için bir kapalı kutu olduğu için uygulamam python application services üzerinde çalışmamaktadır. Hem sizin iyiliğiniz hem de bahsettiğim bu konudan dolayı programı kendi bilgisayarınız üzerinden çalıştırmanız önerilir.



![image](https://github.com/smtsarial/sahibinden-bot/blob/main/images/token.png)

Buradaki linkten https://discord.com/developers/applications application sayfasına ulaşabilirsiniz.

Eğer bir botunuz yoksa yenisini oluşturun ve token kodunu kopyalayın ! 

![image](https://github.com/smtsarial/sahibinden-bot/blob/main/images/token_key.png)


Aldığınız token adresini kodun en sonunda bulacağınız bloga resimdeki gibi yapıştırın.

# Çalıştırma

Bu kurulu yaptığınızda requirements.txt içeriğini python install yaparak kurmalısınız. Ve kurulumunu yaptığınız botu sunucunuza çağırmayı unutmayın.
Daha sonra bot.py çalıştırınca discord üzerinden aktif olacaktır geçerli komutları kullanarak işlem yapabilirsiniz.

!komutlar size nasıl kullanılacağınız anlatacaktır!

Tüm dosyaların Aynı dizinde olduğuna ve requirements.txt kurulduğuna EMİN OLUN !


# NASIL ÇALIŞIYOR
bot.py -> Discord ile olan bağlantımızı yapıyor komutlara göre size linkleri döndürüyor.

vitrin.py -> istediğiniz komuta göre size son 1 sayfadaki en güncel araçları ilanları getirecek. 

Bunları yaparken request ile siteye ulaşıp bs4 ile verileri okuyorum.
![image](https://github.com/smtsarial/sahibinden-bot/blob/main/images/1.png)
![image](https://github.com/smtsarial/sahibinden-bot/blob/main/images/2.png)
![image](https://github.com/smtsarial/sahibinden-bot/blob/main/images/3.png)
