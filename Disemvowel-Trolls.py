def disem_vowel (input_string):
    return ''.join ((filter (lambda x: x.lower () not in [ 'a' , 'e' , 'i' , 'o' , 'u' ] , input_string)))
