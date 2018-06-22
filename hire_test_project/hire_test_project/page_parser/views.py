from rest_framework.response import Response
from rest_framework.views import APIView

from hire_test_project.tasks import parse_html_page

from .serializers import *


class Tags(APIView):

    def post(self, request):
        data = TagsPostInputSerializer(data=request.data)
        data.is_valid(raise_exception=True)
        task = parse_html_page.delay(data.validated_data['url'])
        outp = TagsPostOutputSerializer(data={'task_id': task.id})
        outp.is_valid(raise_exception=True)
        return Response(outp.data)

    def get(self, request):
        """
         Возможные коды ошибок:
            0 - Успех
            1 - Ошибка сервиса
        """
        result = {'code': 1}

        data = TagsGetInputSerializer(data=request.query_params)
        data.is_valid(raise_exception=True)
        task_id = data.validated_data['task_id']
        parsed_page = parse_html_page.AsyncResult(task_id).result
        if parsed_page and not isinstance(parsed_page, Exception):
            result['code'] = 0
            result.update(parsed_page)
        outp = TagsGetOutputSerializer(data=result)
        outp.is_valid(raise_exception=True)
        return Response(outp.data)