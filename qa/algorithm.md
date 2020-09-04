# Questions on Algorithms for pairwise Alignments

## How does the algorithm work?
* What is the reason to choose the maximum score in the Needleman-Wunsch and Smith-Waterman for each position in the matrix S?
* What was the approach of finding the best global alignment before Needleman and Wunsch published their article? Were all possibilities of alignment tested or was it considered to be too time consuming for longer sequences so no one bothered?
* Is it really necessary to back trace in these examples in order to find the optimal alignment?  it looks to me that you can find them by only going forward... but maybe its more relevant for longer sequences?
* In the lecture video. In the example of the Needleman-Wunsch , a grid was drawn with the two different sequences (one horizontal and the other vertical). Why does -1, -2, -3  go along the axes (closest to the sequences) from S(0.0)? Could it be any other way?
* When investigating the most optimal alignment of two sequences with Needleman-Wunsch, is it performed programmatically or manually? If it’s performed manually, what maximum length of the two sequences is possible to manage?

## (Non)uniqness of optimal Alignments

* After completing a matrix which returns more than one optimal alignment, how do you then between these decide which is the actual optimal alignment? I.e. is there a next step?

## Global/Local/Glocal
* Why is Smith Waterman a better method for just comparing a part of two sequences?
* When would you use global, semi-global and local alignment? That is, is there a hard limit for when each method is valid or not?
* What is the reason for setting the score to 0 when all other options are negative for the Smith Waterman alignment?compared to the Needleman-Wunch method
* As I understand it, the main differense between the global and local algorithms is that in the local all values are forced to be zero or above, how does this make the aligment local?
* Why are the initiations for Needleman-Wunsch and Smith-Waterman so different?

## Significance
* Until which score, sequences are considered as genetically related?
* What is a good alignment score?
* Is the score unitless?

## Complexity
* What is the computaional complexity of these alignment algorithms? And are they parallelizable?
* How are both algorithms used when it comes to larger proteins? Do you divide the protein into smaller sections? And are they also capable of running several parallel processes in real-time?


## Score functions
* In your video example, the scoring for mismatches and gaps are the same (-1). I was thinking about the fact that insertions and deletions can cause frameshift mutations and that this should affect the optimal alignment. If we choose to set the scoring of both the mismatches and the gaps to -1, how do we take the frameshift-problem into account?
* How are the values for p, g and n chosen, i.e what is the scoring based on? Are these arbitrary as long as you keep the same scoring function when comparing sequences?
* Why does not the sophisticated scoring system take the size of the gap as a factor? What if a new essential function of the protein would lie in the new gap that is longer than another gap without the function?
* Are there cases where a mismatch is more troublesome (should be more penalized) than a gap? If so, for what kind of genes/sequences?
* How often is gap penalties used?
* The book explains the difficulty of doing local alignments. One of the difficulties is the sensitivity of the gap parameters (for both the first introduced gap and for gap extensions). How do we know what values to use (when the sequences aren't so short we can use our own eyes to see what is the best)? How can we make local alignments robust?
* In which condition (Can you give un example?) we use a scoring system where n is higher than g, and in which condition g should be higher than n? And is there a reasonable range for the difference between the three scores p, g, and n?
* In the online lecture video where you give an example of aligning using Needleman-Wunch, the score is -1 for both a mismatch and a gap. In the example in the book, the score for a gap is also -1 but the score for a mismatch is 0. How do you know what scoring function to use, or do you get to choose yourself?



## Next lecture
* When would you choose to calculate the alignment score with methods based on aligned residues (such as BLOSUM62) and when is it more preferable to use the methods based on aligned bases?
* Can you do a Needleman-Wunsch Algorithm for a AA sequence?
* Can alignment of DNA give other information that alignments of protein strands can not? Or viceversa?
* Are there any scoring methods that differentiate between different mismatches (like BLOSUM for proteins) - for example scores the mismatch A&C lower than the mismatch A&G - or are all mismatches always scored equally?
* As it has been explained , for Needlman-Wunschand and Smith-Waterman two sequences are needed. What we have to do if instead two sequences we want to compare 3,4,5... or more at the same time?
* In the notebook on pairwise alignments:  How were the scores in the PAM250 matrix determined?


## Previous lecture
* I was thinking about the crime you talked about that was recently solved using alignment. In which way was alignment more effective than other DNA techniques commonly used at crime scenes?

## General questions
* What is recursion?



## Not understood
* In the Needleman-Wunsch alignment method, what are the criteria for dividing the long stretch of genome into smaller sub-parts and performing dynamic programming? Can the target gene be eliminated in this way?
