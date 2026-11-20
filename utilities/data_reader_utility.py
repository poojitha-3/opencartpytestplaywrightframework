import json,csv,openpyxl

def data_json(self):
        data=[]
        try:
           file=open("testdata/logindata.json",'r')
           login_data=json.load(file)
           for i in login_data:
               data.append(tuple(i.values()))
        except Exception as e:
            print(f"while collecting the data: {e}")
        return data

def data_csv(self):
        data=[]
        try:
            file=open("testdata/logindata.csv",newline='',encoding='utf-8')
            reader=csv.DictReader(file)
            for row in reader:
                data.append(tuple(row.values()))
        except Exception as e:
            print(f"while collecting the data: {e}")
        return data

def data_excel(self,filepath,sheet_name):
        data=[]
        try:
            file=openpyxl.load_workbook(filepath)
            sheet=file[sheet_name] if sheet_name else file.active
            for row in sheet.iter_rows(min_row=2,values_only=True):
                data.append(row)
        except Exception as e:
            print(f"while collecting the data: {e}")
        return data

