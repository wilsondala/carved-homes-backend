import json
import os
import shutil

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.room import Room
from app.schemas.room import RoomCreate, RoomResponse

router = APIRouter()

UPLOAD_BASE = "app/static/uploads/rooms"


@router.post("/", response_model=RoomResponse)
def create_room(room_data: RoomCreate, db: Session = Depends(get_db)):
    room = Room(**room_data.model_dump())

    db.add(room)
    db.commit()
    db.refresh(room)

    room_folder = f"{UPLOAD_BASE}/room_{room.id}"

    images_folder = f"{room_folder}/images"
    videos_folder = f"{room_folder}/videos"

    os.makedirs(images_folder, exist_ok=True)
    os.makedirs(videos_folder, exist_ok=True)

    room.upload_folder = room_folder

    db.commit()
    db.refresh(room)

    return room


@router.post("/{room_id}/upload-image")
def upload_room_image(
    room_id: int,
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    room = db.query(Room).filter(Room.id == room_id).first()

    if not room:
        raise HTTPException(status_code=404, detail="Quarto não encontrado")

    room_folder = f"{UPLOAD_BASE}/room_{room.id}/images"

    os.makedirs(room_folder, exist_ok=True)

    file_path = f"{room_folder}/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    image_url = f"/uploads/rooms/room_{room.id}/images/{file.filename}"

    gallery = []

    if room.gallery_images:
        gallery = json.loads(room.gallery_images)

    gallery.append(image_url)

    room.gallery_images = json.dumps(gallery)

    if not room.image_url:
        room.image_url = image_url

    db.commit()

    return {
        "message": "Imagem enviada com sucesso",
        "image_url": image_url
    }


@router.post("/{room_id}/upload-video")
def upload_room_video(
    room_id: int,
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    room = db.query(Room).filter(Room.id == room_id).first()

    if not room:
        raise HTTPException(status_code=404, detail="Quarto não encontrado")

    room_folder = f"{UPLOAD_BASE}/room_{room.id}/videos"

    os.makedirs(room_folder, exist_ok=True)

    file_path = f"{room_folder}/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    video_url = f"/uploads/rooms/room_{room.id}/videos/{file.filename}"

    gallery = []

    if room.gallery_videos:
        gallery = json.loads(room.gallery_videos)

    gallery.append(video_url)

    room.gallery_videos = json.dumps(gallery)

    if not room.video_url:
        room.video_url = video_url

    db.commit()

    return {
        "message": "Vídeo enviado com sucesso",
        "video_url": video_url
    }


@router.get("/", response_model=list[RoomResponse])
def list_rooms(db: Session = Depends(get_db)):
    return db.query(Room).all()


@router.get("/{room_id}", response_model=RoomResponse)
def get_room(room_id: int, db: Session = Depends(get_db)):
    room = db.query(Room).filter(Room.id == room_id).first()

    if not room:
        raise HTTPException(status_code=404, detail="Quarto não encontrado")

    return room


@router.put("/{room_id}", response_model=RoomResponse)
def update_room(
    room_id: int,
    room_data: RoomCreate,
    db: Session = Depends(get_db)
):
    room = db.query(Room).filter(Room.id == room_id).first()

    if not room:
        raise HTTPException(status_code=404, detail="Quarto não encontrado")

    for key, value in room_data.model_dump().items():
        setattr(room, key, value)

    db.commit()
    db.refresh(room)

    return room


@router.delete("/{room_id}")
def delete_room(room_id: int, db: Session = Depends(get_db)):
    room = db.query(Room).filter(Room.id == room_id).first()

    if not room:
        raise HTTPException(status_code=404, detail="Quarto não encontrado")

    db.delete(room)
    db.commit()

    return {
        "message": "Quarto removido com sucesso"
    }