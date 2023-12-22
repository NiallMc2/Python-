income = 100000
single_person_tax_allowance = 36800
taxable_at_20_percent = income - single_person_tax_allowance
taxable_at_40_percent = income - taxable_at_20_percent
percent_tax_20 = taxable_at_20_percent * .2
percent_tax_40 = taxable_at_40_percent * .4
total_tax = percent_tax_20 + percent_tax_40
print(total_tax)