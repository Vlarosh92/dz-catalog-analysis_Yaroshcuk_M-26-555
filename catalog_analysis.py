import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]
def average_rating(movies: list[dict]) -> float:
    """
    Функция считающая средний рейтинг по списку
    :param movies: Список
    :return: Среднее значение рейтинга
    """
    sum = 0
    count = len(movies)
    for m in movies:
        sum += m["rating"]
    return round(sum / count, 1) if count != 0 else "not movies in list"


def catalog_age_stats(movies: list[dict], current_year: int = 2026) -> tuple:
    """
    Функция выдающая возраст самого старого фильма, нового, а также средний возраст
    :param movies: Список, текущий год
    :return: кортеж(
        самый старый фильм в годах,
        самый новый фильм в годах,
        средний возраст фильмов в годах)
    """
    oldest = 0
    newest = 0
    medium = 0
    count = len(movies)
    for num, m in enumerate(movies):

        age = current_year - m["year"]
        medium += age
        # условие (or num==0) необходимо для инициализации первого значения вместо 0
        if oldest < age or num == 0:
            oldest = age
        if newest > age or num == 0:
            newest = age
    ret = (oldest, newest, math.ceil(medium / count))
    return ret if count != 0 else "not movies in list"

def duration_in_hours(minutes: int) -> str:
    """
    Функция переводит минуты в формат "Xч Yм"
    :param movies: duration_min из списка
    :return: строка в формате "Xч Yм"
    """
    hour = minutes // 60
    min = minutes % 60
    return f"{hour}ч {min}м"
