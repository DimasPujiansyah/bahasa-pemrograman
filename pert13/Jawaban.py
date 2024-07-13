import uuid
from datetime import datetime

# Struktur data untuk menyimpan event
events = {}

# Fungsi untuk menambahkan event
def add_event(name, date_str, location, description):
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print("Format tanggal salah. Gunakan format YYYY-MM-DD.")
        return None

    event_id = str(uuid.uuid4())
    events[event_id] = {
        'name': name,
        'date': date,
        'location': location,
        'description': description
    }
    return event_id

# Fungsi untuk menampilkan semua event
def list_events():
    for event_id, event in events.items():
        print(f"ID: {event_id}")
        print(f"Nama: {event['name']}")
        print(f"Tanggal: {event['date'].strftime('%Y-%m-%d')}")
        print(f"Lokasi: {event['location']}")
        print(f"Deskripsi: {event['description']}")
        print("---------")

# Fungsi untuk memperbarui event
def update_event(event_id, name=None, date_str=None, location=None, description=None):
    if event_id not in events:
        print(f"Event dengan ID {event_id} tidak ditemukan.")
        return False
    
    if name:
        events[event_id]['name'] = name
    if date_str:
        try:
            date = datetime.strptime(date_str, "%Y-%m-%d")
            events[event_id]['date'] = date
        except ValueError:
            print("Format tanggal salah. Gunakan format YYYY-MM-DD.")
            return False
    if location:
        events[event_id]['location'] = location
    if description:
        events[event_id]['description'] = description
    
    return True

# Fungsi untuk menghapus event berdasarkan ID
def delete_event(event_id):
    if event_id in events:
        del events[event_id]
        print(f"Event dengan ID {event_id} telah dihapus.")
    else:
        print(f"Event dengan ID {event_id} tidak ditemukan.")

# Contoh penggunaan
if __name__ == "__main__":
    event_id1 = add_event("Konser Musik", "2023-07-15", "Jakarta", "Konser musik pop")
    event_id2 = add_event("Pameran Seni", "2023-08-10", "Bandung", "Pameran seni modern")

    print("Daftar Event:")
    list_events()

    print("Memperbarui event pertama...")
    update_event(event_id1, name="Konser Musik Rock", date_str="2023-07-20")

    print("Daftar Event Setelah Pembaruan:")
    list_events()

    print("Menghapus event pertama...")
    delete_event(event_id1)

    print("Daftar Event Setelah Penghapusan:")
    list_events()
