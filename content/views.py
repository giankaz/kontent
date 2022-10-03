from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_204_NO_CONTENT
from django.forms.models import model_to_dict
from .models import Content


class ContentsView(APIView):
    def get(self, request):
        try:
            contents = Content.objects.all()

            contents_dict = [model_to_dict(content) for content in contents]

            return Response(contents_dict, HTTP_200_OK)
        except:
            return Response({'message': 'content not found'}, HTTP_404_NOT_FOUND)

    def post(self, request):
        title = request.data.get('title')
        module = request.data.get('module')
        students = request.data.get('students')
        description = request.data.get('description')
        is_active = request.data.get('is_active')

        if (is_active == None):
            is_active = False

        if (description == None):
            description = ''

        treated_content = dict(title=title, module=module, students=students,
                               description=description, is_active=is_active)

            

        error_message = 'Oops, something went wrong: '

        if not (title):
            error_message += 'title is required'
            if (type(title) != str):
                error_message += ' and should be a string, '
            else:
                error_message += ', '
        else:
            if (type(title) != str):
                error_message += 'title should be a string, '

        if not (module):
            error_message += 'module is required'
            if (type(module) != str):
                error_message += ' and should be a string, '
            else:
                error_message += ', '
        else:
            if (type(module) != str):
                error_message += 'module should be a string, '

        if not (students):
            error_message += 'students is required'
            if (type(students) != int):
                error_message += ' and should be an integer, '
            else:
                error_message += ', '
        else:
            if (type(students) != int):
                error_message += 'students should be an integer, '

        if (description):
            if (type(description) != str):
                error_message += 'description should be a string, '

        if (is_active):
            if (type(is_active) != bool):
                error_message += 'is_active should be a boolean, '

        if (error_message != 'Oops, something went wrong: '):
            error_message = error_message[0: (len(error_message) - 2)] + '.'

            error_message_dict = dict(message=error_message)

            return Response(error_message_dict, HTTP_400_BAD_REQUEST)

        content = Content.objects.create(**treated_content)

        content_dict = model_to_dict(content)

        return Response(content_dict, HTTP_201_CREATED)


class ContentsById(APIView):
    def get(self, request, content_id):
        try:
            content = Content.objects.get(pk=content_id)
        except Content.DoesNotExist:
            return Response({'message': 'content not found'}, HTTP_404_NOT_FOUND)

        content_dict = model_to_dict(content)

        return Response(content_dict)

    def patch(self, request, content_id):
        try:
            title = request.data.get('title')
            module = request.data.get('module')
            students = request.data.get('students')
            description = request.data.get('description')
            is_active = request.data.get('is_active')

            content = Content.objects.get(pk=content_id)
            if (title):
                if (type(title) == str):
                    content.title = title
            
            if (module):
                if (type(module) == str):
                    content.module = module
            if (students):
                if (type(students) == int):
                    content.students = students

            if (description):
                if (type(description) == str):
                    content.description = description

            if (is_active):
                if (type(is_active) == bool):
                    content.is_active = is_active

            content.save()                                                

            content_dict = model_to_dict(content)


            return Response(content_dict)
        except Content.DoesNotExist:
            return Response({'message': 'content not found'}, HTTP_404_NOT_FOUND)

    def delete(self, request, content_id):
        try:
            content = Content.objects.get(pk=content_id)
            content.delete()
        except Content.DoesNotExist:
            return Response({'message': 'content not found'}, HTTP_404_NOT_FOUND)

        

        return Response('', HTTP_204_NO_CONTENT)


class FilteredContents(APIView):
    def get(self, request):
        try:
            title = request.query_params.get('title', None)

            contents = Content.objects.filter(title=title)

            contents_dicts = [model_to_dict(content) for content in contents]

            return Response(contents_dicts)
        except Content.DoesNotExist:
            return Response({'message': 'content not found'}, HTTP_404_NOT_FOUND)


       
