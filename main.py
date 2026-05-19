from sqlalchemy import create_engine, Column, Integer, String, Float, func
from sqlalchemy.orm import DeclarativeBase, Session
from sqlalchemy import select

engine = create_engine('sqlite:///movies.db', echo=False)

class Base(DeclarativeBase):
    pass


class Movie(Base):
    __tablename__ = 'movies'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    genre = Column(String)
    release_year = Column(Integer)
    duration = Column(Integer)
    rating = Column(Float)
    director = Column(String)


Base.metadata.create_all(bind=engine)


with Session(engine) as session:
    k1 = Movie(title="Interstellar", genre="Sci-Fi", release_year=2014, duration=169, rating=8.7, director="Christopher Nolan")

    k2 = Movie(title="Inception", genre="Sci-Fi", release_year=2010, duration=148, rating=8.8, director="Christopher Nolan")

    k3 = Movie(title="Titanic", genre="Drama", release_year=1997, duration=195, rating=7.9, director="James Cameron")

    k4 = Movie(title="Joker", genre="Thriller", release_year=2019, duration=122, rating=8.4, director="Todd Phillips")

    k5 = Movie(title="Avatar", genre="Fantasy", release_year=2009, duration=162, rating=7.8, director="James Cameron")

    k6 = Movie(title="The Batman", genre="Action", release_year=2022, duration=176, rating=7.9, director="Matt Reeves")

    k7 = Movie(title="Oppenheimer", genre="Biography", release_year=2023, duration=180, rating=8.6, director="Christopher Nolan")

    k8 = Movie(title="Parasite", genre="Thriller", release_year=2019, duration=132, rating=8.5, director="Bong Joon-ho")

    k9 = Movie(title="John Wick", genre="Action", release_year=2014, duration=101, rating=7.4, director="Chad Stahelski")

    k10 = Movie(title="Dune", genre="Sci-Fi", release_year=2021, duration=155, rating=8.0, director="Denis Villeneuve")

with Session(engine) as session:
    session.add_all([k1, k2, k3, k4, k5, k6, k7, k8, k9, k10])
    session.commit()

# #1. Barcha kinolar
# all_movies = session.query(Movie).all()
# for m in all_movies:
#     print(f"{m.title} ({m.release_year}) - {m.genre}, Rating: {m.rating}")

# #2. Faqat 'Sci-Fi' janridagi kinolar
# sci_fi = session.query(Movie).filter(Movie.genre == "Sci-Fi").all()
# for m in sci_fi:
#     print(m.title)

# #3. 2015 yildan keyingi kinolar
# recent = session.query(Movie).filter(Movie.release_year >= 2015).all()
# for m in recent:
#     print(m.title, m.release_year)

# #4. Reytingi 8.5 dan yuqori kinolar
# high_rated = session.query(Movie).filter(Movie.rating > 8.5).all()
# for m in high_rated:
#     print(m.title, m.rating)

# #5. Davomiyligi 150 daqiqadan ortiq kinolar
# long_movies = session.query(Movie).filter(Movie.duration > 150).all()
# for m in long_movies:
#     print(m.title, m.duration, "min")

# #6. Faqat 'Christopher Nolan' rejissyorning kinolari
# nolan = session.query(Movie).filter(Movie.director == "Christopher Nolan").all()
# for m in nolan:
#     print(m.title)

# #7. 'Action' janri va reytingi 7.5
# action_high = session.query(Movie).filter(
#     Movie.genre == "Action", 
#     Movie.rating > 7.5
# ).all()
# for m in action_high:
#     print(m.title, m.rating)

# #8. 'James Cameron' yoki 'Christopher Nolan' kinolari
# directors = session.query(Movie).filter(
#     Movie.director.in_(["James Cameron", "Christopher Nolan"])
# ).all()
# for m in directors:
#     print(m.title, "-", m.director)

# #9. 'Thriller' yoki 'Drama' janridagi kinolar
# thriller_drama = session.query(Movie).filter(
#     Movie.genre.in_(["Thriller", "Drama"])
# ).all()
# for m in thriller_drama:
#     print(m.title, m.genre)

# #10. Nomida 'The' so'zi bor kinolar
# the_movies = session.query(Movie).filter(Movie.title.like('%The%')).all()
# for m in the_movies:
#     print(m.title)

# #11. Nomida 'Dune' yoki 'John Wick' bor
# specific = session.query(Movie).filter(
#     Movie.title.like('%Dune%') | Movie.title.like('%John Wick%')
# ).all()
# for m in specific:
#     print(m.title)

# #13. O'rtacha reyting
# avg_rating = session.query(func.avg(Movie.rating)).scalar()
# print(f"O'rtacha reyting: {avg_rating:.2f}")

# #14. Har bir rejissyorning kinolari soni
# director_count = session.query(
#     Movie.director, 
#     func.count(Movie.id).label('count')
# ).group_by(Movie.director).all()
# for d, c in director_count:
#     print(d, "-", c)

# #15. Eng yuqori reytingli kino
# best = session.query(Movie).order_by(Movie.rating.desc()).first()
# print(best.title, best.rating)