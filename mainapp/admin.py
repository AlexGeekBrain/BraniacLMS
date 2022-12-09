from django.contrib import admin

from mainapp.models import News, Course, Lesson, CourseTeacher


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    search_fields = ['title', 'preamble', 'body']
    list_display = ['pk', 'title', 'deleted']
    list_filter = ['created_at', 'deleted']
    list_per_page = 5
    actions = ['mark_as_delete']

    def mark_as_delete(self, request, queryset):
        queryset.update(deleted=True)

    mark_as_delete.short_description = 'Пометить удаленным'


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['pk', 'get_course_name', 'num', 'title', 'deleted']
    ordering = ['-course__title', '-num']
    list_per_page = 5
    list_filter = ['course', 'created_at', 'deleted']
    actions = ['mark_as_delete']

    def get_course_name(self, obj):
        return obj.course

    get_course_name.short_description = 'Курс'

    def mark_as_delete(self, request, queryset):
        queryset.update(deleted=True)

    mark_as_delete.short_description = 'Пометить удаленным'


@admin.register(CourseTeacher)
class CourseTeacherAdmin(admin.ModelAdmin):
    pass
