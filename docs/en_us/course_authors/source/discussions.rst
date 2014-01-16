##############
Discussions
##############

Discussions, or discussion forums, promote interaction among your students and between students and course staff. You organize the discussions that you want to take place when you create your course, and then run and moderate discussions throughout the course to guide participation and community development. Discussions are also excellent sources of feedback and ideas for the future.

*************************************************
Organizing discussions for your course
*************************************************

Discussions in an edX course are either specific topics that you add to course units as discussion components or course-wide areas of interest, such as Feedback or Technical Help, that you add to the set of 

============================================
Adding units with a discussion component
============================================

Typically, all units are added when you design your course in Studio. If you decide to add a design component to a unit, follow the instructions in...

These discussions are tied to the release date of the subsection (?) that contains them, so they are not visible until that date

=====================================
Creating discussion categories
=====================================
All courses have a static page for Discussion which includes a course-wide discussion category named General. 

<image>

You can add more categories to this list so that students can share and find information throughout the course about topics like Feedback, Troubleshooting, or Technical Help.

(? still can't figure out how to do this - not in instructor dashboard. Melanie's screen shot)
Studio > course > Settings > Advanced 
Policy Key = discussion_topics
Copy "General" through it's closing brace
"General": {
        "id": "i4x-test_doc-SB101-course-2014_Jan"
    }
and paste it in
change General to the new category name
change the id value to a unique value, perhaps by adding the category name
<image>    

These discussions are available when your course is available.

=======================
Discussion who's who 
=======================

You can designate members of your course staff, and registered students, to help you run and moderate discussions. Different options for working with discussion posts are available to these different roles:

- Forum admins typically include the course author and some members of the staff
- Forum moderators also are usually the course staff and may include some registered students
- Forum community TAs are often registered students

(I'm making this up, not yet clear on the different roles/options for each designation.)

To designate forum admins, forum moderators, or forum community TAs, you need the user name of the person you want to add or delete. (? how do they get this info?) Then, you use the instructor dashboard (old instructor dashboard) > forum admin > insert user name (are there requirements as to admin must already be staff, or any registered student?) > **Add forum admin**)


*********************
Running a discussion
*********************

========================
Seeding a discussion
========================

 There are a number of ways that course staff can contribute to a discussion. You might want these contributions to be identified as coming from a staff member, or you might want to post as a student peer to initiate or guide a discussion.

 * Log in with your course staff username and add the post or response. Your posts are identified with a colored banner with your role (admin, moderator, or community TA).
 .. <image>
 * Set up an alternate edX user name under a different email address, register for the course, and post under that name. These posts do not have a banner and appear like any other student post.
 
 You can also post anonymously. Regardless of your role, you can choose to make a post anonymous. However, you may want to discourage your students from posting anonymously, and therefore choose not to use this option yourself.

=======================================
Using conventions in discussion subjects
=======================================

To identify certain types of posts and make them easier for your students to find, you can define a set of standard tags to include in the subject. 
- An announcement about a change to the course might have subject that begins "[OFFICIAL]"
- Information about a corrected error  might have subject that begins "[ERRATA]"
- A thread in the General discussion for individual introductions could be started by a post with the subject "[INTRO]"
- Students can be directed to use [STAFF] at the beginning of posts that need the attention by a course staff member

=====================
Minimizing thread proliferation
=====================

Different techniques are available to encourage longer, threaded discussions rather than multiple similar but separate posts.

- Pin a post. Pinning a post makes it appear first in the discussion, making it more likely that students will respond to it. You can seed a discussion by writing your own post and then pinning it, or pin a post by any author. Forum admins and moderators (?) can click the **pin** icon that displays at lower right of the post text.
- Close a thread. You can respond to a post by pasting in a link to the thread that you want students to contribute to, and then prevent further responses to the thread by closing it. Forum admins and moderators (?) can click the **Close** button that displays below a post to close it.

Your Discussion Forum Guidelines or an [OFFICIAL] post under the General discussion can also provide explicit information about when to respond to an existing post as distinct from creating a new post (that is, by clicking **New Post** and selecting a discussion).

***********************
Moderating discussions
***********************

Designated forum admins, moderators, and community TAs  

========================================
Providing discussion guidelines 
========================================

(either as a course handout file or as a static page, reinforced by posts)
(write up boilerplate)


========================================
Developing a positive forum culture
========================================

(?)
- Encourage quality posts: review posts with a large number of votes and recognize those "star posters" regularly.
- Thank students who answer questions.
- Provide timely answers: schedule more time for answering discussion questions when deadlines for homework, quizzes, and other milestones approach.
- Check all posted content: links, images, videos, and any other additions to posted text should also be reviewed to assure compliance with the honor code.
- Discourage redundancy: redirect the poster to an earlier, more active, or higher quality thread by pasting its URL into your response. 
- Add questions and their answers to an FAQ (or other appropriate) discussion category, or announce them on the Course Info page.

==================
Editing posts 
==================

Posts can be edited by their authors, and also by forum admins/moderators/TAs (?). Posts that include spoilers, solutions, etc. can be edited to remove the inappropriate text, images, or links. Click the **Edit** button below the post.

When you edit a post, consider using a convention that communicates that a change has been made, and why. For example, (?).

==================
Deleting posts 
==================

Posts can be deleted by their authors, and also by forum admins/moderators/TAs (?). Posts that include abusive or harrassing language, that are made during an exam (if posting is prohibited), or that otherwise violate the honor code, may need to be deleted, rather than edited. Click the **Delete** button below the post.

When you delete a post, be sure to communicate why to with the student. For example, (? both example and how?).

important:: If a post is threatening or indicates serious harmful intent, contact your institution's campus security. Report the incident before taking any other action. 

==================================
Responding to reports of misuse
==================================
(? this is a ui control available to students)
(I can't figure out how this gets surfaced to forum admins)

===============
Blocking users
===============

(?) 
(is this standard instructor dashboard > Batch Enrollment > enter email address > **Unenroll multiple students**?)

