from django.db import models


class KindOfCourse(models.QuerySet):

    def courses_trb(self):
        return self.filter(coursetrb__isnull=False)

    def courses_normal(self):
        return self.filter(coursetrb__isnull=True)
