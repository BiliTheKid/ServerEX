import logging


def log(x):
 logging.basicConfig(filename='app.log', filemode='w', format=x+'%(name)s - %(levelname)s - %(message)s')
 logging.warning('This will get logged to a file')



if __name__ == "__main__":
    log("yaron")

#create class for Client known as client someone who stay in wifi range
#id=mac_adress , Location = Destantion
class Client:
  def __init__(Client_obj,Id,Location,Categorie,Gender,Age,Email):
      Client_obj.Id=Id
      Client_obj.Gender = Gender
      Client_obj.Age = Age
      Client_obj.Categorie = Categorie
      Client_obj.Email=Email
      Client_obj.Location= Location
  def myfunc(abc):
    print("Data of Client "  + abc.Id + abc.Categorie + abc.Gender + abc.Age + abc.Email +abc.Location)


#create adv, known as Third party, which provide the adv for Client.

#create banner, for ad to Client as notification
class banner:
    def __init__(Banner_obj,Id_adv,Id_url, Categorie ,price):
        Banner_obj.Id_adv= Id_adv
        Banner_obj.Id_url = Id_url
        Banner_obj.Categorie = Categorie
        Banner_obj.price = price
    def myfunc(abc):
        print("Banner-Info " + abc.Id_adv + abc.Id_url +abc.Categorie  + abc.price)

#create host known as publisher/buisness
class buisness:
    def __init__(buisness_obj, Id_buisness, Location , Categorie, price):
        buisness_obj.Id_buisness =  Id_buisness
        buisness_obj.Location = Location
        buisness_obj.Categorie = Categorie
        buisness_obj.price = price
        buisness_obj.Clients = []

    #status of Client in WIFI host
    #Add Client to Host list of Client(real time)
    def addClient(buisness_obj, Client):
        print(buisness_obj.Id_buisness)  # debugging...
        print ("pre: ", buisness_obj.Client)
        buisness_obj.Clients.append(Client)
        print ("post: ", buisness_obj.Clients)

    #delete Client....

    #print  buisness_info
    def myfunc(abc):
        print(" buisness-Info " + abc.Id_buisness + abc.Location + abc.Categorie + abc.price)

#example for using Client
# Client1 = Client("111","","","","")
# Client1.myfunc()