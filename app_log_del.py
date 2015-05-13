#!/usr/bin/env python
import os,time,datetime
from stat import *

def log_del(dir,number):
    for root,dirs,files in os.walk(dir):
       	for filepath in files:
            files=[]
            files.append(os.path.join(root,filepath))
            for file in files:
                if file[-4:] == '.log':
                    t1=time.gmtime(os.stat(file)[ST_MTIME])
                    t11=time.strftime('%Y-%m-%d',t1)
                    year,month,day=t11.split('-')
                    t111=datetime.datetime(int(year),int(month),int(day))
                            
                    t2=time.gmtime()
                    t22=time.strftime('%Y-%m-%d',t2)
                    year,month,day=t22.split('-')
                    t222=datetime.datetime(int(year),int(month),int(day))
                    days=(t222-t111).days
                          
                    if days > number:
                        try:
                            #print file,os.path.getsize(file)
                            #os.remove(file)
                            opt_record=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+" remove "+file+" success\n"
                        except:
                            opt_record=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')+" remove "+file+" fail\n"
                        with open('/tmp/del_result.log','a') as applog_del_result:
                            applog_del_result.write(opt_record)
    
if __name__ == "__main__":
    deploy_path='/opt/deploy/'
    java_app_30=['gemini','gemini-lottery','gemini-push','hera','leheq','leo','libra','oa','panalysis','parchive','pfinance','phoenix','pluto','prandom','prizedata','pstation','pstatistic','pstatistic-new','pstatistic-new-consumer','ptrend','search-transfer','taurus','ucenter','virgo','zeus-api']
    php_app_60=['draw-service','plot','plot-api','plot-d','plot-drawer','plot-passport','plot-powerapi','plot-queue','plot-roapi','plot-rwapi','plot-search-api','plot-wap']
    padmin_90=['padmin']
    #engine_app=['lehecai-engine-caitong','lehecai-engine-joyvebbj','lehecai-engine-monitor','lehecai-engine-phase','lehecai-engine-phase-general','lehecai-engine-scanner','lehecai-engine-sender','lehecai-engine-sender-highfreq','lehecai-engine-tickets','lehecai-engine-tickets-splitter-general','lehecai-engine-trigger','lehecai-engine-vender-ticket']
    #wireless_app=['android-push-mgr','mobile-push','proxyapi','proxyapi-admin','wap5-touch','touch-admin']
    for app in os.listdir(deploy_path):
        if app in java_app_30:
            log_del(deploy_path+app,30)
        elif app in php_app_60:
            log_del(deploy_path+app,60)
        elif app in padmin_90:
            log_del(deploy_path+app,90)
        else:
            pass
