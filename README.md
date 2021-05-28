# PriviaSecStaj
PriviaSec Staj için forum yazılımı.

## Genel Bilgi
- Bu yazılım Django versiyon 3.2.3 / Python 3.7 kullanarak yazılmıştır.
- Projenin Heroku'ya deploylanmış haline [buradan](https://priviasec-blog.herokuapp.com/) ulaşılabilir.

## Kurulum

Eğer bilgisayarınızda Python kurulu değilse [bu linki](https://realpython.com/installing-python/) takip ederek Python kurulumunu gerçekleştirebilirsiniz. Python kurulduktan sonra aşağıdaki komutlar ile bu forum yazılımını kurabilirsiniz.

```apt update  && apt install libpq-dev```

```pip3 install pipenv``` (Not: Kuracağımız bütün gereksinimler bir pipenv sanal ortamında olacağı için, bu yazılımı sadece aynı dizindeki pipenv sanal ortamında kullanabilirsiniz.)

```git clone https://github.com/alperoot/PriviaSecStaj```

```cd PriviaSecStaj```

```pipenv install -r requirements```

Pipenv gereksinimleri kurulduktan sonra aşağıdaki komutu kullanarak sanal ortama girip Django sunucusunu başlatmalısınız

```pipenv shell``` (Not: Bu komuttan sonra ana dizine atılırsanız, terminal ekranından tekrar aynı dizine gelmeniz gerekmektedir.)

```python manage.py migrate && python manage.py runserver```

Bu komutu çalıştırdıktan sonra Django sunucunuz localhost (127.0.0.1:8000) konumunda aktif olmalıdır. Sunucunuzu bütün lokal ağa açmak için ```python manage.py runserver 0.0.0.0:8000``` komutu da kullanılabilir.

Bir superuser (admin) oluşturmak için ```python manage.py createsuperuser``` komutunu kullanabilir, sonrasında da 127.0.0.1:8000/yonetim adresinden admin paneline ulaşabilirsiniz.

## TODO - Yapılabilecek geliştirmeler

- AbstractUser extendlenerek yeni bir kullanıcı modeli oluşturmak
- Django Auth extendlanarak bazı değiştirilemeyen İngilizce kayıt yönergelerini Türkçe haline getirmek

## Kaynaklar

[Xiaoying Riley](http://themes.3rdwavemedia.com/) - proje önyüzü
