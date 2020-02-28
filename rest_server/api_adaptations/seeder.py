from faker import Faker
from .models import Movie, GENRES
from api_books.models import Book
import random

fake = Faker()


def fake_movies(num_movies=100, overwrite=False):
    if overwrite:
        print("Overwritnig existing data")
        Movie.objects.all().delete()

    t1 = ["Tajemnica", "Śmierć", "Kod", "Zabójstwo", "Śledztwo", "Proces",
          "Gra", "Bogactwo", "Teoria", "Miłość", "Dane", "Szyfry", "Zagadka",
          "Manipulacja", "Szansa", "Żal", "Broń", "Zdrowie", "Herezja",
          "Porwanie", "Poszukiwania", "Zabawa", "Programy", "Pieniądze",
          "Komunikat", "Leczenie", "Psychoterapia", "Rozrywka", "Ból",
          "Dziewczyny", "Chłopaki", "Druhny", "Rodzice", "Dzieci", "Dziadkowie",
          "Narzeczone", "Żony", "Szaleńcy", "Prześladowcy", "Smutek", "Zabawki",
          "Samotność", "Krew"]

    t2 = ["Afrodyty", "Da Vinci", "ucznia", "Newtona", "Einsteina", "rycerza",
          "wojownika", "lęku", "sportowców", "komputerów", "nauki",
          "czarownic", "kierowców", "żołnierzy", "przyrody",
          "dla profesjonalistów", "naukowców", "zwierząt", "w Kosmosie",
          "na bogato", "w Polsce", "w Azji", "w Afryce", "w Europie", "w Ameryce",
          "we współczesnym świecie", "w górach", "nad morzem", "na rynku",
          "w polityce", "Polaków", "Europy", "na wojnie", "dla każdego",
          "w weekend", "w twoim domu", "lekarzy", "królów", "prezydentów",
          "zapomnianych", "Złego", "bogów", "szpiega", "w deszczu",
          "tyrana", "milionerów", "w wielkim mieście", "dla dzieci",
          "w ciemności"]

    for i in range(num_movies):
        title = f'{random.choice(t1)} {random.choice(t2)}'
        director = f'{fake.first_name()} {fake.last_name()}'
        date = fake.date()
        genre = random.choice(GENRES)[0]
        books = list(Book.objects.all())
        book = random.choice(books)
        movie = Movie.objects.create(
            title=title,
            director=director,
            date=date,
            genre=genre,
            book=book
        )

        movie.save()
