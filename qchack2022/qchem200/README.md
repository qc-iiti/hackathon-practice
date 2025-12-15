QChem200 Solution (Team 4)
## Team Members
- Arya Patil (Team Lead)
- Anushri Maheshwari
- Juzer Lakadwala

---
  
  
  
  Hello and welcome to the great unnecesarily long explanation by Team 4 ( yay i get to use the team name instead of just ruining my own reputation :P )

  The first step of the code was to check if two words were superimposable, meaning that could they be imposed into a single word. This was done by checking the two words and seeing if any two "non-I" gates were present at the same index. If this was true, the gates would be non-superimposable, and in every other case they would be superimposable.
Once it was made sure that the two gates were superimposable, the output would be returned as true, sending the two words for compression

  The following is the explanation for compressing the two words into a single word:
So, the idea was to basically have the letter I act as a multiplier of 1, meaning that when comparing two different gate letters, if one of them is an I, the other letter is saved by default into the final set.
Similarly, if both the gate letters were the same, either of them were saved into the final set.

  In this way, the process would be repeated until the words were reduced to the minimum number possible, giving the most optimized set of words. After this, the compression ratio was calculated, and the final set of words was returned.
Thats ✨all✨ idk what else to put here :P

k byeee :D
