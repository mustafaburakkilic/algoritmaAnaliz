
# coding: utf-8

# In[61]:

def power(x,y):
    t=1
    for i in range(0,y):
        t=t*x
    return t

def power_recursive(x,y):
    global s
    s=0
    print(x," üzeri ",y," sonucu =",power_recursive2(x,y)," || Bulduğu adım sayısı =",s)
    r=power_recursive2(x,y)
    return r

def power_recursive2(x,y):
    global s
    s=s+1
    if(y==0):
        return 1
    if(y==1):
        return x
    if(y%2==0):
        return power_recursive2(x*x,int(y/2))
    else:
        return power_recursive2(x*x,int(y/2))*x


# In[62]:

power_recursive(2,16)


# In[60]:

def power_2(x,n):
    global sayac
    sayac=sayac+1
    if(n==0):
        return 1
    if(n==1):
        return x
    if(n%2==0):
        return power_2(x*x,int(n/2))
    else:
        return power_2(x*x,int(n/2))*x
    
def call_report_recursive(x,y):
    global sayac
    sayac=0
    r=power_2(x,y)
    print(x," üzeri", y," değeri",r ," çağrım sayısı : ",sayac)
    
call_report_recursive(2,8)
call_report_recursive(2,16)
call_report_recursive(2,32)
call_report_recursive(2,8)


# In[ ]:




# In[ ]:



