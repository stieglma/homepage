Projects
########
:date: 2014-02-27 23:03
:author: Thomas Stieglmaier
:sortorder: 2
:icon: folder-open

| This is simply a list of my current and finished projects. Feel free to use them.
|

Science
-------
- `CPAchecker`_ is a software used for automated software verification. It is mainly used for verifying C code against specifications like the reachability of error labels or if conditions of assert statements hold in every possible program execution. CPAchecker is a Project of the `Software Systems Lab`_ where I am working as a student assistant since 2011/07.
- `Octagon-Based Software Verification with CPAchecker`_ is the topic of my Bachelor's Thesis. It introduces a formalism for a configurable program analysis (CPA) based on the octagon abstract domain. Several different configurations of this CPA and how it can be used to analyze programs in a time- and memory-efficient manner are discussed. The evaluation of these approaches is done on two implementations of octagon-based CPAs in CPAchecker, a CPA using the Octagon Abstract Domain Library and a CPA using the APRON library. Both CPAs are compared to other analyses implemented in CPAchecker and other tools. Overall, octagon-based CPAs are not as memory-efficient as an explicit-value analysis, but they perform strictly better on programs which rely on inter-variable relations.
- `Live-Variables within CPAchecker`_ was a project that I worked on during the lecture *Software Verification* with two colleagues, Sebastian Ott and Thomas Ziegler. In the project we created a CPA that computes the set of live-variables for each program location. This information is quite useful for later analyses, especially when it comes to shrinking the possible state space by removing variables that are irrelevant at certain location from the appropriate states, and therefore having a higher level of abstraction.
- `Path Invariants in CPAchecker`_ is the outcome of a seminar on software verification. I implemented and evaluated invariant generation bound to found (infeasible) error paths in CPAchecker. With invariants we hoped to reduce the number of necessary loop unrollings while doing predicate abstraction together with CEGAR. The evaluation shows that the overall impact is not very high, but still about 1.5% (about 30 runs) more of the analyzed programs could be verified correctly.
- `Integration and Evaluation of the Multext-East Corpus in NLTK`_ was the topic of our work in the *Text-Mining Project*, a course I attended in 2015 during my studies. I worked on this project with two colleagues, Alexander Böhm and Thomas Ziegler. We created a corpus reader for the `Multext-East`_ corpus which is now integrated in `NLTK`_. For more information about the evaluation and the code please refer to the linked github repository and the documentation which resides there, too. The work can also be downloaded `here`_

Wordpress
---------
- `Mail()man Subscription`_ a simple plugin which generates a widget allowing users to subscribe to mailing-lists via the php mail() function

Games
-----
- `Sillard`_ a game which was created by 5 friends of mine + me on a `Weekend of Code`_. It is a mixture of soccer and billiard.
- `Schafkopfauswerter`_ is a tool for the documentation and evaluation of Schafkopf-games. It provides statistics in the form of tables and plots, allows saving the current scores and also a pdf export is available. This tool was completely rewritten with `AspectJ`_ as a project during the lecture *Software Product-Line Engineering*. AspectJ is a seamless aspect-oriented extension to Java which, for example, allows to modularize crosscutting concerns.
- `jSoccer`_ a Framework where self-programmed AI's can play soccer against each other. This project was developed during the "Software Engineering Project" at the University of Passau with 5 other students. It is no longer maintained, however if you have questions, feel free to contact me.


.. _`Mail()man Subscription`: https://github.com/IEEE-SB-Passau/Mailman-Subscription
.. _`Sillard`: //play.google.com/store/apps/details?id=de.passau.ieee.woc.sillard.android&hl=de
.. _`Weekend of Code`: //ieee.uni-passau.de/de/event/weekend-of-code-2/
.. _`Schafkopfauswerter`: https://github.com/stieglma/Schafkopfauswerter
.. _`jSoccer`: //stieglmaier.me/uploads/jSoccer.zip
.. _`CPAchecker`: //cpachecker.sosy-lab.org
.. _`Octagon-Based Software Verification with CPAchecker`: //stieglmaier.me/uploads/thesis.pdf
.. _`Live-Variables within CPAchecker`: //stieglmaier.me/uploads/liveVariables.pdf
.. _`Software Systems Lab`: //sosy-lab.org
.. _`Integration and Evaluation of the MULTEXT-East Corpus in NLTK`: //github.com/jwacalex/MULTEX-EAST-PoS-Tagger
.. _`NLTK`: //www.nltk.org/
.. _`Multext-East`: //nl.ijs.si/ME/V4/
.. _`Path Invariants in CPAchecker`: //stieglmaier.me/uploads/invariants.pdf
.. _`AspectJ`: https://eclipse.org/aspectj/
.. _`here`: //stieglmaier.me/uploads/multext_nltk.pdf
