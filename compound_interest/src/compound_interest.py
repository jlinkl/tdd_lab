class CompoundInterest:
    def do_compound_interest(prinicipal, percent, years):
        return round(prinicipal * ((1 + percent/12) ** (12*years)), 2)

    def compound_interest_with_monthly_contribution(principal, percent, years, monthly):
        return round(principal * ((1 + percent/12) ** (12*years)), 2)