import pyperclip

import re

def title_except(s, exceptions):
    s2 = s.lower()
    word_list = re.split(' ', s2)
    final = [word_list[0].capitalize()]
    for word in word_list[1:]:
        final.append(word if word in exceptions else word.capitalize())
    return " ".join(final)

articles = ['a', 'an', 'of', 'the', 'is', 'or', 'and', 'with', 'to', 'as', 'in']

def acronym_check(s, exceptions):
    word_list = re.split(' ', s)
    final = []
    for word in word_list:
        if word not in exceptions:
            final.append(word)
        else:
            final.append(word.upper())
    return " ".join(final)

acronyms = ['Ach',
 'Dda',
 'Gl',
 'Trsf',
 'Rcip',
 'Atm',
 'G//l',
 'Iolta',
 'Ibreta',
 'Eft',
 'Loc',
 'Heloc',
 'Apy',
 'Cd',
 'Cesa',
 'Cip',
 'Ctr',
 'Ein',
 'Emv',
 'Faq',
 'Fha',
 'Fico',
 'Fmla',
 'Gap',
 'He',
 'Hr',
 'Hsa',
 'Iban',
 'Iqq',
 'Ira',
 'Isa',
 'It',
 'Itm',
 'Llc',
 'Lms',
 'Loc',
 'Los',
 'Ltv',
 'Mla',
 'Nada',
 'Ncua',
 'Nsf',
 'Ofac',
 'Pin',
 'Poa',
 'Pto',
 'Rcip',
 'Seg',
 'Sepa',
 'Slo',
 'Ssn',
 'Tin',
 'Va',
 'W-8ben',
 'Ytd']


def run_case_format():
    foo = pyperclip.paste()
    title_case = title_except(foo, articles)
    except_acronyms = acronym_check(title_case, acronyms)
    pyperclip.copy(except_acronyms)


if __name__ == '__main__':
	run_case_format()
