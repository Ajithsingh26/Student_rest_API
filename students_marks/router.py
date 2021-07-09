from students.viewsets import StudentsViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Students',StudentsViewset)