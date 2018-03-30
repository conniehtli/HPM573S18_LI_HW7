import SurvivalClasses as Cls


CohortOne = Cls.Cohort(id=1, pop_size=573, mortality_prob=0.1)

Cohort1Outcome = CohortOne.simulate(100)



print('Portion of patients who survived beyond 5 years, given mortality probability is 0.1:', Cohort1Outcome.get_survival_after_five())

print()