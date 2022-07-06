import unittest
from student import Student
from datetime import timedelta, date
from unittest.mock import patch

class TestStudent(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        print('setUp')
        self.student = Student('John', 'Doe')

    def tearDown(self):
        print('tearDown')

    def test_full_name(self):
        print('test_full_name')
        self.assertEqual(self.student.full_name, 'John Doe')

    def start_date(self):
        print("Start_date")
        self.assertEqual(self.student._start_date, date.today())

    def test_alert_santa(self):
        print('test_alert_santa')
        self.student.alert_santa()
    
    def test_apply_extension(self):
        old_end_date = self.student.end_date
        self.student.apply_extension(5)
        self.assertEqual(self.student.end_date, old_end_date + timedelta(days=5))
    
    def test_email_address(self):
        print('test_email_address')
        self.assertEqual(self.student.email_address, 'john.doe@email.com')

    def test_course_schedule_success(self):
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Success")

    def test_course_schedule_failed(self):
        with patch("student.requests.get") as mocked_get:
            mocked_get.return_value.ok = False

            schedule = self.student.course_schedule()
            self.assertEqual(schedule, "Something went wrong with the request")


if __name__ == '__main__':
    unittest.main()