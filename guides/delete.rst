.. _delete:

***********************
delete
***********************

give an example

how does delete work?

soft update concept

delete cleanup and it's properties. automatic/manual, in transaction or background

automatic background gives fast delete, minimal transaction overhead,
small cost to queries until background reorganised

pointer to the time based management idea - delete is optimised for this

when does delete use the metadata effectively

more examples

truncate is the same as delete without a predicate/ delete where true

