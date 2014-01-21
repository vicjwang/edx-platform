##############
Discussions
##############

Discussions, or discussion forums, foster interaction among your students and between students and course staff. You set up discussion topics and categories when you create your course, and then run and moderate discussion threads throughout the course to guide participation and develop course community. 

Discussions are also excellent sources of feedback and ideas for the future.

* :ref:`Organizing_discussions`

* :ref:`Running_discussions`

* :ref:`Moderating_discussions`

.. _Organizing_discussions:

*************************************************
Setting up discussions for your course
*************************************************

Discussions in an edX course include both the specific topics that you add to course units as discussion components, and  broader forums on course-wide areas of interest, such as Feedback, Troubleshooting, or Technical Help, that you add can add as discussion categories. 

============================================
Adding units with a discussion component
============================================

Typically, all units are added during the design and creation of your course in Studio. To add a design component to a unit, follow the instructions in :ref:`Working with Discussion Components`.   

This type of discussion is subject to the release date of the section that contains it. Students cannot contribute to these discussions until that date.

=====================================
Creating discussion categories
=====================================
All courses have a static page named Discussion that includes a course-wide discussion category named General by default.

You can add more discussion categories to guide how students share and find information during your course. Categories might include Feedback, Troubleshooting, or Technical Help. Discussions in these categories can begin as soon as your course is available.

To create a discussion category:

#. Open your course in Studio. 

#. Select **Settings** > **Advanced Settings**.

#. Scroll down to the Policy Key labeled **discussion_topics**. By default, its Policy Value is:

 | {
 |    "General": {
 |        "id": "i4x-test_doc-SB101-course-2014_Jan"
 |    }
 | }

4. Copy the three lines provided for the General tab and paste them above the closing brace:

  | {
  |   "General": {
  |       "id": "i4x-test_doc-SB101-course-2014_Jan"
  |   }
  |   "General": {
  |       "id": "i4x-test_doc-SB101-course-2014_Jan"
  |   }
  | }

5. Replace the second "General" with the quoted name of your new discussion category.

#. Change the second id value to a unique identifier. For example, append the category name:


 | {
 |   "General": {
 |       "id": "i4x-test_doc-SB101-course-2014_Jan"
 |   }
 |    "FAQ": {
 |        "id": "i4x-test_doc-SB101-course-2014_Jan_faq"
 |    }
 | }

7. Click **Save Changes**.

When students click **Discussion** for your course, the drop-down list includes this new category.

.. _Assigning_discussion_roles:

========================================
Assigning discussion management roles 
========================================

You can designate a team of people to help you run course discussions. Different options for working with discussion posts are available to discussion managers with these roles:

* Forum moderators can edit and delete posts, review posts flagged for misuse, close and reopen threads, pin posts and endorse responses, and, if the course is cohorted, see posts from all cohorts. Posts by moderators are marked as "Staff".

* Forum community TAs have the same options for working with discussions as moderators. Posts by community TAs are marked as "Community TA".

* Forum admins have the same options for working with discussions as moderators. Admins can also assign these discussion management roles to more people while your course is running, or remove a role from a user whenever necessary. Posts by admins are marked as "Staff".

Before you can assign roles to your discussion managers, you need their email addresses. 

.. To get the email address for a staff member, on the Instructor Dashboard click **Membership** and then select Course Staff from the drop-down list.
.. To get the email address of a student, (? how do they get this info?).

To assign a role:

#. On the Instructor dashboard for your course, click **Membership**.

#. In the Administration List Management section, use the drop-down list to select Forum Admins, Forum Moderators, or Forum Community TAs.

#. Under the list of users who currently have that role, enter an email address and click **Add** for the role type.

#. To remove an assigned role, view the list of users and then click revoke access (the **X**) next to that email address. 

.. _Running_discussions:

*********************
Running a discussion
*********************

On an ongoing basis, discussion managers run the course discussions by making contributions and guiding student posts into threads. Techniques that you can use throughout your course to make discussions successful follow.

========================
Seeding a discussion
======================== 

Before you contribute to a discussion, you can decide whether you want your post to be identified as coming from a staff member or community TA, or appear without that identifier. Depending on the subject and purpose of your post, one or the other might be more appropriate to spark discussion and inform students.

* To identify your posts with your role, log in with your discussion manager email address and add the post or response. The responses and comments that you make include a colored banner with either "Staff" or "Community TA".
 
* To post as a student, you must set up an alternate user account with a different email address, register for the course, and tehn join the discussion. These contributions do not have a banner and appear like any other student post. See :ref:`Seed a Discussion Space in Your Course`.
 
You can also post anonymously. Regardless of your role, you can choose to make a post anonymous. However, you may want to discourage your students from posting anonymously, and therefore choose not to use this option yourself.

==========================================
Using conventions in discussion subjects
==========================================

To identify certain types of posts and make them easier for your students to find, you can define a set of standard tags to include at the beginning of the subject. Examples follow.

