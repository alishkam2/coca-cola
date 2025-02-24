from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.PositiveIntegerField()  # Продолжительность в минутах
    director = models.ForeignKey(
        Director, on_delete=models.CASCADE, related_name="movies"
    )

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews")
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], default=5)

    def __str__(self):
        return self.text[:50]
