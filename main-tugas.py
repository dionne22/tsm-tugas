#Regina Dionne Aurelia H. -18219030

import json
from typing import Optional
from fastapi import FastAPI,HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

with open("tugas.json", "r") as read_file:
    data = json.load(read_file)
app = FastAPI()


@app.get("/")  
async def root(): 
    return {"Task Management System -": "Tugas"}

#Read All Tugas
@app.get('/tugas')
async def get_all_tugas():
    return data['tugas']

#Read Tugas
@app.get('/tugas/{id_tugas}')
async def get_tugas(id_tugas: int):
    for tugas_item in data['tugas']:
        if tugas_item['id_tugas'] == id_tugas:
            return tugas_item
    raise HTTPException(
        status_code=404, detail=f'Tugas not found'
)

#Add Tugas 
@app.post('/tugas')
async def add_tugas(nama_tugas:str, departemen:str, koordinator:str, tanggal_pemberian: str, tenggat_waktu: str, description: str): 
    id=1
    if(len(data['tugas'])>0):
        id=data['tugas'][len(data['tugas'])-1]['id_tugas']+1
        new_data={'id_tugas':id,'nama_tugas':nama_tugas, 'departemen':departemen, 'koordinator':koordinator,'tanggal_pemberian':tanggal_pemberian,'tenggat_waktu':tenggat_waktu,'description':description}
    data['tugas'].append(dict(new_data))
    read_file.close()
    with open("tugas.json", "w") as write_file:
        json.dump(data,write_file,indent=4)
    write_file.close()
    
    return (new_data)
    raise HTTPException(
        status_code=500, detail=f'Internal Server Error' 
)

#Edit Tugas
@app.put('/tugas/{id_tugas}')
def edit_tugas(id_tugas : int, hasil_tugas:str, status: str): 
    for tugas_item in data['tugas']:
        if tugas_item['id_tugas'] == id_tugas:
            tugas_item['hasil_tugas']=hasil_tugas
            tugas_item['status']=status
            read_file.close()
            with open("tugas.json", "w") as write_file:
                json.dump(data,write_file,indent=4)
            write_file.close()
            return{"message":"Update Tugas Success"}
    raise HTTPException(
        status_code=404, detail=f'Tugas not found')


#Delete Tugas
@app.delete('/tugas/{id_tugas}')
async def delete_tugas(id_tugas: int):
    for tugas_item in data['tugas']:
        if tugas_item['id_tugas'] == id_tugas:
            data['tugas'].remove(tugas_item)
            read_file.close()
            with open("tugas.json", "w") as write_file:
                json.dump(data,write_file,indent=4)
            write_file.close()
            return{"message":"Delete Tugas Success"}
    raise HTTPException(
        status_code=404, detail=f'Item not found'
)






