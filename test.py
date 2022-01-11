from typing import Optional
from fastapi import FastAPI

BD_HOST = "e-valuation.cluster-ro-cgqfl0ed0rgz.ap-south-1.rds.amazonaws.com"
DB_NAME = "propsamc"
DB_USER = "propsamc"
DB_PASS = "oKr7FxrZdGktC0Mve9g6"

# pip install psycopg2
import psycopg2
import psycopg2.extras


app = FastAPI()

conn = psycopg2.connect(dbname=DB_NAME,user=DB_USER,password=DB_PASS,host = BD_HOST)
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/transaction_mh/{building_id}")

def transaction_mh(building_id: str):
    print(type(id))
    cur.execute("select * from transactions_mh where building_id = '{}' ".format(building_id))

    t=cur.fetchall()
    
    t1=t[0]


    y={"record_id":t1[0],"geocode_point":t1[1],"building_id":t1[2],"source":t1[3],
    "record_status":t1[4],"asset_type":t1[5],"transaction_type":t1[6],"transaction_category":t1[7],"year":t1[8],
    "village":t1[9],"district":t1[10],"document_number":t1[11],"cts_plot":t1[12],
    "unit_number":t1[13],"block":t1[14],"tower_number":t1[15],
    "wing_number":t1[16],"property_name":t1[17],"address":t1[18],"location":t1[19],
    "locality":t1[20],"city":t1[21],"pincode":t1[22],"document_type":t1[23],
    "document_date":t1[24],"registration_date":t1[25],"registration_index_date":t1[26],
    "sro_code":t1[27],"sro_name":t1[28],"sro_status":t1[29],"configuration":t1[30],
    "floor_number":t1[31],"serial_volume":t1[32],"remarks":t1[33],"area":t1[34],
    "rate_per_sqft":t1[35],"sale_rent_value":t1[36],"registration_value":t1[37],
    "govt_deposit_value":t1[38],"stamp_duty":t1[39],"filling_value":t1[40],
    "date_of_submission":t1[41],"seller_details":t1[42]}
                                                                         
    return y
    





