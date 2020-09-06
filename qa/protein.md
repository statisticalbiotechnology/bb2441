
# Questions on Alignments of Protein Sequence

## AA vs. DNA
* When we use protein alignments, we use the amino acid sequences of genetic codes instead of nucleotide sequences. How sure are we usually in the translation to amino acid sequence? Is it easy to know from the nucleotide sequence what amino acid it corresponds to, or do we have some uncertainty due to the reading frame etc? The book mentioned that a small nucleotide difference in alignment wouldn't always change the amino acid, and that made me wonder how this works. Furthermore, where lies the boundary between when we want to use nucleotide alignment and protein alignment?

* Is aligning proteins instead of sequences something that has recently started being used? Has this in that case led to any specific improvement within the field of bioinformatics?

## BLOSUM vs. PAM

* What is the difference in scores between the PAM matrix and the BLOSUM matrix, and why? i.e. how does the scores/matrix change depending on if it is suitable for global/local alignments or similar/non-similar sequences?

* Which method is most commonly used, PAM or BLOSUM?

## Their numbering

* What does the number in PAM250 and BLOSUM45 stand for? And if higher numbers (for PAM) and lower numbers (for BLOSOM) are preferred, why use any other number, e.g. why use BLOSUM62 when you can use BLOSUM45?
> The numbers after PAM are the no. of mutations per 100 amino acid and for the numbers of BLOSOM it's the percentage identity of the proteins used, I assume the ones that we compare.
  And to answer why BLOSOM62 is used is because apparently it's the standard matrix for BLAST is has been found, through experimentation, to be the best for detecting most weak protein similarities.

* If PAM1 represents an average change of 1 amino acid in 100, is then PAM 250 represents an average change of 250 amino acid in 100? How does that work?

* If you use a substitution matrix as a scoring matrix as described in the book, would you always use it with a Needleman-Wunsch algorithm? Or would you use the PAM matrix to score the Needleman-Wunsch algorithm (since PAM is based on global alignments) and the BLOSUM matrix to score the Smith-Waterman algorithm (since BLOSUM is based on local alignments)?

* According to chapter 5, lower numbers of PAM are suitable for short sequence alignments. Why is this more suitable? Is it because shorter sequences are more likely to be evolutionarily closely related compared to longer sequences?  

* How do we choose what matrix to use if we do not have any prior expectations on % identity for our alignment? If we use for example BLOSUM65, which is built on target frequencies for 65% identity, and it gives a high score, what does that tell us? If we have higher than 65% identity, would that give a high or low score when using BLOSUM65?

* About the BLOSUM numbering: In the book on p. 86, it says, "... a BLOSUM matrix [is] computed by choosing blocks more than 62% identical", whereas in the paper by Eddy, it is stated that "[they] only counted pairwise sequence alignments related by less than some threshold percentage identity. A threshold of 62% identity or less resulted in in the target frequencies for the BLOSUM62 matrix." So, are the chosen blocks for BLOSUM62 more or less than 62% identical?


## How are the LLR Calculated
* Just want to check if I have understood this correctly. In protein alignment, is the substitution matrix ​​a way to evaluate if you do not match with the same amino acid there are certain other amino acids that are more or less beneficial to the alignment of a certain amino acid?
  If you look at figure 5.5 on page 85. You see that Alanine is best aligned with Threonine (if you ignore taking Alanine). What makes me confused is that it gives the same score to take Alanine as Threonine (score 2 for both), shouldn't Alanine be most beneficial?

* In order to calculate a score 's(a,b)' according to the equation given in the article you need to have the target frequencies as well as the likelihood of the null hypothesis. How are these values retrieved? From a databank or should they be statistically calculated?

* When calculating the scores, where does one find all the different probabilities for a, b and ab? Are they to be found in a databank and in that case, which?

