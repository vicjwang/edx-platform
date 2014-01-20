"""
Stub implementation of ORA service.
"""

from .http import StubHttpRequestHandler, StubHttpService


class StubOraHandler(StubHttpRequestHandler):
    """
    Handler for ORA requests.
    """

    def do_GET(self):
        """
        """
        self.send_response(200)

    def do_POST(self):
        """
        """
        self.send_response(200)


class StubOraService(StubHttpService):
    """
    Stub ORA service.
    """
    HANDLER_CLASS = StubOraHandler

    DEFAULTS = {
        'submission_id': 1,
        'submission_key': 'test key',
        'student_response': 'Test response',
        'prompt': 'Test prompt',
        'rubric': 'TODO', # <-- TODO
        'max_score': 2,
        'message': 'Successfully saved calibration record.',
        'actual_score': 2,
        'actual_rubric': 'TODO', # <-- TODO
        'actual_feedback': 'Great job!',
        'location': 'test location',
        'problem_name': 'Test Problem',
        'student_sub_count': 1,
        'initial_num_pending': 3,
    }
