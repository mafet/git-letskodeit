from pages.courses.register_courses_page import RegisterCoursesPage
from pages.home.navigation_page import NavigationPage
from utilities.teststatus import TestStatus
import unittest
import pytest
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData

@pytest.mark.usefixtures("oneTimeSetup", "setUp")
@ddt
class RegisterCoursesTests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetup):
        self.course = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.nav = NavigationPage(self.driver)

    def setUp(self):
        self.nav.navigateToAllCourses()

    @pytest.mark.run(order=1)
    @data(*getCSVData("C:/Users/Maria.Misa/workspace_python/letskodeit/testdata.csv"))
    @unpack
    def test_invalidEnrollment(self, courseName, ccNum, ccExp, ccCVV):
        self.course.enterCourseName(courseName)
        self.course.selectCourseToEnroll(courseName)
        self.course.enrollCourse(num=ccNum, exp=ccExp, cvc=ccCVV)
        result = self.course.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result,
                          "Enrollment Failed Verification")
