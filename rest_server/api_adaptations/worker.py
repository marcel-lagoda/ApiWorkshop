from faker import Factory
from random import choice
from .models import Movie, GENRES


def fake_movie(locale='en=US'):
    fake = Factory.create(locale)
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

    title = f'{choice(t1)} {choice(t2)}'
    director = f'{fake.first_name()} {fake.last_name()}'
    date = fake.date()
    genre = choice(GENRES)[0]

    m = Movie()
    m.title = title
    m.director = director
    m.date = date
    m.genre = genre
    print(m)
    m.save()

    def populate_db():
        locales = ["pl-PL", "en-US", "es-ES", "de-DE", "cs-CZ", "fr-FR", "it-IT",
                   "hr-HR", "nl-NL", "dk-DK", "fi-FI", "lt-LT", "pt-PT", "no-NO",
                   "sv-SE", "tr-TR"]
        for i in range(0, 100):
            loc = choice(locales)
            fake_movie(loc)

