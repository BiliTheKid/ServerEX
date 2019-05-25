import MySQLdb


def catifi_connect():
 mydb = MySQLdb.connect(
  host="localhost",
  user="cat",
  passwd="catwifi808" ,
  database = "catifi"
 )
 #show DB tables
 #mycursor = mydb.cursor()
 # mycursor.execute("SHOW TABLES")
 # for x in mycursor:
 #     print(x)
 #
 return mydb

def run_campaign(mydb):
  mycursor = mydb.cursor()
  sql = "SELECT * FROM campaign WHERE location_id = 1"

  mycursor.execute(sql)
  myresult = mycursor.fetchall()

  #x=row
  for x in myresult:
    #print(x)
    # print("campaignID = ", x[0])
    # print("campaignName = ",x[1])
    # print("id  = ", x[2])
    # print("adID  = ", x[3])
    # print("gender  = ", x[4])
    # print("ageMin = ", x[5])
    # print("ageMax = ", x[6])
    # print("budget  = ", x[7])
    # print("category  = ", x[8])
    # print("startingDate = ", x[9])
    # print("endDate = ", x[10])
    # print("location_id  = ", x[11],"\n")
    return x[11] , x[8]


def all_users_in_specific_router_location(location_id,mydb):
  mycursor = mydb.cursor()
  sql = "SELECT * FROM locations WHERE location_id = {}".format(location_id)
  mycursor.execute(sql)
  myresult = mycursor.fetchall()
  index_for_rows_of_users = 0
  index_for_row_of_users = 0
  list_of_rows_from_db =[]
  for rows in myresult:
    for row in rows:
     print(row)




    #print(rows)
    #list_of_rows_from_db.append(rows)

  print(list_of_rows_from_db)


if __name__== "__main__":
  db_catwifi = catifi_connect()
  location_id_returned_value , category_id_returned_value = run_campaign(db_catwifi)
  print("location_id: ,",location_id_returned_value,"category: ",category_id_returned_value)
  all_users_in_specific_router_location(location_id_returned_value,db_catwifi)