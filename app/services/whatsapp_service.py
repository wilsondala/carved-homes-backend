from urllib.parse import quote


def build_booking_whatsapp_message(booking):
    message = f"""
New Booking - Carved Homes

Booking ID: #{booking.id}
Guest: {booking.guest_name}
Email: {booking.guest_email}
Phone: {booking.guest_phone or "Not provided"}

Room ID: #{booking.room_id}
Check-in: {booking.check_in}
Check-out: {booking.check_out}
Guests: {booking.guests_count}

Total: {booking.currency} {booking.total_price}
Status: {booking.status}
Payment: {booking.payment_status}
""".strip()

    return message


def build_whatsapp_link(phone_number: str, message: str):
    clean_phone = (
        phone_number
        .replace("+", "")
        .replace(" ", "")
        .replace("-", "")
        .replace("(", "")
        .replace(")", "")
    )

    return f"https://wa.me/{clean_phone}?text={quote(message)}"