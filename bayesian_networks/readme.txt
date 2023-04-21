Programming language used is Python for both the programs

***********************************************************************************************************
***********************************************************************************************************

Task1:

All the code is written in compute_a_posteriori.py file.

output function will write the output to the file.

Probability of bag at observation t is given by

Pt(hi) = (P(Qt|hi)*Pt-1(hi))/Pt-1(Qt)

updated Probability for candy after observation t isgiven by

Pt(Qt+1) = Summation of (P(Qt+1|hi)(Pt(hi)))

Program can be executed using the following command:

python compute_a_posteriori.py observations

ex: python compute_a_posteriori.py CLLCCLLLCCL

Note: Program will still execute without any observations as well

*******************************************************************************************************************
*******************************************************************************************************************

Task2:

All the code is written in bnet.py file

Once we initialize the Probabilities given, we will take the arguments provided and look for the condition

If no condition is given then we enumerate and find Probabilities

If there is a condition given then we will have a denominator, hence we enumerate for both numerator and denominator
and find Probabilities, final Probability will be numerator divided by denominator.

We will print the final Probability to the terminal

Program can be executed using the following command:

python bnet.py expression

ex: 
1) python bnet.py Bf At Mt
2) python bnet.py Jt given Et Bf

Note: Program will output the Probability only if the arguments are between 1 and 6.