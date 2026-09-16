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


#Этап 1. Разминка: переменные, числа, math

def average_rating(movies: list[dict]) -> float:
    """
    Функция считающая средний рейтинг по списку
    :param: list[dict] -> Список movies
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
    :param: list[dict] -> Список movies, int -> текущий год
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
    :param: int -> duration_min из списка
    :return: строка в формате "Xч Yм"
    """
    hour = minutes // 60
    min = minutes % 60
    return f"{hour}ч {min}м"

#Этап 2. Условия и match

def rating_tier(rating: float) -> str:
    """
    Функция определения категории рейтинга
    :param: float -> rating из списка movies
    :return: str, категория рейтинга
    """
    ret = ""
    if rating >= 9:
        ret = "шедевр"
    elif rating >= 7:
        ret = "хорошо"
    else:
        ret = "средне" if rating >= 5 else "слабо"
    return ret

def decade_label(year: int) -> str:
    """
    Функция возвращает метку по дате выхода фильма
    :param: int -> year из списка movies
    :return: str, возрастная метку
    """

    match year:
        case _ if year > 2020:
            return "новые"
        case _ if 2020 >= year >= 2015:
            return "недавние"
        case _:
            return "старые"

# Этап 3. Циклы

for m in movies:
    if "comedy" in m["genres"]:
        continue
    print(m["title"])

num = 0
while num < len(movies):
    if movies[num]["rating"] > 9.0:
        break
    num += 1
else:
    print("Шедевров не найдено")

def count_long_movies(movies: list[dict], threshold: int = 120) -> int:
    """
    Функция считает количество фильмов длиннее threshold минут
    :param: list[dict] -> списка movies, int -> threshold ограничение времени
    :return: количество фильмов
    """
    count = 0
    for m in movies:
        if m["duration_min"] > threshold:
            count += 1
    return count

# Этап 4. Строки

def normalize_title(title: str) -> str:
    """
    Функция приводящяя строку к формату Title Case
    :param: str -> title название фильма
    :return: название формата Title Case
    """
    return " ".join([word[0].upper() + word[1:] for word in title.split()])
def make_slug(title: str) -> str:
    """
    Функция превращающяя нормализованное название в «слаг»
    :param: str -> title название фильма
    :return: название формата «слаг»
    """
    return title.lower().replace(" ", "-")
def format_report_line(move: dict) -> str:
    """
    Функция возвращающую единую строку с описанием фильма
    :param: dict -> move данные фильма
    :return: строка с информацией о фильме
    """
    return (f"{move['title']} ({move['year']}) - {move["rating"]}/10, "
            f"{duration_in_hours(move['duration_min'])}, "
            f"жанры: {', '.join(sorted(move["genres"]))}")

# Этап 5. Списки
def titles_sorted_by_rating(movies: list[dict]) -> list:
    """
    Функция возвращающая список названий фильмов,
        отсортированных по убыванию рейтинга
    :param: list[dict] -> списка movies
    :return: список отсортированных по убыванию рейтинга фильмов
    """
    return sorted(movies, key=lambda x: x["rating"], reverse=True)
def top_n_by_rating(movies: list[dict], n: int = 3) -> list:
    """
    Функция возвращающая список из n кортежей
        (title, rating) — топ по рейтингу
    :param: list[dict] -> списка movies, int -> n топ рейтинга
    :return: n - топ рейтинга в виде кортежей
    """
    # как альтернативу можно использовать функцию titles_sorted_by_rating
    # return [(x["title"], x["rating"]) for x in titles_sorted_by_rating(movies)[:n]]
    sorted_movies = sorted(movies, key=lambda x: x["rating"], reverse=True)
    return [(x["title"], x["rating"]) for x in sorted_movies[:n]]
