class CompoundInterest:
    def do_compound_interest(principal, percent, years):
        return round(principal * ((1 + percent/12) ** (12*years)), 2)

    def compound_interest_with_monthly_contribution(principal, percent, years, monthly):
        p = principal * ((1 + percent/12) ** (12*years))
        # p = CompoundInterest.do_compound_interest(principal, percent, years)
        pmt = monthly * (((1 + percent/12) ** (12*years) - 1) / (percent/12)) * (1 + percent/12)
        return round((p + pmt), 2)