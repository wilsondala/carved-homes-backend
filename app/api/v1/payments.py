from fastapi import APIRouter

router = APIRouter()


@router.post("/create")
def create_payment():
    return {
        "status": "pending",
        "message": "Pagamento criado com sucesso",
        "provider": "manual_gateway",
    }