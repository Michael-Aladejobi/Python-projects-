'''Convert your phone number to words by Michael Aladejobi'''

phone = input('Phone: ')
digits_mapping = {
'+':'plus',
'1':'One',
'2':'Two',
'3':'Three',
'4':'Four',
'5':'Five',
'6':'Six',
'7':'Seven',
'8':'Eight',
'9':'Nine',
'0':'Zero'
}

for digits in phone:
    print(digits_mapping.get(digits), end = ' ')
