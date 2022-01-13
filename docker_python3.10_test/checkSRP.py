# SRP(Single Responsibility Principle)
from abc import *


class HumanBase(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def go_restroom(self):
        pass


class Male(HumanBase):
    def __init__(self, name):
        super().__init__(name)
        self.sex = "남자"

    def go_restroom(self):
        print("남자화장실로 간다.")


class Female(HumanBase):
    def __init__(self, name):
        super().__init__(name)
        self.sex = "여자"

    def go_restroom(self):
        print("여자화장실로 간다.")


class Course:
    """SRP원칙을 준수한 Course 클래스"""

    def __init__(self, code, name, schedule, pf):
        self.code = code
        self.name = name
        self.schedule = schedule
        self.pf = pf


class CourseDB:
    """SRP원칙을 준수한 CourseDB 클래스"""

    def __init__(self, con):
        self.con = con

    def connect(self) -> bool:
        """DB connecting"""
        pass

    def close(self) -> bool:
        """DB closing"""
        pass

    def get_course_by_pf(self, professor) -> list:
        """professor로 강의 찾기 함수"""
        pass

    def save_course(self, Course) -> bool:
        """DB에 course 저장하기"""
        pass

    def update_course(self, code) -> bool:
        """특정 code를 가진 course를 DB update 하기"""
        pass
