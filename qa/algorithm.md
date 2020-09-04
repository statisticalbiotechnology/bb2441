# Questions on Algorithms for pairwise Alignments

* If we get multiple alignments with the same score from the matrix, which alignment is "chosen"? Are they both investigated further?
* In what context/situation is the semi-global alignment used instead of the other two methods? Basically, what are the benefits of using the semi-global alignment rather than the other methods.
* In your video example, the scoring for mismatches and gaps are the same (-1). I was thinking about the fact that insertions and deletions can cause frameshift mutations and that this should affect the optimal alignment. If we choose to set the scoring of both the mismatches and the gaps to -1, how do we take the frameshift-problem into account?
* What is the reason for vertical and horisontal movements in the matrix being registered as gaps? That is, what is the logical reasoning behind it?
* In the video examples of how to calculate the optimal alignment, the best movement in each position is calculated to find the path yielding the highest score. Isn't this time consuming for longer sequences? Is there a faster way to do this?
* In the online lecture video where you give an example of aligning using Needleman-Wunch, the score is -1 for both a mismatch and a gap. In the example in the book, the score for a gap is also -1 but the score for a mismatch is 0. How do you know what scoring function to use, or do you get to choose yourself?
* What is the reason to choose the maximum score in the Needleman-Wunsch and Smith-Waterman for each position in the matrix S?
* What is the reason for setting the score to 0 when all other options are negative for the Smith Waterman alignment?compared to the Needleman-Wunch method
* Is the highest score alignment always the best option? Has it ever happened that a suboptimal alignment was chosen instead of a higher score? What can we do if our best score alignment doesn't fit our experimental needs?
* What do you mean by that recursion in semi-global is similar to Needleman-Wunch when the algorithm is similar to Smith-Waterman and can a Needleman-Wunch algorithm  then carry out the semi-global alignment?
* What was the approach of finding the best global alignment before Needleman and Wunsch published their article? Were all possibilities of alignment tested or was it considered to be too time consuming for longer sequences so no one bothered?
* What is the definition of overshooting sequence terminals?
* When would you use global, semi-global and local alignment? That is, is there a hard limit for when each method is valid or not?
* How are the values for p, g and n chosen, i.e what is the scoring based on? Are these arbitrary as long as you keep the same scoring function when comparing sequences?
* What would be the upper limit for a Smith-Waterman alignment, at what point should a global alignment be used instead?   
* When would you choose to calculate the alignment score with methods based on aligned residues (such as BLOSUM62) and when is it more preferable to use the methods based on aligned bases?
* What is the "benefit" or difference between using a global and a semi-global aligment approach regarding the result? When/why would you use either approach?  
* Until which score, sequences are considered as genetically related?
* What are the main limitations of the Needleman-Wunsch algorithm? How is it modified for other types of alignments?  * What are the strengths and weaknesses of the Smith-Waterman algorithm?
* Could you give some other actual examples/reasons of aligments where you either have to choose between a doing a global, semiglobal, or a sectional search?

When should I choose one over the other?

* What are the limitations of using dynamic programming for alignments?
* Why does not the sophisticated scoring system take the size of the gap as a factor? What if a new essential function of the protein would lie in the new gap that is longer than another gap without the function?

* What is the main difference between the PairWise algorithm (local alignment algorithm) and other alignment algorithms?
* What is a good alignment score?
* As I understand it, the main differense between the global and local algorithms is that in the local all values are forced to be zero or above, how does this make the aligment local?
* In the lecture video. In the example of the Needleman-Wunsch , a grid was drawn with the two different sequences (one horizontal and the other vertical). Why does -1, -2, -3  go along the axes (closest to the sequences) from S(0.0)? Could it be any other way?
* When investigating the most optimal alignment of two sequences with Needleman-Wunsch, is it performed programmatically or manually? If it’s performed manually, what maximum length of the two sequences is possible to manage?
* Are there cases where a mismatch is more troublesome (should be more penalized) than a gap? If so, for what kind of genes/sequences?
* I was thinking about the crime you talked about that was recently solved using alignment. In which way was alignment more effective than other DNA techniques commonly used at crime scenes?
* I have a question about the semiglobal- alignment. Which algorithm is commonly used for this type of alignment and in which case is this alignment desired?  
* Is Smith-Waterman ever preferred over Needleman-Wunsch, if so, when and why?
* Can you do a Needleman-Wunsch Algorithm for a AA sequence?

* Can alignment of DNA give other information that alignments of protein strands can not? Or viceversa?
* For which purpose are the global alignment technique used?
* How often is gap penalties used?
* Why are the initiations for Needleman-Wunsch and Smith-Waterman so different?
* After completing a matrix which returns more than one optimal alignment, how do you then between these decide which is the actual optimal alignment? I.e. is there a next step?
* Why are the scores compared to zero in the Smith-Waterman algorithm?
* The book explains the difficulty of doing local alignments. One of the difficulties is the sensitivity of the gap parameters (for both the first introduced gap and for gap extensions). How do we know what values to use (when the sequences aren't so short we can use our own eyes to see what is the best)? How can we make local alignments robust?
* The book briefly mentions semi-global alignments. Can this be carried out with the Needleman-Wunsch algorithm by simply removing the gap penalty? Or does it require a different approach regarding the design of the matrix?
* In real life, what would be the reason (which experiments or what we are looking for) for using the global, local or semi-global methods ?
* What is recursion?
* An addition of what is added to the score?
* Is the score unitless?
* Are there any scoring methods that differentiate between different mismatches (like BLOSUM for proteins) - for example scores the mismatch A&C lower than the mismatch A&G - or are all mismatches always scored equally?
* how to backtrack through the matrix to see possible path and get the optimal alignment ?
* Can you explain the difference between local and semiglobal alignment?
Can you give practical examples on when you could have more use of local alignment, i.e not to use penalty?  Also, when would it be better to use a semi-global alignment instead of a local alignment?
* In which condition (Can you give un example?) we use a scoring system where n is higher than g, and in which condition g should be higher than n? And is there a reasonable range for the difference between the three scores p, g, and n?
* Why is Smith Waterman a better method for just comparing a part of two sequences?
* if multiple alignments give the same score how to proceed further?
* Is it really necessary to back trace in these examples in order to find the optimal alignment?  it looks to me that you can find them by only going forward... but maybe its more relevant for longer sequences?
* As it has been explained , for Needlman-Wunschand and Smith-Waterman two sequences are needed. What we have to do if instead two sequences we want to compare 3,4,5... or more at the same time?
* In what cases are each aligment (global, semi-global or local) prefered?  
* In the Needleman-Wunsch alignment method, what are the criteria for dividing the long stretch of genome into smaller sub-parts and performing dynamic programming? Can the target gene be eliminated in this way?
* What is the computaional complexity of these alignment algorithms? And are they parallelizable?
* In the notebook on pairwise alignments:  How were the scores in the PAM250 matrix determined?
* How are both algorithms used when it comes to larger proteins? Do you divide the protein into smaller sections? And are they also capable of running several parallel processes in real-time?
* On semi-global alignments: In your video, you say that the final score is calculated as the maximal element on the rightmost column or the bottommost row. Does this mean that the optimal alignments provided by semi-global alignments are shorter sequences than the provided sequences, similar to the optimal sequences for local alignments?
