import pandas as pd
import numpy as np


def r_csv(df, path, f, ctdf):
    print(f)
    df1 = df.reset_index(drop = True)
    modes = [b'PFlt_Rgn1', b'PFlt_Rgn2']
    df1['op'] = df1.apply(lambda row: 1 if row.CoEOM_numOpModeAct in modes else 0, axis = 1)
    df1_t = df1[df1['op'] == 1]
    isempty = df1_t.empty
    if not isempty:
        sti = df1_t.index[0]
        if df1['op'].iloc[-5] == 1 or df1['op'].iloc[-1] == 1:
            edi = df1_t.index[-1]
        else:
            edi = df1_t.index[-1] + 10
        df2 = df1.iloc[sti:edi, :]
        df2 = df2.reset_index(drop = True)
        scnt = df2['PFltRgn_ctRgnSuc'][0]
        ecnt = df2['PFltRgn_ctRgnSuc'].iloc[-1]
        mSot = df2['PFltLd_mSot'][0]
        lSnce = int(df2['PFltRgn_lSnceRgn'][0] / 1000)
        mSote = df2['PFltLd_mSot'].iloc[-1]
        
        cdata2 = df2[df2['InjCrv_qPoI1Des_mp'] > 0]
        cdata3 = df2[df2['Exh_tPFltUs'] > 550]
        cdata4 = df2[(df2['CoEOM_numOpModeAct'] == b'PFlt_Rgn1')]
        cdata2 = cdata2.reset_index(drop = True)
        cdata3 = cdata3.reset_index(drop = True)
        cdata4 = cdata4.reset_index(drop = True)
        if cdata2.empty:
            t_p = 0
            poi1_m = 0
        else:
            t_p = round(cdata2.index[-1] / 100)
            poi1_m = round(cdata2['InjCrv_qPoI1Des_mp'].mean(), 2)
        if cdata3.empty:
            t_550 = 0
            t5_a = 0
        else:
            t_550 = round(cdata3.index[-1] / 100)
            t5_a = int(cdata3['Exh_tPFltUs'].mean())
        if cdata4.empty:
            t_t = 0
        else:
            t_t = round(cdata4.index[-1] / 100)
        
        # Calculating Poi1 Integral
        poi1_g_s = ((df['InjCrv_qPoI1Des_mp'] * df['Epm_nEng'] * 120) / 1000000) * (1000 / 3600)
        poi1_g = np.trapz(y = poi1_g_s, x = df['timestamps'])
        poi1_l = round((poi1_g / 832), 2)
        
        ctdf = ctdf.append(
            {'FileName': f, 'Strt Count': scnt, 'End Count': ecnt, 'mSot Strt': mSot, 'lSnce (kms)': lSnce,
             'mSot End': mSote, 'T5_Avg': t5_a, 'ti_OnRoad(s)': t_t, 'ti(t5>550)(s)': t_550, 'ti(poi1>0)(s)': t_p,
             'PoI1_a(mg)': poi1_m, 'PoI1_lts': poi1_l}, ignore_index = True)
        # outname = f + "_" + str(scnt) + "_" + str(ecnt) + "_" + str(mSot) + " gms_" + str(lSnce) + " kms_"+str(mSote)+" gms"
        df2.to_csv(path + "/" + f + ".csv")
    return ctdf
