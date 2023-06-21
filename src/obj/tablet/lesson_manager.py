import pygame
import configparser

from obj.tablet.lesson import Lesson


teachers_config = configparser.ConfigParser()
teachers_config.read('data/teachers.ini')
teacher_list = teachers_config.get('Teachers', 'teacher_list')
teachers = teacher_list.split(',')


class LessonManager:

    def __init__(self) -> None:
        self.lessons: list[Lesson] = []

        for name in teachers:
            lesson = Lesson(name)
            self.lessons.append(lesson)

        self.current_lesson = None

    
    def setCurrentLesson(self, lesson: str) -> None:
        self.current_lesson = lesson