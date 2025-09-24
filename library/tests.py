from django.test import TestCase
from datetime import date

from .models import Author, Book, Review


class ModelTests(TestCase):
    def setUp(self):
        self.author1 = Author.objects.create(
            first_name="Александр",
            last_name="Пушкин",
            birth_date=date(1799, 6, 6),
        )
        self.author2 = Author.objects.create(
            first_name="Иван",
            last_name="Бунин",
            birth_date=date(1870, 10, 22),
        )
        # Нарочно создаём книги в «перевёрнутом» порядке, чтобы проверить ordering по title
        self.book_b = Book.objects.create(
            title="Евгений Онегин",
            publication_date=date(1833, 1, 1),
            author=self.author1,
            review="Классика",
            recommend=True,
        )
        self.book_a = Book.objects.create(
            title="Арап Петра Великого",
            publication_date=date(1827, 1, 1),
            author=self.author1,
        )

    # --- __str__ ---
    def test_author_str(self):
        self.assertEqual(str(self.author1), "Александр Пушкин")

    def test_book_str(self):
        self.assertEqual(str(self.book_b), "Евгений Онегин")

    def test_review_str(self):
        review = Review.objects.create(book=self.book_b, rating=5, comment="Отлично")
        self.assertEqual(str(review), f"Review for {self.book_b.title}")

    # --- Связи и reverse-relations ---
    def test_author_books_relation(self):
        # у автора1 две книги; обратная связь related_name='books' работает
        self.assertEqual(self.author1.books.count(), 2)
        self.assertIn(self.book_a, self.author1.books.all())
        self.assertIn(self.book_b, self.author1.books.all())

    def test_book_reviews_relation(self):
        Review.objects.create(book=self.book_b, rating=4, comment="Норм")
        Review.objects.create(book=self.book_b, rating=5, comment="Супер")
        self.assertEqual(self.book_b.reviews.count(), 2)

    # --- Meta.ordering ---
    def test_book_ordering_by_title(self):
        # В Meta у Book: ordering = ['title']
        titles = list(Book.objects.values_list("title", flat=True))
        self.assertEqual(titles, sorted(titles))

    def test_author_ordering_by_last_name(self):
        # В Meta у Author: ordering = ['last_name']
        last_names = list(Author.objects.values_list("last_name", flat=True))
        self.assertEqual(last_names, sorted(last_names))

    # --- Custom permissions объявлены в модели Book ---
    def test_book_custom_permissions_declared(self):
        perms = dict(Book._meta.permissions)  # [('can_review_book', '...'), ...] -> dict
        self.assertIn("can_review_book", perms)
        self.assertIn("can_recommend_book", perms)
