from rest_framework.routers import DynamicRoute, SimpleRouter

class CustomReadOnlyRouter(SimpleRouter):
    """
    A router for read-only APIs, which doesn't use trailing slashes.
    """
    routes = [
        DynamicRoute(
            url=r'^{url_path}$',
            name='{url_name}',
            detail=True,
            initkwargs={}
        )
    ]