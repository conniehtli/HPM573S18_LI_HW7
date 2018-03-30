from scipy.stats import binom

print('--------------------Problem 2-----------------------')
print('The number of participants that survived beyond 5 years in a cohort of N particpants follows a binominal '
      'distribution with the parameters '
      'N (number of individuals in the cohort) and q (probabilty of 5-year survival caluclated in problem 1). ')

print('--------------------Problem 3-----------------------')

print('The likelihood that 400 of 573 participants have survived at the end of a 5 year study period, given 50% surivival probability:')
print(binom.pmf(k=400, n=573, p=0.5))