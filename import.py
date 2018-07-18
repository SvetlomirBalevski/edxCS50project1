import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

def main():
    filestream = open("books.csv")
    reader = csv.reader(filestream)
    for isdn, title, author, published in reader:
        if(published != 'published'): # first value of published field is always string (title is published), so this check is needed
            db.execute("INSERT INTO books (isdn, title, author, published) VALUES (:isdn, :title, :author, :published)",
                        {"isdn": isdn, "title": title, "author": author, "published": published})
            print(f"Added books with isdn {isdn} named {title} from {author} published at {published} year.")
            db.commit()

if __name__ == "__main__":
    main()
