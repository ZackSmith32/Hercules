.name "bambi"
.comment "The shadows betray you, because they belong to me"

live:	
		live %1
		fork %:frkn	
		zjmp %:live

frkn:
		live %10000
