"""
Tests for peer-grading module.

These tests are specifically for *giving* feedback;
the tests for receiving peer-assessment feedback are located
with the tests for receiving self-, AI-, and instructor feedback.

For this reason, these tests stub ORA peer-grading HTTP interface,
but not the XQueue interface.
"""

from .helpers import UniqueCourseTest

from ..edxapp_pages.studio.auto_auth import AutoAuthPage
from ..edxapp_pages.lms.course_info import CourseInfoPage
from ..edxapp_pages.lms.tab_nav import TabNavPage

from ..fixtures.course import XBlockFixtureDesc, CourseFixture


class PeerModuleTest(UniqueCourseTest):
    """
    Tests for the peer grading module.

    The peer-grading module allows students to *give* feedback,
    including going through the calibration process.

    Note that this is NOT the same as a peer-grading problem,
    in which students *receive* feedback from peers.
    """
    page_object_classes = [
        AutoAuthPage, CourseInfoPage, TabNavPage,
    ]

    def setUp(self):
        """
        Always start on the page with a peer-grading module.
        """

        # Ensure fixtures are installed
        super(PeerModuleTest, self).setUp()

        # Log in and navigate to the peer-grading module
        self.ui.visit('studio.auto_auth', course_id=self.course_id)
        self.ui.visit('lms.course_info', course_id=self.course_id)
        self.ui['lms.tab_nav'].go_to_tab('Courseware')

    @property
    def fixtures(self):
        """
        Configure a course with a peer grading module.
        """
        course_fix = CourseFixture(
            self.course_info['org'], self.course_info['number'],
            self.course_info['run'], self.course_info['display_name']
        )

        course_fix.add_children(
            XBlockFixtureDesc('chapter', 'Test Section').add_children(
                XBlockFixtureDesc('sequential', 'Test Subsection').add_children(
                    XBlockFixtureDesc('peergrading', 'Peer Module')
        )))

        return [course_fix]

    def test_calibration(self):
        """
        Given I am viewing a peer-assessment problem
        And the instructor has submitted enough example essays
        When I submit submit acceptable scores for enough calibration essays
        Then I am able to peer-grade other students' essays.
        """
        pass

    def test_submit_feedback(self):
        """
        Given I am viewing another student's essay in peer-grading
        When I submit rubric scores and written feedback
        Then I see that my feedback has been submitted.
        """
        pass
