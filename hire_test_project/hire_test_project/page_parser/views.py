from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from hire_test_project.tasks import parse_html_page

from .serializers import *


class Tags(APIView):

    def post(self, request):
        data = TagsPostInputSerializer(data=request.data)
        if not data.is_valid():
            return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
        task = parse_html_page.delay(data.validated_data['url'])
        outp = TagsPostOutputSerializer(data={'task_id': task.id})
        if not outp.is_valid():
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(outp.data)

    def get(self, request):
        """
         Возможные коды ошибок:
            0 - Успех
            1 - Ошибка сервиса
        """
        result = {'code': 1}

        data = TagsGetInputSerializer(data=request.query_params)
        if not data.is_valid():
            return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
        task_id = data.validated_data['task_id']
        parsed_page = parse_html_page.AsyncResult(task_id).result
        if parsed_page and not isinstance(parsed_page, Exception):
            result['code'] = 0
            result.update(parsed_page)
        outp = TagsGetOutputSerializer(data=result)
        if not outp.is_valid():
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(outp.data)