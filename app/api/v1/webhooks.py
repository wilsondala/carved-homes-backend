from fastapi import APIRouter

router = APIRouter()


@router.post("/payment")
def payment_webhook():
    return {
        "status": "received",
        "message": "Webhook recebido com sucesso"
    }