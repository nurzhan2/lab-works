import re

text1 = " a b ab df abb dbbb abbb "
text2 = " ab abb Abbb abbb cbb baaa "
text3 = " a_b c_d aa_F dc ab "  
text4 = " Abcde abcde a_b_c_d A"
text5 = " abdceb afjsijib bsjsdsoa a_d a______f "
text6 = " desawdw. swdadwd, efefea. a. "

text8 = "Abcde BCde ABCD "
text9 = "Abcde BCde ABCD "

print(re.findall(r'ab*', text1 )) 
print(re.findall(r'ab{2,3}', text2 )) 
print(re.findall(r'\b[a-z]+_[a-z]+\b', text3)) 
print(re.findall(r'[A-Z][a-z]+', text4))  
print(re.findall(r'\ba.*b\b', text5)) 
print(re.sub(r'[ ,.]', ':', text6)) 

print(re.split(r'(?=[A-Z])', text8))
print(re.sub(r'(?<!^)(?=[A-Z])', ' ', text9))  
