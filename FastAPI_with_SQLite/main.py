from fastapi import Depends, FastAPI, status, Response
import Schema
import Model
from db_handler import SessionLocal, engine
from sqlalchemy.orm import Session
from Location import getlocation
from geopy.distance import geodesic

app = FastAPI(
    title="Address Manager",
    description="perform crud operations on a given address"
)

Model.Base.metadata.create_all(engine)


def getDb():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "Welcome to the address manager FastAPI service"}

# creating address frombody


@app.post("/createNewAddress", status_code=status.HTTP_201_CREATED)
def create_new_address(req: Schema.Address, res: Response, db: Session = Depends(getDb)):
    try:
        # removing leading and ending extra space
        address = req.address.strip()
        city = req.city.strip()
        state = req.state.strip()
        pincode = req.pincode

        # getting the location & coordinate data from mapquest api
        locationData = getlocation(address, city, state)

        # creaing row for address
        newAddress = Model.Address(
            address=address,
            city=city,
            state=state,
            country=locationData,
            pincode=pincode,
            latitude=locationData,
            longitude=locationData,
            maplink=locationData
        )

        # adding row to tabel
        db.add(newAddress)
        db.commit()
        db.refresh(newAddress)

        return {
            "status": "sucessfullycomplete",
            "data": newAddress
        }

    except Exception as e:
        res.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {
            "status": "failed to create",
            "msg": str(e)
        }


# get all the address

@app.get("/getAddresses", status_code=status.HTTP_200_OK)
def get_addresses(res: Response, db: Session = Depends(getDb)):
    try:
        # get all the address data from  database and send to user
        allAddress = db.query(Model.Address).all()
        return{
            "status": "completed",
            "data": allAddress
        }

    except Exception as e:
        res.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {
            "status": "failed to load",
            "msg": str(e)
        }


# update the address through id and request body

@app.put("/updateAddressByID/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_address_by_id(id, req: Schema.Address, res: Response, db: Session = Depends(getDb)):
    try:
        # removing leading and ending extra space
        address = req.address.strip()
        city = req.city.strip()
        state = req.state.strip()
        pincode = req.pincode

        # getting the location & coordinate data from mapquest api
        locationData = getlocation(address, city, state)

        newAddress = {
            "address": address,
            "city": city,
            "state": state,
            "country": locationData,
            "pincode": pincode,
            "longitude":  locationData,
            "latitude":  locationData,
            "maplink": locationData
        }

        # updating address through id and query params
        updatedAddress = db.query(Model.Address).filter(
            Model.Address.id == id).update(newAddress)

        # if data not found in database
        if not updatedAddress:
            res.status_code = status.HTTP_404_NOT_FOUND
            return {
                "status": "failed",
                "msg": f"Address id {id} not found"
            }

        db.commit()

        # if data got sucessfully updated
        return {
            "status": "ok",
            "data": updatedAddress
        }

    except Exception as e:
        res.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {
            "status": "failed",
            "msg": str(e)
        }


# delete the address through id

@app.delete("/deleteAddressBYID/{id}", status_code=status.HTTP_202_ACCEPTED)
def delete_address_by_id(id, res: Response, db: Session = Depends(getDb)):
    try:
        # deleting address from databse through id
        deletedAddress = db.query(Model.Address).filter(
            Model.Address.id == id).delete(synchronize_session=False)

        # if data not found in database
        if not deletedAddress:
            res.status_code = status.HTTP_404_NOT_FOUND
            return {
                "status": "failed",
                "msg": f"Address id {id} not found"
            }

        db.commit()

        # if data got sucessfully deleted
        return {
            "status": "ok",
            "data": deletedAddress
        }

    except Exception as e:
        res.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {
            "status": "failed",
            "msg": str(e)
        }
