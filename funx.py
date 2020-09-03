#!/usr/bin/env python
# -*- coding: utf-8 -*-

#funx.py
import matplotlib.pyplot as plt
import warnings
import numpy as np
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import ipywidgets as widgets

#def function(option):
#    print(option)

def test(a):
    print(a)

    
def plot_dfs(keyword,dfs,startdate,enddate):
    if keyword[-1]=="1":
        plotdf(dfs[0],startdate,enddate,keyword)
    elif keyword[-1]=="2":
        plotdf(dfs[1],startdate,enddate,keyword)
    else:
        plotdfs_inoneplot(dfs,startdate,enddate)
    plt.savefig('Export/'+keyword+'.png',dpi=300)        
        
        
    
def dropdown_menu(dfs,startdate,enddate):
    plot_dfs('Alle_Logger',dfs,startdate,enddate)
    w = widgets.Dropdown(
        options=['Beide_Logger', 'Logger_01', 'Logger_02', 'Logger_03'],
        description='Darstellung:',
        disabled=False
    )
    w.observe(
        lambda c: plot_dfs(c['new'],dfs,startdate,enddate) if (c['type'] == 'change' and c['name'] == 'value') else None
    )
    display(w)
    #plot_dfs('test',dfs,startdate,enddate)

def getstring(a):
    outstr=str(a)+'_output'
    return outstr

def a():
    import datetime as dt
    fname=dt.datetime.today().strftime('%Y%m%d')
    return str(fname)

def startup():
    warnings.filterwarnings("ignore")
    pd.options.mode.chained_assignment = None  #pandas Warnungen ausblenden
    df = pd.DataFrame(np.random.randn(3, 2), columns=list('AB')) #df-dummy wird in nächster Zellen  
    #print("start erfolgreich")
    return(df)

def plotdf(df, startdate,enddate,title):
     
    plt.rcParams['figure.figsize'] = [15,15] 
    plt.rcParams['figure.dpi'] = 200
    
    colortable=['b','g', 'r', 'c', 'm', 'y', 'k', 'b', 'g', 'r', 'c', 'm', 'y', 'k']
    dfloc=df.loc[startdate:enddate]
    dflen=len(df.columns)
    fig, ax=plt.subplots(dflen)
    #ax.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
    for i, col in enumerate(dfloc.columns):
        plt.subplot(dflen,1,i+1)
        if i==0:
            plt.title(title,loc='left')
        #print(col.find('_p'))
        if col.find('_p')==-1:
            dfloc[col].plot(sharex=plt.gca(),color=colortable[i],label=col,linewidth=1,grid=True)
        else:
            dfloc[col].plot(sharex=plt.gca(),color=colortable[i],marker='|',label=col,grid=True,linestyle=None)
        plt.legend(loc="lower left")
    

        
def plotdfs(dfs, startdate,enddate):
     
    plt.rcParams['figure.figsize'] = [15,15] 
    plt.rcParams['figure.dpi'] = 200
    colortable=['b','g', 'r', 'c', 'm', 'y', 'k', 'b', 'g', 'r', 'c', 'm', 'y', 'k']
    for df in dfs:
        df.head()
        dfloc=df.loc[startdate:enddate]
        dflen=len(df.columns)
        fig, ax=plt.subplots(dflen)
    #ax.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
        for i, col in enumerate(dfloc.columns):
            plt.subplot(dflen,1,i+1)
        #print(col.find('_p'))
            if col.find('_p')==-1:
                dfloc[col].plot(sharex=plt.gca(),color=colortable[i],label=col,linewidth=1,grid=True)
            else:          
                dfloc[col].plot(sharex=plt.gca(),
                    color=colortable[i],marker='|',label=col,grid=True,linestyle=None)
            plt.legend(loc="lower left")

        
        
