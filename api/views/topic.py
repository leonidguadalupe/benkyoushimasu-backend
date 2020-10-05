"""
.. module:: branch
   :synopsis: Endpoints for branch functionalities
.. moduleauthor:: Leonid Guadalupe <github.com/leonidguadalupe>
"""
from django.http import Http404
from django.db.models import Q
from rest_framework import viewsets, status

from api.models import Branch, User, Device
from api.serializers.device import DeviceSerializer
from api.serializers.user import UserSerializer

class BranchViewSet(viewsets.ViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

    def _get_object(self, id):
        try:
            return Branch.objects.get(id=id)
        except Branch.DoesNotExist:
            raise Http404

    def list(self, request):
        branches = Branch.objects.all() # change to all_active later
        serializer = serializer_class(data=branches, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def create(self, request):
        serializer = serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        branch = self._get_object(id=pk)
        if pk:
            serializer = serializer_class(branch, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, url_path='update-branch', url_name='update-branch', methods=['put'])
    def update(self, request, pk=None):
        # A-3: Admin should be able to edit branch detail (name, code?)
        branch = self._get_object(id=pk)
        serializer = serializer_class(branch, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        pass

    @action(detail=True, url_path='deactivate-branch', url_name='deactivate', methods=['delete'])
    def deactivate(self, request, pk=None):
        branch = self._get_object(id=pk)
        branch.is_active = False
        branch.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, url_path='activate-branch', url_name='activate', methods=['post'])
    def activate(self, request, pk=None):
        branch = self._get_object(id=pk)
        branch.is_active = True
        branch.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, url_path='check-name', url_name='check-name', methods=['post'])
    def check_name(self, request):
        name = request.data.get('name')
        result = Branch.objects.filter(name=name).first()
        if result:
            return Response(
                {'message': 'This name already exists, are you sure you want to add this?'},
                status=status.HTTP_302_FOUND
            )
        else:
            return Response(status=status.HTTP_200_OK)
    
    @action(detail=True, url_name='search', methods=['get'])
    def search(self, request):
        search_string = request.query_params.get('q')
        search_type = request.query_params.get('type')

        if search_type == "branch":
            query = Branch.objects.filter(
                Q(name__istartswith=search_string)|
                Q(code__istartswith=search_string)
            )
            serializer = serializer_class(query, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif search_type == "device":
            query = Device.objects.\
                annotate(fullname=Concat('installer__first_name', Value(' '), 'installer__last_name')).\
                filter(
                    Q(fullname__istartswith=search_string),
                    is_active=True
                ).filter(
                Q(serial_number__istartswith=search_string)|
                Q(installer____istartswith=search_string)
                # adding tag soon

            )
            serializer = DeviceSerializer(query, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif search_type == "people":
            query = User.objects.\
                annotate(fullname=Concat('installer__first_name', Value(' '), 'installer__last_name')).\
                filter(
                    Q(fullname__istartswith=search_string),
                    is_active=True
                ).filter(
                Q(serial_number__istartswith=search_string)|
                Q(installer____istartswith=search_string)
                # adding tag soon

            )
            serializer = DeviceSerializer(query, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)