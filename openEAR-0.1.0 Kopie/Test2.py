import Test1 as T1

data = T1.Get_Data("/Users/paul/Desktop/SmileArchiv/2023-01-10 13:11:33.xlsx")
archive_dt_string = data.get("Archive_dt_string", "Key not found")

print (archive_dt_string)