* The book mentions matrices based on chemical properties like hydrophobicity and gives an example of an alignment matrix using a scoring matrix based on it. I was wondering what other chemical (or physicochemical) properties these scoring matrices usually are based on?

* How come the preservation of different aminoasids get different scores in the scoring matrix? It makes sense that different substitutions have different scores because of polarity, hydrofobisity and so on but shouldn't the complet match be the same for all aa as a baseline to compare the substitutions to?


* What is the point of rounding the values up to integers for the scoring matrices? If the calculations are done using a computer would it not be better to just round the final score instead for more correct numbers?
* Lambdas are given in order to round the result of the equation [d(a, b)] can be rounded with as little error as possible to the next integer value, but how do you practically decide which lambda is the best for your matrix? do all matrices have their assigned lambdas and, if so, how were they assigned?
*  Regarding building your own substitution matrix: They mention in the book that a pseudocount is used to account for substitutions that don't appear in the training set. These substitutions  are given a value of 1 divided by the number of aligned positions. However, I tried applying this to the example in figure 5.7 and couldn't reach the same conclusions as them. How exactly did they calculate the values in the substitution matrix?

## Gaps
* In the book, when discussing deciding a score for the gap-penalty,  they mention "not overpenalizing gaps" since the effect of a single amino-acid deletion is likely to be more extreme than of a single nucleotide deletion. However for a gap to occur three nucleotides have to be inserted/deleated in the genomic sequnce - to me this seems more "unlikely" than a  single nt-mutation changing the aminoacid. To summarize, my question is: how do you reason or think in order to set a "realistic" gap penalty? And how do you balance the conservative effect of maintaining the functionality of the finished product/protein with the unlikeliness of certain random mutations occuring?

* How is an appropriate gap penalty that fits the substitution matrix chosen?

* Why is it that the effect of a single amino-acid deletion is likely to be much less extreme than a single nucleotide deletion?
>  From my understanding between a synonymous mutation and a non-synonymous mutation is that a synonymous mutation is a mistake in one of the letters in codons that are read in order to create a protein, so for example if there's a change of the last letter in the codon it can still code for the same amino acid. While for non-synonymous mutations it can be a deletion/insertion thus creating a frameshift mutation that will mess up the whole protein creation part, especially if the deletion/insertion happens in the early stages of the mRNA chain.
> Evolutionwise we still want both of these mutations because a non-synonymous mutation can still be favorable.

* When deciding on a gap score it says in the book that it has to be on the same scale as the match/mismatch scores. What criteria should one follow when deciding a relevant gap score for a hydrophobicity scoring matrix and a PAM250 matrix respectively.

## Conventions
* Why has BLOSUM62 been chosen as the scoring matrix in many sequence alignment programs? Why not a BLOSUM with a higher or lower number?
> Apparently it's because 62 is the default matrix in BLAST and "Experimentation has shown that the BLOSUM-62 matrix is among the best for detecting most weak protein similarities." so it has just become the standard for many protein alignment programs.


## Score of full Alignments
* The Eddy article states that the alignment score is the sum of individual log-odds scores for each residue pair, assuming each pair is statistically independent of the others. How much can this assumed independence affect the resulting alignment score? Should this be taken into account?
* In the article when they say that a certain program for sequence alignment is optimal for detecting homologous DNA alignments that are x% identical do they mean in terms of speed or in terms of number of alignments found with that percentage of homologous matches, or both?

* I read that PAM matrices have some limitations (for example that they incorrectly assume that all sites are equally mutable and that they are based on biased data). My questions follow:

How will this affect the accuracy of the alignment?
Does this mean that BLOSUM matrices are preferred over PAM matrices?
When will a PAM matrix be chosen over a BLOSUM matrix?

## Notebook
* Would it be possible to through a small example on how to use the scoring matrices?

## General
* Are there alignment methods for tertiary or quatenary protein structures?


## Next lectures
* What are the limitations of using BLAST or PAM to identify real samples with added detector noise and measurement uncertainty?
