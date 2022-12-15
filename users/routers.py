from rest_framework.routers import Route, DynamicRoute, SimpleRouter

class CustomRouter(SimpleRouter):
    routes = [
        # Route(
        #     url = r'^{prefix}$',
        #     mapping = {'get':'get'},
        #     name ='{basename}-list',
        #     detail = False,
        #     initkwargs ={'suffix':'List'}
        # ),
        Route(
            url = r'^{prefix}$',
            mapping = {
                'get':'list',
                'post':'create',
                },
            name ='{basename}-list',
            detail = False,
            initkwargs ={'suffix':'List'}
        ),
        Route(
            url=r'^{prefix}/{lookup}$',
            mapping= {
                'get':'retrieve',
                'put':'update',
                'patch':'partial_update',
                'delete':'destroy'
                },
            name='{basename}-detail',
            detail=True,
            initkwargs={'suffix':'Detail'}
        )
    ]



# Route(
#             url=r'^{prefix}/{lookup}',
#             mapping={
#                 'get':'retrieve',
#                 'put':'update',
#                 'patch':'partial_update',
#                 'delete':'destroy',
#             },
#             name='{basename}-detaildestroy',
#             detail=True,
#             initkwargs={'suffix':'Update'}
#         )