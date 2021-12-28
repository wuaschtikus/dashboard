import pandas as pd

def read_excel(file):
    df = pd.read_excel('export.xlsx', usecols = ['Nachname','Stunden', 'Projekt Bezeichnung', 'Requestbezeichnung', 'Aufgabenbezeichnung', 'Monat', 'Tätigkeitsbeschreibung'])
    df.loc[df['Monat'] == 'Januar', 'Monat'] = '01-Jan'
    df.loc[df['Monat'] == 'Februar', 'Monat'] = '02-Feb'
    df.loc[df['Monat'] == 'März', 'Monat'] = '03-Mar'
    df.loc[df['Monat'] == 'April', 'Monat'] = '04-Apr'
    df.loc[df['Monat'] == 'Mai', 'Monat'] = '05-May'
    df.loc[df['Monat'] == 'Juni', 'Monat'] = '06-Jun'
    df.loc[df['Monat'] == 'Juli', 'Monat'] = '07-Jul'
    df.loc[df['Monat'] == 'August', 'Monat'] = '08-Aug'
    df.loc[df['Monat'] == 'September', 'Monat'] = '09-Sep'
    df.loc[df['Monat'] == 'Oktober', 'Monat'] = '10-Oct'
    df.loc[df['Monat'] == 'November', 'Monat'] = '11-Nov'
    df.loc[df['Monat'] == 'Dezember', 'Monat'] = '12-Dec'
    return df

def employees_count(df):
    #df = df.groupby(['Nachname', 'Monat'])['Stunden'].agg(sum)
    #return df['Augustin']
    return len(df['Nachname'].unique())

def hours_count(df):
    return df['Stunden'][0]

def bookings_count(df):
    return len(df)

def project_values(df):
    newdf = df.dropna()[df.dropna()['Tätigkeitsbeschreibung'].str.startswith('STV')].groupby(['Monat'])['Stunden'].agg(sum)
    return newdf.values

def project_labels(df):
    newdf = df.dropna()[df.dropna()['Tätigkeitsbeschreibung'].str.startswith('STV')].groupby(['Monat'])['Stunden'].agg(sum)
    return newdf.index

def admin_values(df):
    newdf = df.dropna()[df.dropna()['Tätigkeitsbeschreibung'].str.startswith('AD')].groupby(['Monat'])['Stunden'].agg(sum)
    return newdf.values

def admin_labels(df):
    newdf = df.dropna()[df.dropna()['Tätigkeitsbeschreibung'].str.startswith('AD')].groupby(['Monat'])['Stunden'].agg(sum)
    return newdf.index

def operations_values(df):
    newdf = df.dropna()[df.dropna()['Tätigkeitsbeschreibung'].str.startswith('MOP')].groupby(['Monat'])['Stunden'].agg(sum)
    return newdf.values

def operations_labels(df):
    newdf = df.dropna()[df.dropna()['Tätigkeitsbeschreibung'].str.startswith('MOP')].groupby(['Monat'])['Stunden'].agg(sum)
    return newdf.index

def employees(df):
    newdf = df['Nachname'].unique()
    return newdf