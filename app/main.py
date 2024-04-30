from __future__ import annotations


class OnlineCourse:
    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks

    @staticmethod
    def days_to_weeks(days: int) -> int:
        weeks, remainder = divmod(days, 7)
        if remainder > 0:
            weeks += 1
        return weeks

    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        name = course_dict["name"]
        description = course_dict["description"]
        weeks = ""
        if "weeks" in course_dict:
            weeks = course_dict["weeks"]
        if "days" in course_dict:
            weeks = cls.days_to_weeks(course_dict["days"])

        return cls(name, description, weeks)


course_dict = {
    "name": "Python Core",
    "description": "After this course you will know everything about Python",
    "days": 12,
}
python_course = OnlineCourse.from_dict(course_dict)
print(python_course.weeks)
