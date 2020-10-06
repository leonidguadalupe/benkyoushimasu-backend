from api.views import TopicViewSet
from api.router import CustomReadOnlyRouter

router = CustomReadOnlyRouter()
router.register(r'topics', TopicViewSet, basename='Custom')