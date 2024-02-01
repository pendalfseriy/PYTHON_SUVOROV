
# Сделать копию функции generate_access_config из задания 7
# Дополнить скрипт: ввести дополнительный параметр, который контролирует будет ли
# настроен port-security
# * имя параметра 'psecurity'
# * значение по умолчанию None
# * для настройки port-security, как значение надо передать список команд
# port-security (находятся в списке port_security_template)
# Функция должна возвращать список всех портов в режиме access с конфигурацией
# на основе шаблона access_mode_template и шаблона port_security_template,если он был передан.
# В конце строк в списке не должно быть символа перевода строки.
# Проверить работу функции на примере словаря access_config, с генерацией конфигурации
# port-security и без.
# Пример вызова функции:
# print(generate_access_config(access_config, access_mode_template))
# print(generate_access_config(access_config, access_mode_template, port_security_template))
# Ограничение: Все задания надо выполнять используя только пройденные темы.

access_mode_template = ["switchport mode access","switchport access vlan","switchport nonegotiate","spanning-tree portfast","spanning-tree bpduguard enable"]
port_security_template = ["switchport port-security maximum 2","switchport port-security violation restrict","switchport port-security"]
access_config = {"FastEthernet0/12": 10, "FastEthernet0/14": 11, "FastEthernet0/16": 17}

def generate_access_config(access_config, access_template,psecurity=None):
    
    Key_=list(access_config.keys())
    Ite_=list(access_config.values())
    # print(Key_[0])
    # print(Ite_[0])
    s=[]
    i=0
    while i<len(Key_):
        q=f"interface {(Key_[i])}"
        print(q)
        # s.append(q)
        ii=0
        while ii<len(access_template):
            qq=access_template[ii]
            if access_template[ii]=="switchport access vlan":
                qq=f"{access_template[ii]} {Ite_[i]}"
            print(qq)
            # s.append(qq)
            ii+=1
        if psecurity!=None:
            iii=0
            while iii<len(psecurity):
                qqq=psecurity[iii]
                print(qqq)
                # s.append(qqq)
                iii+=1
        i+=1    
    return " "

print(generate_access_config(access_config,access_mode_template))
print(generate_access_config(access_config,access_mode_template,port_security_template))