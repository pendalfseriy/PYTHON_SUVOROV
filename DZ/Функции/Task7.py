access_mode_template = ["switchport mode access","switchport access vlan","switchport nonegotiate","spanning-tree portfast","spanning-tree bpduguard enable",]
print(access_mode_template)

access_config = {"FastEthernet0/12": 10, "FastEthernet0/14": 11, "FastEthernet0/16": 17}

access_config_2 = {"FastEthernet0/03": 100,"FastEthernet0/07": 101,"FastEthernet0/09": 107,}

def generate_access_config(access_config, access_template):
    
    Key_=list(access_config.keys())
    Ite_=list(access_config.values())
    # print(Key_[0])
    # print(Ite_[0])
    s=[]
    i=0
    while i<len(Key_):
        q=f"interface {(Key_[i])}"
        print(q)
        ii=0
        while ii<len(access_template):
            qq=access_template[ii]
            if access_template[ii]=="switchport access vlan":
                qq=f"{access_template[ii]} {Ite_[i]}"
            print(qq)
            ii+=1
        i+=1    
    return s
print(generate_access_config(access_config,access_mode_template))
print(generate_access_config(access_config_2,access_mode_template))
