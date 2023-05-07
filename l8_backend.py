import re
import variables as var



class IPv4Address:
    def __init__(self, ipv4:str):
        self.ip_addr = ipv4.split(".")
    def __str__(self):
        return "{}.{}.{}.{}".format(self.ip_addr[0], self.ip_addr[1], self.ip_addr[2], self.ip_addr[3])
    

class SSHTime:
    #Jan  7 16:55:14
    _months = ["Jan", "Feb", "Mar","Apr","May","Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"]
    def __init__(self, _value:str) -> None:
        self.month = re.search(r'^\w{3}', _value).group(0)
        self.day = re.search(r'(?<=^\w{3} {1})\w*|(?<=^\w{3} {2})\w*', _value).group(0)
        self.hour = re.search(r'(?<=^\w{3} {1}\w{2} )\w{2}|(?<=^\w{3} {2}\w )\w{2}', _value).group(0)
        self.minute = re.search(r'(?<=^\w{3} {1}\w{2} \w{2}:)\w{2}|(?<=^\w{3} {2}\w \w{2}:)\w{2}', _value).group(0)
        self.second = re.search(r'(?<=^\w{3} {1}\w{2} \w{2}:\w{2}:)\w{2}|(?<=^\w{3} {2}\w \w{2}:\w{2}:)\w{2}', _value).group(0)
    
    def __str__(self) -> str:
        return "{} {} {}:{}:{}".format(self.month, self.day, self.hour, self.minute, self.second)
    
    def __eq__(self, other: object) -> bool:
        return (self.month==other.month and self.day==other.day and self.hour==other.hour and self.minute==other.minute and self.second==other.second)
    
    def __gt__(self, other: object) -> bool:
        try: 
            if(self.month==other.month):
                if(self.day==other.day):
                    if(self.hour==other.hour):
                        if(self.minute==other.minute):
                            return self.second>other.second
                        else: return self.minute>other.minute
                    else: return self.hour>other.hour
                else: return self.day>other.day
            else: return self._months.index(self.month)>self._months.index(other.month)

        except: 
            return False

    def __lt__(self, other:object) -> bool:
        try: 
            if(self.month==other.month):
                if(self.day==other.day):
                    if(self.hour==other.hour):
                        if(self.minute==other.minute):
                            return self.second<other.second
                        else: return self.minute<other.minute
                    else: return self.hour<other.hour
                else: return self.day<other.day
            else: return self._months.index(self.month)<self._months.index(other.month)

        except: 
            return False
        
    def __ge__(self, other:object) -> bool:
        return (self>other or self==other)
    
    def __le__(self, other:object) -> bool:
        return (self<other or self==other)
    

class SSHLogEntry():
    
    def __init__(self, raw:str):
        self.time=SSHTime(re.search(r'^[A-Z][a-z]{2} {1,2}[0-9]{1,2} \w{2}:\w{2}:\w{2}', raw).group(0))
        self.host_name=re.search(r'(?<=:[0-9]{2} )\w*', raw).group(0)
        self._raw=raw
        self.pid=int(re.search(r'(?<=sshd\[)[0-9]*', raw).group(0))
        tmp_usr = re.search(r'(?<=user )\w+', raw)
        if tmp_usr:
            self.user = tmp_usr.group(0)
        else:
            self.user = ""
        tmp_port = re.search(r'(?<=port )\w*', raw)
        if tmp_port:
            self.port = int(tmp_port.group(0))
    
    
    def __str__(self):
        result = "{}\t\t{}\t\t{}\t\t{}".format(self.time,self.host_name,str(self.pid),self._raw)
        return result
    
   
    def get_ipv4(self):
        ipv4_pattern = r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'
        data = re.search(ipv4_pattern, self._raw)
        if(data): return IPv4Address(data[0])
        else: return None
        
    def has_ip(self):
        if(self.get_ipv4()):
            return True
        else:
            return False
    
    def __repr__(self) -> str:
        return "<{}; time={}, raw={}, pid={}, host_name={}>".format("SSHLogEntry", self.time, self._raw, self.pid, self.host_name)

    def __eq__(self, other: object) -> bool:
        try: 
            return (self.time==other.time)
        except: 
            return False

    def __gt__(self, other: object) -> bool:
        try: 
            return (self.time>other.time)
        except: 
            return False

    def __lt__(self, other:object) -> bool:
        try: 
            return (self.time<other.time)
        except: 
            return False
        

def initializer(path:str):
    var.ssh_list = [SSHLogEntry(l) for l in get_log_file(path)]



def get_log_file(path:str):
    try: 
        print(f"try {path}")
        #pobieranie nazwy pliku i danych
        file_path = path
        file = open(file_path, "r")
        print(f"success {path}")
        return [tmp.strip() for tmp in file.readlines()]
    except:
        print(f"failed {path}")
        raise Exception
    
#tuple = (sshtime, pid, user, ip, port, description)
def get_data(time_start, time_end) -> list:
    try:
        if time_start!= "": 
            start = SSHTime(time_start)
        else:
            start=None
        if time_end!= "": 
            end = SSHTime(time_end)
        else:
            end=None
    except:
        raise Exception
    result = []
    if not start:
        for log in var.ssh_list:
            if(log.time<=end):
                result.append(log)
        return result
    elif not end:
        for log in var.ssh_list:
            if(log.time>=start):
                result.append(log)
        return result
    
    elif not start and not end:
        return var.ssh_list
    
    else: 
        for log in var.ssh_list:
            if(log.time>=start and log.time<=end):
                result.append(log)
        return result