from django.db import models


class Autor(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    # Aqui está o relacionamento 1:N. on_delete=models.CASCADE significa que 
    # se o Autor for deletado, seus livros também serão.
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='livros')
    ano_publicacao = models.IntegerField()

    def __str__(self):
        return self.titulo
