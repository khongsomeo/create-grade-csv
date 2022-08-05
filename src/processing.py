"""The interface for processing"""


class Processing:
    """Processing Interface for later classes"""

    def __init__(self, **kwargs) -> None:
        """Initialise"""

        self.__input_file = kwargs.get("input_file", None)
        self.__output_file = kwargs.get("output_file", None)

    @staticmethod
    def clean_course_code(course_string):
        """Clean the course code from original name-coursecode"""

        return course_string.split("-")[0].strip()

    def process_and_write(self):
        """Processing data, with details described in derived classes"""
        pass
