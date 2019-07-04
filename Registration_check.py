import re



def check_registration_rules(**args):
    temp=[]
    for k,v in zip(args.keys(),args.values()):
       # print(re.findall(r"[^0-9]",v))
        if len(list(k))<4 or len(list(v))<6:
            continue
        elif k=='quera' or k=='codecup':
            continue
        elif len(re.findall(r"[^0-9]",v))==0:
            continue
        else:
            temp.append(k)
            pass
        pass
        
    return temp

print(check_registration_rules(m_ed___='         ', ab_bas='afj$L12',_hamid="ho  sein"))