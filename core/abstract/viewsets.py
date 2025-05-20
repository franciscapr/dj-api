from rest_framework import viewsets
from rest_framework import filters


class AbstractViewSet(viewsets.ModelViewSet):
    filter_backends = [filters.OrderingFilter]    # Backend de filtros
    ordering_fields = ['updated', 'created']    # Campos que pueden usarse como parametros de ordenamiento
    ordering = ['-updated']    # orden en que iran los objetos como respuesta --> en este caso todas las respuestas estaran ordenadas por los elementos más recientes actualizados.