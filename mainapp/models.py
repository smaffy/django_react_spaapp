from django.db import models


class BlogCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name='Category name')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class BlogPostQuerySet(models.QuerySet):
    def find_by_title_in_qs(self, post_title):
        return self.filter(title__icontains=post_title)


class BlogPostManager(models.Manager):
    """
    pereopredeljaet BlogPost.objects.all() i tp
    pomojemu ochenj hrenovaja tema pereopredelitj  all()
    BlogPost._base_manager.all()
    """
    def get_queryset(self):
        return BlogPostQuerySet(self.model, using=self._db)
        # return super().get_queryset()

    def all(self):
        return self.get_queryset().filter(in_archive=False)

    def find_by_title_in_qs(self, post_title):
        return self.get_queryset().find_by_title_in_qs(post_title)
    # BlogPost.objects.all().find_by_title_in_qs('net')
    # BlogPost.objects.find_by_title_in_qs('net')


class BlogPost(models.Model):
    blog_category = models.ForeignKey(BlogCategory, verbose_name='Category name', on_delete=models.Case)
    title = models.CharField(max_length=255, verbose_name='Title')
    slug = models.SlugField(unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_posts/', blank=True, null=True)
    pub_date = models.DateTimeField(auto_now=True)
    in_archive = models.BooleanField(default=False)

    objects = BlogPostManager()

    def __str__(self):
        return f'{self.title} from category "{self.blog_category.name}"'

    # def get_absolute_url(self):
    #     return reverse('blogPost', args=[self.id])