* Use "[OFFICIAL]" at the start of announcements about changes to the course.

* Post information about corrected errors with a subject that begins "[ERRATA]".

* In the General discussion category, add an "[INTRO]" post io initiate a thread for student and staff introductions.

* Direct students to use "[STAFF]" in the subject of each post that needs the attention of a course staff member.


======================================
Minimizing thread proliferation
======================================

To encourage longer, threaded discussions rather than many similar, separate posts, discussion managers can use these techniques.

* Pin a post. 
  Pinning a post makes it appear first in the discussion, so that it is more likely that students will see and respond to it. You can write your own post and then pin it, or pin a post by any author. Click the **pin** icon that displays at lower right of the post text.

* Endorse a response.
  Endorsing a response indicates that it provides value to the discussion, such as a correct answer to a question. Click the **check mark** button that displays at upper right of the response.

* Close a thread. 
  You can respond to a redundant post or response by pasting in a link to the thread that you prefer students to contribute to, and then prevent further thread interaction by closing the entire post or a specific response. Click the **Close** button that displays below the post or response to close it. 

* Provide post/response/comment guidelines.
  Your *Discussion Forum Guidelines* or a post in the General discussion can provide guidance about when to create a new thread, respond to an existing post, or comment on a response. 


.. _Moderating_discussions:

***********************
Moderating discussions
***********************

Discussion managers monitor discussions and keep them productive. They can also collect inforrmation, such as areas of particular confusion or interest, and relay it to the course staff. 

Developing and sustaining a positive discussion culture requires that sufficient moderator time is dedicated to reviewing and responding to discussions. Keeping up-to-date with a large MOOC forum requires a commitment of 5 or more hours per week, and involves reading posts, replying to and editing posts, and communicating with the other discussion managers and course staff.

For information on setting up moderators for your course, see :ref:`Assigning_discussion_roles`.

========================================
Providing guidelines for students
========================================

You can develop a set of best practices for discussion participation and make them avaialbe to students as a course handout file or as a static page. These guidelines can define your expectations and optionally introduce features of edX discussions. 

For a template that you can use to develop your own guidelines, see :ref:`Discussion Forum Guidelines`.

========================================
Developing a positive forum culture
========================================

Mo can cultivate qualities in their own discussion interactions to make their influence positive and their time productive.

* Encourage quality posts: thank students whose posts have a positive impact and who answer questions.

* Check links, images, and videos in addition to the text that students post. Edit offensive or inappropriate posts quickly, and explain why.

* Review posts with a large number of votes and recognize "star posters" publicly and regularly.

* Stay on topic yourself: before responding to a post, be sure to read it completely.

* Maintain a positive attitude. Acknowledge problems and errors without assigning blame.

* Provide timely answers. More time needs to be scheduled for answering discussion questions when deadlines for homework, quizzes, and other milestones approach.

* Discourage redundancy: before responding to a post search for similar posts. Make your response in the most pertinent or active thread, then use links to direct other posts to that thread.  

* Publicize issues raised in the discussions: add questions and their answers to an FAQ discussion category, or announce them on the Course Info page. 

For a template that you can use to develop guidelines for your course moderators, see :ref:`Guidance for discussion moderators`.

==================
Editing posts 
==================

Posts and responses can be edited by discussion moderators, community TAs, and admins. Posts that include spoilers or solutions, or that contain inappropriate or off-topic material, should be edited quickly to remove text, images, or links. 

#. Log in to the course with your discussion manager username.

#. Click the **Edit** button below the post or response.

#. Remove the problematic portion of the post, or replace it with standard text such as "[REMOVED BY MODERATOR]".

#. Communicate the reason for your change. For example, "Posting an answer violates the honor code.""

==================
Deleting posts 
==================

Posts and responses can be deleted by discussion moderators, community TAs, and admins. Posts that include spam or abusive language may need to be deleted, rather than edited. 

#. Log in to the course with your discussion manager username.

#. Click the **Delete** button below the post or response.

#. Click **OK** to confirm the deletion.

.. how to communicate with the poster?

**Important**: If a post is threatening or indicates serious harmful intent, contact campus security at your institution. Report the incident before taking any other action. 

==================================
Responding to reports of misuse
==================================

Students can use the **Report Misuse** flag to indicate posts that they find inappropriate. Moderators, community TAs, and admins can check for posts that have been flagged in this way and edit or delete them as needed.

#. Open the course in Edge or edX and click **Discussion** at the top of the page.

#. On the drop-down list of discussion topics click **Show Flagged Discussions**.

#. Review each post listed as a flagged discussion. Posts and responses show a flag and **Misuse Reported** in red font; comments show only a red flag.

#. Edit or delete the post. Alternatively, leave the post unchanged and click **Misuse Reported** or the flag to remove  the notification.

.. ===============
.. Blocking users
.. ===============
.. is this the same as "unenrollment"? standard instructor dashboard > Batch Enrollment > enter email address > **Unenroll multiple students**?)


