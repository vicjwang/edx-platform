##############
Discussions
##############

Discussions, or discussion forums, foster interaction among your students and between students and course staff. You set up the topics that you want students to discuss when you create your course, and then run and moderate discussions throughout the course to guide participation and community development. Discussions are also excellent sources of feedback and ideas for the future.

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

This type of discussion is subject to the release date of the section that contains it and is not visible to students until that date.

=====================================
Creating discussion categories
=====================================
All courses have a Discussion static page that includes a course-wide discussion category named General by default. 

You can add more discussion categories to guide how students share and find information during your course. Categories might include Feedback, Troubleshooting, or Technical Help. These discussions are available as soon as your course is available.

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

5. Replace the second "General" with the name of your new discussion category.

#. Change the second id value to a unique identifier. For example, add the category name:


 | {
 |   "General": {
 |       "id": "i4x-test_doc-SB101-course-2014_Jan"
 |   }
 |    "FAQ": {
 |        "id": "i4x-test_doc-SB101-course-2014_Jan_faq"
 |    }
 | }

7. Click **Save Changes**.

The list of Discussions that displays for your course includes this new category.

.. _Assigning_discussion_roles:

========================================
Assigning roles 
========================================

In addition to the course staff, you can designate a team of people to help you run and moderate discussions. Different options for working with discussion posts are available to these different discussion-related roles:

* Forum admins typically include the course author and some members of the staff.

* Forum moderators also are usually the course staff and can also include registered students.

* Forum community TAs can be registered students.

