import pyperclip

import re

def lower_all(s):
    s2 = s.lower()
    word_list = re.split(' ', s2)
    final = [word_list[0].capitalize()]
    for word in word_list[1:]:
        final.append(word)
    return " ".join(final)

def acronym_check(s, exceptions):
    word_list = re.split(' ', s)
    final = []
    for word in word_list:
        if word not in exceptions:
            final.append(word)
        else:
            final.append(word.upper())
    return " ".join(final)

acronyms = ['ach',
 'dda',
 'gl',
 'trsf',
 'rcip',
 'atm',
 'g//l',
 'iolta',
 'ibreta',
 'eft',
 'loc',
 'heloc',
 'apy',
 'cd',
 'cesa',
 'cip',
 'ctr',
 'ein',
 'emv',
 'faq',
 'fha',
 'fico',
 'fmla',
 'gap',
 'he',
 'hr',
 'hsa',
 'iban',
 'iqq',
 'ira',
 'isa',
 'it',
 'itm',
 'llc',
 'lms',
 'loc',
 'los',
 'ltv',
 'mla',
 'nada',
 'ncua',
 'nsf',
 'ofac',
 'pin',
 'poa',
 'pto',
 'rcip',
 'seg',
 'sepa',
 'slo',
 'ssn',
 'tin',
 'va',
 'w-8ben',
 'ytd']


def run_case_format():
    foo = pyperclip.paste()
    lower_case = lower_all(foo)
    except_acronyms = acronym_check(lower_case, acronyms)
    pyperclip.copy(except_acronyms)


if __name__ == '__main__':
	run_case_format()
