# What iteration actually uncovered

Updated November 2026.

These classes were observed during development of the research prototype. The
examples below are generic illustrations, not copied article passages. Changes
were evaluated through focused tests and human inspection; they do not establish
that the error class has been eliminated across unseen publications.

| Observed failure | Why it mattered | Response and verification | Remaining boundary |
|---|---|---|---|
| A citation abbreviation such as “et al.” split a sentence | Reviewers saw incomplete claims and extra sentence tasks | Added abbreviation-aware splitting and synthetic regression cases | Unseen abbreviations and layout combinations still require evaluation |
| A paragraph continued in the next column or page but was presented separately | A scientifically relevant sentence could lose its second half | Introduced provenance-preserving reading units and targeted continuity checks | No universal claim that paragraph reconstruction is solved |
| Technical prose was proposed as substantive evidence | A method reference or procedure description could inflate the inventory | Refined category scope, preserved local context and enabled explicit human correction | Scientific classification accuracy is not yet independently benchmarked |
| One sentence supported multiple entities and appeared repeatedly | Entity count became unnecessary reviewer workload | Grouped shared evidence while preserving relationship-specific decisions | Reduced duplication is demonstrated; time savings have not been quantified |
| An exported review existed without confirmed server persistence | A “completed” coding session could remain unsaved on the server | Required save acknowledgement; added history, revision conflicts, draft export and actual save/reload checks | Local safeguards are not a production backup or authenticated multiuser system |
| An isolated sentence lacked enough context for a human judgment | A disagreement could reflect missing information rather than a different scientific interpretation | Added clearer study orientation and nearby source context to review tasks | The effect on independent coding quality still needs measurement |
| A later automated review conflicted with an accepted decision | A new suggestion could silently replace earlier expert work | Retained the first decision and recorded the later conflict separately | Resolving a conflict still requires evidence and, where needed, human judgment |

The engineering pattern is consistent: identify a failure, retain the original
evidence, make the correction explicit, and verify the particular failure mode.
The next scientific task is to measure performance on frozen, independently
coded material rather than treating these development observations as a benchmark.