def plotdfs_inoneplot(dfs, startdate,enddate):
     
    plt.rcParams['figure.figsize'] = [15,15] 
    plt.rcParams['figure.dpi'] = 200
    colortable=['indigo','purple', 'darkslategrey', 'maroon', 'darkolivegreen', 'black','indigo','purple', 'darkslategrey', 'maroon', 'darkolivegreen', 'black' ]
    #for df in dfs:
    #df.head()
    dfloc0=dfs[0].loc[startdate:enddate]
    dfloc1=dfs[1].loc[startdate:enddate]
    dfloc2=dfs[2].loc[startdate:enddate]
    dflen=len(dfloc0.columns)
    fig, ax=plt.subplots(dflen)
    #ax.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
    for i, col in enumerate(dfloc0.columns):
        plt.subplot(dflen,1,i+1)
    #print(col.find('_p'))
        if col.find('_p')==-1:
            dfloc0[col].plot(sharex=plt.gca(),color=colortable[i],label=col,linewidth=1,grid=True)
            dfloc1[col].plot(sharex=plt.gca(),color=colortable[i],label=col,linewidth=1,grid=True,alpha=0.25)
            dfloc2[col].plot(sharex=plt.gca(),color=colortable[i],label=col,linewidth=1,grid=True,alpha=0.4)
        else:          
            dfloc0[col].plot(sharex=plt.gca(),
                color=colortable[i],marker='|',label=col,grid=True,linestyle=None)
            dfloc1[col].plot(sharex=plt.gca(),
                color=colortable[i+1],marker='|',label=col,grid=True,linestyle=None)
            dfloc2[col].plot(sharex=plt.gca(),
                color=colortable[i+2],marker='|',label=col,grid=True,linestyle=None)
        #plt.legend(loc="lower left")
        #
        #plt.legend(('string1','string2'),loc="lower left")
        #print(str(dfloc0.columns[i])+' Logger_01')
        plt.legend((str(dfloc0.columns[i])+' L01',
                      str(dfloc1.columns[i])+' L02',
                       str(dfloc2.columns[i])+' L03'),loc="lower left")

def getdfs_frommulticsv(ndays,fileend='.txt'):
    urls=["https://uni-wuppertal.sciebo.de/s/0WBFg4RTw4I428O/download?path=%2F&files=",
          "https://uni-wuppertal.sciebo.de/s/rEFPb7PQd3yTMNV/download?path=%2F&files=",
          "https://uni-wuppertal.sciebo.de/s/5DnhKrWz5m9w1TL/download?path=%2F&files="]
         
    
    import matplotlib.pyplot as plt
    import warnings
    import numpy as np
    import pandas as pd
    #import datetime as dt
    dfs=[]
    
    for url in urls:
          
        df= pd.DataFrame([])
        i=0
        while i<ndays:
            datestr=(dt.datetime.today()-dt.timedelta(days=i)).strftime('%Y%m%d')
            fname=datestr+fileend
            filelink=url+fname
            try:
                #print(filelink)
                dfi=pd.read_csv(filelink,index_col=None, sep=';',header=None)
                df=df.append(dfi)
                    
            except:
                print(fname+' not found on File Server')
            i+=1
        df[0] = pd.to_datetime(df[0],format="%d.%m.%Y %H:%M:%S")
        del df[8]
        df[3][df[2]<100]=np.NaN #conditional set values to NaN
        df[2][df[2]<100]=np.NaN
        df[1][df[2]<100]=np.NaN
        df[1][df[1]<0]=np.NaN
        df.columns = ['date','r1min','mabs','rsum','T','H','p','U']
        df.set_index('date', inplace=True)
        df=df.loc[df.index.notnull()]
        df=df.sort_index()
        dfs.append(df)
    return(dfs)


def getdf_frommulticsv(ndays,link="https://uni-wuppertal.sciebo.de/s/rEFPb7PQd3yTMNV/download?path=%2F&files=",fileend='.txt'):
    import matplotlib.pyplot as plt
    import warnings
    import numpy as np
    import pandas as pd
    #import datetime as dt
    fname=dt.datetime.today().strftime('%Y%m%d')+fileend
    filelink=link+fname
    
    df=pd.read_csv(filelink,index_col=None, sep=';',header=None)
    #todaystr=datetime.today().strftime('%Y%m%d')
    i=1
    while i<ndays:
        datestr=(dt.datetime.today()-dt.timedelta(days=i)).strftime('%Y%m%d')
        #print(datestr)
        fname=datestr+fileend
        filelink=link+fname
        try:
            dfi=pd.read_csv(filelink,index_col=None, sep=';',header=None)
            df=df.append(dfi)
        except:
            print(fname+' not found on File Server')
        i+=1
    df[0] = pd.to_datetime(df[0],format="%d.%m.%Y %H:%M:%S")
    del df[8]
    df[3][df[2]<100]=np.NaN #conditional set values to NaN
    df[2][df[2]<100]=np.NaN
    df[1][df[2]<100]=np.NaN
    df[1][df[1]<0]=np.NaN
    df.columns = ['date','r1min','mabs','rsum','T','H','p','U']
    df.set_index('date', inplace=True)
    df=df.loc[df.index.notnull()]
    df=df.sort_index()
    return(df)

