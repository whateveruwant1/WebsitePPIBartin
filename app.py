from datetime import datetime

from flask import Flask, render_template, request

app = Flask(__name__)

HERO_STATS = [
    {"label": "Anggota Aktif", "value": 128},
    {"label": "Kota Jaringan", "value": 24},
    {"label": "Program Tahunan", "value": 12},
    {"label": "Mitra Kolaborasi", "value": 18},
]

PROGRAMS = [
    {
        "title": "Pembinaan Akademik",
        "summary": "Pendampingan akademik untuk mahasiswa Indonesia di Bartın.",
        "highlights": [
            "Kelas bahasa Turki dasar",
            "Klinik beasiswa dan riset",
            "Sesi berbagi pengalaman alumni",
        ],
    },
    {
        "title": "Pengabdian Masyarakat",
        "summary": "Kegiatan sosial bersama komunitas lokal dan diaspora Indonesia.",
        "highlights": [
            "Donasi pendidikan",
            "Gerakan lingkungan hijau",
            "Bakti sosial Ramadan",
        ],
    },
    {
        "title": "Kebudayaan & Diplomasi",
        "summary": "Promosi budaya Indonesia lewat festival dan pertunjukan.",
        "highlights": [
            "Festival Nusantara",
            "Lokakarya tari dan musik",
            "Pameran kuliner tradisional",
        ],
    },
]

EVENTS = [
    {
        "date": "2024-09-12",
        "name": "Bartin Student Gathering",
        "location": "Bartın Üniversitesi, Aula Utama",
    },
    {
        "date": "2024-10-05",
        "name": "Turkish-Indonesia Cultural Week",
        "location": "Kültür Merkezi, Bartın",
    },
    {
        "date": "2024-11-20",
        "name": "PPI Bartin Leadership Camp",
        "location": "Amasra Coast Retreat",
    },
]

LEADERS = [
    {"name": "Alya Ramadhani", "role": "Ketua Umum"},
    {"name": "Muhammad Zaki", "role": "Wakil Ketua"},
    {"name": "Nabila Siregar", "role": "Sekretaris"},
    {"name": "Rafi Alamsyah", "role": "Bendahara"},
]

TESTIMONIALS = [
    {
        "name": "Rizal Hidayat",
        "quote": (
            "PPI Bartin jadi rumah kedua saya. Dukungan akademik dan sosialnya"
            " membuat adaptasi di Turki lebih mudah."
        ),
    },
    {
        "name": "Salsabila Nur",
        "quote": (
            "Program budaya PPI Bartin memperkenalkan Indonesia dengan cara yang"
            " hangat dan profesional."
        ),
    },
]

GALLERY = [
    {
        "title": "Festival Nusantara 2023",
        "description": "Perayaan budaya bersama komunitas internasional di Bartın.",
    },
    {
        "title": "Kelas Bahasa Turki",
        "description": "Sesi rutin bahasa Turki untuk mahasiswa baru.",
    },
    {
        "title": "Aksi Sosial Ramadan",
        "description": "Pembagian paket iftar untuk masyarakat lokal.",
    },
]

CONTACT_INFO = {
    "address": "Yolüstü Mah. Üniversite Cad. No. 12, Bartın, Türkiye",
    "email": "info@ppibartin.org",
    "phone": "+90 530 555 2211",
}


@app.route("/")
def index():
    return render_template(
        "index.html",
        hero_stats=HERO_STATS,
        programs=PROGRAMS,
        events=EVENTS,
        leaders=LEADERS,
        testimonials=TESTIMONIALS,
        gallery=GALLERY,
        contact=CONTACT_INFO,
        year=datetime.utcnow().year,
    )


@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name", "")
    email = request.form.get("email", "")
    message = request.form.get("message", "")
    return render_template(
        "thank_you.html",
        name=name,
        email=email,
        message=message,
        year=datetime.utcnow().year,
    )


if __name__ == "__main__":
    app.run(debug=True)