(? I'm not clear on the purposes for these different roles yet, or what UI options apply to each designation. Part of the gudance for moderators? Melanie, Jennifer Akana, Jane from Stanford, Victor)

You can assign these roles to more people while your course is running, or remove a role from a user whenever necessary. 

Before you can designate your forum admins, forum moderators, and forum community TAs, you need the email address of the person you want to add or delete. 

* To get the email address for a staff member, on the Instructor Dashboard click **Membership** and then select Course Staff from the drop-down list.

* To get the email address of a student, (? how do they get this info?).

To assign a role:

#.  On the instructor dashboard for your course, click **Membership**.

#. Select Forum Admins, Forum Moderators, or Forum Community TAs from the drop-down list.

#. Under the list of users who currently have that role, enter the email address and click **Add** for the role type.

(? are there requirements as to whether an admin must already be staff, or can it be a registered student? other requirements?) 

(? why are these labels using "forum" and not "discussion"? asked Victor)

.. _Running_discussions:

*********************
Running a discussion
*********************

On an ongoing basis, the forum admins, moderators, and community TAs run course discussions by making contributions and guiding student posts into threads. Techniques that you can use throughout your course to make discussions successful follow.

========================
Seeding a discussion
======================== 

Before you contribute to a discussion, you can decide whether you want your post to be identified as coming from someone with one of the discussion forum roles, or without any distinguishing identifiers. Depending on the subject and purpose of your post, one or the other might be more appropriate to spark discussion and inform students.

* To identify your posts with your role, log in with your course or forum staff credentials and add the post or response. Contributions that you make while logged in as staff have a colored banner with your role (admin, moderator, or community TA). (? need to determine if it is a staff identifier or a forum-related identifier or both. show image? also, why are responses and comments identified, but not the "new posts" themselves?)
 
* To post as a student, you must set up an alternate user account with a different email address, register for the course, and post under that account. These posts do not have a banner and appear like any other student post. See :ref:`Seed a Discussion Space in Your Course`.
 
You can also post anonymously. Regardless of your role, you can choose to make a post anonymous. However, you may want to discourage your students from posting anonymously, and therefore choose not to use this option yourself.

==========================================
Using conventions in discussion subjects
==========================================

To identify certain types of posts and make them easier for your students to find, you can define a set of standard tags to include at the beginning of the subject. Examples follow.

* "[OFFICIAL]" in the subject can indicate an announcement about a change to the course.

* Information about a corrected error might have subject that begins "[ERRATA]".

* Use "[INTRO]" for a post in the General discussion to start a thread for individual student and staff introductions.

* Direct students to use "[STAFF]" in the subject of each post that needs the attention of a course staff member.

======================================
Minimizing thread proliferation
======================================

To encourage longer, threaded discussions rather than many similar, separate posts, you can use these techniques.

* Pin a post. 

  Pinning a post makes it appear first in the discussion, so that it is more likely that students will see and respond to it. You can write your own post and then pin it, or pin a post by any author. Forum admins and moderators (?) can click the **pin** icon that displays at lower right of the post text. (image)

* Close a thread. 

  You can respond to a redundant post by pasting in a link to the thread that you prefer students to contribute to, and then prevent further thread interaction by closing it. Forum admins and moderators (?) can click the **Close** button that displays below a post to close it. (image)

* Provide guidelines.

  Your *Discussion Forum Guidelines* or a post in the General discussion can provide explicit guidance about when to respond to an existing post instead of clicking **New Post**. For a template that you can use to develop guidelines for your own course, see :ref:`Discussion Forum Guidelines`.

.. _Moderating_discussions:

***********************
Moderating discussions
***********************

Moderators monitor discussions and keep them productive. They also relay inforrmation, such as areas of particular confusion or interest, to the rest of the course staff. Developing and sustaining a positive discussion culture requires sufficient moderator time to be dedicated to reviewing and responding to discussions. 

Keeping up-to-date with a large MOOC forum requires a commitment of 5 or more hours per week, and involves reading posts, replying to and editing posts, and communicating with the other moderators and course staff.

For information on setting up moderators for your course, see :ref:`Assigning_discussion_roles`.

========================================
Providing discussion guidelines 
========================================

TBD

(make available as a course handout file or as a static page, reinforce with posts)

(write up boilerplate, perhaps course 2400 is a useful model?)

For a template that you can use to develop your own guidelines for your course moderators, see :ref:`Guidance for discussion moderators`.

========================================
Developing a positive forum culture
========================================

Moderators and course staff members can cultivate qualities in their own interactions with the discussions to make their influence positive and their time productive.

* Encourage quality posts: thank students whose posts have a positive impact and who answer questions.

* Check links, images, and videos in addition to the text that students post. Edit offensive or inappropriate posts quickly, and explain why.

* Review posts with a large number of votes and recognize "star posters" publicly and regularly.

* Stay on topic yourself: before responding to a post, be sure to read it completely

* Maintain a positive attitude. Acknowledge problems and errors without assigning blame.

* Provide timely answers. More time needs to be scheduled for answering discussion questions when deadlines for homework, quizzes, and other milestones approach.

* Discourage redundancy: before responding to a post search for similar posts. Make your response in the most pertinent or active thread, then use links to direct other posts to that thread.  

* Publicize issues raised in the discussions: add questions and their answers to an FAQ discussion category, or announce them on the Course Info page. 

For a template that you can use to develop your own guidelines for your course moderators, see :ref:`Guidance for discussion moderators`.

==================
Editing posts 
==================

Posts can be edited by their authors, and also by forum admins/moderators/TAs (? find out). Posts that include spoilers or solutions, or that contain inappropriate or off-topic material, should be edited to remove the text, images, or links. 

#. Click the **Edit** button below the post.

#. Remove the problematic portion of the post, or replace it with standard text such as "[REMOVED BY MODERATOR]".

#. Communicate the reason for your change. For example, (?).

==================================
Responding to reports of misuse
==================================

(? this is a ui control available to students)

(? I can't figure out how this gets surfaced to the forum roles)

==================
Deleting posts 
==================

Posts can be deleted by their authors, and also by forum admins/moderators/TAs (?). Posts that include abusive or harrassing language, that are made during an exam (if posting is prohibited), or that otherwise violate the honor code, may need to be deleted, rather than edited. Click the **Delete** button below the post.

When you delete a post, be sure to communicate why to with the student. For example, (? both example and how?).

**Important**: If a post is threatening or indicates serious harmful intent, contact your institution's campus security. Report the incident before taking any other action. 

===============
Blocking users
===============

(?) 

(is this the same as "unenrollment"? standard instructor dashboard > Batch Enrollment > enter email address > **Unenroll multiple students**?)


