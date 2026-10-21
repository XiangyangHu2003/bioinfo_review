# Day 1 Questions

## Whats the difference between 'list' and 'set'?
### List keeps order and allow duplicates. Set stores unique values only, and do not allow indexing. Set can be used to quick membership checks and set options like union and intersection. 

## Would you apply open() to 100GB FATSA file?
### No,because that will fill up all the RAM. Instead, I would use with Path().open().

## What would you do if there's a malformed FASTA when you are parsing a FASTA data?
### I would validate the FASTA format during parsing. If I find issues like a missing header, an empty ID, invalid sequence characters, or duplicate IDs, I would raise an informative error or skip the bad record with a warning, depending on the use case.

# Day 2 Questions

## What should you first do if the number of people turned to 940 from 1000 after merge?
### I would first audit the join cardinality and identify unmatched sample IDs. I want to understand why 60 samples were lost before continuing the analysis.

## Should you just delete all the outliers?
### I would not automatically remove an outlier. I would first determine whether it reflects a technical error, a data-entry issue, or true biological variation, and then perform a sensitivity analysis with and without the outlier.