def exportdf_toexcel_withcharts(df,outfilep):
    #import xlsxwriter
    import pandas as pd
    from datetime import datetime
    writer = pd.ExcelWriter(outfilep, engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Tab1')
    
    workbook = writer.book
    worksheet = writer.sheets['Tab1']
    colortable=['#708090','#B0C4DE','#F4A460','#0000CD','#1E90FF', '#48D1CC','#3CB371', '#006400','#FFFF00','#FF8C00','#800000']
    dfnrows,dfncols=df.shape
    xl0date = datetime(1899, 12, 30)
    mindate=datetime.strptime(str(df.index[0]),'%Y-%m-%d %H:%M:%S')
    maxdate=datetime.strptime(str(df.index[-1]),'%Y-%m-%d %H:%M:%S')
    mindatexl=float((mindate-xl0date).days) + (float((mindate-xl0date).seconds) / 86400)
    maxdatexl=float((maxdate-xl0date).days) + (float((maxdate-xl0date).seconds) / 86400)
    
    for colnr in range(1,dfncols+1): 
        posindex=(chr(98+dfncols)).upper()+str((colnr-1)*7+2)
        colname=df.columns[colnr-1]
        #if colname[-1]=='p':
        chart = workbook.add_chart({'type': 'scatter',
                                   'subtype': 'straight'})
        # Configure the series of the chart from the dataframe data
        chart.add_series({
            'categories': ['Tab1', 1, 0, dfnrows, 0],
            'values':     ['Tab1', 1, colnr, dfnrows, colnr],
            'line': {'color': colortable[colnr-1]},
        })
        # Configure the chart axes.
        chart.set_x_axis({ 'position_axis': 'on_tick','text_axis': True,'min':mindatexl, 'max':maxdatexl, 'num_font':  {'rotation': -45},'major_gridlines': {'visible': True}})
        chart.set_y_axis({'name': colname, 'major_gridlines': {'visible': True}})
        #chart.set_x_axis({'num_font': {'rotation': -45}})
        # Turn off chart legend. It is on by default in Excel.
        chart.set_legend({'position': 'none'})
        # Insert the chart into the worksheet.
        worksheet.insert_chart(posindex, chart,{'x_scale': 1.8, 'y_scale': 0.83})
    
    writer.save()

def exportdfs_toexcel_withcharts(dfs,outfilep):
    #import xlsxwriter
    import pandas as pd
    from datetime import datetime
    #writer = pd.ExcelWriter(outfilep, engine='xlsxwriter')
    i=1
    with pd.ExcelWriter(outfilep) as writer:
        for df in dfs:
            #writer = pd.ExcelWriter(outfilep, engine='xlsxwriter')
            sheetname='Logger_0'+str(i)    
            df.to_excel(writer, sheet_name=sheetname)
            workbook = writer.book
            worksheet = writer.sheets[sheetname]
            colortable=['#708090','#B0C4DE','#F4A460','#0000CD','#1E90FF', '#48D1CC',
                        '#3CB371','#006400','#FFFF00','#FF8C00','#800000']
            dfnrows,dfncols=df.shape
            xl0date = datetime(1899, 12, 30)
            mindate=datetime.strptime(str(df.index[0]),'%Y-%m-%d %H:%M:%S')
            maxdate=datetime.strptime(str(df.index[-1]),'%Y-%m-%d %H:%M:%S')
            mindatexl=float((mindate-xl0date).days) + (float((mindate-xl0date).seconds) / 86400)
            maxdatexl=float((maxdate-xl0date).days) + (float((maxdate-xl0date).seconds) / 86400)
            i+=1
            for colnr in range(1,dfncols+1): 
                posindex=(chr(98+dfncols)).upper()+str((colnr-1)*7+2)
                colname=df.columns[colnr-1]
            #if colname[-1]=='p':
                chart = workbook.add_chart({'type': 'scatter',
                                       'subtype': 'straight'})
            # Configure the series of the chart from the dataframe data
                chart.add_series({
                    'categories': [sheetname, 1, 0, dfnrows, 0],
                    'values':     [sheetname, 1, colnr, dfnrows, colnr],
                    'line': {'color': colortable[colnr-1]},
                })
            # Configure the chart axes.
                chart.set_x_axis({ 'position_axis': 'on_tick','text_axis': True,'min':mindatexl,
                                  'max':maxdatexl, 'num_font':  {'rotation': -45},
                                  'major_gridlines':{'visible': True}})
                chart.set_y_axis({'name': colname, 'major_gridlines': {'visible': True}})
            #chart.set_x_axis({'num_font': {'rotation': -45}})
            # Turn off chart legend. It is on by default in Excel.
                chart.set_legend({'position': 'none'})
            # Insert the chart into the worksheet.
                worksheet.insert_chart(posindex, chart,{'x_scale': 1.8, 'y_scale': 0.83})

        writer.save()
