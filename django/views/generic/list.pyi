from typing import Any, Dict, List, Optional, Sequence, Tuple, Type

from django.db.models import Model
from django.db.models.query import QuerySet
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.views.generic.base import ContextMixin, TemplateResponseMixin, View

class MultipleObjectMixin(ContextMixin):
    allow_empty = ...  # type: bool
    queryset = ...  # type: Optional[QuerySet]
    model = ...  # type: Optional[Type[Model]]
    paginate_by = ...  # type: Optional[int]
    paginate_orphans = ...  # type: int
    context_object_name = ...  # type: Optional[str]
    paginator_class = ...  # type: Type[Paginator]
    page_kwarg = ...  # type: str
    ordering = ...  # type: Sequence[str]
    request = ...  # type: HttpRequest
    kwargs = ...  # type: Dict[str, object]
    object_list = ...  # type: QuerySet

    def get_queryset(self) -> QuerySet: ...
    def get_ordering(self) -> Sequence[str]: ...
    def paginate_queryset(self, queryset: QuerySet, page_size: int) -> Tuple[Paginator, int, QuerySet, bool]: ...
    def get_paginate_by(self, queryset: QuerySet) -> Optional[int]: ...
    def get_paginator(self, queryset: QuerySet, per_page: int, orphans: int = ..., allow_empty_first_page: bool = ..., **kwargs: Any) -> Paginator: ...
    def get_paginate_orphans(self) -> int: ...
    def get_allow_empty(self) -> bool: ...
    def get_context_object_name(self, object_list: QuerySet) -> Optional[str]: ...
    def get_context_data(self, **kwargs: object) -> Dict[str, object]: ...

class BaseListView(MultipleObjectMixin, View):
    object_list = ...  # type: QuerySet
    def render_to_response(self, context: Dict[str, object], **response_kwargs: object) -> HttpResponse: ...
    def get(self, request: HttpRequest, *args: object, **kwargs: object) -> HttpResponse: ...

class MultipleObjectTemplateResponseMixin(TemplateResponseMixin):
    template_name_suffix = ...  # type: str
    object_list = ...  # type: QuerySet
    def get_template_names(self) -> List[str]: ...

class ListView(MultipleObjectTemplateResponseMixin, BaseListView): ...
