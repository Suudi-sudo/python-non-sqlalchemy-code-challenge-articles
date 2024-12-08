class Article:
    all = []  

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)  

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, new_title):
        if not isinstance(new_title, str) or not (5 <= len(new_title) <= 50):
            print(" Title must be a string between 5 and 50 characters.")
            return
        if hasattr(self, "_title"):
            print("Title cannot be changed.")
            return
        self._title = new_title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        if not isinstance(new_author, Author):
            print(" Author must be an instance of Author.")
            return
        self._author = new_author

    


class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or not new_name:
            print("Error: Name must be a non-empty string.")
            return
        if hasattr(self, "_name"):
            print("Error: Name cannot be changed.")
            return
        self._name = new_name

    def articles(self):
        return [article for article in Article.all if article.author is self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        return list({magazine.category for magazine in self.magazines()}) or None


class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or not (2 <= len(new_name) <= 16):
            print("Error: Name must be a string between 2 and 16 characters.")
            return
        self._name = new_name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str) or not new_category:
            print("Error: Category must be a non-empty string.")
            return
        self._category = new_category

    def articles(self):
        return [article for article in Article.all if article.magazine is self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        return [article.title for article in self.articles()] or None

    def contributing_authors(self):
        authors_count = {}
        
        for article in self.articles():
            authors_count[article.author] = authors_count.get(article.author, 0) + 1
        
        return [author for author, count in authors_count.items() if count >= 2] or None



def test_get_all_articles():
   
    
    Article.all.clear()
    
    author = Author("Carry Bradshaw")
    magazine_1 = Magazine("Vogue", "Fashion")
    magazine_2 = Magazine("AD", "Architecture & Design")
    
    
    article_1 = Article(author, magazine_1, "How to wear a tutu with style")
    article_2 = Article(author, magazine_2, "Dating life in NYC")
     
     
    assert len(Article.all_articles) == 2  


