from flask import Flask, render_template
import requests

app = Flask(__name__)

# URL API Fake Store (kategori electronics)
API_URL = "https://fakestoreapi.com/products/category/electronics"

@app.route('/')
def home():
    """Halaman utama: menampilkan daftar produk elektronik"""
    try:
        response = requests.get(API_URL)
        products = response.json()
        return render_template('index.html', products=products)
    except:
        return "<h1>Gagal mengambil data dari API</h1>"

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    """Halaman detail produk berdasarkan ID"""
    try:
        response = requests.get(f"https://fakestoreapi.com/products/{product_id}")
        product = response.json()
        return render_template('product_detail.html', product=product)
    except:
        return "<h1>Produk tidak ditemukan</h1>"

if __name__ == '__main__':
    app.run(debug=True)